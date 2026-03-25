---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code workflow"
  quality_score: 80
  scoring_breakdown:
    stars: 30
    recency: 20
    docs: 20
    community: 10
github_data:
  full_name: "gotalab/cc-sdd"
  url: "https://github.com/gotalab/cc-sdd"
  description: "Spec-driven development (SDD) for your team's workflow. Kiro style commands that enforce structured requirements→design→tasks workflow and steering, transforming how you build with AI. Support Claude Code, Codex, Opencode, Cursor, Github Copilot, Gemini CLI and Windsurf. "
  stars: 2965
  forks: 231
  open_issues: 15
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-08"
  created: "2025-07-17"
  topics: ["claude-code", "codex", "cursor", "gemini-cli", "github-copilot", "kiro", "opencode", "slash-commands", "spec", "spec-driven-development", "steering", "subagents"]
---

# gotalab/cc-sdd

> Discovered by arsenal scout — awaiting manual triage

## Description

Spec-driven development (SDD) for your team's workflow. Kiro style commands that enforce structured requirements→design→tasks workflow and steering, transforming how you build with AI. Support Claude Code, Codex, Opencode, Cursor, Github Copilot, Gemini CLI and Windsurf. 

## README Excerpt

# cc-sdd: Spec-driven development for your team's workflow

<!-- npm badges -->
[![npm version](https://img.shields.io/npm/v/cc-sdd?logo=npm)](https://www.npmjs.com/package/cc-sdd?activeTab=readme)
[![install size](https://packagephobia.com/badge?p=cc-sdd)](https://packagephobia.com/result?p=cc-sdd)
[![license: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

<div align="center" style="font-size: 1.1rem; margin-bottom: 1rem;"><sub>
<a href="./tools/cc-sdd/README.md">English</a> | <a href="./tools/cc-sdd/README_ja.md">日本語</a> | <a href="./tools/cc-sdd/README_zh-TW.md">繁體中文</a>
</sub></div>

## Transform AI coding agents into production-ready spec-driven development

**One command. Hours instead of weeks. Requirements → Design → Tasks → Implementation.**

👻 **Kiro-inspired** — Similar Spec-Driven, AI-DLC style as Kiro IDE, so existing Kiro specs remain compatible and portable.

Stop losing 70% of development time to meetings, documentation ceremonies, and scattered context. cc-sdd brings structured **AI-DLC** (AI-Driven Development Lifecycle) and **Spec-Driven Development** to Claude Code, Cursor, Gemini CLI, Codex CLI, GitHub Copilot, Qwen Code, OpenCode, and Windsurf.

### What you get:
- ✅ **Spec-first guarantees** — Approve requirements/design upfront, then AI implements exactly as specified
- ✅ **Parallel execution ready** — Tasks decomposed for concurrent implementation with dependency tracking
- ✅ **Team-aligned templates** — Customize once, all agents output docs that fit your approval process
- ✅ **Project Memory** — AI remembers your architecture, patterns, and standards across sessions
- ✅ **8 agents, unified workflow** — Same spec-driven process across Claude, Cursor, Gemini, Codex, Copilot, Qwen, OpenCode, Windsurf
- ✅ **Hours instead of weeks** — Feature planning goes from days to hours with AI-assisted specs

## 🚀 Quick Start

```bash
# Run in your project root directory
cd your-project
npx cc-sdd@latest --claude --lang en ## Claude Code

# ✅ That's it! Now run: /kiro:spec-init <what-to-build>
```

**Installation takes 30 seconds.** Supports 8 agents (Claude (Commands / Subagents), Cursor, Gemini, Codex, Copilot, Qwen, OpenCode, Windsurf) × 13 languages.

📖 **Next steps:** [All installation options](#%EF%B8%8F-advanced-installation) | [Command Reference](docs/guides/command-reference.md) | [Spec-Driven Guide](docs/guides/spec-driven.md)

## 📋 See It In Action

### Example: Building a new Photo Albums Feature

```bash
/kiro:spec-init Photo albums with upload, tagging, and sharing
/kiro:spec-requirements photo-albums-en
/kiro:spec-design photo-albums-en -y
/kiro:spec-tasks photo-albums-en -y
```

**Generated in 10 minutes:**
- ✅ [requirements.md](.kiro/specs/photo-albums-en/requirements.md) — 15 EARS-format requirements
- ✅ [design.md](.kiro/specs/photo-albums-en/design.md) — Architecture with Mermaid diagrams
- ✅ [tasks.md](.kiro/specs/photo-albums-en/tasks.md) — 12 implementation tasks with dependencies

Want to 

## Links

- Repository: https://github.com/gotalab/cc-sdd
