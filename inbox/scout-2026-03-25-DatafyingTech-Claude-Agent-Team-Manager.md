---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code configuration"
  quality_score: 67
  scoring_breakdown:
    stars: 17
    recency: 20
    docs: 20
    community: 10
github_data:
  full_name: "DatafyingTech/Claude-Agent-Team-Manager"
  url: "https://github.com/DatafyingTech/Claude-Agent-Team-Manager"
  description: "Visual org-chart desktop app for managing Claude Code agent teams, skills, and configurations"
  stars: 107
  forks: 10
  open_issues: 4
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-11"
  created: "2026-02-24"
  topics: ["agent-management", "ai-agents", "anthropic", "automation", "claude", "claude-code", "desktop-app", "developer-tools", "org-chart", "react", "skill-management", "tauri", "team-management", "typescript", "zustand"]
---

# DatafyingTech/Claude-Agent-Team-Manager

> Discovered by arsenal scout — awaiting manual triage

## Description

Visual org-chart desktop app for managing Claude Code agent teams, skills, and configurations

## README Excerpt

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Built with Tauri](https://img.shields.io/badge/Built_with-Tauri_v2-blue?logo=tauri)](https://v2.tauri.app/)
[![React 19](https://img.shields.io/badge/React-19-61DAFB?logo=react)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.9-3178C6?logo=typescript)](https://www.typescriptlang.org/)
[![Claude AI](https://img.shields.io/badge/Powered_by-Claude_AI-6B4FBB)](https://www.anthropic.com/claude)

# ATM -- Agent Team Manager

**Your Claude agents are scattered across dozens of markdown files and you can't remember which one writes Python tests.**

ATM turns your `.claude/` folder from a graveyard of forgotten agent definitions into an org chart you can actually use. Drag-drop to build teams, click once to deploy 100+ agents in parallel, schedule them to run on cron. It's the missing UI layer between "I wrote some agent configs" and "I have an AI team that runs while I'm away."

---
### Video Demo
https://youtu.be/YhwVby25sJ8
---

## What You're Doing Right Now

You've got 15 Claude agents scattered across `.claude/agents/`. Every time you need to run them:

1. **Open the markdown file** in your editor
2. **Hand-edit the YAML frontmatter** -- was it `apiKey` or `api_key`? Did you close the quotes?
3. **Copy-paste the same API keys** into three different agent configs
4. **Write a 2000-word deployment primer** from scratch because you're running a team and Claude needs context
5. **Hope you described your org structure clearly enough** that the team lead interprets it correctly
6. **Manually kick off the run** from the terminal
7. **Realize you need daily runs** -- spend 30 minutes fighting with cron or Windows Task Scheduler
8. **Want to chain teams together?** Write another deployment primer explaining what the previous team did

You know the config works because you've run it before. But there's no reusable template. No visual overview. No automation. Just you, your text editor, and a growing collection of agent markdown files you're terrified to touch.

### What ATM Does Instead

- **Drag-drop visual org chart** -- see your entire agent hierarchy at a glance
- **One-click agent creation** -- templates autofill the YAML, you just name it
- **Shared API key management** -- edit once at root, applies everywhere
- **Save deployment configs** -- run the same team setup tomorrow with one click
- **Schedule runs** -- daily SOC reports at 6am, weekly content pipelines on Monday morning, no manual cron
- **Chain pipelines** -- Team A feeds into Team B feeds into Team C, automatically
- **Auto-generated deployment primers** -- ATM writes the 2000-word primer for you

Stop editing YAML at 11pm. Start deploying.

---

## What You Can Do

### Generate Entire Organizations from a Paragraph

Describe your company goals and specify how many teams you need. ATM generates the complete org chart: names, roles, detailed descriptions, proper hierarchy. Generate

## Links

- Repository: https://github.com/DatafyingTech/Claude-Agent-Team-Manager
- Homepage: https://github.com/DatafyingTech/AUI
