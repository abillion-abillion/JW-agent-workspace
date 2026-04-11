# jw-agent-workspace

> JW Financial Consulting AI 에이전트 팀 — 단일 원천 소스 (SSoT)
> 관리자: 남진우 | 최종수정: 2026-04-11

---

## 빠른 시작

에이전트는 작업 시작 전 반드시 이 순서로 읽는다:

```
1. AGENTS.md          → 전역 컨텍스트 (나는 누구, 뭘 하는 사람)
2. memory/ongoing.md  → 지금 진행중인 것
3. 해당 skills/ 파일  → 작업 유형에 맞는 스킬
```

---

## 팀 구조

### 경영팀 (c-level/) — 방향·판단·책임

| 파일 | 역할 | 참조 인물 |
|------|------|-----------|
| ceo.md | 비전·의사결정·전략 총괄 | Jobs + Grove + Bezos |
| cfo.md | 사업 재무·자본 배분·리스크 | Buffett + Munger + Marks |
| cto.md | 기술 인프라·자동화·AI 설계 | Graham + Andrew Ng + Fowler |
| cmo.md | 브랜드 전략·마케팅 총괄 | Kotler + Ogilvy + Al Ries |
| cso.md | 경쟁전략·사업 방향·수입원 | Porter + Roger Martin + McGrath |
| cpo.md | 서비스·상품 기획·포지셔닝 | Cagan + Blank + Dunford |
| coo.md | 일상 운영·실행·팀 관리 | Sandberg + Horowitz + Ohno |

### 기능팀 (skills/) — 실행·작업·산출물

| 파일 | 역할 | 참조 인물 |
|------|------|-----------|
| sales.md | 영업·상담·클로징 | Hormozi + Rackham + Tracy |
| marketing.md | 채널 전략·콘텐츠 방향 | Seth Godin + Gary V + Schwartz |
| finance-consulting.md | 재무진단·포트폴리오·매크로 | Damodaran + Marks + Buffett |
| content-creation.md | 콘텐츠 실전 작성 | StoryBrand + Handley + Perell |
| kakao-message.md | 카카오 메시지·시퀀스 | Coleman + Reichheld + Hsieh |
| operations.md | 자동화·프로세스·루틴 | GTD + 도요타 + TOC |
| cs-crm.md | 고객 관계·CRM·이탈 방지 | Hsieh + Coleman + Reichheld |
| hr.md | 채용·온보딩·교육 | McCord + Catmull + Drucker |
| legal.md | 법무·컴플라이언스·계약 | Dershowitz + Garner + Susskind |

---

## 역할 분담 원칙

```
경영팀 (c-level)   →  "무엇을 할 것인가" 판단
기능팀 (skills)    →  "어떻게 실행할 것인가" 수행

JW대장             →  경영팀 참조 + 기능팀 라우팅 + 부장 지시
JW부장             →  기능팀 스킬 참조 + 초안 생성 + 수정
진우님             →  최종 확인 + 고객 발송 승인
```

---

## 폴더 구조

```
jw-agent-workspace/
├── AGENTS.md                    # 전역 컨텍스트 (항상 먼저 읽기)
├── README.md                    # 이 파일
│
├── c-level/                     # 경영팀 (방향·판단)
│   ├── ceo.md
│   ├── cfo.md
│   ├── cto.md
│   ├── cmo.md
│   ├── cso.md
│   ├── cpo.md
│   └── coo.md
│
├── skills/                      # 기능팀 (실행·작업)
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
├── templates/                   # 공통 템플릿
│   ├── agent-template.md        # 스킬 파일 작성 템플릿
│   ├── kakao-message-template.md
│   └── content-template.md
│
├── memory/
│   ├── clients.md               # 클라이언트 현황
│   ├── ongoing.md               # 진행중 프로젝트
│   └── daily-log/               # 날짜별 업무일지
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
    └── agent-rules.md
```

---

## 자주 쓰는 요청 → 스킬 매핑

| 요청 | 참조 스킬 |
|------|-----------|
| `카드뉴스 초안` | marketing + content-creation |
| `2차완료 [이름]` | kakao-message (B 시퀀스) + sales |
| `계약완료 [이름]` | kakao-message (C 시퀀스) |
| `포트폴리오 북 [이름]` | finance-consulting + content-creation |
| `핀사이트랩스 리포트` | finance-consulting + marketing |
| `전략 방향` | c-level/ceo + c-level/cso |
| `새 기능 개발` | c-level/cto + operations |
| `채용 기준` | hr |
| `계약서 검토` | legal |
| `고객 이탈 대응` | cs-crm + kakao-message |

---

## 관련 레포지토리

| 레포 | 역할 |
|------|------|
| jw-telegram-agent | Telegram 봇 (대장/부장 실행 환경) |
| abillion-abillion.github.io | jwfinancial.co.kr 메인 사이트 |

---

## 업데이트 이력

| 버전 | 날짜 | 내용 |
|------|------|------|
| v1.0 | 2026-04-09 | 초기 구조 생성 |
| v2.0 | 2026-04-11 | skills 9종 + c-level 7종 + templates 완성 |

---

_관리자: 남진우 | jw-agent-workspace v2.0_
