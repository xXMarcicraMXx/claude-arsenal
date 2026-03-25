---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code configuration"
  quality_score: 62
  scoring_breakdown:
    stars: 16
    recency: 25
    docs: 15
    community: 6
github_data:
  full_name: "lirantal/ls-mcp"
  url: "https://github.com/lirantal/ls-mcp"
  description: "List MCP Server configurations in your system used by AI applications like Cursor, Claude Desktop, VS Code and others"
  stars: 79
  forks: 9
  open_issues: 1
  language: "TypeScript"
  license: "Apache-2.0"
  last_push: "2026-03-23"
  created: "2025-05-26"
  topics: ["claude-ai", "claude-desktop", "cursor", "cursor-ai", "mcp", "mcp-server", "model-context-protocol"]
---

# lirantal/ls-mcp

> Discovered by arsenal scout — awaiting manual triage

## Description

List MCP Server configurations in your system used by AI applications like Cursor, Claude Desktop, VS Code and others

## README Excerpt

<!-- markdownlint-disable -->

<p align="center"><h1 align="center">
  ls-mcp
  </h1>
</p>

<p align="center">
  Detect Configured MCP (Model Context Protocol) in your local dev environment
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/ls-mcp"><img src="https://badgen.net/npm/v/ls-mcp" alt="npm version"/></a>
  <a href="https://www.npmjs.com/package/ls-mcp"><img src="https://badgen.net/npm/license/ls-mcp" alt="license"/></a>
  <a href="https://www.npmjs.com/package/ls-mcp"><img src="https://badgen.net/npm/dt/ls-mcp" alt="downloads"/></a>
  <a href="https://github.com/lirantal/ls-mcp/actions?workflow=CI"><img src="https://github.com/lirantal/ls-mcp/workflows/CI/badge.svg" alt="build"/></a>
  <a href="https://app.codecov.io/gh/lirantal/ls-mcp"><img src="https://badgen.net/codecov/c/github/lirantal/ls-mcp" alt="codecov"/></a>
  <a href="https://snyk.io/test/github/lirantal/ls-mcp"><img src="https://snyk.io/test/github/lirantal/ls-mcp/badge.svg" alt="Known Vulnerabilities"/></a>
  <a href="./SECURITY.md"><img src="https://img.shields.io/badge/Security-Responsible%20Disclosure-yellow.svg" alt="Responsible Disclosure Policy" /></a>
</p>

<div align="center">
  <img src="https://raw.githubusercontent.com/lirantal/ls-mcp/refs/heads/main/.github/ls-mcp-logo.png" alt="ls-mcp logo"/>
</div>

## Features

- **🔍 MCP Discovery**: Automatically detect MCP servers across various AI applications and agentic IDEs
- **📁 Directory Bubbling**: Intelligent discovery of project-scoped MCP configs from nested directories, supporting project-scoped MCP Server configuration and global configurations
- **🔄 Process Detection**: Real-time status of running MCP servers
- **🔒 Credential Analysis**: Security analysis of environment variables and API keys for potentially exposed credentials in MCP Servers

## Usage: CLI

```bash
npx ls-mcp
```

### Analyze Specific Files

To analyze specific MCP configuration files instead of using automatic discovery, use the `--files` flag. This flag **replaces** automatic discovery and only analyzes the files you specify:

```bash
# Single file
npx ls-mcp --files ./mcp-config.json

# Multiple files (comma-separated)
npx ls-mcp --files ./config1.json,./config2.json

# Multiple files (space-separated)
npx ls-mcp --files ./config1.json ./config2.json
```

The `--files` flag automatically detects the configuration structure in your files, supporting various formats including:
- `servers` - Standard MCP configuration key
- `mcpServers` - Alternative MCP configuration key
- `mcp.servers` - Nested configuration format
- `context_servers` - Context-based configuration format

### Show All Providers

By default, `ls-mcp` hides providers that have zero configured servers to reduce clutter. To show all providers including those with empty configurations, use the `--all` or `-a` flag:

```bash
# Show all providers including empty ones
npx ls-mcp --all

# Short form
npx ls-mcp -a

# Combine with JSON output
npx ls-mcp --all --json
```


## Links

- Repository: https://github.com/lirantal/ls-mcp
