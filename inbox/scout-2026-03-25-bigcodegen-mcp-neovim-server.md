---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "anthropic mcp server"
  quality_score: 60
  scoring_breakdown:
    stars: 21
    recency: 8
    docs: 20
    community: 11
github_data:
  full_name: "bigcodegen/mcp-neovim-server"
  url: "https://github.com/bigcodegen/mcp-neovim-server"
  description: "Control Neovim using Model Context Protocol (MCP) and the official neovim/node-client JavaScript library"
  stars: 301
  forks: 26
  open_issues: 8
  language: "TypeScript"
  license: "MIT"
  last_push: "2025-10-11"
  created: "2024-12-22"
  topics: ["anthropic", "claude", "mcp", "modelcontextprotocol", "neovim"]
---

# bigcodegen/mcp-neovim-server

> Discovered by arsenal scout — awaiting manual triage

## Description

Control Neovim using Model Context Protocol (MCP) and the official neovim/node-client JavaScript library

## README Excerpt

# Neovim MCP Server

Connect Claude Desktop (or any Model Context Protocol client) to Neovim using MCP and the official neovim/node-client JavaScript library. This server leverages Vim's native text editing commands and workflows, which Claude already understands, to create a lightweight code or general purpose AI text assistance layer.

<a href="https://glama.ai/mcp/servers/s0fywdwp87"><img width="380" height="200" src="https://glama.ai/mcp/servers/s0fywdwp87/badge" alt="mcp-neovim-server MCP server" /></a>

## Features

- Connects to your nvim instance if you expose a socket file, for example `--listen /tmp/nvim`, when starting nvim
- Views your current buffers and manages buffer switching
- Gets cursor location, mode, file name, marks, registers, and visual selections
- Runs vim commands and optionally shell commands through vim
- Can make edits using insert, replace, or replaceAll modes
- Search and replace functionality with regex support
- Project-wide grep search with quickfix integration
- Comprehensive window management
- Health monitoring and connection diagnostics

## API

### Resources

- `nvim://session`: Current neovim text editor session
- `nvim://buffers`: List of all open buffers in the current Neovim session with metadata including modified status, syntax, and window IDs

### Tools

#### Core Tools
- **vim_buffer**
  - Get buffer contents with line numbers (supports filename parameter)
  - Input `filename` (string, optional) - Get specific buffer by filename
  - Returns numbered lines with buffer content
- **vim_command**
  - Send a command to VIM for navigation, spot editing, and line deletion
  - Input `command` (string)
  - Runs vim commands with `nvim.replaceTermcodes`. Multiple commands work with newlines
  - Shell commands supported with `!` prefix when `ALLOW_SHELL_COMMANDS=true`
  - On error, `'nvim:errmsg'` contents are returned 
- **vim_status**
  - Get comprehensive Neovim status
  - Returns cursor position, mode, filename, visual selection with enhanced detection, window layout, current tab, marks, registers, working directory, LSP client info, and plugin detection
  - Enhanced visual selection reporting: detects visual mode type (character/line/block), provides accurate selection text, start/end positions, and last visual selection marks
- **vim_edit**
  - Edit lines using insert, replace, or replaceAll modes
  - Input `startLine` (number), `mode` (`"insert"` | `"replace"` | `"replaceAll"`), `lines` (string)
  - insert: insert lines at startLine
  - replace: replace lines starting at startLine
  - replaceAll: replace entire buffer contents
- **vim_window**
  - Manipulate Neovim windows (split, vsplit, close, navigate)
  - Input `command` (string: "split", "vsplit", "only", "close", "wincmd h/j/k/l")
- **vim_mark**
  - Set named marks at specific positions
  - Input `mark` (string: a-z), `line` (number), `column` (number)
- **vim_register**
  - Set content of registers
  - Input `register` (string: a-z or "), `conten

## Links

- Repository: https://github.com/bigcodegen/mcp-neovim-server
