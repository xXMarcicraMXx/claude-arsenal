---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code configuration"
  quality_score: 73
  scoring_breakdown:
    stars: 22
    recency: 20
    docs: 20
    community: 11
github_data:
  full_name: "neiii/bridle"
  url: "https://github.com/neiii/bridle"
  description: "TUI / CLI config manager for agentic harnesses (Amp, Claude Code, Opencode, Goose, Copilot CLI, Crush, Droid)"
  stars: 403
  forks: 15
  open_issues: 17
  language: "Rust"
  license: "MIT"
  last_push: "2026-03-14"
  created: "2025-12-27"
  topics: ["ai", "ampcode", "claude-code", "cli", "configuration", "copilot-cli", "crush-cli", "mcp", "opencode", "rust", "terminal", "tui"]
---

# neiii/bridle

> Discovered by arsenal scout — awaiting manual triage

## Description

TUI / CLI config manager for agentic harnesses (Amp, Claude Code, Opencode, Goose, Copilot CLI, Crush, Droid)

## README Excerpt

![Bridle](assets/bridle_header.png)

# Bridle

Unified configuration manager for AI coding assistants. Manage profiles, install skills/agents/commands, and switch configurations across Claude Code, OpenCode, Goose, Amp, Copilot CLI, and Crush.

## Installation

### Try it instantly (no install)

Run once without installing:

| Package Manager | Command              |
| --------------- | -------------------- |
| npx             | `npx bridle-ai`      |
| bunx            | `bunx bridle-ai`     |
| pnpm            | `pnpm dlx bridle-ai` |

### Install globally

For repeated use, install once:

**Node package managers:**

| Manager | Command                    |
| ------- | -------------------------- |
| npm     | `npm install -g bridle-ai` |
| bun     | `bun install -g bridle-ai` |
| pnpm    | `pnpm add -g bridle-ai`    |

**Other methods:**

```bash
# Homebrew
brew install neiii/bridle/bridle

# Cargo
cargo install bridle

# From source
git clone https://github.com/neiii/bridle && cd bridle && cargo install --path .
```

## Quick Start

```bash
# Launch the TUI
bridle

# See what's configured across all harnesses
bridle status

# Create a profile from your current config
bridle profile create claude work --from-current

# Switch between profiles
bridle profile switch claude personal
```

![Screenshot](assets/screenshot.png)

## "Package Manager" for your harness

With Bridle, you're able to install skills, agents, commands, and MCPs from any GitHub repository, similar to how Claude Code does it. With Bridle, however, you're not limited to just one harness; we auto-translate all the paths, namings, schemas, and configurations for you. 

```bash
# Install from GitHub
bridle install owner/repo

# What happens:
# 1. Bridle scans the repo for skills, agents, commands, and MCPs
# 2. You select which components to install
# 3. You choose target harnesses and profiles
# 4. Bridle translates paths and configs for each harness automatically
```

**Why this matters:** A skill written for Claude Code uses `~/.claude/skills/`. The same skill on OpenCode lives at `~/.config/opencode/skill/`. MCPs follow different JSON/YAML schemas. Bridle handles all these differences for you.

| Component | Claude Code | OpenCode | Goose | Copilot CLI | Crush |
| --------- | ----------- | -------- | ----- | ----------- | ----- |
| Skills    | `~/.claude/skills/` | `~/.config/opencode/skill/` | `~/.config/goose/skills/` | `~/.copilot/skills/` | `~/.config/crush/skills/` |
| Agents    | `~/.claude/plugins/*/agents/` | `~/.config/opencode/agent/` | — | `~/.copilot/agents/` | — |
| Commands  | `~/.claude/plugins/*/commands/` | `~/.config/opencode/command/` | — | — | — |
| MCPs      | `~/.claude/.mcp.json` | `opencode.jsonc` | `config.yaml` | `~/.copilot/mcp-config.json` | `crush.json` |

## Core Concepts

**Harnesses** are AI coding assistants: `claude`, `opencode`, `goose`, `amp`, `copilot`, `crush`

**Profiles** are saved configurations. Each harness can have multiple profiles (e

## Links

- Repository: https://github.com/neiii/bridle
