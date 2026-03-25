---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 63
  scoring_breakdown:
    stars: 18
    recency: 15
    docs: 20
    community: 10
github_data:
  full_name: "severity1/claude-code-auto-memory"
  url: "https://github.com/severity1/claude-code-auto-memory"
  description: "Claude Code plugin that automatically maintains CLAUDE.md files"
  stars: 125
  forks: 9
  open_issues: 12
  language: "Python"
  license: "MIT"
  last_push: "2026-02-14"
  created: "2025-11-26"
  topics: []
---

# severity1/claude-code-auto-memory

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Code plugin that automatically maintains CLAUDE.md files

## README Excerpt

# claude-code-auto-memory

**Your CLAUDE.md, always in sync.** Minimal tokens. Zero config. Just works.

A Claude Code plugin that watches what Claude Code edits, deletes, and moves - then quietly updates your project memory in the background. No manual maintenance needed.

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blueviolet)](https://claude.ai/code)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Config](https://img.shields.io/badge/setup-zero--config-brightgreen)]()
[![Token Efficient](https://img.shields.io/badge/tokens-minimal--overhead-blue)]()

## The Problem

CLAUDE.md files become stale as codebases evolve:

- Build commands change but memory stays outdated
- Architecture shifts go unrecorded
- Code conventions drift without memory updates
- New team members get incorrect context

**Manual maintenance is tedious and often forgotten.**

## The Solution

claude-code-auto-memory automatically updates CLAUDE.md when Claude Code makes changes. Processing happens in an isolated agent, so it doesn't consume your main conversation's context window.

```
Claude Code edits code -> Plugin tracks changes -> Isolated agent updates memory -> Context stays fresh
```

## Features

- **Automatic sync**: Tracks Edit/Write/Bash operations and updates CLAUDE.md at end of turn
- **Bash operation tracking**: Detects rm, mv, git rm, git mv, unlink commands
- **Minimal-token tracking**: PostToolUse hook has no output; stop hook triggers isolated agent
- **Isolated processing**: Agent runs in separate context window, doesn't consume main session tokens
- **Marker-based updates**: Only modifies AUTO-MANAGED sections, preserves manual content
- **Subtree support**: Hierarchical CLAUDE.md for monorepos

## Installation

### From Marketplace

```bash
claude plugin marketplace add severity1/severity1-marketplace
claude plugin install auto-memory@severity1-marketplace
```

### Local Development

```bash
# Add local marketplace
claude plugin marketplace add /path/to/claude-code-auto-memory/.dev-marketplace/.claude-plugin/marketplace.json

# Install from local
claude plugin install auto-memory@local-dev
```

## Commands

### `/auto-memory:init`

Initialize CLAUDE.md structure for your project with an interactive wizard.

```
/auto-memory:init
```

The wizard will:
1. Analyze your codebase structure
2. Detect frameworks and build commands
3. Identify subtree candidates (for monorepos)
4. Present findings for your approval
5. Generate CLAUDE.md with auto-managed sections

### `/auto-memory:calibrate`

Force a full recalibration of all CLAUDE.md files.

```
/auto-memory:calibrate
```

### `/auto-memory:sync`

Sync CLAUDE.md with manual file changes detected by git. Use this when you've edited files outside Claude Code (in your IDE, terminal, etc.) and want to update memory without a full recalibration.

```
/auto-memory:sync
```

Detects:
- Modified tracked files (`git diff`)
- Staged files (`git diff --

## Links

- Repository: https://github.com/severity1/claude-code-auto-memory
