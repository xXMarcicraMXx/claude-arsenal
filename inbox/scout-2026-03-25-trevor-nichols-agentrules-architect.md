---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 73
  scoring_breakdown:
    stars: 17
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "trevor-nichols/agentrules-architect"
  url: "https://github.com/trevor-nichols/agentrules-architect"
  description: "AGENTS.md/CLAUDE.md generator and ExecPlan harness for Codex, Claude Code, Cursor, Antigravity, OpenCode and other coding agents. Use api keys or authenticate with Codex"
  stars: 110
  forks: 17
  open_issues: 0
  language: "Python"
  license: "MIT"
  last_push: "2026-03-21"
  created: "2024-11-30"
  topics: ["agents", "antigravity", "claude-code", "codex", "codex-app-server", "cursor", "gemini-cli", "opencode", "windsurf"]
---

# trevor-nichols/agentrules-architect

> Discovered by arsenal scout — awaiting manual triage

## Description

AGENTS.md/CLAUDE.md generator and ExecPlan harness for Codex, Claude Code, Cursor, Antigravity, OpenCode and other coding agents. Use api keys or authenticate with Codex

## README Excerpt

# 🤖 AgentRules Architect v3

<div align="center">

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![PyPI](https://img.shields.io/pypi/v/agentrules.svg)](https://pypi.org/project/agentrules/)
[![OpenAI](https://img.shields.io/badge/OpenAI-supported-blue.svg)](https://openai.com/)
[![Codex Runtime](https://img.shields.io/badge/Codex%20app--server-supported-orange.svg)](https://github.com/openai/codex)
[![Anthropic](https://img.shields.io/badge/Anthropic-supported-purple.svg)](https://www.anthropic.com/)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-supported-red.svg)](https://deepseek.com/)
[![Google](https://img.shields.io/badge/Google-supported-green.svg)](https://ai.google.dev/)
[![xAI](https://img.shields.io/badge/xAI-supported-black.svg)](https://x.ai/)
[![Built By](https://img.shields.io/badge/Built%20By-trevor-nichols-orange.svg)](https://github.com/trevor-nichols)

**Your multi-provider AI code analysis and AGENTS.md generator 🚀**

[Demo](#-cli-demo) • [Highlights](#-v3-highlights) • [Features](#-feature-overview) • [Requirements](#-requirements) • [Installation](#-installation) • [Codex Runtime](#-configure-codex-runtime-optional) • [CLI](#-cli-at-a-glance) • [Configuration](#-configuration--preferences) • [Architecture](#-project-architecture) • [Outputs](#-output-artifacts) • [Development](#-development-workflow)

</div>

## 🎥 CLI Demo

![AgentRules CLI demo](docs/assets/media/demo.gif)

## Why AgentRules Architect?

Version 3 rebrands the project from **CursorRules Architect** to **AgentRules Architect** to match the standardized `AGENTS.md` contract used across modern AI coding agents. The rename comes with a fresh Typer-powered CLI, a persistent configuration service, broader provider support across Anthropic, OpenAI, Google, DeepSeek, xAI, and the local Codex app-server runtime, and a tooling layer that keeps the six-phase analysis reliably consistent yet flexibly extensible to your project's unique needs.

## 🔥 v3 Highlights

- ✨ **Rebrand & packaging** – ships on PyPI with console-script and `python -m agentrules` entry points.
- 🧭 **Typer CLI overhaul** – `agentrules` launches an interactive main menu with subcommands for `analyze`, `configure`, and `keys`.
- 🗂️ **Persistent settings** – API keys, model presets, logging, and output preferences live in `~/.config/agentrules/config.toml` (override with `AGENTRULES_CONFIG_DIR`).
- 🧠 **Expanded provider matrix** – the preset catalog spans Anthropic, OpenAI, Google, DeepSeek, xAI, and Codex runtime presets, with phase-by-phase model selection from the CLI or config file.
- 🧰 **Codex runtime support** – route phases through local `codex app-server` with ChatGPT auth via `CODEX_HOME` (no AgentRules-stored OpenAI API key required).
- 🔌 **Unified tool management** – the new `ToolManager` adapts JSON tool schemas for each provider; Tavily web search is available to researcher agents with one toggle.
- ✅ **Test & quality b

## Links

- Repository: https://github.com/trevor-nichols/agentrules-architect
