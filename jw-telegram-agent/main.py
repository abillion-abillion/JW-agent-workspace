"""
JW Financial Telegram Agent
- Telegram에서 메시지 받음 → Claude API 처리 → 결과 응답
- Railway 클라우드 배포용 (24/7 상주)
"""

import os
import httpx
import logging
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ──────────────────────────────────────────
# 전역 컨텍스트 (AGENTS.md 내용)
# GitHub에서 자동으로 읽어오거나, 여기 직접 관리
# ──────────────────────────────────────────
SYSTEM_PROMPT = """
당신은 남진우 자산관리사(JW Financial Consulting)의 전담 AI 에이전트입니다.

## 운영자
- 이름: 남진우 | 자산관리사/팀장 5년차
- 소속: 하나증권 연계 JW Financial Consulting
- 사이트: jwfinancial.co.kr
- 리서치 브랜드: 핀사이트랩스(FINSIGHT LABS)

## 사업 구조
- 주 수입: 컨설팅 비용 + 금융 계약(연금보험, IRP, ISA, 보장성보험, 변액연금)
- 핵심 고객: 30대 맞벌이 직장인 (100~150명 클라이언트)
- 채널: 네이버 블로그(moneymustard), 유튜브(@honeymoneymustard), Kmong, KakaoTalk

## 현재 운영중인 자동화
- 모닝 브리핑: RSS → Claude API → Telegram
- 상담 분석: Notion DB → Claude/Gemini → Telegram
- 상담 인테이크: Google Forms → GAS → Telegram
- Clova Note 요약: 녹취 → Claude → 카카오 초안

## 콘텐츠 원칙
- 어려운 금융을 쉽게: 비유 먼저, 인과관계 중심
- JW Financial: 고객 대상 실용 정보 + 상담 CTA
- 핀사이트랩스: 매크로 분석, 기관투자자 시각

## 에이전트 행동 원칙
1. 짧고 명확하게 답변 (Telegram 가독성)
2. 고객 발송용 초안은 반드시 "✅ 검토 후 발송해주세요" 문구 포함
3. 금융 수치/상품 정보는 "확인 필요" 표시
4. 외부 발송 행동은 직접 실행하지 않고 초안만 제공

## 주요 링크
- 상담 예약: jwfinancial.co.kr/consult.html
- 무료 진단: jwfinancial.co.kr/diagnosis.html

당신은 진우님이 Telegram으로 보내는 업무 지시를 받아 처리합니다.
콘텐츠 초안, 고객 메시지 초안, 업무 분석, 아이디어 정리 등 모든 업무를 도와줍니다.
"""

# 대화 히스토리 (메모리) - 간단한 인메모리 방식
# 운영 안정화 후 Redis로 교체 가능
conversation_history: list[dict] = []
MAX_HISTORY = 20  # 최근 20개 메시지 유지

# ──────────────────────────────────────────
# FastAPI 앱
# ──────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작 시 Telegram webhook 등록
    await set_webhook()
    yield

app = FastAPI(lifespan=lifespan)

# ──────────────────────────────────────────
# Telegram 유틸
# ──────────────────────────────────────────
TELEGRAM_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"
ALLOWED_CHAT_ID = int(os.environ["ALLOWED_CHAT_ID"])  # 진우님 개인 chat_id만 허용


async def set_webhook():
    """Railway 배포 URL로 webhook 등록"""
    webhook_url = os.environ.get("WEBHOOK_URL", "")
    if not webhook_url:
        logger.warning("WEBHOOK_URL 환경변수 없음 - webhook 미등록")
        return
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            f"{TELEGRAM_API}/setWebhook",
            json={"url": f"{webhook_url}/webhook", "drop_pending_updates": True}
        )
        logger.info(f"Webhook 등록: {resp.json()}")


async def send_message(chat_id: int, text: str):
    """Telegram 메시지 발송"""
    # Telegram 메시지 4096자 제한 → 초과 시 분할
    chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
    async with httpx.AsyncClient() as client:
        for chunk in chunks:
            await client.post(
                f"{TELEGRAM_API}/sendMessage",
                json={
                    "chat_id": chat_id,
                    "text": chunk,
                    "parse_mode": "Markdown"
                }
            )


