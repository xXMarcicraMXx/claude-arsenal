---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "anthropic mcp server"
  quality_score: 74
  scoring_breakdown:
    stars: 21
    recency: 25
    docs: 20
    community: 8
github_data:
  full_name: "levnikolaevich/claude-code-skills"
  url: "https://github.com/levnikolaevich/claude-code-skills"
  description: "Plugin suite + bundled MCP servers for Claude Code. Full delivery lifecycle: Agile pipeline with multi-model AI review, project bootstrap, documentation generation, codebase audits, performance optimization, community workflows. Includes hex-line (hash-verified editing), hex-graph (code knowledge graph), and hex-ssh (remote SSH) MCP servers."
  stars: 257
  forks: 46
  open_issues: 11
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2025-10-24"
  topics: ["agile-workflows", "ai-agents", "anthropic", "claude-ai", "claude-code", "claude-code-skills", "code-analysis", "code-review", "codebase-audit", "developer-productivity", "developer-tools", "documentation-generator", "mcp", "mcp-server", "model-context-protocol", "performance-optimization", "remote-ssh", "software-architecture", "tree-sitter", "workflow-automation"]
---

# levnikolaevich/claude-code-skills

> Discovered by arsenal scout — awaiting manual triage

## Description

Plugin suite + bundled MCP servers for Claude Code. Full delivery lifecycle: Agile pipeline with multi-model AI review, project bootstrap, documentation generation, codebase audits, performance optimization, community workflows. Includes hex-line (hash-verified editing), hex-graph (code knowledge graph), and hex-ssh (remote SSH) MCP servers.

## README Excerpt

# Claude Code Skills

![Version](https://img.shields.io/badge/version-2026.03.21-blue)
![Skills](https://img.shields.io/badge/skills-128-green)
![License](https://img.shields.io/badge/license-MIT-green)
[![GitHub stars](https://img.shields.io/github/stars/levnikolaevich/claude-code-skills?style=social)](https://github.com/levnikolaevich/claude-code-skills)

> **7 plugins. One install command.** Automate your full delivery workflow —
> from project bootstrap to code audit to production quality gates.
> Works standalone or as a complete Agile pipeline.

> [!TIP]
> **Multi-Model AI Review** — Delegate code & story reviews to Codex and Gemini agents running in parallel, with automatic fallback to Claude Opus. Ship faster with 3x review coverage.

[Plugins](#plugins) · [Installation](#installation) · [Quick Start](#quick-start) · [Workflow](#workflow) · [MCP](#mcp-servers-optional) · [AI Review](#ai-review-models-optional) · [FAQ](#faq) · [Full Skill Tree](#whats-inside) · [Links](#links)

---

## Plugins

Install the full suite or pick only the plugins you need. Each works independently.

```bash
# All 7 plugins
/plugin add levnikolaevich/claude-code-skills

# Or individually:
/plugin add levnikolaevich/claude-code-skills --plugin agile-workflow
/plugin add levnikolaevich/claude-code-skills --plugin documentation-pipeline
/plugin add levnikolaevich/claude-code-skills --plugin codebase-audit-suite
/plugin add levnikolaevich/claude-code-skills --plugin project-bootstrap
/plugin add levnikolaevich/claude-code-skills --plugin optimization-suite
/plugin add levnikolaevich/claude-code-skills --plugin community-engagement
/plugin add levnikolaevich/claude-code-skills --plugin setup-environment
```

| Plugin | Description |
|--------|-------------|
| **agile-workflow** | Scope decomposition, Story/Task management, Execution, Quality gates, Orchestration |
| **documentation-pipeline** | Full project docs pipeline with auto-detection (backend/frontend/devops) |
| **codebase-audit-suite** | Documentation, Security, Build, Code quality, Tests, Architecture, Performance |
| **project-bootstrap** | CREATE or TRANSFORM projects to production-ready Clean Architecture |
| **optimization-suite** | Performance optimization, Dependency upgrades, Code modernization |
| **community-engagement** | GitHub community management: triage, announcements, RFCs, responses |
| **setup-environment** | Install CLI agents, configure MCP servers, sync settings, audit instruction files |

Browse and discover individual skills at [skills.sh](https://skills.sh/LevNikolaevich/claude-code-skills).

> [!NOTE]
> **skills.sh is a showcase only.** Skills depend on shared resources (`shared/` directory) that are not copied by `npx skills add`. Use `/plugin add` for a working installation.

---

## Installation

**Prerequisites:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code)

```bash
/plugin add levnikolaevich/claude-code-skills
```

Verify: run `ln-010-dev-environment-setup`

--

## Links

- Repository: https://github.com/levnikolaevich/claude-code-skills
- Homepage: https://levnikolaevich.github.io/claude-code-skills/
