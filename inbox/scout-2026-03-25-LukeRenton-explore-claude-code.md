---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 75
  scoring_breakdown:
    stars: 19
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "LukeRenton/explore-claude-code"
  url: "https://github.com/LukeRenton/explore-claude-code"
  description: "Learn Claude Code by exploring it as it was designed - interactive IDE-style docs for commands, MCP, skills, CLAUDE.md and more."
  stars: 194
  forks: 26
  open_issues: 0
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-03-17"
  created: "2026-03-05"
  topics: ["claude", "claude-code", "claude-skills"]
---

# LukeRenton/explore-claude-code

> Discovered by arsenal scout — awaiting manual triage

## Description

Learn Claude Code by exploring it as it was designed - interactive IDE-style docs for commands, MCP, skills, CLAUDE.md and more.

## README Excerpt

<p align="center">
  <img src="logo.png" alt="Explore Claude Code" width="360">
</p>

<p align="center">
  <strong>Learn Claude Code by exploring it.</strong>
</p>

<p align="center">
  <a href="https://exploreclaudecode.com"><img src="https://img.shields.io/badge/live%20demo-exploreclaudecode.com-c47a50?style=flat-square" alt="Live Demo"></a>
  <a href="https://github.com/LukeRenton/explore-claude-code/blob/main/LICENSE"><img src="https://img.shields.io/github/license/LukeRenton/explore-claude-code?style=flat-square&color=8e82ad" alt="License"></a>
  <a href="https://github.com/LukeRenton/explore-claude-code/stargazers"><img src="https://img.shields.io/github/stars/LukeRenton/explore-claude-code?style=flat-square&color=b8965e" alt="Stars"></a>
  <img src="https://img.shields.io/badge/zero%20dependencies-vanilla%20JS-3a3632?style=flat-square" alt="Zero Dependencies">
</p>

---

A simulated Claude Code project you can click through. Every file and folder in the sidebar is a real Claude Code concept — the same `.claude/` directory, config files, and scaffolding you'd find in an actual repo. Click any file to learn what it does, how to set it up, and see annotated examples you can copy into your own projects.

<p align="center">
  <img src="current.png" alt="Screenshot" width="820">
</p>

## 📚 What You'll Learn

| Folder / File | Feature |
|---|---|
| `CLAUDE.md` | Project memory that persists across sessions |
| `.claude/settings.json` | Permissions, tool access, and guardrails |
| `.claude/commands/` | Custom slash commands for saved workflows |
| `.claude/skills/` | Knowledge folders Claude loads autonomously |
| `.claude/agents/` | Subagents for specialised, delegated tasks |
| `.claude/hooks/` | Shell scripts that run on Claude lifecycle events |
| `.claude/plugins/` | Extend Claude with custom tools and resources |
| `.mcp.json` | MCP server config for external tool integrations |
| `src/` | Example source code sitting alongside real config |
| **built-in/** | Features that ship with Claude Code (no setup required) |
| `built-in/bundled-skills/` | `/simplify`, `/batch`, `/debug`, `/loop`, `/claude-api` |

The explorer is split into two sections. Everything under `.claude/` is project config you create and commit. Everything under `built-in/` covers features that ship with Claude Code out of the box, no setup required. A visual separator divides the two.

Every piece of content is written as if it were a real config file in a real repo. You're not reading *about* the config, you're reading *the config itself*, annotated so you understand every line. When you're done exploring, you can copy the scaffolding straight into your own projects.

## 🚀 Try It

The fastest way to get started is the live site:

**👉 [exploreclaudecode.com](https://exploreclaudecode.com)**

No install, no signup, no build step. Just open it and start clicking.

If you want to run it locally, clone the repo and point any static server at the `site/` directory:

```bash
git c

## Links

- Repository: https://github.com/LukeRenton/explore-claude-code
- Homepage: https://www.exploreclaudecode.com/
