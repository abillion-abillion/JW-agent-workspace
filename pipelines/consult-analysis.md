# 파이프라인: 상담 분석

> 상태: ✅ 운영중

---

## 개요

상담 녹취(Clova Note) → Claude 구조화 요약 → KakaoTalk 메시지 초안 생성

---

## 플로우

```
상담 진행 (Clova Note 녹취)
  ↓
Clova Note → 텍스트 추출
  ↓
Claude API 구조화 분석
  - 고객 니즈 파악
  - 추천 상품 매핑
  - 팔로업 포인트 추출
  ↓
Telegram 알림 (진우님)
  ↓
KakaoTalk 초안 생성 (skills/kakao-message.md 참조)
  ↓
진우님 검토 → 발송
```

---

## Notion CRM 연동

- Notion DB 폴링: APScheduler로 주기적 확인
- 새 상담 등록 시 자동 분석 트리거
- 분석 결과 Notion 해당 레코드에 업데이트

---

## 출력 형식 (Telegram 알림)

```
📋 신규 상담 분석 완료

👤 고객: [이니셜/ID]
📅 상담일: [날짜]

🎯 핵심 니즈
- [니즈 1]
- [니즈 2]

💡 추천 상품
- [상품 1]: [이유]
- [상품 2]: [이유]

📌 팔로업 포인트
- [포인트]

💬 카카오 메시지 초안 준비됨 → [링크 or 내용]
```

---

## 기술 스택

- 언어: Python
- 스케줄러: APScheduler
- API: Claude API + Gemini API
- CRM: Notion DB
- 발송: Telegram Bot API + Solapi

---

## 개선 아이디어

- [ ] 상담 패턴 분석 (월별 트렌드 리포트)
- [ ] 고객 세그먼트별 추천 상품 자동 매핑 고도화
- [ ] Google Forms 인테이크와 완전 통합

---

_마지막 업데이트: 2026-04-09_
