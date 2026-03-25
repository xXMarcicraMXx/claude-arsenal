---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code configuration"
  quality_score: 71
  scoring_breakdown:
    stars: 21
    recency: 20
    docs: 20
    community: 10
github_data:
  full_name: "nyatinte/ccexp"
  url: "https://github.com/nyatinte/ccexp"
  description: "interactive terminal interface for discovering, previewing, and managing Claude Code configuration files and slash commands."
  stars: 258
  forks: 9
  open_issues: 9
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-16"
  created: "2025-06-30"
  topics: ["claude", "claude-code"]
---

# nyatinte/ccexp

> Discovered by arsenal scout — awaiting manual triage

## Description

interactive terminal interface for discovering, previewing, and managing Claude Code configuration files and slash commands.

## README Excerpt

# ccexp (claude-code-explorer)

<div align="center">
  <img src="assets/icon.svg" alt="ccexp Icon" width="128" height="128">
  <br><br>
  <strong>Interactive CLI tool for exploring and managing Claude Code settings and slash commands</strong>
  <br><br>
  <a href="https://www.npmjs.com/package/ccexp">
    <img src="https://img.shields.io/npm/v/ccexp.svg" alt="npm version">
  </a>
  <a href="https://www.npmjs.com/package/ccexp">
    <img src="https://img.shields.io/npm/dm/ccexp.svg" alt="npm downloads">
  </a>
  <a href="https://github.com/nyatinte/ccexp/blob/main/LICENSE">
    <img src="https://img.shields.io/npm/l/ccexp.svg" alt="license">
  </a>
  <a href="https://github.com/nyatinte/ccexp">
    <img src="https://img.shields.io/badge/node-%3E%3D20-brightgreen.svg" alt="node version">
  </a>
  <a href="https://github.com/hesreallyhim/awesome-claude-code">
    <img src="https://awesome.re/mentioned-badge.svg" alt="Mentioned in Awesome Claude Code">
  </a>
</div>

## Overview

> [!IMPORTANT]
> **ccexp** is the shortened name for **claude-code-explorer**. The npm package [claude-code-explorer](https://www.npmjs.com/package/claude-code-explorer) is the previous version of this tool. The name was shortened to **ccexp** for brevity and easier command-line usage.

**ccexp** (short for **claude-code-explorer**) is a React Ink-based CLI tool that provides an interactive terminal interface for discovering, previewing, and managing Claude Code configuration files and slash commands. Navigate through your codebase to find CLAUDE.md files, slash command definitions, and other Claude-related configurations with a beautiful terminal UI.

## Features

- 🔍 **Interactive File Discovery** - Automatically finds Claude Code configuration files
- 📁 **Split-pane Interface** - File list on the left, preview on the right
- ⌨️ **Keyboard Navigation** - Arrow keys, Enter, ESC for smooth navigation
- 🔎 **Live Search** - Filter files as you type
- 📋 **File Actions** - Copy content, copy paths, open files in default applications
- 🎨 **Terminal UI** - Beautiful React Ink interface with proper focus management
- 📝 **Markdown Preview** - Renders CLAUDE.md files with syntax highlighting

## Screenshots

<div align="center">
  <img src="assets/thumbnail.png" alt="ccexp Thumbnail" width="600">
  <br><br>
  <img src="assets/screenshot_filelist.png" alt="ccexp File List" width="800">
  <br><br>
  <img src="assets/screenshot_actionmenu.png" alt="ccexp Action Menu" width="800">
</div>

## Target Files

ccexp (claude-code-explorer) automatically discovers these configuration files:

### Memory Files
- **CLAUDE.md** → Project memory (project configuration)
- **CLAUDE.local.md** → Project memory local (local overrides, gitignored) (deprecated: https://docs.anthropic.com/en/docs/claude-code/memory#determine-memory-type)
- **~/.claude/CLAUDE.md** → User memory (global configuration)

### Command Files
- **.claude/commands/**/*.md** → Project commands (project-specific slash commands)
- **~

## Links

- Repository: https://github.com/nyatinte/ccexp
- Homepage: https://www.npmjs.com/package/ccexp
