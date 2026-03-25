---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 78
  scoring_breakdown:
    stars: 25
    recency: 20
    docs: 20
    community: 13
github_data:
  full_name: "BayramAnnakov/claude-reflect"
  url: "https://github.com/BayramAnnakov/claude-reflect"
  description: "A self-learning system for Claude Code that captures corrections, positive feedback, and preferences — then syncs them to CLAUDE.md and AGENTS.md."
  stars: 843
  forks: 64
  open_issues: 6
  language: "Python"
  license: "MIT"
  last_push: "2026-03-16"
  created: "2026-01-03"
  topics: ["claude-code", "claude-skills", "memory", "productivity", "self-learning"]
---

# BayramAnnakov/claude-reflect

> Discovered by arsenal scout — awaiting manual triage

## Description

A self-learning system for Claude Code that captures corrections, positive feedback, and preferences — then syncs them to CLAUDE.md and AGENTS.md.

## README Excerpt

# claude-reflect

[![GitHub stars](https://img.shields.io/github/stars/BayramAnnakov/claude-reflect?style=flat-square)](https://github.com/BayramAnnakov/claude-reflect/stargazers)
[![Version](https://img.shields.io/badge/version-2.6.0-blue?style=flat-square)](https://github.com/BayramAnnakov/claude-reflect/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-160%20passing-brightgreen?style=flat-square)](https://github.com/BayramAnnakov/claude-reflect/actions)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey?style=flat-square)](https://github.com/BayramAnnakov/claude-reflect#platform-support)

A self-learning system for Claude Code that captures corrections and discovers workflow patterns — turning them into permanent memory and reusable skills.

## What it does

### 1. Learn from Corrections

When you correct Claude ("no, use gpt-5.1 not gpt-5"), it remembers forever.

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  You correct    │ ──► │  Hook captures  │ ──► │  /reflect adds  │
│  Claude Code    │     │  to queue       │     │  to CLAUDE.md   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
      (automatic)            (automatic)            (manual review)
```

### 2. Discover Workflow Patterns (NEW in v2)

Analyzes your session history to find repeating tasks that could become reusable commands.

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Your past      │ ──► │ /reflect-skills │ ──► │   Generates     │
│  sessions       │     │ finds patterns  │     │   /commands     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
    (68 sessions)         (AI-powered)            (you approve)
```

Example: You've asked "review my productivity" 12 times → suggests creating `/daily-review`

## Key Features

| Feature | What it does |
|---------|--------------|
| **Permanent Memory** | Corrections sync to CLAUDE.md — Claude remembers across sessions |
| **Skill Discovery** | Finds repeating patterns in your history → generates commands |
| **Multi-language** | AI understands corrections in any language |
| **Skill Improvement** | Corrections during `/deploy` improve the deploy skill itself |

## Installation

```bash
# Add the marketplace
claude plugin marketplace add bayramannakov/claude-reflect

# Install the plugin
claude plugin install claude-reflect@claude-reflect-marketplace

# IMPORTANT: Restart Claude Code to activate the plugin
```

After installation, **restart Claude Code** (exit and reopen). Then hooks auto-configure and commands are ready.

> **First run?** When you run `/reflect` for the first time, you'll be prompted to scan your past sessions for learnings.

### Prerequisites

- [Claude Code](https://claude.ai/code) CLI installed
- Python 3.6+ (included on most systems)

### Pl

## Links

- Repository: https://github.com/BayramAnnakov/claude-reflect
