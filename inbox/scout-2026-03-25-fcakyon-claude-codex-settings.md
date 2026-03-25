---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 76
  scoring_breakdown:
    stars: 23
    recency: 25
    docs: 20
    community: 8
github_data:
  full_name: "fcakyon/claude-codex-settings"
  url: "https://github.com/fcakyon/claude-codex-settings"
  description: "My personal Claude Code and OpenAI Codex setup with battle-tested skills, commands, hooks, agents and MCP servers that I use daily."
  stars: 533
  forks: 48
  open_issues: 3
  language: "Python"
  license: "Apache-2.0"
  last_push: "2026-03-25"
  created: "2025-07-09"
  topics: ["ai-agents", "ai-tools", "claude-ai", "claude-code", "claude-code-plugin", "claude-skills", "claudecode", "claudecode-config", "codex", "codex-cli", "commit-message", "cursor", "frontend-design", "gemini-cli", "github", "mcp", "mcp-server", "plugin", "pull-requests", "slack"]
---

# fcakyon/claude-codex-settings

> Discovered by arsenal scout — awaiting manual triage

## Description

My personal Claude Code and OpenAI Codex setup with battle-tested skills, commands, hooks, agents and MCP servers that I use daily.

## README Excerpt

<div align="center">
  <img src="https://github.com/user-attachments/assets/a978cb0a-785d-4a7d-aff2-7e962edd3120" width="10000" alt="Claude Codex Settings Logo">

[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/hesreallyhim/awesome-claude-code)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin-blue)](#available-plugins)
[![Context7 MCP](https://img.shields.io/badge/Context7%20MCP-Indexed-blue)](https://context7.com/fcakyon/claude-codex-settings)
[![llms.txt](https://img.shields.io/badge/llms.txt-✓-brightgreen)](https://context7.com/fcakyon/claude-codex-settings/llms.txt)

My daily battle-tested Claude [Code](https://github.com/anthropics/claude-code)/[Desktop](https://claude.ai/download) and [OpenAI Codex](https://developers.openai.com/codex) setup with skills, commands, hooks, subagents and MCP servers.

[Installation](#installation) • [Plugins](#plugins) • [Configuration](#configuration) • [Statusline](#statusline) • [References](#references)

</div>

## Installation

> **Prerequisites:** Before installing, ensure you have Claude Code and required tools installed. See [INSTALL.md](INSTALL.md) for complete prerequisites.

Install agents, commands, hooks, skills, and MCP servers via [Claude Code Plugins](https://docs.claude.com/en/docs/claude-code/plugins) system:

```bash
# Add marketplace
/plugin marketplace add fcakyon/claude-codex-settings

# Install plugins (pick what you need)
/plugin install anthropic-essentials@claude-settings     # Anthropic feature-dev, frontend, CLAUDE.md, skills
/plugin install anthropic-creative-suite@claude-settings # Anthropic docs, theming, artifacts
/plugin install anthropic-plugin-dev@claude-settings     # Anthropic plugin development toolkit
/plugin install phd-skills@claude-settings               # Hypothesis design, paper review, citation checks
/plugin install react-skills@claude-settings             # React, Next.js, React Native best practices
/plugin install agent-browser@claude-settings            # Browser automation CLI
/plugin install web-design-guidelines@claude-settings    # UI review for accessibility, forms, performance
/plugin install github-dev@claude-settings               # Git workflow + GitHub MCP
/plugin install statusline-tools@claude-settings         # Session + 5H usage statusline
/plugin install ultralytics-dev@claude-settings          # Auto-formatting hooks
/plugin install notification-tools@claude-settings       # OS notifications
/plugin install azure-tools@claude-settings              # Azure MCP & Skills (40+ services)
/plugin install ccproxy-tools@claude-settings            # Use any LLM via ccproxy/LiteLLM
/plugin install claude-tools@claude-settings             # Sync CLAUDE.md + allowlist
/plugin install gcloud-tools@claude-settings             # GCloud MCP & Skills
/plugin install general-dev@claude-settings              # Code simplifier + utilities
/plugin install linear-tools@claude-settings      

## Links

- Repository: https://github.com/fcakyon/claude-codex-settings
