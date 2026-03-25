---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "awesome claude code"
  quality_score: 79
  scoring_breakdown:
    stars: 22
    recency: 25
    docs: 20
    community: 12
github_data:
  full_name: "JackyST0/awesome-agent-skills"
  url: "https://github.com/JackyST0/awesome-agent-skills"
  description: "🤖 精选的 AI Agent Skills 列表，适用于 Cursor、Claude Code、GitHub Copilot 等 AI 编程工具"
  stars: 410
  forks: 45
  open_issues: 3
  language: "Shell"
  license: "CC0-1.0"
  last_push: "2026-03-24"
  created: "2026-01-28"
  topics: ["agent-skills", "ai", "awesome", "awesome-list", "claude", "copilot", "cursor"]
---

# JackyST0/awesome-agent-skills

> Discovered by arsenal scout — awaiting manual triage

## Description

🤖 精选的 AI Agent Skills 列表，适用于 Cursor、Claude Code、GitHub Copilot 等 AI 编程工具

## README Excerpt

# Awesome Agent Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<p align="center">
  <img src="assets/banner.svg" alt="Awesome Agent Skills" width="100%">
</p>

<p align="center">
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <img src="https://img.shields.io/github/stars/JackyST0/awesome-agent-skills?style=social" alt="GitHub Stars">
</p>

<p align="center">
  <a href="https://jackyst0.github.io/awesome-agent-skills/"><b>🔍 Search Skills Online</b></a>
</p>

> Modular instruction packages that give AI coding assistants on-demand capabilities for specific tasks, working across Cursor, Claude Code, GitHub Copilot, and more.

English | [简体中文](README_ZH.md)

## Contents

- [Quick Start](#quick-start)
- [What Are Agent Skills](#what-are-agent-skills)
- [Official Resources](#official-resources)
- [Skills Collections](#skills-collections)
- [Development Tools](#development-tools)
- [Productivity](#productivity)
- [DevOps](#devops)
- [Data Processing](#data-processing)
- [Writing](#writing)
- [Design](#design)

## Quick Start

### One-Click Install (Recommended)

**macOS / Linux:**

```bash
# Interactive mode - install, uninstall, or list
curl -sL https://raw.githubusercontent.com/JackyST0/awesome-agent-skills/main/install.sh | bash

# Or install all skills to a specific platform
curl -sL https://raw.githubusercontent.com/JackyST0/awesome-agent-skills/main/install.sh | bash -s -- -p cursor -a
```

**Windows (PowerShell):**

```powershell
# Download and run the install script
irm https://raw.githubusercontent.com/JackyST0/awesome-agent-skills/main/install.ps1 | iex
```

> Note: The installer currently installs the bundled example skills from this repository's `examples/` directory. It is not a general-purpose package manager for every third-party project listed below.

### Manual Install

```bash
# Clone examples from this repository
git clone https://github.com/JackyST0/awesome-agent-skills.git
cp -r awesome-agent-skills/examples/code-review ~/.cursor/skills/

# Or clone official skills
git clone https://github.com/anthropics/skills.git ~/.cursor/skills/anthropics
```

> 📖 See [How to Use Agent Skills](docs/how-to-use.md) for the complete guide.

## What Are Agent Skills

Agent Skills are instruction sets, scripts, and resources that AI agents can discover and use to perform specific tasks. Each skill contains a `SKILL.md` file that tells the AI how to use it.

Skills work across multiple platforms:

|Platform   |Global Directory             |Project Directory   |
|-----------|-----------------------------|--------------------|
|Cursor     |`~/.cursor/skills/`          |`.cursor/skills/`   |
|Claude Code|`~/.claude/skills/`          |`.claude/skills/`   |
|Copilot    |`~/.copilot/skills/`         |`.github/skills/`   |
|Windsurf   |`~/.windsurf/skills/`        |`.windsurf/skills/` |
|Codex      |`~/.codex/skills/`           |`.codex/skills/`    |
|OpenCode   

## Links

- Repository: https://github.com/JackyST0/awesome-agent-skills
- Homepage: https://jackyst0.github.io/awesome-agent-skills/
