---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude desktop extension"
  quality_score: 68
  scoring_breakdown:
    stars: 17
    recency: 25
    docs: 20
    community: 6
github_data:
  full_name: "HarmonicSecurity/claudit-sec"
  url: "https://github.com/HarmonicSecurity/claudit-sec"
  description: "Security audit tool for Claude Desktop and Claude Code on macOS — single-command visibility into MCP servers, extensions, plugins, connectors, scheduled tasks, and permissions."
  stars: 88
  forks: 9
  open_issues: 1
  language: "Shell"
  license: "Apache-2.0"
  last_push: "2026-03-20"
  created: "2026-03-16"
  topics: ["ai-security", "audit-tool", "claude", "claude-ai", "claude-code", "claude-cowork", "claude-desktop", "cowork", "endpoint-security", "macos", "mcp", "mdm", "security", "security-audit", "shell-script"]
---

# HarmonicSecurity/claudit-sec

> Discovered by arsenal scout — awaiting manual triage

## Description

Security audit tool for Claude Desktop and Claude Code on macOS — single-command visibility into MCP servers, extensions, plugins, connectors, scheduled tasks, and permissions.

## README Excerpt

# 🛡️ CLAUDIT-SEC

**Security audit tool for Claude Desktop on macOS — including CoWork, extensions, plugins, MCP servers, connectors, and scheduled tasks.**

One command. Full visibility. Read-only.

<p align="center">
  <img src="media/claudit-terminal.png" alt="CLAUDIT terminal output" width="700">
</p>

## 🤔 Why

Claude Desktop introduces a new class of endpoint risk: AI agents with autonomous execution, persistent scheduled tasks, MCP server integrations, browser-control extensions, and OAuth-authenticated connectors to external services. Most of this configuration lives in JSON files scattered across multiple directories with no centralised visibility.

CLAUDIT gives you that visibility in a single command.

> 📝 **A note on "Code":** Claude Desktop includes a built-in agent coding feature called **Code** (visible in the app's sidebar). This is **not** the same as **Claude Code**, the standalone terminal CLI. CLAUDIT primarily audits Claude Desktop and its CoWork features. It does include a basic check of `~/.claude/settings.json` (the terminal CLI's config), but the focus is squarely on the Desktop app.

## 📋 What It Audits

| Area | What's Checked |
|------|---------------|
| 🖥️ **Desktop Settings** | `keepAwakeEnabled`, sidebar/menuBar preferences |
| 🤖 **CoWork Settings** | Scheduled tasks, web search, browser use, network mode, egress policy, enabled plugins, marketplaces |
| 🔌 **MCP Servers** | Server names, commands, arguments, environment variable keys |
| 🧩 **Extensions (DXT)** | Installed extensions, signature status, dangerous tool grants |
| ⚙️ **Extension Settings** | Per-extension allowed directories and configuration |
| 🚦 **Extension Governance** | Allowlist enabled/disabled, blocklist entries |
| 📦 **Plugins** | Installed, remote (org-deployed), cached (downloaded) |
| 🪝 **Plugin Hooks** | Lifecycle hooks executing shell commands (PreToolUse, PostToolUse, Stop, etc.) |
| 🔗 **Connectors** | OAuth-authenticated web services, desktop integrations |
| 🎯 **Skills** | User-created, scheduled, session-local, and plugin skills across 9 paths |
| ⏰ **Scheduled Tasks** | Task names, cron expressions (with plain English translation) |
| 🔐 **App Config** | Network mode, extension allowlist/blocklist keys, device identifiers |
| 🔇 **Disabled MCP Tools** | Per-session tools explicitly disabled (with dangerous tool callout) |
| 🏃 **Runtime State** | Running processes, sleep assertions, LaunchAgents, crontab entries |
| 🍪 **Cookies** | `Cookies` and `Cookies-journal` presence |

> 📖 For a detailed breakdown of every individual check, what it means, and why it matters, see the [Findings Reference](docs/findings-reference.md).

## ⚡ Getting Started

### Prerequisites

| Requirement | How to check | How to install |
|-------------|-------------|---------------|
| 🍎 **macOS** | You're on a Mac | — |
| 🐚 **zsh** | `zsh --version` | Ships with macOS since Catalina |
| 🔧 **jq** | `jq --version` | `brew install jq` |

### Install & Run

```bash
git 

## Links

- Repository: https://github.com/HarmonicSecurity/claudit-sec
