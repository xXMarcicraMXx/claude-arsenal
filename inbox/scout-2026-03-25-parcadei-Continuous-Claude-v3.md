---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code hook"
  quality_score: 79
  scoring_breakdown:
    stars: 30
    recency: 15
    docs: 20
    community: 14
github_data:
  full_name: "parcadei/Continuous-Claude-v3"
  url: "https://github.com/parcadei/Continuous-Claude-v3"
  description: "Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows."
  stars: 3624
  forks: 281
  open_issues: 41
  language: "Python"
  license: "MIT"
  last_push: "2026-01-26"
  created: "2025-12-23"
  topics: ["agents", "claude-code", "claude-code-cli", "claude-code-hooks", "claude-code-mcp", "claude-code-skills", "claude-code-subagents", "claude-skills", "mcp"]
---

# parcadei/Continuous-Claude-v3

> Discovered by arsenal scout — awaiting manual triage

## Description

Context management for Claude Code. Hooks maintain state via ledgers and handoffs. MCP execution without context pollution. Agent orchestration with isolated context windows.

## README Excerpt

# Continuous Claude

> A persistent, learning, multi-agent development environment built on Claude Code

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude-Code-orange.svg)](https://claude.ai/code)
[![Skills](https://img.shields.io/badge/Skills-109-green.svg)](#skills-system)
[![Agents](https://img.shields.io/badge/Agents-32-purple.svg)](#agents-system)
[![Hooks](https://img.shields.io/badge/Hooks-30-blue.svg)](#hooks-system)

**Continuous Claude** transforms Claude Code into a continuously learning system that maintains context across sessions, orchestrates specialized agents, and eliminates wasting tokens through intelligent code analysis.

## Table of Contents

- [Why Continuous Claude?](#why-continuous-claude)
- [Design Principles](#design-principles)
- [How to Talk to Claude](#how-to-talk-to-claude)
- [Quick Start](#quick-start)
- [Architecture](#architecture)
- [Core Systems](#core-systems)
  - [Skills (109)](#skills-system)
  - [Agents (32)](#agents-system)
  - [Hooks (30)](#hooks-system)
  - [TLDR Code Analysis](#tldr-code-analysis)
  - [Memory System](#memory-system)
  - [Continuity System](#continuity-system)
  - [Math System](#math-system)
- [Workflows](#workflows)
- [Installation](#installation)
- [Updating](#updating)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## Why Continuous Claude?

Claude Code has a **compaction problem**: when context fills up, the system compacts your conversation, losing nuanced understanding and decisions made during the session.

**Continuous Claude solves this with:**

| Problem | Solution |
|---------|----------|
| Context loss on compaction | YAML handoffs - more token-efficient transfer |
| Starting fresh each session | Memory system recalls + daemon auto-extracts learnings |
| Reading entire files burns tokens | 5-layer code analysis + semantic index |
| Complex tasks need coordination | Meta-skills orchestrate agent workflows |
| Repeating workflows manually | 109 skills with natural language triggers |

**The mantra: Compound, don't compact.** Extract learnings automatically, then start fresh with full context.

### Why "Continuous"? Why "Compounding"?

The name is a pun. **Continuous** because Claude maintains state across sessions. **Compounding** because each session makes the system smarter—learnings accumulate like compound interest.

---

## Design Principles

An agent is five things: **Prompt + Tools + Context + Memory + Model**.

| Component | What We Optimize |
|-----------|------------------|
| **Prompt** | Skills inject relevant context; hooks add system reminders |
| **Tools** | TLDR reduces tokens; agents parallelize work |
| **Context** | Not just *what* Claude knows, but *how* it's provided |
| **Memory** | Daemon extracts learnings; recall surfaces them |
| **Model** | Becomes swappable when the other four are solid |

### Anti-Complexity

We resist plugin 

## Links

- Repository: https://github.com/parcadei/Continuous-Claude-v3
