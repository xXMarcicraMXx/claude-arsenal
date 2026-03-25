---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 75
  scoring_breakdown:
    stars: 26
    recency: 15
    docs: 20
    community: 14
github_data:
  full_name: "steipete/claude-code-mcp"
  url: "https://github.com/steipete/claude-code-mcp"
  description: "Claude Code as one-shot MCP server to have an agent in your agent."
  stars: 1198
  forks: 148
  open_issues: 16
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-01-01"
  created: "2025-05-13"
  topics: ["agent", "claude", "mcp"]
---

# steipete/claude-code-mcp

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Code as one-shot MCP server to have an agent in your agent.

## README Excerpt

# Claude Code MCP Server

<img src="assets/claude_code_mcp_logo.png" alt="Claude Code MCP Logo">

[![npm package](https://img.shields.io/npm/v/@steipete/claude-code-mcp)](https://www.npmjs.com/package/@steipete/claude-code-mcp)
[![View changelog](https://img.shields.io/badge/Explore%20Changelog-brightgreen)](/CHANGELOG.md)

An MCP (Model Context Protocol) server that allows running Claude Code in one-shot mode with permissions bypassed automatically.

Did you notice that Cursor sometimes struggles with complex, multi-step edits or operations? This server, with its powerful unified `claude_code` tool, aims to make Claude a more direct and capable agent for your coding tasks.

<img src="assets/screenshot.png" width="300" alt="Screenshot">

## Overview

This MCP server provides one tool that can be used by LLMs to interact with Claude Code. When integrated with Claude Desktop or other MCP clients, it allows LLMs to:

- Run Claude Code with all permissions bypassed (using `--dangerously-skip-permissions`)
- Execute Claude Code with any prompt without permission interruptions
- Access file editing capabilities directly
- Enable specific tools by default

## Benefits

- Claude/Windsurf often have trouble editing files. Claude Code is better and faster at it.
- Multiple commands can be queued instead of direct execution. This saves context space so more important stuff is retained longer, fewer compacts happen.
- File ops, git, or other operations don't need costy models. Claude Code is pretty cost effective if you sign up for Antropic Max. You can use Gemini or o3 in Max mode and save costs with offloading tasks to cheaper models.
- Claude has wider system access and can do things that Cursor/Windsurf can't do (or believe they can't), so whenever they are stuck just ask them "use claude code" and it will usually un-stuck them.
- Agents in Agents rules.

<img src="assets/agents_in_agents_meme.jpg" alt="Agents in Agents Meme">

## Prerequisites

- Node.js v20 or later (Use fnm or nvm to install)
- Claude CLI installed locally (run it and call /doctor) and `-dangerously-skip-permissions` accepted.

## Configuration

### Environment Variables

- `CLAUDE_CLI_NAME`: Override the Claude CLI binary name or provide an absolute path (default: `claude`). This allows you to use a custom Claude CLI binary. This is useful for:
  - Using custom Claude CLI wrappers
  - Testing with mocked binaries
  - Running multiple Claude CLI versions side by side
  
  Supported formats:
  - Simple name: `CLAUDE_CLI_NAME=claude-custom` or `CLAUDE_CLI_NAME=claude-v2`
  - Absolute path: `CLAUDE_CLI_NAME=/path/to/custom/claude`
  
  Relative paths (e.g., `./claude` or `../claude`) are not allowed and will throw an error.
  
  When set to a simple name, the server will look for the specified binary in:
  1. The system PATH (instead of the default `claude` command)
  
  Note: The local user installation path (`~/.claude/local/claude`) will still be checked but only for the default `clau

## Links

- Repository: https://github.com/steipete/claude-code-mcp
