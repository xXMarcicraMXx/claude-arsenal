---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code hook"
  quality_score: 77
  scoring_breakdown:
    stars: 24
    recency: 20
    docs: 20
    community: 13
github_data:
  full_name: "sangrokjung/claude-forge"
  url: "https://github.com/sangrokjung/claude-forge"
  description: "Supercharge Claude Code with 11 AI agents, 36 commands & 15 skills — the claude-code plugin framework inspired by oh-my-zsh. 6-layer security hooks included. 5-min install."
  stars: 603
  forks: 133
  open_issues: 14
  language: "Shell"
  license: "MIT"
  last_push: "2026-03-17"
  created: "2026-02-23"
  topics: ["agents", "ai-assistant", "ai-coding", "ai-framework", "ai-pair-programming", "anthropic", "automation", "claude-code", "claude-code-agents", "cli-tools", "developer-experience", "developer-tools", "dotfiles", "hooks", "llm", "macos", "productivity", "shell", "slash-commands", "workflow"]
---

# sangrokjung/claude-forge

> Discovered by arsenal scout — awaiting manual triage

## Description

Supercharge Claude Code with 11 AI agents, 36 commands & 15 skills — the claude-code plugin framework inspired by oh-my-zsh. 6-layer security hooks included. 5-min install.

## README Excerpt

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/banner.jpg">
  <source media="(prefers-color-scheme: light)" srcset="docs/banner-light.jpg">
  <img src="docs/banner.jpg" alt="Claude Forge" width="100%">
</picture>

<p align="center">
  <strong>Turn Claude Code into a full development environment</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/LICENSE-MIT-blue?style=for-the-badge" alt="MIT License"></a>
  <a href="https://claude.com/claude-code"><img src="https://img.shields.io/badge/CLAUDE_CODE-%E2%89%A51.0-blueviolet?style=for-the-badge" alt="Claude Code"></a>
  <a href="https://github.com/sangrokjung/claude-forge/stargazers"><img src="https://img.shields.io/github/stars/sangrokjung/claude-forge?style=for-the-badge&color=yellow" alt="Stars"></a>
  <a href="https://github.com/sangrokjung/claude-forge/network/members"><img src="https://img.shields.io/github/forks/sangrokjung/claude-forge?style=for-the-badge&color=orange" alt="Forks"></a>
  <a href="https://github.com/sangrokjung/claude-forge/graphs/contributors"><img src="https://img.shields.io/github/contributors/sangrokjung/claude-forge?style=for-the-badge&color=green" alt="Contributors"></a>
  <a href="https://github.com/sangrokjung/claude-forge/commits/main"><img src="https://img.shields.io/github/last-commit/sangrokjung/claude-forge?style=for-the-badge" alt="Last Commit"></a>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> &bull;
  <a href="#-development-workflows">Workflows</a> &bull;
  <a href="#-whats-inside-claude-forge">What's Inside</a> &bull;
  <a href="#-claude-forge-installation-guide">Installation</a> &bull;
  <a href="#-claude-forge-architecture">Architecture</a> &bull;
  <a href="#-customization">Customization</a> &bull;
  <a href="README.ko.md">한국어</a>
</p>

---

## What is Claude Forge?

Claude Forge is an open-source development environment for Claude Code that provides 11 specialized agents, 40 slash commands, 15 skill workflows, and 15 automation hooks. Often described as "oh-my-zsh for Claude Code", it transforms Claude Code from a basic CLI into a full-featured development environment. One install gives you agents, commands, skills, hooks, and 9 rule files -- all pre-wired and ready to go.

> Think of it as **oh-my-zsh for Claude Code**: the same way oh-my-zsh enhances your terminal, Claude Forge supercharges your AI coding assistant.

---

## ⚡ Quick Start

### Install as Plugin (Recommended)

Claude Forge is available on the **Anthropic Official Plugin Marketplace** and can be installed directly from Claude Code:

```bash
# Option A: Install from Official Marketplace (after approval)
/plugin install claude-forge@claude-plugins-official

# Option B: Install from Claude Forge Marketplace
/plugin marketplace add sangrokjung/claude-forge
/plugin install claude-forge@claude-forge

# Option C: Install directly from GitHub
claude plugin install github:sangrokjung/claude-forge
```

To update:
``

## Links

- Repository: https://github.com/sangrokjung/claude-forge
- Homepage: https://sangrokjung.github.io/claude-forge
