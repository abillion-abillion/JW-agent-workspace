# JW Agent Workspace — 전역 컨텍스트

> 이 문서는 JW Financial 에이전트 시스템의 단일 원천 소스(SSoT)입니다.
> 모든 에이전트는 작업 시작 전 반드시 이 문서를 읽어야 합니다.

---

## 1. 운영자 정보

| 항목 | 내용 |
|---|---|
| 이름 | 남진우 |
| 직책 | 자산관리사 / 팀장 (경력 5년) |
| 소속 | 하나증권 연계 JW Financial Consulting |
| 사이트 | jwfinancial.co.kr (GitHub Pages, PWA) |
| 리서치 브랜드 | 핀사이트랩스 (FINSIGHT LABS) |
| 블로그 | 네이버 블로그 moneymustard |
| 유튜브 | @honeymoneymustard |
| 프리랜서 | Kmong |
| 주요 채널 | KakaoTalk (Solapi 비즈채널), Telegram |

---

## 2. 사업 구조

### 주 수입원
- 컨설팅 비용 (상담 예약 → consult.html → Cal.com)
- 금융 계약 (연금보험, IRP, ISA, 보장성보험, 변액연금 등)

### 부 수입원 (성장중)
- 교육 콘텐츠 / 지식창업
- 핀사이트랩스 리서치 콘텐츠

### 타겟 고객
- 핵심: 30대 맞벌이 직장인
- 범위: 20~40대 직장인 100~150명 클라이언트 보유
- 확장: 네이버 직원, 중국어권 서울 거주자 (위챗/샤오홍슈)

### 팀 구성
- 진우님 (대표)
- 주니어 동료 1명 (한국어/중국어 이중언어, 중국어권 커뮤니티 담당)

### 금지 단어 (고객 발송물 전체)
- **가입, 계약, 납입, 판매** → 위 단어 일체 사용 금지

---

## 3. 기술 인프라

### 운영 시스템
- 사이트: GitHub Pages (abillion-abillion.github.io → jwfinancial.co.kr)
- 결제: Toss Payments
- CRM: Notion DB
- 자동화: Python + Claude API + Telegram Bot
- 알림: Solapi (KakaoTalk 비즈채널), Telegram

### 운영중인 에이전트/자동화
| 파이프라인 | 설명 | 상태 |
|---|---|---|
| 모닝 브리핑 | RSS → Claude API → Telegram | ✅ 운영중 |
| 상담 분석 | Notion DB 폴링 → Claude/Gemini → Telegram | ✅ 운영중 |
| 상담 인테이크 | Google Forms → GAS → Telegram | ✅ 운영중 |
| Clova Note 요약 | 녹취 → Claude → 상담 요약 + 카카오 초안 | ✅ 운영중 |
| 섹터 밸류에이션 | pykrx/DART → Claude → Telegram | ✅ 운영중 |

### 주요 레포지토리 (약 12개)
- AGENTS.md 이중 구조 적용 (전역 + 레포별)
- 로컬 경로: C:\Users\njw85\

---

## 4. 콘텐츠 전략

### 브랜드별 역할
- **JW Financial**: 고객 대상 실용 금융 정보, 상담 CTA
- **핀사이트랩스**: 매크로 분석, 기관투자자 시각, 리서치

### 콘텐츠 원칙
- 어려운 금융/경제를 쉽게: 비유 먼저, 인과관계 중심
- 짧고 명확하게: 카드뉴스, 숏폼 친화적
- 행동 유도: 매 콘텐츠에 상담 CTA 포함

### 주요 소스
- 손에 잡히는 경제, 삼프로TV, 메르 블로그
- 오건영 Facebook 칼럼, 한국경제

---

## 5. 현재 진행중인 프로젝트 (ongoing.md 참조)

- 라에미안 라그란데 등기이전 (관리처분 변경 총회 5~6월 예정, 등기 9~10월 목표)
- 보험료 비교 시뮬레이터 (기획 단계)
- 新IFP vs AFPK 자격증 공부 (시험일: 2026-05-16)
- 네이버 직원 대상 마케팅 카드이미지 시리즈

