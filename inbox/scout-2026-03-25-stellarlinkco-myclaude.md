---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code workflow"
  quality_score: 83
  scoring_breakdown:
    stars: 29
    recency: 20
    docs: 20
    community: 14
github_data:
  full_name: "stellarlinkco/myclaude"
  url: "https://github.com/stellarlinkco/myclaude"
  description: "Multi-agent orchestration workflow (Claude Code  Codex Gemini OpenCode)"
  stars: 2523
  forks: 286
  open_issues: 6
  language: "Go"
  license: "AGPL-3.0"
  last_push: "2026-03-05"
  created: "2025-07-17"
  topics: []
---

# stellarlinkco/myclaude

> Discovered by arsenal scout — awaiting manual triage

## Description

Multi-agent orchestration workflow (Claude Code  Codex Gemini OpenCode)

## README Excerpt

[中文](README_CN.md) [English](README.md)

# Claude Code Multi-Agent Workflow System

[![Run in Smithery](https://smithery.ai/badge/skills/stellarlinkco)](https://smithery.ai/skills?ns=stellarlinkco&utm_source=github&utm_medium=badge)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Claude Code](https://img.shields.io/badge/Claude-Code-blue)](https://claude.ai/code)
[![Version](https://img.shields.io/badge/Version-6.x-green)](https://github.com/stellarlinkco/myclaude)

> AI-powered development automation with multi-backend execution (Codex/Claude/Gemini/OpenCode)

## Quick Start

```bash
npx github:stellarlinkco/myclaude
```

## Modules Overview

| Module | Description | Documentation |
|--------|-------------|---------------|
| [do](skills/do/README.md) | **Recommended** - 5-phase feature development with codeagent orchestration | `/do` command |
| [omo](skills/omo/README.md) | Multi-agent orchestration with intelligent routing | `/omo` command |
| [bmad](agents/bmad/README.md) | BMAD agile workflow with 6 specialized agents | `/bmad-pilot` command |
| [requirements](agents/requirements/README.md) | Lightweight requirements-to-code pipeline | `/requirements-pilot` command |
| [essentials](agents/development-essentials/README.md) | 11 core dev commands: ask, bugfix, code, debug, docs, enhance-prompt, optimize, refactor, review, test, think | `/code`, `/debug`, etc. |
| [sparv](skills/sparv/README.md) | SPARV workflow (Specify→Plan→Act→Review→Vault) | `/sparv` command |
| course | Course development (combines dev + product-requirements + test-cases) | Composite module |
| claudekit | ClaudeKit: do skill + global hooks (pre-bash, inject-spec, log-prompt) | Composite module |

### Available Skills

Individual skills can be installed separately via `npx github:stellarlinkco/myclaude --list` (skills bundled in modules like do, omo, sparv are listed above):

| Skill | Description |
|-------|-------------|
| browser | Browser automation for web testing and data extraction |
| codeagent | codeagent-wrapper invocation for multi-backend AI code tasks |
| codex | Direct Codex backend execution |
| dev | Lightweight end-to-end development workflow |
| gemini | Direct Gemini backend execution |
| product-requirements | Interactive PRD generation with quality scoring |
| prototype-prompt-generator | Structured UI/UX prototype prompt generation |
| skill-install | Install skills from GitHub with security scanning |
| test-cases | Comprehensive test case generation from requirements |

## Installation

```bash
# Interactive installer (recommended)
npx github:stellarlinkco/myclaude

# List installable items (modules / skills / wrapper)
npx github:stellarlinkco/myclaude --list

# Detect installed modules and update from GitHub
npx github:stellarlinkco/myclaude --update

# Custom install directory / overwrite
npx github:stellarlinkco/myclaude --install-dir ~/.claude --force
```

`--update` detects

## Links

- Repository: https://github.com/stellarlinkco/myclaude
