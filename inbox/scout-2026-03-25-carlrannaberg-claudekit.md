---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code hook"
  quality_score: 68
  scoring_breakdown:
    stars: 24
    recency: 15
    docs: 20
    community: 9
github_data:
  full_name: "carlrannaberg/claudekit"
  url: "https://github.com/carlrannaberg/claudekit"
  description: "A toolkit of custom commands, hooks, and utilities for Claude Code"
  stars: 637
  forks: 103
  open_issues: 10
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-01-15"
  created: "2025-07-11"
  topics: []
---

# carlrannaberg/claudekit

> Discovered by arsenal scout — awaiting manual triage

## Description

A toolkit of custom commands, hooks, and utilities for Claude Code

## README Excerpt

![claudekit banner](assets/banner.png)

# claudekit

> Smart guardrails and workflow automation for Claude Code - catch errors in real-time, save checkpoints, and enhance AI coding with expert subagents

[![npm version](https://img.shields.io/npm/v/claudekit.svg)](https://www.npmjs.com/package/claudekit)
[![npm downloads](https://img.shields.io/npm/dt/claudekit.svg)](https://www.npmjs.com/package/claudekit)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js Version](https://img.shields.io/node/v/claudekit.svg)](https://nodejs.org)
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/hesreallyhim/awesome-claude-code)
[![Buy Me a Coffee](https://img.shields.io/badge/☕-Buy%20me%20a%20coffee-ffdd00?style=flat&logo=buy-me-a-coffee)](https://buymeacoffee.com/carlrannaberg)

## 🚀 Installation

> **⚠️ Requires:** Claude Code **Max plan** (for optimal token usage) • Node.js 20+

```bash
npm install -g claudekit
# or: yarn global add claudekit
# or: pnpm add -g claudekit
```

## ⚡ Quick Start

```bash
# Initialize in your project
claudekit setup

# In Claude Code, try these commands:
/git:status                      # Groups changes by type & suggests commit strategy
/spec:create "your next feature" # Researches codebase & writes full spec
/code-review                     # 6 specialized agents analyze code in parallel
```

## 🎯 What It Does

Claudekit acts as your safety net while coding with Claude:

```
Before: Claude adds 'any' type → ❌ Lost type safety discovered in code review
After:  Claude adds 'any' type → ✅ Instant block: "Use specific type: User | null"

Before: Risky refactor fails → ❌ Git archaeology to find working version  
After:  Risky refactor fails → ✅ One command: /checkpoint:restore

Before: Claude breaks tests → ❌ You discover it after Claude finishes
After:  Claude breaks tests → ✅ Claude sees error immediately and fixes it

Before: Ask Claude to review → ❌ Shallow analysis, general feedback, sequential execution
After:  Use /code-review → ✅ 6 specialized agents analyze in parallel, dynamically pull technology-specific expertise
```

## Key Features

### 🗺️ Instant Codebase Navigation
**Claude sees your entire project structure automatically - skips most discovery searches.**
- **Navigate directly to code** - Jump straight to files, functions, and classes
- **No trial-and-error** - Avoid sifting through test files, docs, and irrelevant matches  
- **Confident code access** - Claude knows exactly what exists and where
- **See relationships** - Claude understands dependencies and architecture instantly
- **Automatic setup** - Runs invisibly on first prompt, updates as you code

[Codebase map guide →](docs/guides/codebase-map.md)

### 🔍 Comprehensive Code Review
- **Multi-aspect analysis**: 6 parallel agents for architecture, security, performance, testing, quality, and documentation
- **Smart targeting**: Automatically s

## Links

- Repository: https://github.com/carlrannaberg/claudekit
