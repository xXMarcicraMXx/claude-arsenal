---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code configuration"
  quality_score: 62
  scoring_breakdown:
    stars: 17
    recency: 15
    docs: 20
    community: 10
github_data:
  full_name: "eticmedya/uces"
  url: "https://github.com/eticmedya/uces"
  description: "Production-grade configuration system for Claude Code CLI with smart routing, skill modules, and automation hooks."
  stars: 107
  forks: 6
  open_issues: 0
  language: "Shell"
  license: "MIT"
  last_push: "2026-02-04"
  created: "2026-02-04"
  topics: []
---

# eticmedya/uces

> Discovered by arsenal scout — awaiting manual triage

## Description

Production-grade configuration system for Claude Code CLI with smart routing, skill modules, and automation hooks.

## README Excerpt

# UCES - Universal Claude Enhancement System

> Transform your Claude Code CLI into a production-grade development powerhouse.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude-Code-purple.svg)](https://claude.ai)

## What is UCES?

UCES is a battle-tested configuration framework that supercharges Claude Code with:

- **Smart Routing** - Automatically dispatches tasks to specialized skill modules
- **Zero-Tolerance Mode** - Eliminates incomplete code, placeholder implementations, and technical debt
- **Skill Modules** - Domain-specific knowledge packs for UI, API, Mobile, DevOps, and more
- **Automation Hooks** - Pre/post execution scripts for validation, formatting, and safety checks
- **Session Intelligence** - Remembers project context and learnings across sessions

## Installation

### One-Line Install

```bash
curl -fsSL https://raw.githubusercontent.com/eticmedya/uces/main/setup.sh | bash
```

### Manual Installation

```bash
git clone https://github.com/eticmedya/uces.git
cd uces
chmod +x setup.sh
./setup.sh
```

## Architecture

```
~/.claude/
├── CLAUDE.md              # Core directives
├── CONVENTIONS.md         # Code quality rules
├── config.json            # Runtime configuration
├── skills/                # Skill modules
│   ├── ui/               # React, Next.js, Tailwind
│   ├── api/              # REST, GraphQL, Webhooks
│   ├── native/           # React Native, Expo
│   ├── debug/            # Testing, debugging
│   ├── guard/            # Security, authentication
│   ├── architect/        # System design, planning
│   ├── data/             # Analytics, queries
│   └── devops/           # CI/CD, deployment
├── hooks/                 # Automation scripts
│   ├── init.sh           # Session initialization
│   ├── validate.sh       # Pre-execution checks
│   ├── format.sh         # Post-edit formatting
│   └── commit-check.sh   # Pre-commit validation
└── modules/               # Extension modules
```

## Skill Modules

| Module | Triggers | Description |
|--------|----------|-------------|
| `ui` | component, page, form, button, React, Tailwind | Frontend development with React/Next.js |
| `api` | endpoint, route, database, REST, GraphQL | Backend APIs and server logic |
| `native` | mobile, Expo, React Native, iOS, Android | Cross-platform mobile apps |
| `debug` | bug, error, fix, test, failing | Debugging and test automation |
| `guard` | auth, security, permission, OWASP | Security hardening and auth flows |
| `architect` | design, plan, architecture, PRD | System design and technical specs |
| `data` | analytics, metrics, query, dashboard | Data analysis and reporting |
| `devops` | deploy, CI/CD, Docker, pipeline | Infrastructure and deployment |

## Zero-Tolerance Mode

UCES enforces production-quality standards:

### Prohibited Patterns
```
[X] Mock data in production code
[X] TODO/FIXME comments
[X] Empty event handlers
[X] Missing error boun

## Links

- Repository: https://github.com/eticmedya/uces