async def send_typing(chat_id: int):
    """타이핑 중 표시"""
    async with httpx.AsyncClient() as client:
        await client.post(
            f"{TELEGRAM_API}/sendChatAction",
            json={"chat_id": chat_id, "action": "typing"}
        )

# ──────────────────────────────────────────
# Claude API
# ──────────────────────────────────────────
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]
CLAUDE_MODEL = "claude-sonnet-4-5"


async def ask_claude(user_message: str) -> str:
    """Claude API 호출 (대화 히스토리 유지)"""
    global conversation_history

    # 히스토리에 사용자 메시지 추가
    conversation_history.append({"role": "user", "content": user_message})

    # 히스토리 길이 제한
    if len(conversation_history) > MAX_HISTORY:
        conversation_history = conversation_history[-MAX_HISTORY:]

    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    payload = {
        "model": CLAUDE_MODEL,
        "max_tokens": 2000,
        "system": SYSTEM_PROMPT,
        "messages": conversation_history
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        resp = await client.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=payload
        )
        resp.raise_for_status()
        data = resp.json()

    assistant_reply = data["content"][0]["text"]

    # 히스토리에 어시스턴트 응답 추가
    conversation_history.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply

# ──────────────────────────────────────────
# 명령어 처리
# ──────────────────────────────────────────
async def handle_command(chat_id: int, text: str) -> bool:
    """특수 명령어 처리. 명령어면 True 반환"""
    if text.strip() == "/start":
        await send_message(chat_id,
            "👋 *JW 에이전트 시작*\n\n"
            "업무를 지시해 주세요. 예시:\n"
            "• `카드뉴스 초안 짜줘 - 오늘 미국 금리 동결 관련`\n"
            "• `30대 맞벌이 고객한테 보낼 IRP 안내 메시지 초안`\n"
            "• `핀사이트랩스 주간 매크로 요약 초안`\n\n"
            "/clear - 대화 기록 초기화\n"
            "/help - 도움말"
        )
        return True

    if text.strip() == "/clear":
        global conversation_history
        conversation_history = []
        await send_message(chat_id, "🗑 대화 기록을 초기화했습니다.")
        return True

    if text.strip() == "/help":
        await send_message(chat_id,
            "*JW 에이전트 사용법*\n\n"
            "*콘텐츠 초안*\n"
            "`카드뉴스 초안 - [주제]`\n"
            "`블로그 포스트 초안 - [주제]`\n"
            "`핀사이트랩스 리포트 - [주제]`\n\n"
            "*고객 메시지*\n"
            "`카카오 메시지 초안 - [상황]`\n"
            "`신규 고객 팔로업 메시지`\n\n"
            "*업무 분석*\n"
            "`[주제] 분석해줘`\n"
            "`[아이디어] 정리해줘`\n\n"
            "/clear - 대화 초기화\n"
        )
        return True

    return False

# ──────────────────────────────────────────
# Webhook 엔드포인트
# ──────────────────────────────────────────
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()

    # 메시지가 없으면 무시
    message = data.get("message")
    if not message:
        return {"ok": True}

    chat_id = message["chat"]["id"]
    text = message.get("text", "").strip()

    # 보안: 진우님 채팅만 허용
    if chat_id != ALLOWED_CHAT_ID:
        logger.warning(f"허용되지 않은 chat_id 접근: {chat_id}")
        return {"ok": True}

    if not text:
        return {"ok": True}

    # 특수 명령어 처리
    if await handle_command(chat_id, text):
        return {"ok": True}

    # 타이핑 표시
    await send_typing(chat_id)

    # Claude 처리
    try:
        reply = await ask_claude(text)
        await send_message(chat_id, reply)
    except Exception as e:
        logger.error(f"Claude API 오류: {e}")
        await send_message(chat_id, f"⚠️ 오류 발생: {str(e)}\n\n잠시 후 다시 시도해 주세요.")

    return {"ok": True}


@app.get("/")
async def health():
    return {"status": "JW Agent 운영중 ✅"}
