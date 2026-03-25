---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code agent subagent"
  quality_score: 72
  scoring_breakdown:
    stars: 17
    recency: 25
    docs: 20
    community: 10
github_data:
  full_name: "undeadlist/claude-code-agents"
  url: "https://github.com/undeadlist/claude-code-agents"
  description: "Claude Code Agents Prompt templates for Claude Code's subagent system. Run parallel code audits, automate fix cycles, get stuff reviewed. Built for the Claude Code Task tool. Not a framework. Just prompts that work. What This Does Claude Code can spawn subagents via Task(). These are the prompts those agents receive."
  stars: 92
  forks: 6
  open_issues: 0
  language: "Shell"
  license: "MIT"
  last_push: "2026-03-22"
  created: "2025-12-24"
  topics: []
---

# undeadlist/claude-code-agents

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Code Agents Prompt templates for Claude Code's subagent system. Run parallel code audits, automate fix cycles, get stuff reviewed. Built for the Claude Code Task tool. Not a framework. Just prompts that work. What This Does Claude Code can spawn subagents via Task(). These are the prompts those agents receive.

## README Excerpt

# Complete E2E Development Workflow

[![Claude Code Ready](badges/claude-code-ready.svg)](https://undeadlist.com) [![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)

## For Solo Dev Startups Building with Next.js + Claude Code

![Parallel Audit Demo](./assets/terminal-demo.svg)

> **Target User:** Solo dev running a startup, only engineer, entire company.
> **Goal:** Pull this repo into any project and have a full agent team ready to go.
> **Designed for:** Next.js / React / TypeScript full-stack web apps (Prisma, npm/pnpm, Vercel).
> Other stacks can adapt the agent prompts, but examples and tooling defaults target this stack.
> **Built by:** Paul @ UndeadList — learned the hard way what works.

---

## The Reality Check

You're a solo dev. You don't have:
- A QA team
- A code reviewer
- A DevOps engineer
- Time to waste on AI agents going rogue

This workflow package gives you all of that via Claude Code subagents, with strict protocols to prevent the bullshit that wastes your time.

---

## What's In This Repo

```
claude-code-agents/
├── .claude-plugin/
│   ├── plugin.json                 # Plugin manifest
│   └── marketplace.json            # Marketplace config
│
├── agents/                         # 24 agent definitions
│   ├── # AUDIT AGENTS (11 - run in parallel)
│   ├── code-auditor.md             # Code quality, DRY, complexity
│   ├── bug-auditor.md              # Runtime bugs, auth gaps
│   ├── security-auditor.md         # OWASP deep scan
│   ├── doc-auditor.md              # Documentation gaps
│   ├── infra-auditor.md            # Config, env vars, headers
│   ├── ui-auditor.md               # Accessibility, UX
│   ├── db-auditor.md               # Database, N+1, indexes
│   ├── perf-auditor.md             # Performance, bundle size
│   ├── dep-auditor.md              # Dependencies, vulnerabilities
│   ├── seo-auditor.md              # SEO, meta tags, OpenGraph
│   ├── api-tester.md               # API endpoint testing
│   ├── # FIX/IMPLEMENT AGENTS (4)
│   ├── fix-planner.md              # Prioritizes findings into FIXES.md
│   ├── code-fixer.md               # Implements fixes
│   ├── test-runner.md              # Validates fixes
│   ├── test-writer.md              # Auto-generates tests
│   ├── # BROWSER AGENTS (4 - Chrome integration)
│   ├── browser-qa-agent.md         # Navigates UI, finds console errors
│   ├── fullstack-qa-orchestrator.md  # Find → Fix → Verify loop
│   ├── console-monitor.md          # Real-time console watching
│   ├── visual-diff.md              # Screenshot comparison
│   ├── # DEPLOY AGENTS (2)
│   ├── deploy-checker.md           # Pre-deployment validation
│   ├── env-validator.md            # Environment configuration
│   ├── # UTILITY AGENTS (2)
│   ├── pr-writer.md                # PR description generator
│   ├── seed-generator.md           # Test data creation
│   └── # SUPERVISORS (1)
│   └── architect-reviewer.md   

## Links

- Repository: https://github.com/undeadlist/claude-code-agents
