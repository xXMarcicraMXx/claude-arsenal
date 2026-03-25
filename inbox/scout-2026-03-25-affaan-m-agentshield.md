---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "anthropic mcp server"
  quality_score: 77
  scoring_breakdown:
    stars: 20
    recency: 25
    docs: 20
    community: 12
github_data:
  full_name: "affaan-m/agentshield"
  url: "https://github.com/affaan-m/agentshield"
  description: "AI agent security scanner. Detect vulnerabilities in agent configurations, MCP servers, and tool permissions. Available as CLI, GitHub Action, ECC plugin, and GitHub App integration. 🛡️"
  stars: 216
  forks: 43
  open_issues: 0
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2026-02-11"
  topics: ["ai-agent", "anthropic", "claude-code", "hackathon", "mcp", "opus", "security"]
---

# affaan-m/agentshield

> Discovered by arsenal scout — awaiting manual triage

## Description

AI agent security scanner. Detect vulnerabilities in agent configurations, MCP servers, and tool permissions. Available as CLI, GitHub Action, ECC plugin, and GitHub App integration. 🛡️

## README Excerpt

<div align="center">

<img src="./assets/agentshield-logo.png" alt="AgentShield" width="180" />

# AgentShield

**Security auditor for AI agent configurations**

Scans Claude Code setups for hardcoded secrets, permission misconfigs,<br/>
hook injection, MCP server risks, and agent prompt injection vectors.<br/>
Available as CLI, GitHub Action, and [GitHub App](https://github.com/apps/ecc-tools) integration.

[![npm version](https://img.shields.io/npm/v/ecc-agentshield)](https://www.npmjs.com/package/ecc-agentshield)
[![npm downloads](https://img.shields.io/npm/dm/ecc-agentshield)](https://www.npmjs.com/package/ecc-agentshield)
[![tests](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![coverage](https://img.shields.io/badge/coverage-v8-blue)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[Quick Start](#quick-start) · [What It Catches](#what-it-catches) · [API Reference](#api-reference) · [Opus Pipeline](#opus-46-deep-analysis---opus) · [GitHub Action](#github-action) · [Distribution](#distribution) · [MiniClaw](#miniclaw) · [Changelog](./CHANGELOG.md)

</div>

---

## Why

The AI agent ecosystem is growing faster than its security tooling. In January 2026 alone:

- **12%** of a major agent skill marketplace was malicious (341 of 2,857 community skills)
- A **CVSS 8.8** CVE exposed 17,500+ internet-facing instances to one-click RCE
- The Moltbook breach compromised **1.5M API tokens** across 770,000 agents

Developers install community skills, connect MCP servers, and configure hooks without any automated way to audit the security of their setup. AgentShield scans your `.claude/` directory and flags vulnerabilities before they become exploits.

Built at the [Claude Code Hackathon](https://cerebralvalley.ai/e/claude-code-hackathon) (Cerebral Valley x Anthropic, Feb 2026). Part of the [Everything Claude Code](https://github.com/affaan-m/everything-claude-code) ecosystem (42K+ stars).

## Quick Start

```bash
# Scan your Claude Code config (no install required)
npx ecc-agentshield scan

# Or install globally
npm install -g ecc-agentshield
agentshield scan
```

That's it. AgentShield auto-discovers your `~/.claude/` directory, scans all config files, and prints a graded security report.

Discovery intentionally skips common generated directories such as `node_modules`, build output, and `.dmux` worktree mirrors so transient copies do not duplicate findings.

```
  AgentShield Security Report

  Grade: F (0/100)

  Score Breakdown
  Secrets        ░░░░░░░░░░░░░░░░░░░░ 0
  Permissions    ░░░░░░░░░░░░░░░░░░░░ 0
  Hooks          ░░░░░░░░░░░░░░░░░░░░ 0
  MCP Servers    ░░░░░░░░░░░░░░░░░░░░ 0
  Agents         ░░░░░░░░░░░░░░░░░░░░ 0

  ● CRITICAL  Hardcoded Anthropic API key
    CLAUDE.md:13
    Evidence: sk-ant-a...cdef
    Fix: Replace with environment variable reference [auto-fixable]

  ● CRITICAL  Overly permissive allow rule: Bash(*)
    settings.json
    Evidence: Bash(*)
    Fix: Restrict to specific com

## Links

- Repository: https://github.com/affaan-m/agentshield
- Homepage: https://cerebralvalley.ai/e/claude-code-hackathon
