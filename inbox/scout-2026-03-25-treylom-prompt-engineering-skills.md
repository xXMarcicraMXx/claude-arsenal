---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code prompt engineering"
  quality_score: 71
  scoring_breakdown:
    stars: 15
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "treylom/prompt-engineering-skills"
  url: "https://github.com/treylom/prompt-engineering-skills"
  description: "Comprehensive AI prompt engineering skills for Claude Code, ChatGPT GPTs, and Gemini Gems. Includes model-specific patterns for GPT-5.4, Claude 4.6, Gemini 3.1, Veo 3.1, and Nano Banana2"
  stars: 55
  forks: 13
  open_issues: 0
  language: ""
  license: "NOASSERTION"
  last_push: "2026-03-23"
  created: "2025-12-28"
  topics: ["ai", "prompts"]
---

# treylom/prompt-engineering-skills

> Discovered by arsenal scout — awaiting manual triage

## Description

Comprehensive AI prompt engineering skills for Claude Code, ChatGPT GPTs, and Gemini Gems. Includes model-specific patterns for GPT-5.4, Claude 4.6, Gemini 3.1, Veo 3.1, and Nano Banana2

## README Excerpt

# 프롬프트 엔지니어링 스킬

> **모델 순위**: [LMArena Leaderboard](https://lmarena.ai) 기반 (2026년 3월 기준)

Claude Code, ChatGPT GPTs, Gemini Gems를 위한 종합 AI 프롬프트 엔지니어링 스킬 모음입니다.

---

## 바로 사용하기

설정 없이 바로 사용할 수 있는 링크입니다:

| 플랫폼 | 링크 |
|--------|------|
| **ChatGPT GPTs** | [두부경 종합 프롬프트 생성기](https://chatgpt.com/g/g-694feb6bf18481918acd876e3c3eed37-tofukyung-jonghab-peurompeuteu-saengseonggi) |
| **Gemini Gems** | [프롬프트 생성기 Gem](https://gemini.google.com/gem/1ZV9S3vNOwExi4_yLHRJKFtpNpATPDI5d?usp=sharing) |

---

## 개요

이 저장소는 다음 모델에 최적화된 프롬프트 엔지니어링 자료를 제공합니다:

| 모델 | 커버리지 |
|------|----------|
| **GPT-5.4 / GPT-5.4-Codex** | XML 패턴, reasoning_effort, Compaction |
| **Claude 4.6 (Opus/Sonnet)** | 명시적 지시, Adaptive Thinking |
| **Gemini 3** | Constraints First, 멀티모달 컨텍스트 |
| **Veo 3.1** | 오디오 포함 동영상 생성 |
| **Gemini Image** | 이미지 생성 |

### 목적별 추천 모델 (LMArena 기준)

> 출처: [LMArena Leaderboard](https://lmarena.ai) - 사용자 투표 기반 순위

| 목적 | 1순위 | 2순위 | 3순위 |
|------|-------|-------|-------|
| **코딩/개발** | Claude Opus 4.6 | GPT-5.4 | Gemini 3.1 Pro |
| **수학/논리** | Claude Opus 4.6 | Gemini 3.1 Pro | GPT-5.4 |
| **글쓰기/창작** | Gemini 3.1 Pro | Gemini 3 Pro | Claude Opus 4.6 |
| **이미지 생성** | NanoBanana2 (Gemini 3.1 Flash Image) | GPT Image 1.5 | gpt-image |
| **동영상 생성** | Kling 3.0 | Grok Imagine Video | Veo 3 |
| **웹 검색/리서치** | Claude Opus 4.6 Search | GPT-5.2 Search | Gemini 3 Pro Grounding |
| **팩트체크** | **GPT-5.4 Thinking** | Gemini 3 Pro Grounding | Perplexity Sonar Pro |

---

## 저장소 구조

```
prompt-engineering-skills/
├── README.md                           # 이 파일
├── LICENSE                             # MIT 라이선스
│
├── skills/                             # 핵심 스킬 파일
│   ├── prompt-engineering-guide.md     # 모델별 프롬프트 전략
│   ├── image-prompt-guide.md           # 이미지 생성 가이드
│   ├── gpt-5.4-prompt-enhancement.md   # GPT-5.4 전용 패턴
│   ├── claude-4.6-prompt-strategies.md # Claude 4.6 전용 전략
│   ├── gemini-3.1-prompt-strategies.md # Gemini/Veo/Nano Banana 전략
│   ├── context-engineering-collection.md  # CE 원칙
│   ├── expert-domain-priming.md        # 전문 도메인 프라이밍
│   ├── research-prompt-guide.md        # 검색/리서치 프롬프트 가이드
│   └── slide-prompt-guide.md           # 슬라이드 프롬프트 가이드
│
├── commands/                           # Claude Code 커맨드
│   ├── prompt.md                       # /prompt 커맨드
│   └── prompt-sync.md                  # /prompt-sync 동기화 커맨드
│
├── instructions/                       # GPTs/Gems 시스템 프롬프트
│   ├── GPTs-Prompt-Generator.md        # ChatGPT GPTs용
│   └── Gems-Prompt-Generator.md        # Gemini Gems용
│
└── examples/                           # 사용 예시
    ├── gpt-5.4-examples.md
    ├── claude-4.5-examples.md
    └── image-generation-examples.md
```

---

## 직접 설정하기

### Claude Code 사용자

#### ⚡ 원클릭 글로벌 설치 (모든 프로젝트에서 사용)

**macOS / Linux:**
```bash
git clone https://github.com/treylom/prompt-engineering-skills.git /tmp/pes && \
mkdir -p ~/.claude/skills ~/.claude/commands && \
cp /tmp/pes/skills/*.md ~/.claude/skills/ && \
cp /tmp/pes/commands/*.md ~/.claude/commands/ && \

## Links

- Repository: https://github.com/treylom/prompt-engineering-skills
