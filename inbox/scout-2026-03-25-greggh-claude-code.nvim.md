---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code plugin"
  quality_score: 72
  scoring_breakdown:
    stars: 28
    recency: 15
    docs: 20
    community: 9
github_data:
  full_name: "greggh/claude-code.nvim"
  url: "https://github.com/greggh/claude-code.nvim"
  description: "Seamless integration between Claude Code AI assistant and Neovim"
  stars: 1954
  forks: 63
  open_issues: 49
  language: "Lua"
  license: "MIT"
  last_push: "2026-02-04"
  created: "2025-02-24"
  topics: ["ai-assistant", "anthropic", "claude", "claude-code", "neovim", "nvim", "plugin", "terminal"]
---

# greggh/claude-code.nvim

> Discovered by arsenal scout — awaiting manual triage

## Description

Seamless integration between Claude Code AI assistant and Neovim

## README Excerpt

# Claude Code Neovim Plugin

[![GitHub License](https://img.shields.io/github/license/greggh/claude-code.nvim?style=flat-square)](https://github.com/greggh/claude-code.nvim/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/greggh/claude-code.nvim?style=flat-square)](https://github.com/greggh/claude-code.nvim/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/greggh/claude-code.nvim?style=flat-square)](https://github.com/greggh/claude-code.nvim/issues)
[![CI](https://img.shields.io/github/actions/workflow/status/greggh/claude-code.nvim/ci.yml?branch=main&style=flat-square&logo=github)](https://github.com/greggh/claude-code.nvim/actions/workflows/ci.yml)
[![Neovim Version](https://img.shields.io/badge/Neovim-0.7%2B-blueviolet?style=flat-square&logo=neovim)](https://github.com/neovim/neovim)
[![Tests](https://img.shields.io/badge/Tests-44%20passing-success?style=flat-square&logo=github-actions)](https://github.com/greggh/claude-code.nvim/actions/workflows/ci.yml)
[![Version](https://img.shields.io/badge/Version-0.4.2-blue?style=flat-square)](https://github.com/greggh/claude-code.nvim/releases/tag/v0.4.2)
[![Discussions](https://img.shields.io/github/discussions/greggh/claude-code.nvim?style=flat-square&logo=github)](https://github.com/greggh/claude-code.nvim/discussions)

*A seamless integration between [Claude Code](https://github.com/anthropics/claude-code) AI assistant and Neovim*

[Features](#features) •
[Requirements](#requirements) •
[Installation](#installation) •
[Configuration](#configuration) •
[Usage](#usage) •
[Contributing](#contributing) •
[Discussions](https://github.com/greggh/claude-code.nvim/discussions)

![Claude Code in Neovim](https://github.com/greggh/claude-code.nvim/blob/main/assets/claude-code.png?raw=true)

This plugin was built entirely with Claude Code in a Neovim terminal, and then inside itself using Claude Code for everything!

## Features

- 🚀 Toggle Claude Code in a terminal window with a single key press
- 🧠 Support for command-line arguments like `--continue` and custom variants
- 🔄 Automatically detect and reload files modified by Claude Code
- ⚡ Real-time buffer updates when files are changed externally
- 📱 Customizable window position and size (including floating windows)
- 🤖 Integration with which-key (if available)
- 📂 Automatically uses git project root as working directory (when available)
- 🧩 Modular and maintainable code structure
- 📋 Type annotations with LuaCATS for better IDE support
- ✅ Configuration validation to prevent errors
- 🧪 Testing framework for reliability (44 comprehensive tests)

## Requirements

- Neovim 0.7.0 or later
- [Claude Code CLI](https://github.com/anthropics/claude-code) tool installed and available in your PATH
- [plenary.nvim](https://github.com/nvim-lua/plenary.nvim) (dependency for git operations)

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

## Installation

### Using [lazy.nvim](https://github.com/folke/lazy.nvim)


## Links

- Repository: https://github.com/greggh/claude-code.nvim
