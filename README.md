# jw-agent-workspace

> JW Financial Consulting 에이전트 SSoT (단일 원천 소스)

남진우(@abillion-abillion) JW Financial의 AI 에이전트 워크스페이스입니다.
모든 에이전트는 이 레포를 기반으로 업무 맥락을 공유합니다.

---

## 빠른 시작

에이전트는 작업 시작 전 반드시 이 순서로 읽습니다:

1. `AGENTS.md` — 전역 컨텍스트 (나는 누구, 뭘 하는 사람)
2. `memory/ongoing.md` — 지금 진행중인 것
3. 관련 `skills/` 또는 `pipelines/` 문서

---

## 폴더 구조

```
jw-agent-workspace/
├── AGENTS.md              # 전역 컨텍스트 (항상 먼저 읽기)
├── README.md              # 이 파일
├── memory/
│   ├── clients.md         # 클라이언트 현황
│   ├── ongoing.md         # 진행중 프로젝트
│   └── daily-log/         # 날짜별 업무일지
├── skills/
│   ├── content-creation.md
│   ├── client-report.md
│   └── kakao-message.md
├── pipelines/
│   ├── morning-briefing.md
│   └── consult-analysis.md
├── sop/
│   ├── new-client-onboarding.md
│   └── weekly-content.md
└── rules/
    └── agent-rules.md
```

---

## 관련 레포

- `abillion-abillion.github.io` — jwfinancial.co.kr 메인 사이트
- 기타 프로젝트 레포들 — 각각 로컬 AGENTS.md 보유

---

_관리자: 남진우 | 시작일: 2026-04-09_
