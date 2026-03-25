---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 81
  scoring_breakdown:
    stars: 27
    recency: 20
    docs: 20
    community: 14
github_data:
  full_name: "benborla/mcp-server-mysql"
  url: "https://github.com/benborla/mcp-server-mysql"
  description: "A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries."
  stars: 1412
  forks: 183
  open_issues: 35
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-03-10"
  created: "2024-12-09"
  topics: []
---

# benborla/mcp-server-mysql

> Discovered by arsenal scout — awaiting manual triage

## Description

A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries.

## README Excerpt

# MCP Server for MySQL - Claude Code Edition

> **🚀 This is a modified version optimized for Claude Code with SSH tunnel support**  
> **Original Author:** [@benborla29](https://github.com/benborla)  
> **Original Repository:** [https://github.com/benborla/mcp-server-mysql](https://github.com/benborla/mcp-server-mysql)  
> **License:** MIT  

## MCP Server for MySQL based on NodeJS

[![Trust Score](https://archestra.ai/mcp-catalog/api/badge/quality/benborla/mcp-server-mysql)](https://archestra.ai/mcp-catalog/benborla__mcp-server-mysql)

### Key Features of This Fork

- ✅ **Claude Code Integration** - Optimized for use with Anthropic's Claude Code CLI
- ✅ **SSH Tunnel Support** - Built-in support for SSH tunnels to remote databases
- ✅ **Auto-start/stop Hooks** - Automatic tunnel management with Claude start/stop
- ✅ **DDL Operations** - Added `MYSQL_DISABLE_READ_ONLY_TRANSACTIONS` for CREATE TABLE support
- ✅ **Multi-Project Setup** - Easy configuration for multiple projects with different databases

### Quick Start for Claude Code Users

1. **Read the Setup Guide**: See [PROJECT_SETUP_GUIDE.md](PROJECT_SETUP_GUIDE.md) for detailed instructions
2. **Configure SSH Tunnels**: Set up automatic SSH tunnels for remote databases
3. **Use with Claude**: Integrated MCP server works seamlessly with Claude Code

A Model Context Protocol server that provides access to MySQL databases through SSH tunnels. This server enables Claude and other LLMs to inspect database schemas and execute SQL queries securely.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
  - [Smithery](#using-smithery)
  - [Clone to Local Repository](#running-from-local-repository)
  - [Remote mode](#run-in-remote-mode)
- [Components](#components)
- [Configuration](#configuration)
- [Environment Variables](#environment-variables)
- [Multi-DB Mode](#multi-db-mode)
- [Schema-Specific Permissions](#schema-specific-permissions)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Requirements

- Node.js v20 or higher
- MySQL 5.7 or higher (MySQL 8.0+ recommended)
- MySQL user with appropriate permissions for the operations you need
- For write operations: MySQL user with INSERT, UPDATE, and/or DELETE privileges

## Installation

### Using Smithery

There are several ways to install and configure the MCP server but the most common would be checking this website [https://smithery.ai/server/@benborla29/mcp-server-mysql](https://smithery.ai/server/@benborla29/mcp-server-mysql)

### Cursor

For Cursor IDE, you can install this MCP server with the following command in your project:

1. Visit [https://smithery.ai/server/@benborla29/mcp-server-mysql](https://smithery.ai/server/@benborla29/mcp-server-mysql)
2. Follow the instruction for Cursor

MCP Get provides a centralized registry of MCP servers and simplifies the installation process.

### Codex CLI

Codex CLI installation is similar to Claude Code

## Links

- Repository: https://github.com/benborla/mcp-server-mysql
