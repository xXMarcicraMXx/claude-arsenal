---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 82
  scoring_breakdown:
    stars: 31
    recency: 20
    docs: 20
    community: 11
github_data:
  full_name: "Pimzino/spec-workflow-mcp"
  url: "https://github.com/Pimzino/spec-workflow-mcp"
  description: "A Model Context Protocol (MCP) server that provides structured spec-driven development workflow tools for AI-assisted software development, featuring a real-time web dashboard and VSCode extension for monitoring and managing your project's progress directly in your development environment."
  stars: 4061
  forks: 333
  open_issues: 8
  language: "TypeScript"
  license: "GPL-3.0"
  last_push: "2026-03-07"
  created: "2025-08-07"
  topics: []
---

# Pimzino/spec-workflow-mcp

> Discovered by arsenal scout — awaiting manual triage

## Description

A Model Context Protocol (MCP) server that provides structured spec-driven development workflow tools for AI-assisted software development, featuring a real-time web dashboard and VSCode extension for monitoring and managing your project's progress directly in your development environment.

## README Excerpt

# Spec Workflow MCP

[![npm version](https://img.shields.io/npm/v/@pimzino/spec-workflow-mcp)](https://www.npmjs.com/package/@pimzino/spec-workflow-mcp)
[![VSCode Extension](https://vsmarketplacebadges.dev/version-short/Pimzino.spec-workflow-mcp.svg)](https://marketplace.visualstudio.com/items?itemName=Pimzino.spec-workflow-mcp)

A Model Context Protocol (MCP) server for structured spec-driven development with real-time dashboard and VSCode extension.

## ☕ Support This Project

<a href="https://buymeacoffee.com/Pimzino" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## 📺 Showcase

### 🔄 Approval System in Action
<a href="https://www.youtube.com/watch?v=C-uEa3mfxd0" target="_blank">
  <img src="https://img.youtube.com/vi/C-uEa3mfxd0/maxresdefault.jpg" alt="Approval System Demo" width="600">
</a>

*See how the approval system works: create documents, request approval through the dashboard, provide feedback, and track revisions.*

### 📊 Dashboard & Spec Management
<a href="https://www.youtube.com/watch?v=g9qfvjLUWf8" target="_blank">
  <img src="https://img.youtube.com/vi/g9qfvjLUWf8/maxresdefault.jpg" alt="Dashboard Demo" width="600">
</a>

*Explore the real-time dashboard: view specs, track progress, navigate documents, and monitor your development workflow.*

## ✨ Key Features

- **Structured Development Workflow** - Sequential spec creation (Requirements → Design → Tasks)
- **Real-Time Web Dashboard** - Monitor specs, tasks, and progress with live updates
- **VSCode Extension** - Integrated sidebar dashboard for VSCode users
- **Approval Workflow** - Complete approval process with revisions
- **Task Progress Tracking** - Visual progress bars and detailed status
- **Implementation Logs** - Searchable logs of all task implementations with code statistics
- **Multi-Language Support** - Available in 11 languages

## 🌍 Supported Languages

🇺🇸 English • 🇯🇵 日本語 • 🇨🇳 中文 • 🇪🇸 Español • 🇧🇷 Português • 🇩🇪 Deutsch • 🇫🇷 Français • 🇷🇺 Русский • 🇮🇹 Italiano • 🇰🇷 한국어 • 🇸🇦 العربية

**📖 Documentation in your language:**

[English](README.md) | [日本語](README.ja.md) | [中文](README.zh.md) | [Español](README.es.md) | [Português](README.pt.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Русский](README.ru.md) | [Italiano](README.it.md) | [한국어](README.ko.md) | [العربية](README.ar.md)

## 🚀 Quick Start

### Step 1: Add to your AI tool

Add to your MCP configuration (see client-specific setup below):

```json
{
  "mcpServers": {
    "spec-workflow": {
      "command": "npx",
      "args": ["-y", "@pimzino/spec-workflow-mcp@latest", "/path/to/your/project"]
    }
  }
}
```

### Step 2: Choose your interface

**Option A: Web Dashboard** (Required for CLI users)
Start the dashboard (runs on port 5000 by default):
```bash
npx -y @pimzino/spec-workflow-mcp@latest --dashboard
```

The dashboard will be accessible at: http://localhost:5000

> *

## Links

- Repository: https://github.com/Pimzino/spec-workflow-mcp
