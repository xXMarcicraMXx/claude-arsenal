---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "anthropic mcp server"
  quality_score: 73
  scoring_breakdown:
    stars: 25
    recency: 15
    docs: 20
    community: 13
github_data:
  full_name: "QuantGeekDev/mcp-framework"
  url: "https://github.com/QuantGeekDev/mcp-framework"
  description: "A framework for writing MCP (Model Context Protocol) servers in Typescript"
  stars: 907
  forks: 102
  open_issues: 44
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-02-05"
  created: "2024-12-08"
  topics: ["anthropic", "claude", "genai", "llm", "llms", "mcp", "modelcontextprotocol"]
---

# QuantGeekDev/mcp-framework

> Discovered by arsenal scout — awaiting manual triage

## Description

A framework for writing MCP (Model Context Protocol) servers in Typescript

## README Excerpt

# MCP Framework

MCP-Framework is a framework for building Model Context Protocol (MCP) servers elegantly in TypeScript.

MCP-Framework gives you architecture out of the box, with automatic directory-based discovery for tools, resources, and prompts. Use our powerful MCP abstractions to define tools, resources, or prompts in an elegant way. Our cli makes getting started with your own MCP server a breeze

## Features

- 🛠️ Automatic discovery and loading of tools, resources, and prompts
- Multiple transport support (stdio, SSE, HTTP Stream)
- TypeScript-first development with full type safety
- Built on the official MCP SDK
- Easy-to-use base classes for tools, prompts, and resources
- Out of the box authentication for SSE endpoints (OAuth 2.1, JWT, API Key)

## Projects Built with MCP Framework

The following projects and services are built using MCP Framework:

- ### [tip.md](https://tip.md)
A crypto tipping service that enables AI assistants to help users send cryptocurrency tips to content creators directly from their chat interface. The MCP service allows for:
 - Checking wallet types for users
 - Preparing cryptocurrency tips for users/agents to complete
Setup instructions for various clients (Cursor, Sage, Claude Desktop) are available in their [MCP Server documentation](https://docs.tip.md/mcp-server/).

## Support our work

[![Tip in Crypto](https://tip.md/badge.svg)](https://tip.md/QuantGeekDev)


# [Read the full docs here](https://mcp-framework.com)





## Creating a repository with mcp-framework

### Using the CLI (Recommended)

```bash
# Install the framework globally
npm install -g mcp-framework

# Create a new MCP server project
mcp create my-mcp-server

# Navigate to your project
cd my-mcp-server

# Your server is ready to use!
```

## CLI Usage

The framework provides a powerful CLI for managing your MCP server projects:

### Project Creation

```bash
# Create a new project
mcp create <your project name here>

# Create a new project with the new EXPERIMENTAL HTTP transport
Heads up: This will set cors allowed origin to "*", modify it in the index if you wish
mcp create <your project name here> --http --port 1337 --cors
```

# Options:
# --http: Use HTTP transport instead of default stdio
# --port <number>: Specify HTTP port (default: 8080)
# --cors: Enable CORS with wildcard (*) access

### Adding a Tool

```bash
# Add a new tool
mcp add tool price-fetcher
```

### Building and Validation

The framework provides comprehensive validation to ensure your tools are properly documented and functional:

```bash
# Build with automatic validation (recommended)
npm run build

# Build with custom validation settings
MCP_SKIP_TOOL_VALIDATION=false npm run build  # Force validation (default)
MCP_SKIP_TOOL_VALIDATION=true npm run build   # Skip validation (not recommended)
```

### Validating Tools

```bash
# Validate all tools have proper descriptions (for Zod schemas)
mcp validate
```

This command checks that all tools using Zod schemas h

## Links

- Repository: https://github.com/QuantGeekDev/mcp-framework
- Homepage: https://mcp-framework.com/
