---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 67
  scoring_breakdown:
    stars: 13
    recency: 25
    docs: 20
    community: 9
github_data:
  full_name: "jrenaldi79/harness-engineering"
  url: "https://github.com/jrenaldi79/harness-engineering"
  description: "Context engineering for coding agents - CLAUDE.md templates, mechanical enforcement, and a field guide to 20+ best practices. Bootstrap with one command."
  stars: 31
  forks: 3
  open_issues: 1
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2026-03-11"
  topics: ["agents-md", "ai-agents", "ai-coding", "claude-code", "claude-md", "codex", "developer-tools", "documentation", "git-hooks", "harness-engineering", "nodejs", "tdd"]
---

# jrenaldi79/harness-engineering

> Discovered by arsenal scout — awaiting manual triage

## Description

Context engineering for coding agents - CLAUDE.md templates, mechanical enforcement, and a field guide to 20+ best practices. Bootstrap with one command.

## README Excerpt

<div align="center">

# Harness Engineering and Best Practices for Coding Agents

**A reference guide and Claude Code plugin for long-running AI coding agent harnesses**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue?labelColor=1A1C29)](./LICENSE)
[![Node.js](https://img.shields.io/badge/node-%3E%3D18.0.0-brightgreen?labelColor=1A1C29)](https://nodejs.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?labelColor=1A1C29)](https://github.com/jrenaldi79/harness-engineering)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey?labelColor=1A1C29)](https://github.com/jrenaldi79/harness-engineering)
[![GitHub last commit](https://img.shields.io/github/last-commit/jrenaldi79/harness-engineering?labelColor=1A1C29)](https://github.com/jrenaldi79/harness-engineering/commits)
[![GitHub stars](https://img.shields.io/github/stars/jrenaldi79/harness-engineering?style=social)](https://github.com/jrenaldi79/harness-engineering)

</div>

[Andrej Karpathy](https://x.com/karpathy/status/2035173492447224237) put it bluntly: "The agents do not listen to my instructions." They bloat abstractions, copy-paste code blocks, and ignore style guidance, no matter how carefully you write your AGENTS.md. If the person who coined "[context engineering](https://x.com/karpathy/status/1937902205765607626)" can't get agents to follow written rules, the answer isn't better prompting. It's mechanical enforcement: git hooks that block bad code before it lands, linters that catch what instructions can't, and rule files that load only when relevant so the agent's finite attention isn't wasted.

Harness engineering is context engineering applied to coding agents: structuring rule files, planning before building, enforcing quality with automation, and keeping documentation in sync with code so the agent stays aligned across long sessions.

This repo contains:

1. **A reference guide** that maps 20+ best practices from [OpenAI](https://openai.com/index/harness-engineering/), [Augment Code](https://www.augmentcode.com/blog/your-agents-context-is-a-junk-drawer), [Anthropic](https://www.threads.com/@boris_cherny/post/DUMZr4VElyb/), and practitioners like [Andrej Karpathy](https://x.com/karpathy/status/1937902205765607626) (AI researcher, co-founder of OpenAI), [Boris Cherny](https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny) (creator of Claude Code), and [Thariq Shihipar](https://x.com/trq212) (Claude Code team at Anthropic) to concrete implementation patterns.

2. **A Claude Code plugin** that configures your developer environment for agent-assisted development. Install the plugin and get two skills that do the actual work:
   - **`/readiness`**: Analyzes any existing codebase and produces a scored readiness report across 8 pillars and 5 maturity levels. Shows you exactly where you stand, what's missing, and what to fix first. Saves reports for delta tracking over time. Work

## Links

- Repository: https://github.com/jrenaldi79/harness-engineering
