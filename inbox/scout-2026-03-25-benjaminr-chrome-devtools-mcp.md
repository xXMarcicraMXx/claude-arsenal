---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 61
  scoring_breakdown:
    stars: 21
    recency: 8
    docs: 20
    community: 12
github_data:
  full_name: "benjaminr/chrome-devtools-mcp"
  url: "https://github.com/benjaminr/chrome-devtools-mcp"
  description: "An MCP Server for Chrome DevTools, following the Chrome DevTools Protocol. Integrates with Claude Desktop and Claude Code."
  stars: 292
  forks: 46
  open_issues: 6
  language: "Python"
  license: "MIT"
  last_push: "2025-10-06"
  created: "2025-06-27"
  topics: ["chrome", "chromium", "chromium-browser", "claude-code", "claude-desktop", "debugging-tools", "dev", "dev-tools", "frontend", "mcp", "mcp-server", "monitoring-tool"]
---

# benjaminr/chrome-devtools-mcp

> Discovered by arsenal scout — awaiting manual triage

## Description

An MCP Server for Chrome DevTools, following the Chrome DevTools Protocol. Integrates with Claude Desktop and Claude Code.

## README Excerpt

# Chrome DevTools MCP

A Model Context Protocol (MCP) server that provides Chrome DevTools Protocol integration through MCP. This allows you to debug web applications by connecting to Chrome's developer tools.

**Available as a Claude Desktop Extension (.dxt)** for easy one-click installation!

## What This Does

This MCP server acts as a bridge between Claude and Chrome's debugging capabilities. Once installed in Claude Desktop, you can:
- Connect Claude to any web application running in Chrome
- Debug network requests, console errors, and performance issues
- Inspect JavaScript objects and execute code in the browser context
- Monitor your application in real-time through natural conversation with Claude

**Note**: This is an MCP server that runs within Claude Desktop - you don't need to run any separate servers or processes.

## Features

- **Network Monitoring**: Capture and analyse HTTP requests/responses with filtering options
- **Console Integration**: Read browser console logs, analyse errors, and execute JavaScript
- **Performance Metrics**: Timing data, resource loading, and memory utilisation
- **Page Inspection**: DOM information, page metrics, and multi-frame support
- **Storage Access**: Read cookies, localStorage, and sessionStorage
- **Real-time Monitoring**: Live console output tracking
- **Object Inspection**: Inspect JavaScript objects and variables

## Installation

### Option 1: Claude Desktop Extension (Easiest)

**Download the pre-built extension:**
1. Download the latest `.dxt` file from [Releases](https://github.com/benjaminr/chrome-devtools-mcp/releases)
2. Open Claude Desktop
3. Go to Extensions and install the downloaded `.dxt` file
4. Configure Chrome path if needed in extension settings

The extension includes all dependencies and is ready to use immediately!

### Option 2: MCP CLI (Advanced)

**Quick Install (most common):**
```bash
git clone https://github.com/benjaminr/chrome-devtools-mcp.git
cd chrome-devtools-mcp
mcp install server.py -n "Chrome DevTools MCP" --with-editable .
```

> **Note**: The `mcp` command is part of the [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk). Install it with `pip install mcp` if not already available.

**All Installation Options:**

```bash
# Clone the repository
git clone https://github.com/benjaminr/chrome-devtools-mcp.git
cd chrome-devtools-mcp

# The --with-editable flag uses pyproject.toml to install dependencies

# Basic installation with local dependencies
mcp install server.py --with-editable .

# Install with custom name
mcp install server.py -n "Chrome DevTools MCP" --with-editable .

# Install with environment variables
mcp install server.py -n "Chrome DevTools MCP" --with-editable . -v CHROME_DEBUG_PORT=9222

# Install with additional packages if needed
mcp install server.py -n "Chrome DevTools MCP" --with-editable . --with websockets --with aiohttp

# Install with environment file (copy .env.example to .env first)
cp .env.example .env
# Edit .env 

## Links

- Repository: https://github.com/benjaminr/chrome-devtools-mcp
