---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code configuration"
  quality_score: 71
  scoring_breakdown:
    stars: 16
    recency: 25
    docs: 20
    community: 10
github_data:
  full_name: "miroapp/miro-ai"
  url: "https://github.com/miroapp/miro-ai"
  description: "Official Miro AI developer tools and integrations. Includes MCP server configuration, Claude Code skills, and resources for building AI-powered experiences with Miro boards."
  stars: 74
  forks: 7
  open_issues: 7
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2025-12-18"
  topics: []
---

# miroapp/miro-ai

> Discovered by arsenal scout — awaiting manual triage

## Description

Official Miro AI developer tools and integrations. Includes MCP server configuration, Claude Code skills, and resources for building AI-powered experiences with Miro boards.

## README Excerpt

# Miro AI Developer Tools

[![Documentation](https://img.shields.io/badge/docs-developers.miro.com-blue)](https://developers.miro.com/docs/mcp-intro)

Connect AI coding assistants to your Miro boards. Create diagrams, extract context, generate code from designs, and track tasks—all through natural conversation. 

![Gemini CLI docs, diagram, table demo](https://github.com/user-attachments/assets/54cb6aa9-9174-4d23-91a2-3cb4caa69d3d)

---

> [Share your feedback](https://q2oeb0jrhgi.typeform.com/to/YATmJPVx).

---

## What's in This Repository?

This repo provides everything you need to connect AI tools to Miro:

| Component | What It Does |
|-----------|--------------|
| **Miro MCP Server** | API that gives AI agents access to your Miro boards |
| **Plugins & Extensions** | Pre-built integrations for popular AI tools |
| **Documentation** | Guides for using and developing integrations |

### Supported AI Tools

| AI Tool | Integration |
|---------|-------------|
| **Claude Code** | Plugins |
| **Gemini CLI** | Extensions |
| **Kiro** | Power |
| **Agent Skills** | Skills |
| **Cursor, VSCode, Windsurf, etc.** | MCP Config |

---

## Quick Start

### Step 1: Choose Your AI Tool

Select your AI tool below and follow the installation steps.

### Step 2: Install

<details open>
<summary><strong>Claude Code</strong> (Recommended)</summary>

```bash
/plugin marketplace add miroapp/miro-ai
/plugin install miro@miro-ai
```

Optional plugins:

```bash
/plugin install miro-tasks@miro-ai      # Task tracking in Miro tables
/plugin install miro-solutions@miro-ai   # Demo plugin generator
/plugin install miro-research@miro-ai    # Research visualization
/plugin install miro-review@miro-ai      # Code review workflows
```

**Restart Claude Code** after installation. If you previously configured Miro MCP manually, [remove the duplicate](https://developers.miro.com/docs/miro-mcp-server-faq-and-troubleshooting#-duplicate-mcp-servers) to avoid conflicts — the plugin already manages the MCP connection for you.

See [Claude Code Plugins](docs/claude-code/overview.md) for full documentation.

</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

**Quick start** — install the root extension for MCP access:

```bash
gemini extensions install https://github.com/miroapp/miro-ai
```

This installs the root `gemini-extension.json`, which gives Gemini access to the Miro MCP server (board reading, diagrams, tables, docs).

**Full install** — for commands, skills, and hooks, clone the repo and install individual extensions:

```bash
git clone https://github.com/miroapp/miro-ai.git
gemini extensions install ./miro-ai/gemini-extensions/miro
gemini extensions install ./miro-ai/gemini-extensions/miro-tasks
gemini extensions install ./miro-ai/gemini-extensions/miro-research
gemini extensions install ./miro-ai/gemini-extensions/miro-review
```

Restart Gemini CLI and authenticate when prompted.

See [Gemini CLI Extension](docs/gemini-cli/overview.md) | [Official Docs

## Links

- Repository: https://github.com/miroapp/miro-ai