---

## 6. 에이전트 행동 원칙

1. **맥락 우선**: 작업 전 반드시 관련 skills/, c-level/, pipelines/, sop/ 문서 확인
2. **SSoT 준수**: 새로운 정보 발생 시 memory/ 폴더에 즉시 기록
3. **진우님 말투 반영**: 고객 대상 글은 친근하되 전문적, 비유 우선
4. **확인 후 실행**: 외부 발송(문자, 이메일, 발행) 전 반드시 진우님 승인 요청
5. **업무일지 작성**: 매 세션 종료 시 memory/daily-log/YYYY-MM-DD.md 업데이트
6. **금지 단어 준수**: 가입/계약/납입/판매 — 고객 발송물 전체 적용
7. **투자 권유 금지**: 모든 금융 분석은 참고용임을 명시

---

## 7. 팀 구조

### 경영팀 (c-level/) — 방향·판단
| 파일 | 역할 |
|---|---|
| ceo.md | 비전·의사결정 (Jobs + Grove + Bezos) |
| cfo.md | 사업 재무·리스크 (Buffett + Munger + Marks) |
| cto.md | 기술·자동화 (Graham + Ng + Fowler) |
| cmo.md | 브랜드·마케팅 총괄 (Kotler + Ogilvy + Ries) |
| cso.md | 경쟁전략·방향 (Porter + Martin + McGrath) |
| cpo.md | 상품·서비스 기획 (Cagan + Blank + Dunford) |
| coo.md | 운영·실행·팀 (Sandberg + Horowitz + Ohno) |

### 기능팀 (skills/) — 실행·작업
| 파일 | 역할 |
|---|---|
| sales.md | 영업·상담·클로징 |
| marketing.md | 채널 전략·콘텐츠 방향 |
| finance-consulting.md | 재무진단·포트폴리오·매크로 |
| content-creation.md | 콘텐츠 실전 작성 |
| kakao-message.md | 카카오 메시지·시퀀스 |
| operations.md | 자동화·프로세스·루틴 |
| cs-crm.md | 고객 관계·CRM |
| hr.md | 채용·온보딩·교육 |
| legal.md | 법무·컴플라이언스 |

---

## 8. 폴더 구조 가이드

```
jw-agent-workspace/
├── AGENTS.md                    ← 지금 이 파일 (항상 먼저 읽기)
├── README.md                    ← 전체 구조 및 사용법
│
├── c-level/                     ← 경영팀 (방향·판단)
│   ├── ceo.md
│   ├── cfo.md
│   ├── cto.md
│   ├── cmo.md
│   ├── cso.md
│   ├── cpo.md
│   └── coo.md
│
├── skills/                      ← 기능팀 (실행·작업)
│   ├── sales.md
│   ├── marketing.md
│   ├── finance-consulting.md
│   ├── content-creation.md
│   ├── kakao-message.md
│   ├── operations.md
│   ├── cs-crm.md
│   ├── hr.md
│   └── legal.md
│
├── templates/                   ← 공통 템플릿
│   ├── agent-template.md
│   ├── kakao-message-template.md
│   └── content-template.md
│
├── memory/
│   ├── clients.md               ← 클라이언트 현황 및 주요 메모
│   ├── ongoing.md               ← 진행중 프로젝트 트래킹
│   └── daily-log/               ← 날짜별 업무일지 (YYYY-MM-DD.md)
│
├── pipelines/
│   ├── morning-briefing.md
│   ├── consult-analysis.md
│   └── sector-valuation.md
│
├── sop/
│   ├── new-client-onboarding.md
│   └── weekly-content.md
│
└── rules/
    └── agent-rules.md           ← 에이전트 협업 내규
```

---

_마지막 업데이트: 2026-04-11_
_관리자: 남진우 / jw-agent-workspace v2.0_
