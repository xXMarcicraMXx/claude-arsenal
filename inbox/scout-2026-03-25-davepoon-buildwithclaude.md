---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code hook"
  quality_score: 88
  scoring_breakdown:
    stars: 29
    recency: 25
    docs: 20
    community: 14
github_data:
  full_name: "davepoon/buildwithclaude"
  url: "https://github.com/davepoon/buildwithclaude"
  description: "A single hub to find Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections to extend Claude Code, Claude Desktop, Agent SDK and OpenClaw"
  stars: 2638
  forks: 292
  open_issues: 2
  language: "Python"
  license: "MIT"
  last_push: "2026-03-24"
  created: "2025-07-25"
  topics: ["claude", "claude-code", "claude-code-commands", "claude-skills", "cli-tool", "commands", "mcp", "mcp-server", "mcp-tools", "openclaw", "plugin-marketplace", "subagents"]
---

# davepoon/buildwithclaude

> Discovered by arsenal scout — awaiting manual triage

## Description

A single hub to find Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections to extend Claude Code, Claude Desktop, Agent SDK and OpenClaw

## README Excerpt

# Build with Claude

## **Claude Skills, Agents, Commands, Hooks, Plugins, Marketplaces collections for and extend Claude Code**

[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub stars](https://img.shields.io/github/stars/davepoon/buildwithclaude.svg?style=social&label=Star)](https://github.com/davepoon/buildwithclaude)


**A plugin marketplace and discovery platform for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Browse curated plugins, discover community contributions, and extend your Claude Code workflows.**

## Quick Start

```bash
# Add the Build with Claude marketplace
/plugin marketplace add davepoon/buildwithclaude

# Browse available plugins
/plugin search @buildwithclaude

# Install plugins
/plugin install <plugin-name>@buildwithclaude
```

## What's Included

### Build with Claude Plugins

Curated collections maintained in this repository:

| Type | Count | Description |
|------|-------|-------------|
| **Agents** | 117 | Specialized AI experts (Python, Go, DevOps, Security, etc.) |
| **Commands** | 175 | Slash commands for automation (`/commit`, `/docs`, `/tdd`) |
| **Hooks** | 28 | Event-driven automation (notifications, git, formatting) |
| **Skills** | 26 | Reusable capabilities from plugins |
| **Plugins** | 50 | Bundled plugin packages by category |

### Community Discovery

The platform indexes plugins from the broader Claude Code ecosystem:

- **20k+ Community Plugins** from external marketplaces
- **4,500+ MCP Servers** for database, API, and tool connections
- **1,100+ Plugin Marketplaces** from the community


## Web UI

Browse, search, and explore everything at **[buildwithclaude.com](https://www.buildwithclaude.com)**

![Build with Claude Homepage](buildwithclaude-homepage.png)

![Browse Plugins](buildwithclaude-plugins.png)

![Browse Skills](buildwithclaude-skills.png)

![Browse MCP Servers](buildwithclaude-mcp.png)

![Browse Plugin Marketplaces](buildwithclaude-plugin-marketplaces.png)

### Features

- Browse all plugin types with filtering
- Search across plugins, agents, commands, hooks, skills
- Copy install commands with one click
- View full documentation and usage examples
- Discover MCP servers and community plugins

## Installation Options

### Option 1: Plugin Marketplace (Recommended)

```bash
# Add marketplace
/plugin marketplace add davepoon/buildwithclaude

# Install specific plugins
/plugin install agents-python-expert@buildwithclaude
/plugin install commands-version-control-git@buildwithclaude
/plugin install hooks-notifications@buildwithclaude

# Or install everything
/plugin install all-agents@buildwithclaude
/plugin install all-commands@buildwithclaude
/plugin install all-hooks@buildwithclaude
```

### Option 2: Manual Installati

## Links

- Repository: https://github.com/davepoon/buildwithclaude
- Homepage: https://www.buildwithclaude.com
