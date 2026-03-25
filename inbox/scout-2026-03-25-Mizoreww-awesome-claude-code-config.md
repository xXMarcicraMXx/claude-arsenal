---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code configuration"
  quality_score: 75
  scoring_breakdown:
    stars: 19
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "Mizoreww/awesome-claude-code-config"
  url: "https://github.com/Mizoreww/awesome-claude-code-config"
  description: "Production-ready Claude Code configuration with self-improvement loop, multi-language rules, MCP integrations, and custom skills"
  stars: 176
  forks: 20
  open_issues: 1
  language: "Shell"
  license: "MIT"
  last_push: "2026-03-20"
  created: "2026-02-25"
  topics: []
---

# Mizoreww/awesome-claude-code-config

> Discovered by arsenal scout — awaiting manual triage

## Description

Production-ready Claude Code configuration with self-improvement loop, multi-language rules, MCP integrations, and custom skills

## README Excerpt

<!-- This is the source of truth. README.zh-CN.md is the Chinese translation. Keep both in sync. -->

**English** | [中文](./README.zh-CN.md) | [Codex Branch](https://github.com/Mizoreww/awesome-claude-code-config/tree/codex)

# Awesome Claude Code Configuration

![Statusline](assets/statusline.png)

Production-ready configuration for [Claude Code](https://claude.com/claude-code) — one-command install of global instructions, multi-language coding rules (Python / TypeScript / Go), 20 curated plugins, custom skills (paper-reading, [adversarial-review](https://github.com/poteto/noodle/tree/main/.agents/skills/adversarial-review), [humanizer](https://github.com/blader/humanizer), update_config), custom status bar, MCP integration, and a self-improvement loop that remembers corrections across sessions.

## Showcase

![Claude Code Demo](images/claude-code-demo.png)

**Paper Reading Skill in action** — Structured research paper analysis with the `paper-reading` skill. See the full summary: [Attention Is All You Need — Paper Summary](docs/Attention_Is_All_You_Need.md)

**Adversarial Review Skill in action** — Cross-model adversarial code review. Claude spawns Codex reviewers with distinct critical lenses (Skeptic, Architect, Minimalist), then synthesizes a structured verdict (PASS / CONTESTED / REJECT). See the full showcase: [Adversarial Review Showcase](docs/adversarial-review-showcase.md)

## Directory Structure

```
.
├── CLAUDE.md              # Global instructions
├── settings.json          # Settings (permissions, plugins, hooks, model)
├── lessons.md             # Self-correction log template (auto-loaded via hook)
├── rules/                 # Multi-language coding standards (common + python/typescript/golang)
├── hooks/                 # Statusline with gradient progress bars (context + 5h usage)
├── mcp/                   # MCP server config (Lark-MCP)
├── plugins/               # Plugin installation guide (20 plugins, 5 marketplaces)
├── skills/                # Custom skills (paper-reading, adversarial-review, humanizer, update_config)
├── docs/                  # Research paper summaries
├── images/                # Showcase screenshots
├── VERSION                # Semantic version number
├── install.sh             # One-command installer (macOS / Linux)
└── install.ps1            # One-command installer (Windows PowerShell)
```

## Quick Start

### macOS / Linux

**One-line remote install** (no clone needed):

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/Mizoreww/awesome-claude-code-config/main/install.sh)
```

This launches the interactive selector. Add `--all` to install everything non-interactively.

**Local install** (from clone):

```bash
git clone https://github.com/Mizoreww/awesome-claude-code-config.git
cd awesome-claude-code-config
./install.sh              # Interactive selector
./install.sh --all        # Install everything (non-interactive)
```

### Windows

**One-line remote install** (PowerShell, no clone needed):

## Links

- Repository: https://github.com/Mizoreww/awesome-claude-code-config
