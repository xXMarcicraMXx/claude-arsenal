---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "awesome claude code"
  quality_score: 75
  scoring_breakdown:
    stars: 23
    recency: 25
    docs: 15
    community: 12
github_data:
  full_name: "milisp/codexia"
  url: "https://github.com/milisp/codexia"
  description: "Agent Workstation for Codex CLI + Claude Code — with task scheduler, git worktree & remote control, Tauri"
  stars: 506
  forks: 54
  open_issues: 10
  language: "TypeScript"
  license: "AGPL-3.0"
  last_push: "2026-03-25"
  created: "2025-08-13"
  topics: ["agentic-ai", "ai", "ai-agents", "awesome", "chatgpt", "claude-code", "codex", "codex-cli", "codex-desktop", "codex-gui", "codex-ide", "codex-ui", "gpt-5-codex", "gpt-oss", "mcp", "mcp-client", "ollama", "openai", "openai-codex", "openai-codex-cli"]
---

# milisp/codexia

> Discovered by arsenal scout — awaiting manual triage

## Description

Agent Workstation for Codex CLI + Claude Code — with task scheduler, git worktree & remote control, Tauri

## README Excerpt

# Codexia

[![Downloads](https://img.shields.io/github/downloads/milisp/codexia/total.svg)](https://github.com/milisp/codexia/releases)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=flat&logo=discord&logoColor=white)](https://discord.gg/zAjtD4kf5K)
[![Follow on 𝕏](https://img.shields.io/badge/𝕏-@lisp__mi-1c9bf0)](http://x.com/intent/follow?screen_name=lisp_mi)

Codexia is a **Tauri v2 app** for Codex CLI + Claude Code — combining agent workflows, an IDE-like editor, a headless web server, and a prompt notepad in one workspace.

![Codexia Home](docs/images/codexia-agent-command-center.png)

## Features

- **Agent workflows**: Task Scheduler for recurring jobs, remote control via headless web server
- **Workspace**: Git worktree management, project file tree, IDE-like editor, prompt notepad, local web preview
- **Data tools**: One-click PDF / XLSX / CSV preview
- **Ecosystem**: MCP server marketplace, agent skills marketplace
- **Personalization**: Theme and accent customization, usage analytics dashboard

## Requirements

- [Codex CLI](https://github.com/openai/codex)
- [Claude Code CLI](https://claude.ai/code)

## Installation

### Homebrew (macOS)
```sh
brew tap milisp/codexia
brew install --cask codexia
```

### Prebuilt releases (macOS / Linux / Windows)
- [GitHub Releases](https://github.com/milisp/codexia/releases)
- [Modern GitHub Release Mirror](https://milisp.github.io/modern-github-release/#/repo/milisp/codexia)

## Quick Start

1. Launch Codexia.
2. Add your project directory.
3. Enter a prompt and start your agent session.
4. Create an Agent Task Scheduler job for recurring workflows.

## Architecture at a Glance
- Codex app-server integration
- Claude agent rust sdk integration
- Frontend: React + TypeScript + Zustand + shadcn/ui in `src/`
- Desktop backend: Tauri v2 + Rust in `src-tauri/src/`
- Headless backend: Axum web server for remote control in `src-tauri/src/web_server/`
- Agent runtime: Codex `app-server` JSON-RPC integration for session/turn lifecycle
- Real-time updates: WebSocket broadcast stream at `/ws` for browser clients

Core entry points:
- `src-tauri/src/lib.rs` (desktop commands and state)
- `src-tauri/src/web_server/server.rs` (headless server startup)
- `src-tauri/src/web_server/router.rs` (HTTP API route surface)
- `src/services/tauri/` (frontend invoke layer)

## API Surface
Codexia exposes a browser-accessible API when running in web/headless mode:

- Health and stream: `GET /health`, `GET /ws`
- Codex lifecycle: `/api/codex/thread/*`, `/api/codex/turn/*`, `/api/codex/model/*`, `/api/codex/approval/*`
- Automation scheduler: `/api/automation/*` (create/update/list/run/pause/delete)
- Files, git, and terminal: `/api/filesystem/*`, `/api/git/*`, `/api/terminal/*`
- Claude integration: `/api/cc/*`
- Notes and productivity: `/api/notes/*`, `/api/codex/usage/token`

Contributor note:
- Add new API handlers under `src-tauri/src/web_server/handlers/`
- Register routes in `src-tauri/src/web_server/

## Links

- Repository: https://github.com/milisp/codexia
- Homepage: https://milisp.dev/codexia
