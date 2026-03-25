---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 86
  scoring_breakdown:
    stars: 31
    recency: 25
    docs: 20
    community: 10
github_data:
  full_name: "getsentry/XcodeBuildMCP"
  url: "https://github.com/getsentry/XcodeBuildMCP"
  description: "A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects."
  stars: 4880
  forks: 231
  open_issues: 21
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-21"
  created: "2025-03-09"
  topics: ["mcp", "mcp-server", "model-context-protocol", "model-context-protocol-servers", "tag-production", "xcode", "xcodebuild"]
---

# getsentry/XcodeBuildMCP

> Discovered by arsenal scout — awaiting manual triage

## Description

A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

## README Excerpt

<img src="assets/banner.png" alt="XcodeBuild MCP" width="600"/>

A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects.

[![CI](https://github.com/getsentry/XcodeBuildMCP/actions/workflows/ci.yml/badge.svg)](https://github.com/getsentry/XcodeBuildMCP/actions/workflows/ci.yml)
[![npm version](https://badge.fury.io/js/xcodebuildmcp.svg)](https://badge.fury.io/js/xcodebuildmcp) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Node.js](https://img.shields.io/badge/node->=18.x-brightgreen.svg)](https://nodejs.org/) [![Xcode 16](https://img.shields.io/badge/Xcode-16-blue.svg)](https://developer.apple.com/xcode/) [![macOS](https://img.shields.io/badge/platform-macOS-lightgrey.svg)](https://www.apple.com/macos/) [![MCP](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io/) [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/getsentry/XcodeBuildMCP) [![AgentAudit Security](https://img.shields.io/badge/AgentAudit-Safe-brightgreen?logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAxTDMgNXY2YzAgNS41NSAzLjg0IDEwLjc0IDkgMTIgNS4xNi0xLjI2IDktNi40NSA5LTEyVjVsLTktNHoiLz48L3N2Zz4=)](https://www.agentaudit.dev/skills/xcodebuildmcp)

## Installation

XcodeBuildMCP ships as a single package with two modes: a **CLI** for direct terminal use and an **MCP server** for AI coding agents. Both installation methods give you both modes.

### Option A — Homebrew

```bash
brew tap getsentry/xcodebuildmcp
brew install xcodebuildmcp
```

Use the CLI:
```bash
xcodebuildmcp --help
```

MCP client config:
```json
"XcodeBuildMCP": {
  "command": "xcodebuildmcp",
  "args": ["mcp"]
}
```

Upgrade later with `brew update && brew upgrade xcodebuildmcp`.

### Option B — npm / npx (Node.js 18+)

**For CLI use**, install globally:
```bash
npm install -g xcodebuildmcp@latest
xcodebuildmcp --help
```

**For MCP server only**, no global install needed — add directly to your client config:
```json
"XcodeBuildMCP": {
  "command": "npx",
  "args": ["-y", "xcodebuildmcp@latest", "mcp"]
}
```

To pin a specific version, replace `@latest` with an exact version (e.g. `xcodebuildmcp@latest`).

### Client-specific setup

The examples below use npx (Option B). If you installed via Homebrew, replace the command with `"command": "xcodebuildmcp", "args": ["mcp"]` instead.

<details>
  <summary>Cursor</summary>
  <br />

  Recommended (project-scoped): add `.cursor/mcp.json` in your workspace root:
  ```json
  {
    "mcpServers": {
      "XcodeBuildMCP": {
        "command": "npx",
        "args": ["-y", "xcodebuildmcp@latest", "mcp"]
      }
    }
  }
  ```

  For global Cursor config (`~/.cursor/mcp.json`), use this variant so startup is aligned with the active workspace:
  ```json
  {
    "mcpServers": {
      "XcodeBuildMCP": {
 

## Links

- Repository: https://github.com/getsentry/XcodeBuildMCP
- Homepage: https://www.xcodebuildmcp.com
