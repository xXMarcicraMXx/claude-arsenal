---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code hook"
  quality_score: 73
  scoring_breakdown:
    stars: 21
    recency: 25
    docs: 20
    community: 7
github_data:
  full_name: "vibeeval/vibecosystem"
  url: "https://github.com/vibeeval/vibecosystem"
  description: "121 agents, 223 skills, 49 hooks — AI software team built on Claude Code. No custom model. No custom API. Just good engineering."
  stars: 294
  forks: 22
  open_issues: 5
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2026-03-14"
  topics: ["ai-agents", "ai-software-team", "automation", "claude-code", "claude-skills", "developer-tools", "hooks", "multi-agent", "open-source", "self-learning", "vibe-coding", "vibecoding"]
---

# vibeeval/vibecosystem

> Discovered by arsenal scout — awaiting manual triage

## Description

121 agents, 223 skills, 49 hooks — AI software team built on Claude Code. No custom model. No custom API. Just good engineering.

## README Excerpt

<div align="center">

# vibecosystem

**Your AI software team. Built on Claude Code.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Agents](https://img.shields.io/badge/agents-121-blue.svg)](#agents)
[![Skills](https://img.shields.io/badge/skills-223-green.svg)](#skills)
[![Hooks](https://img.shields.io/badge/hooks-49-orange.svg)](#hooks)
[![Rules](https://img.shields.io/badge/rules-21-red.svg)](#rules)
[![Validate](https://github.com/vibeeval/vibecosystem/actions/workflows/validate.yml/badge.svg)](https://github.com/vibeeval/vibecosystem/actions/workflows/validate.yml)

[Turkce](#turkce) | [English](#english) | [Espanol](docs/README_ES.md) | [Francais](docs/README_FR.md) | [Deutsch](docs/README_DE.md) | [Portugues](docs/README_PT.md) | [Italiano](docs/README_IT.md) | [Nederlands](docs/README_NL.md) | [中文](docs/README_ZH.md) | [日本語](docs/README_JA.md) | [한국어](docs/README_KO.md) | [العربية](docs/README_AR.md) | [हिन्दी](docs/README_HI.md) | [Русский](docs/README_RU.md)

![vibecosystem](assets/gif1-numbers.gif)

</div>

vibecosystem turns Claude Code into a full AI software team — 121 specialized agents that plan, build, review, test, and learn from every mistake. No configuration needed — just install and code.

> **v1.4**: 2 new agents (browser-agent, harvest) + 9 new skills + 3 MCP integrations (browser-use, codebase-memory, crawl4ai) + security-reviewer hard exclusions + experiment loop. See [UPGRADING.md](UPGRADING.md) for details.

## The Problem

Claude Code is powerful, but it's one assistant. You prompt, it responds, you review. For complex projects you need a planner, a reviewer, a security auditor, a tester — and you end up being all of them yourself.

## The Solution

vibecosystem is a complete [Claude Code](https://docs.anthropic.com/en/docs/claude-code) ecosystem that creates a self-organizing AI team:

1. **121 agents** — specialized roles from frontend-dev to security-analyst
2. **223 skills** — reusable knowledge from TDD workflows to Kubernetes patterns
3. **49 hooks** — TypeScript sensors that observe, filter, and inject context
4. **21 rules** — behavioral guidelines that shape every agent's output
5. **Self-learning** — every error becomes a rule, automatically

After setup, you say "build a feature" and 20+ agents coordinate across 5 phases.

<a name="english"></a>

## Quick Start

```bash
git clone https://github.com/vibeeval/vibecosystem.git
cd vibecosystem
./install.sh
```

That's it. Use Claude Code normally. The team activates.

## How It Works

```
YOU SAY SOMETHING                VIBECOSYSTEM ACTIVATES              RESULT
┌──────────────┐                 ┌──────────────────────┐            ┌──────────┐
│ "add a new   │──→ Intent ──→  │ Phase 1: scout +     │──→ Code   │ Feature  │
│  feature"    │   Classifier   │   architect plan     │   Written │ built,   │
│              │                 │ Phase 2: backend-dev │   Tested  │ reviewed,│
│              

## Links

- Repository: https://github.com/vibeeval/vibecosystem
