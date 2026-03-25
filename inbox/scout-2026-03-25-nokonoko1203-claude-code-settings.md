---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code configuration"
  quality_score: 64
  scoring_breakdown:
    stars: 17
    recency: 20
    docs: 20
    community: 7
github_data:
  full_name: "nokonoko1203/claude-code-settings"
  url: "https://github.com/nokonoko1203/claude-code-settings"
  description: "Best Practices for Claude Code Configuration"
  stars: 90
  forks: 14
  open_issues: 0
  language: ""
  license: "MIT"
  last_push: "2026-03-04"
  created: "2025-07-17"
  topics: ["ai", "ai-agents", "claude", "claude-code", "claude-skill", "codex", "codex-cli", "llm"]
---

# nokonoko1203/claude-code-settings

> Discovered by arsenal scout — awaiting manual triage

## Description

Best Practices for Claude Code Configuration

## README Excerpt

# Claude Code Settings Best Practices

English | [日本語](./README_ja.md)

A repository collecting best practices for Claude Code settings and customization. We will continue to update and improve this repository to make it even better.

**Note:** Some settings in this repository are specifically configured for Japanese users. Please use LLM to translate and adapt them appropriately to your environment.

The configuration files in this repository are designed to be placed under `~/.claude/` directory. By placing these configuration files in the appropriate locations, you can customize Claude Code's behavior and build an efficient development environment.

## Approach

Models are powerful enough now that complex configuration is unnecessary. Over-configuring can actually be counterproductive. This repository focuses on a few high-impact areas only.

- Claude Code has a rich set of slash commands. Master these first — add custom configuration later.
    - /resume, /rewind, /fork, /copy: Resume, restore, branch, and copy conversations
    - /review: Review pull requests
    - /simplify: Review and fix changed code
    - /copy: Copy session contents to clipboard
    - /add-dir: Add directories to the search scope
    - /batch: Create multiple PRs for large-scale changes using git worktrees
    - /plan: Run in plan mode
- Agent Teams let you distribute tasks across multiple agents working in parallel. By separating roles such as design, review, implementation, and testing, you can tackle large-scale tasks efficiently.
- Enable official plugins. The LSP plugins `typescript-lsp`, `pyright-lsp`, and `rust-analyzer-lsp` provide accurate code navigation without extra token cost.
- In some cases, prefer CLI tools over MCP. MCP servers consume context on every call. CLI tools can accomplish the same tasks with far fewer tokens. For example, replacing Playwright MCP with Playwright CLI.

## Project Structure

```
claude-code-settings/
├── CLAUDE.md          # Global user guidelines for ~/.claude/ placement
├── LICENSE            # MIT License file
├── README.md          # This file (English)
├── README_ja.md       # Japanese version
├── settings.json      # Claude Code configuration file
├── skills/            # Skill definitions
│   ├── kill-dev-process/
│   │   └── SKILL.md   # Dev process cleanup skill
│   └── playwright-cli/
│       ├── SKILL.md   # Browser automation via Playwright CLI (token-efficient)
│       └── references/ # Detailed reference docs
└── symlinks/          # External tools config files as symbolic links
    └── claude.json    # Claude Code MCP server configuration template
```

## About the symlinks Folder

The `symlinks/` folder contains configuration files for various external tools related to Claude Code. Since Claude Code is frequently updated and configuration changes are common, having all configuration files centralized in one folder makes editing much easier. Even if related files are normally placed outside the `~/.claude/` direc

## Links

- Repository: https://github.com/nokonoko1203/claude-code-settings
