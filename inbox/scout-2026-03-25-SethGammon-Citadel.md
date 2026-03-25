---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code hook"
  quality_score: 74
  scoring_breakdown:
    stars: 21
    recency: 25
    docs: 20
    community: 8
github_data:
  full_name: "SethGammon/Citadel"
  url: "https://github.com/SethGammon/Citadel"
  description: "Agent orchestration harness for Claude Code. Four-tier routing (/do), campaign persistence across sessions, parallel agents in isolated worktrees, discovery relay between waves, lifecycle hooks, circuit breaker, and 6 production-quality skills. From solo developer to institutional scale."
  stars: 320
  forks: 34
  open_issues: 1
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2026-03-20"
  topics: []
---

# SethGammon/Citadel

> Discovered by arsenal scout — awaiting manual triage

## Description

Agent orchestration harness for Claude Code. Four-tier routing (/do), campaign persistence across sessions, parallel agents in isolated worktrees, discovery relay between waves, lifecycle hooks, circuit breaker, and 6 production-quality skills. From solo developer to institutional scale.

## README Excerpt

# Citadel — Agent Orchestration Harness for Claude Code

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Node.js 18+](https://img.shields.io/badge/Node.js-18%2B-green.svg)](https://nodejs.org/)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-blueviolet.svg)](https://docs.anthropic.com/en/docs/claude-code)

Run autonomous coding campaigns with Claude Code. Route any task through the right tool at the right scale — from a one-line fix to a multi-day parallel campaign.

**25 skills | 4 autonomous agents | 10 lifecycle hooks | campaign persistence | fleet coordination**

<img src="assets/citadel-overview.svg" width="100%" alt="Citadel system overview — app creation pipeline and safety systems" />

## Quickstart

**Prerequisites:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code) + [Node.js 18+](https://nodejs.org/)

Citadel is a Claude Code **plugin** — install once, works across all your projects. No per-project file copying.

```bash
# 1. Clone Citadel
git clone https://github.com/SethGammon/Citadel.git

# 2. Launch Claude Code with the plugin loaded
claude --plugin-dir /path/to/Citadel

# 3. Run setup (inside any project)
/do setup

# 4. Try something
/do review src/main.ts
```

For persistent install across all sessions, use the marketplace method inside Claude Code:
```
/plugin marketplace add /path/to/Citadel
/plugin install citadel@citadel-local
/reload-plugins
```

[Full install guide →](QUICKSTART.md)

## Try These First

```
/do fix the typo on line 42        # Direct edit, zero overhead
/do review the auth module         # 5-pass structured code review
/do why is the API returning 500   # Root cause analysis
/do build a caching layer          # Multi-step orchestrated build
```

Say what you want. `/do` routes it to the cheapest tool that can handle it.

## How It Works

You type what you want. `/do` classifies your intent and picks the cheapest tool that can handle it — no menus, no flags, no routing decisions on your end.

```
You say:                               Citadel runs:
─────────────────────────────────────────────────────────────
"fix the typo on line 42"          →   Direct edit (zero overhead)
"review the auth module"           →   /review (5-pass code review)
"add payments to my app"           →   /create-app tier 5 (feature addition)
"build me a recipe app"            →   /create-app → /prd → /architect → /archon
"overhaul all three services"      →   /fleet (parallel agents)
```

Simple tasks get simple tools. Complex tasks get campaigns with phases, verification, and self-correction. You never have to choose.

## The Orchestration Ladder

Four tiers. Use the cheapest one that fits.

<table>
<tr>
<td width="50%" align="center">
<img src="assets/card-skill.svg" width="400" alt="Skill — Domain Expert" />
</td>
<td width="50%" align="center">
<img src="assets/card-marshal.svg" width="400" alt="Marshal — Session Commander" />
</td>
</tr>
<tr>
<td width="50%" ali

## Links

- Repository: https://github.com/SethGammon/Citadel
