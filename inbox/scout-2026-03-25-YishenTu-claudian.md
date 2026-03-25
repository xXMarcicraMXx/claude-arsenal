---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code plugin"
  quality_score: 88
  scoring_breakdown:
    stars: 32
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "YishenTu/claudian"
  url: "https://github.com/YishenTu/claudian"
  description: "An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault"
  stars: 5073
  forks: 292
  open_issues: 43
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2025-12-05"
  topics: ["claude-code", "ide", "obsidian", "obsidian-plugin", "productivity"]
---

# YishenTu/claudian

> Discovered by arsenal scout — awaiting manual triage

## Description

An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault

## README Excerpt

# Claudian

![GitHub stars](https://img.shields.io/github/stars/YishenTu/claudian?style=social)
![GitHub release](https://img.shields.io/github/v/release/YishenTu/claudian)
![License](https://img.shields.io/github/license/YishenTu/claudian)

![Preview](Preview.png)

An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault. Your vault becomes Claude's working directory, giving it full agentic capabilities: file read/write, search, bash commands, and multi-step workflows.

## Features

- **Full Agentic Capabilities**: Leverage Claude Code's power to read, write, and edit files, search, and execute bash commands, all within your Obsidian vault.
- **Context-Aware**: Automatically attach the focused note, mention files with `@`, exclude notes by tag, include editor selection (Highlight), and access external directories for additional context.
- **Vision Support**: Analyze images by sending them via drag-and-drop, paste, or file path.
- **Inline Edit**: Edit selected text or insert content at cursor position directly in notes with word-level diff preview and read-only tool access for context.
- **Instruction Mode (`#`)**: Add refined custom instructions to your system prompt directly from the chat input, with review/edit in a modal.
- **Slash Commands**: Create reusable prompt templates triggered by `/command`, with argument placeholders, `@file` references, and optional inline bash substitutions.
- **Skills**: Extend Claudian with reusable capability modules that are automatically invoked based on context, compatible with Claude Code's skill format.
- **Custom Agents**: Define custom subagents that Claude can invoke, with support for tool restrictions and model overrides.
- **Claude Code Plugins**: Enable Claude Code plugins installed via the CLI, with automatic discovery from `~/.claude/plugins` and per-vault configuration. Plugin skills, agents, and slash commands integrate seamlessly.
- **MCP Support**: Connect external tools and data sources via Model Context Protocol servers (stdio, SSE, HTTP) with context-saving mode and `@`-mention activation.
- **Advanced Model Control**: Select between Haiku, Sonnet, and Opus, configure custom models via environment variables, fine-tune thinking budget, and enable Opus and Sonnet with 1M context window (requires Max subscription or extra usage).
- **Plan Mode**: Toggle plan mode via Shift+Tab in the chat input. Claudian explores and designs before implementing, presenting a plan for approval with options to approve in a new session, continue in the current session, or provide feedback.
- **Security**: Permission modes (YOLO/Safe/Plan), safety blocklist, and vault confinement with symlink-safe checks.
- **Claude in Chrome**: Allow Claude to interact with Chrome through the `claude-in-chrome` extension.

## Requirements

- [Claude Code CLI](https://code.claude.com/docs/en/overview) installed (strongly recommend install Claude Code via Native Install)
- Obsidian v1.8.9+
- Claude subscriptio

## Links

- Repository: https://github.com/YishenTu/claudian
