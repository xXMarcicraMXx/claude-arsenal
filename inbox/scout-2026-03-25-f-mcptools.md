---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 68
  scoring_breakdown:
    stars: 27
    recency: 8
    docs: 20
    community: 13
github_data:
  full_name: "f/mcptools"
  url: "https://github.com/f/mcptools"
  description: "A command-line interface for interacting with MCP (Model Context Protocol) servers using both stdio and HTTP transport."
  stars: 1535
  forks: 118
  open_issues: 35
  language: "Go"
  license: "MIT"
  last_push: "2025-12-18"
  created: "2025-03-25"
  topics: ["mcp", "mcp-server", "modelcontextprotocol"]
---

# f/mcptools

> Discovered by arsenal scout — awaiting manual triage

## Description

A command-line interface for interacting with MCP (Model Context Protocol) servers using both stdio and HTTP transport.

## README Excerpt

<p align="center">
  <img src="./.github/resources/logo.png" alt="MCP Tools" height="150">
</p>

<p align="center">
  <h1 align="center">Swiss Army Knife for MCP Servers</h1>
  <p align="center">
    A comprehensive command-line interface for interacting with MCP (Model Context Protocol) servers.
    <br>
    Discover, call, and manage tools, resources, and prompts from any MCP-compatible server.
    <br>
    Supports multiple transport methods, output formats, and includes powerful mock and proxy server capabilities.
  </p>
</p>

[![Blog Post](https://img.shields.io/badge/Blog-Read%20about%20MCP%20Tools-blue)](https://blog.fka.dev/blog/2025-03-27-mcp-inspector-vs-mcp-tools/)

## Table of Contents

- [Overview](#overview)
- [Difference Between the MCP Inspector and MCP Tools](https://blog.fka.dev/blog/2025-03-27-mcp-inspector-vs-mcp-tools/)
- [Installation](#installation)
  - [Using Homebrew](#using-homebrew)
  - [From Source](#from-source)
- [Getting Started](#getting-started)
- [Features](#features)
  - [Transport Options](#transport-options)
  - [Output Formats](#output-formats)
  - [Commands](#commands)
  - [Interactive Shell](#interactive-shell)
  - [Web Interface](#web-interface)
  - [Project Scaffolding](#project-scaffolding)
- [Server Aliases](#server-aliases)
- [LLM Apps Config Management](#llm-apps-config-management)
- [Server Modes](#server-modes)
  - [Mock Server Mode](#mock-server-mode)
  - [Proxy Mode](#proxy-mode)
  - [Guard Mode](#guard-mode)
- [Examples](#examples)
  - [Basic Usage](#basic-usage)
  - [Script Integration](#script-integration)
  - [Debugging](#debugging)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)

## Overview

MCP Tools provides a versatile CLI for working with Model Context Protocol (MCP) servers. It enables you to:

- Discover and call tools provided by MCP servers
- Access and utilize resources exposed by MCP servers
- Create mock servers for testing client applications
- Proxy MCP requests to shell scripts for easy extensibility
- Create interactive shells for exploring and using MCP servers
- Scaffold new MCP projects with TypeScript support
- Format output in various styles (JSON, pretty-printed, table)
- Guard and restrict access to specific tools and resources
- Support all transport methods (HTTP, stdio)

<p align="center">
  <img src=".github/resources/screenshot.png" alt="MCP Tools Screenshot" width="700">
</p>

## Installation

### Using Homebrew (for macOS)

```bash
brew tap f/mcptools
brew install mcp
```

> ❕ The binary is installed as `mcp` but can also be accessed as `mcpt` to avoid conflicts with other tools that might use the `mcp` command name.

### From Source (for Windows and GNU/Linux)

```bash
go install github.com/f/mcptools/cmd/mcptools@latest
```

> ❕ The binary will be installed as `mcptools` when but can be aliased to `mcpt` for convenience.
> 
> <img width="500" alt="Screenshot 2025-05-05 at 22 21 29" src="https://github.com/user-attachments/assets/eaba

## Links

- Repository: https://github.com/f/mcptools
