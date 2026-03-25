---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code agent subagent"
  quality_score: 52
  scoring_breakdown:
    stars: 14
    recency: 8
    docs: 20
    community: 10
github_data:
  full_name: "roddutra/agent-mcp-gateway"
  url: "https://github.com/roddutra/agent-mcp-gateway"
  description: "Provides per-subagent MCP access controls to Claude Code (or any MCP client) across all your MCPs and prevents context window bloat. Loads only 3 tools instead of all your MCP Server's tool definitions. Agents discover tools on-demand, only when needed. Control which servers and individual tools each agent/subagent can access."
  stars: 40
  forks: 6
  open_issues: 0
  language: "Python"
  license: "MIT"
  last_push: "2025-12-02"
  created: "2025-10-29"
  topics: []
---

# roddutra/agent-mcp-gateway

> Discovered by arsenal scout — awaiting manual triage

## Description

Provides per-subagent MCP access controls to Claude Code (or any MCP client) across all your MCPs and prevents context window bloat. Loads only 3 tools instead of all your MCP Server's tool definitions. Agents discover tools on-demand, only when needed. Control which servers and individual tools each agent/subagent can access.

## README Excerpt

# Agent MCP Gateway

<!-- mcp-name: io.github.roddutra/agent-mcp-gateway -->

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io) gateway that aggregates multiple MCP servers and provides policy-based access control for agents and subagents. Solves Claude Code's MCP context window waste by enabling on-demand tool discovery instead of loading all tool definitions upfront.

<a href="https://glama.ai/mcp/servers/@roddutra/agent-mcp-gateway">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@roddutra/agent-mcp-gateway/badge" />
</a>

## Status

- ✅ **M0: Foundation** - Configuration, policy engine, audit logging, `list_servers` tool
- ✅ **M1: Core** - Proxy infrastructure, `get_server_tools`, `execute_tool`, middleware, metrics, hot reload, OAuth support
- 🚧 **M2: Production** - HTTP transport, health checks (planned)
- 🚧 **M3: DX** - Single-agent mode, config validation CLI, Docker (planned)

**Current Version:** M1-Core Complete (with OAuth)

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Command-Line Options](#command-line-options)
- [Configuration File Discovery](#configuration-file-discovery)
- [Configuration](#configuration)
- [Usage](#usage)
- [Gateway Tools](#gateway-tools)
- [Security Considerations](#security-considerations)
- [Troubleshooting](#troubleshooting)
- [Testing](#testing)
- [Development](#development)
- [Architecture](#architecture)
- [Future Features](#future-features)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)
- [Acknowledgments](#acknowledgments)

## Overview

### The Problem

When multiple MCP servers are configured in development environments (Claude Code, Cursor, VS Code), all tool definitions from all servers load into every agent's and subagent's context window at startup:

- 5,000-50,000+ tokens consumed upfront
- 80-95% of loaded tools never used by individual agents
- Context needed for actual work gets wasted on unused tool definitions

### The Solution

The Agent MCP Gateway acts as a single MCP server that proxies to multiple downstream MCP servers based on configurable per-agent rules:

- **3 gateway tools** load at startup (~2k tokens)
- Agents discover and request specific tools on-demand
- **90%+ context reduction**
- Policy-based access control per agent/subagent

### How It Works

![Agent MCP Gateway Architecture](docs/diagram-snippet.png)

The gateway sits between agents and downstream MCP servers, exposing only 3 lightweight tools. When an agent needs specific functionality, it discovers available servers and tools through the gateway, which filters visibility based on policy rules - agents only see servers and tools they have access to. This reduces each agent's context window to only relevant tools, while the gateway handles proxying authorized requests to downstream servers.

**[View detailed diagram with examples →](docs/diagram-full.png)** (in

## Links

- Repository: https://github.com/roddutra/agent-mcp-gateway
