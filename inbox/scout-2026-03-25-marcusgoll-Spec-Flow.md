---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code bash automation"
  quality_score: 54
  scoring_breakdown:
    stars: 16
    recency: 8
    docs: 20
    community: 10
github_data:
  full_name: "marcusgoll/Spec-Flow"
  url: "https://github.com/marcusgoll/Spec-Flow"
  description: "Turn product ideas into production launches with Spec-Driven Development. Repeatable Claude Code workflows with quality gates, token budgets, and auditable artifacts."
  stars: 73
  forks: 9
  open_issues: 1
  language: "Shell"
  license: "MIT"
  last_push: "2025-12-16"
  created: "2025-10-04"
  topics: ["ai-agents", "ai-assisted-development", "ai-workflows", "automation", "bash", "claude", "claude-ai", "claude-code", "developer-tools", "documentation", "powershell", "productivity", "spec-driven-development", "workflow", "workflow-automation"]
---

# marcusgoll/Spec-Flow

> Discovered by arsenal scout — awaiting manual triage

## Description

Turn product ideas into production launches with Spec-Driven Development. Repeatable Claude Code workflows with quality gates, token budgets, and auditable artifacts.

## README Excerpt

<div align="center">
  <h1>Spec-Flow</h1>
  <p><strong>Ship features faster with AI-powered spec-driven development.</strong></p>

  <p>
    <a href="https://www.npmjs.com/package/spec-flow">
      <img src="https://img.shields.io/npm/v/spec-flow.svg?logo=npm&color=CB3837" alt="npm package">
    </a>
    <a href="https://github.com/marcusgoll/Spec-Flow/blob/main/LICENSE">
      <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT">
    </a>
    <a href="https://github.com/marcusgoll/Spec-Flow/actions/workflows/ci.yml">
      <img src="https://img.shields.io/github/actions/workflow/status/marcusgoll/Spec-Flow/ci.yml?branch=main" alt="CI Status">
    </a>
    <a href="https://github.com/marcusgoll/Spec-Flow/stargazers">
      <img src="https://img.shields.io/github/stars/marcusgoll/Spec-Flow?style=social" alt="GitHub Stars">
    </a>
  </p>
</div>

---

Spec-Flow is a workflow toolkit for [Claude Code](https://claude.ai/code) that transforms how you build software with AI. Instead of ad-hoc prompting, you get a structured pipeline that takes ideas from specification to production.

```
/feature "add user authentication"
```

That's it. Spec-Flow handles the rest: writing specs, planning architecture, breaking down tasks, implementing with TDD, running quality gates, and deploying.

## Why Spec-Flow?

| Without Spec-Flow | With Spec-Flow |
|-------------------|----------------|
| "What were we building again?" | Every decision tracked in NOTES.md |
| Features shipped without tests | TDD enforced, quality gates block bad code |
| Context bloat slows Claude down | Auto-compaction keeps context efficient |
| Each feature starts from scratch | Reusable patterns, proven workflows |
| "Did we test this? Who approved?" | Auditable artifacts for every phase |

## Quick Start

### 1. Install

```bash
npx spec-flow init
```

This copies workflow files directly into your project (`.claude/`, `.spec-flow/`, `CLAUDE.md`). No dependency is added to your `package.json` — Spec-Flow becomes part of your codebase.

### 2. Build your first feature

```bash
/feature "add dark mode toggle"
```

Spec-Flow runs you through:

```
spec → plan → tasks → implement → optimize → ship
```

Each phase produces artifacts, runs quality checks, and hands off cleanly to the next.

### 3. That's it

Your feature is deployed. All decisions documented. Tests passing. Ready for the next one.

### Staying Updated

Check for updates anytime:

```bash
npx spec-flow status
```

Update to the latest version:

```bash
npx spec-flow update
```

For CI/CD pipelines, use `--check` to fail if outdated:

```bash
npx spec-flow status --check
```

---

## The Workflow

### Features (< 16 hours)

For focused work on a single subsystem:

```bash
/feature "user profile editing"     # Start the workflow
/feature continue                   # Resume after a break
```

### Epics (> 16 hours)

For complex work spanning multiple subsystems:

```bash
/epic "OAuth 2.1 authentication"  

## Links

- Repository: https://github.com/marcusgoll/Spec-Flow
- Homepage: https://github.com/marcusgoll/Spec-Flow
