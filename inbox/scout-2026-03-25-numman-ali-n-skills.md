---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code plugin"
  quality_score: 83
  scoring_breakdown:
    stars: 25
    recency: 25
    docs: 20
    community: 13
github_data:
  full_name: "numman-ali/n-skills"
  url: "https://github.com/numman-ali/n-skills"
  description: "Curated plugin marketplace for AI agents - works with Claude Code, Codex, and openskills"
  stars: 942
  forks: 92
  open_issues: 9
  language: "TypeScript"
  license: "Apache-2.0"
  last_push: "2026-03-22"
  created: "2026-01-02"
  topics: []
---

# numman-ali/n-skills

> Discovered by arsenal scout — awaiting manual triage

## Description

Curated plugin marketplace for AI agents - works with Claude Code, Codex, and openskills

## README Excerpt

<div align="center">

<img src="./assets/logo.svg" alt="n-skills" width="400"/>

<br/>
<br/>

**Curated by [Numman Ali](https://x.com/nummanali)**

[![Twitter Follow](https://img.shields.io/twitter/follow/nummanali?style=social)](https://x.com/nummanali)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![agentskills.io](https://img.shields.io/badge/format-agentskills.io-purple.svg)](https://agentskills.io)
[![AGENTS.md](https://img.shields.io/badge/discovery-AGENTS.md-green.svg)](https://www.infoq.com/news/2025/08/agents-md/)

**One marketplace. Every agent.**

[Install](#-quick-start) · [Skills](#-available-skills) · [Submit a Skill](#-want-to-be-featured) · [Philosophy](#-philosophy)

</div>

---

## 💡 Philosophy

> **"Write once. Run everywhere."**

AI coding agents are evolving fast, and each has its own way of doing things:

```
Claude Code    →  CLAUDE.md, .claude/skills/
GitHub Copilot →  AGENTS.md, copilot-instructions.md
Codex          →  SKILL.md, ~/.codex/skills/
Cursor         →  .cursor/rules/*.mdc
Windsurf       →  Cascade Rules, Memories
Cline          →  .clinerules
Factory/Droid  →  .factory/droids/*.md
OpenCode       →  .opencode/skill/, opencode.json
```

### The n-skills Way

We embrace the diversity with a universal approach:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   SKILL.md          →  The universal skill format      │
│   AGENTS.md         →  The universal discovery file    │
│   openskills        →  The universal installer         │
│                                                         │
│   Write once. Run everywhere.                          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

[AGENTS.md](https://www.infoq.com/news/2025/08/agents-md/) is now adopted by **20,000+ repositories** and natively supported by GitHub Copilot, Google Gemini, OpenAI Codex, Factory Droid, Cursor, and more.

**n-skills is a curated marketplace.** Install via [openskills](https://github.com/numman-ali/openskills) or use your agent's native installer — your choice!

---

## 🚀 Quick Start

### Claude Code

```bash
/plugin marketplace add numman-ali/n-skills
```

Then install any skill:
```bash
/plugin install orchestration@n-skills
/plugin install open-source-maintainer@n-skills
/plugin install gastown@n-skills
/plugin install dev-browser@n-skills
/plugin install zai-cli@n-skills
```

### OpenSkills (Universal)

Works with **every agent**: Claude Code, Cursor, Windsurf, Cline, OpenCode, and anything that reads AGENTS.md.

```bash
npm i -g openskills
openskills install numman-ali/n-skills
openskills sync
```

> **New to OpenSkills?** It's the universal skills installer. [Learn more →](https://github.com/numman-ali/openskills)

<details>
<summary><strong>Other native installers</strong></summary>

**Codex:**
```bash
$skill-installer https://

## Links

- Repository: https://github.com/numman-ali/n-skills
