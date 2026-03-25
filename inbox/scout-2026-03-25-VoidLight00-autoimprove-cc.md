---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 63
  scoring_breakdown:
    stars: 14
    recency: 25
    docs: 15
    community: 9
github_data:
  full_name: "VoidLight00/autoimprove-cc"
  url: "https://github.com/VoidLight00/autoimprove-cc"
  description: "Claude Code version of skill-autoimprove — auto-improve any CLAUDE.md using Karpathy autoresearch loop"
  stars: 50
  forks: 4
  open_issues: 1
  language: ""
  license: "MIT"
  last_push: "2026-03-19"
  created: "2026-03-19"
  topics: []
---

# VoidLight00/autoimprove-cc

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Code version of skill-autoimprove — auto-improve any CLAUDE.md using Karpathy autoresearch loop

## README Excerpt

# autoimprove-cc

> Karpathy autoresearch loop for SKILL.md — Claude Code native implementation.

SKILL.md를 밤새 자동 개선하는 Claude Code 네이티브 시스템.
`/autoimprove` 한 줄로 실행하면, 아침에 더 나은 스킬로 깨어납니다.

Python 스크립트 없이 **Claude Code agents + commands**만으로 동작합니다.

## How It Works

[Karpathy의 autoresearch](https://github.com/karpathy/autoresearch) 루프를 SKILL.md에 적용합니다:

```
1. SKILL.md 읽기
2. eval.json의 binary assertions로 채점
3. 실패한 assertion 하나를 고치도록 SKILL.md 수정
4. 재채점 → 점수 올랐으면 git commit, 아니면 git reset
5. 100% 달성하거나 max_loops까지 반복
```

핵심 차이: Karpathy는 `train.py`의 수치 메트릭을 사용하지만,
우리는 **binary assertions**(참/거짓 테스트)의 패스율을 메트릭으로 사용합니다.

## Quick Start

### 글로벌 설치 (모든 Claude Code 프로젝트에서 사용)

```bash
# 이 저장소를 클론
git clone https://github.com/VoidLight00/autoimprove-cc.git

# Claude Code 글로벌 agents/commands에 심볼릭 링크
ln -s $(pwd)/autoimprove-cc/.claude/agents/skill-optimizer.md ~/.claude/agents/skill-optimizer.md
ln -s $(pwd)/autoimprove-cc/.claude/commands/autoimprove.md ~/.claude/commands/autoimprove.md
```

### 프로젝트별 설치

```bash
# 프로젝트 디렉토리에서
cp -r autoimprove-cc/.claude/agents/skill-optimizer.md .claude/agents/
cp -r autoimprove-cc/.claude/commands/autoimprove.md .claude/commands/
```

### 실행

```bash
# Claude Code 세션에서:

# 1. eval.json 자동 생성 + 루프 실행
/autoimprove skills/my-skill

# 2. eval.json만 생성 (검토 후 수동 실행)
/autoimprove skills/my-skill --gen-eval-only

# 3. 최대 50회 반복
/autoimprove skills/my-skill --max-loops 50

# 4. Dry-run (git 변경 없이 채점만)
/autoimprove skills/my-skill --dry-run
```

## eval.json 작성법

eval.json은 SKILL.md의 품질을 측정하는 **binary assertions** 모음입니다.

### 구조

```json
{
  "skill_name": "my-skill",
  "skill_md_path": "skills/my-skill/SKILL.md",
  "tests": [
    {
      "id": "test-001",
      "description": "구조 — 필수 섹션 존재 여부",
      "prompt": "/my-skill 이라고 입력했을 때",
      "expected_behavior": "스킬이 활성화되고 워크플로우를 시작한다",
      "assertions": [
        "SKILL.md에 스킬 이름이 포함된 H1 헤딩이 있다",
        "Workflow 섹션이 존재한다",
        "Rules 섹션에 최소 2개의 금지 사항이 있다"
      ]
    }
  ]
}
```

### 필드 설명

| 필드 | 설명 |
|------|------|
| `id` | `test-001` 형식의 고유 ID |
| `description` | 테스트 그룹 설명 |
| `prompt` | 사용자가 입력할 프롬프트 시나리오 |
| `expected_behavior` | 프롬프트에 대한 기대 동작 |
| `assertions` | 참/거짓으로 판별 가능한 assertion 배열 |

### 좋은 assertion 작성 팁

```
# 좋은 assertion (명확한 참/거짓)
"SKILL.md에 '## Workflow' 섹션이 존재한다"
"워크플로우에 최소 5개의 단계가 있다"
"코드 블록이 최소 2개 포함되어 있다"

# 나쁜 assertion (주관적, 판단 불가)
"SKILL.md가 잘 작성되어 있다"
"워크플로우가 충분히 상세하다"
```

### 권장 카테고리 (5개)

1. **구조** — 필수 섹션 존재, 헤딩 계층, 파일 구조
2. **트리거** — 슬래시 커맨드, 활성화 조건, 인자 형식
3. **워크플로우** — 단계별 프로세스, 분기 조건, 출력 형식
4. **규칙** — 금지 사항, 제약 조건, Do NOT 항목
5. **완성도** — 예시, 코드블록, 에지 케이스, 의존성

eval.json이 없으면 `/autoimprove`가 SKILL.md를 분석하여 자동 생성합니다.
생성 후 검토하고 필요시 수정하세요.

## Architecture

```
autoimprove-cc/
├── README.md                     ← 이 파일
├── CLAUDE.md                     ← Claude Code 프로젝트 지시문
├── .claude/
│   ├── agents/
│   │   └── skill-optimizer.md    ← 루프 에이전트 (핵심)
│   └── commands/
│       └── autoimprove.md        ← /autoimprove 슬래시 커맨드
├── eval/
│  

## Links

- Repository: https://github.com/VoidLight00/autoimprove-cc
