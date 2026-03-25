---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 61
  scoring_breakdown:
    stars: 13
    recency: 20
    docs: 20
    community: 8
github_data:
  full_name: "egebese/skill-manager"
  url: "https://github.com/egebese/skill-manager"
  description: "Save ~4,000 tokens per conversation by auto-disabling irrelevant Claude Code skills per project. Detects tech stack, scores skill relevance, injects CLAUDE.md."
  stars: 34
  forks: 1
  open_issues: 0
  language: "Python"
  license: "MIT"
  last_push: "2026-02-22"
  created: "2026-02-22"
  topics: []
---

# egebese/skill-manager

> Discovered by arsenal scout — awaiting manual triage

## Description

Save ~4,000 tokens per conversation by auto-disabling irrelevant Claude Code skills per project. Detects tech stack, scores skill relevance, injects CLAUDE.md.

## README Excerpt

# skill-manager

**Save ~4,000 tokens per conversation** by automatically disabling irrelevant Claude Code skills per project.

50+ installed skills? Most are noise for your current project. `skill-manager` detects your tech stack, scores every skill's relevance, and tells Claude to ignore the ones that don't belong — all through your project's `CLAUDE.md`.

## Install

```bash
npx skills add egebese/skill-manager -g -y
```

## Usage

```
/skill-manager
```

Or just say: *"manage skills"*, *"optimize skills"*, *"disable irrelevant skills"*, *"which skills do I need?"*

## Before & After

### Next.js + Stripe project

```
Stack: Next.js / TypeScript / React / Stripe / Tailwind CSS

53 skills analyzed:
  27 essential  (kept)    — page-cro, stripe-integration, analytics-tracking, ...
  10 universal  (kept)    — brainstorming, writing-plans, find-skills, ...
  16 irrelevant (disabled) — asc-xcode-build, mobile-ios-design, fal-audio, ...

16 skills disabled → ~1,200 tokens saved per conversation
```

### iOS Swift project

```
Stack: iOS/macOS Native / Swift / SwiftUI

53 skills analyzed:
   9 essential  (kept)    — mobile-ios-design, asc-xcode-build, app-store-optimization, ...
  13 useful     (kept)    — copywriting, marketing-ideas, stripe-integration, ...
  10 universal  (kept)    — brainstorming, writing-plans, find-skills, ...
  21 irrelevant (disabled) — seo-audit, schema-markup, programmatic-seo, page-cro, ...

21 skills disabled → ~1,600 tokens saved per conversation
```

### Rust CLI project

```
Stack: Rust

53 skills analyzed:
   0 essential
   0 useful
  10 universal  (kept)    — brainstorming, writing-plans, find-skills, ...
  43 irrelevant (disabled) — all iOS, web, marketing, media skills

43 skills disabled → ~3,200 tokens saved per conversation
```

## How It Works

**1. Detects** your tech stack from project files:
  - `package.json` → Node.js, Next.js, React, Vue, Stripe, Remotion, etc.
  - `*.xcodeproj` / `Podfile` / `Package.swift` → iOS/macOS
  - `Cargo.toml` → Rust | `go.mod` → Go | `pubspec.yaml` → Flutter
  - `build.gradle` → Android | `composer.json` → PHP | `Gemfile` → Ruby
  - Monorepo support: scans `packages/`, `apps/` subdirectories

**2. Discovers** all installed skills from every source:
  - `~/.agents/.skill-lock.json` (primary lock file)
  - `~/.agents/skills/` and `~/.claude/skills/` directories
  - Project-local `.claude/skills/` (always kept active)

**3. Scores** each skill 0–100 based on tech stack match:

| Tier | Score | Action |
|------|-------|--------|
| **essential** | 80–100 | Kept active — directly relevant |
| **useful** | 40–79 | Kept active — cross-platform utility |
| **irrelevant** | 0–39 | Disabled in CLAUDE.md |
| **universal** | always | Never disabled (brainstorming, TDD, find-skills, etc.) |

**4. Auto-categorizes unknown skills** by reading their `SKILL.md` description — your custom skills and newly installed skills are handled automatically, no hardcoded lists needed.

**5. Injects** a bound

## Links

- Repository: https://github.com/egebese/skill-manager
