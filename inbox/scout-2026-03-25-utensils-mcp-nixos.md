---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "anthropic mcp server"
  quality_score: 75
  scoring_breakdown:
    stars: 23
    recency: 20
    docs: 20
    community: 12
github_data:
  full_name: "utensils/mcp-nixos"
  url: "https://github.com/utensils/mcp-nixos"
  description: "MCP-NixOS - Model Context Protocol Server for NixOS resources"
  stars: 514
  forks: 29
  open_issues: 5
  language: "Python"
  license: "MIT"
  last_push: "2026-03-11"
  created: "2025-03-20"
  topics: ["ai-assistant", "ai-integration", "ai-tools", "anthropic", "claude", "developer-tools", "devops-tools", "fastmcp", "llm-tools", "mcp", "model-context-protocol", "nix", "nix-options", "nix-packages", "nix-search", "nixos", "package-search", "python", "sre-tools"]
---

# utensils/mcp-nixos

> Discovered by arsenal scout — awaiting manual triage

## Description

MCP-NixOS - Model Context Protocol Server for NixOS resources

## README Excerpt

# MCP-NixOS - Because Your AI Shouldn't Hallucinate Package Names

[![CI](https://github.com/utensils/mcp-nixos/actions/workflows/ci.yml/badge.svg)](https://github.com/utensils/mcp-nixos/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/utensils/mcp-nixos/graph/badge.svg?token=kdcbgvq4Bh)](https://codecov.io/gh/utensils/mcp-nixos)
[![PyPI](https://img.shields.io/pypi/v/mcp-nixos.svg)](https://pypi.org/project/mcp-nixos/)
[![FlakeHub](https://img.shields.io/endpoint?url=https://flakehub.com/f/utensils/mcp-nixos/badge)](https://flakehub.com/flake/utensils/mcp-nixos)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
![CodeRabbit Pull Request Reviews](https://img.shields.io/coderabbit/prs/github/utensils/mcp-nixos?utm_source=oss&utm_medium=github&utm_campaign=utensils%2Fmcp-nixos&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews)
[![Built with Claude](https://img.shields.io/badge/Built%20with-Claude-D97757?logo=claude&logoColor=white)](https://claude.ai)

## Quick Start

**🚨 No Nix/NixOS Required!** Works on any system - Windows, macOS, Linux. You're just querying APIs.

### Option 1: uvx (Recommended)

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=nixos&config=eyJjb21tYW5kIjoidXZ4IG1jcC1uaXhvcyJ9)

```json
{
  "mcpServers": {
    "nixos": {
      "command": "uvx",
      "args": ["mcp-nixos"]
    }
  }
}
```

### Option 2: Nix

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=nixos&config=eyJjb21tYW5kIjoibml4IHJ1biBnaXRodWI6dXRlbnNpbHMvbWNwLW5peG9zIC0tIn0%3D)

```json
{
  "mcpServers": {
    "nixos": {
      "command": "nix",
      "args": ["run", "github:utensils/mcp-nixos", "--"]
    }
  }
}
```

### Option 3: Docker

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/install-mcp?name=nixos&config=eyJjb21tYW5kIjoiZG9ja2VyIiwiYXJncyI6WyJydW4iLCItLXJtIiwiLWkiLCJnaGNyLmlvL3V0ZW5zaWxzL21jcC1uaXhvcyJdfQ%3D%3D)

```json
{
  "mcpServers": {
    "nixos": {
      "command": "docker",
      "args": ["run", "--rm", "-i", "ghcr.io/utensils/mcp-nixos"]
    }
  }
}
```

Your AI now has access to real NixOS data instead of making things up. You're welcome.

### Option 4: HTTP (Remote MCP)

FastMCP supports running this server over HTTP at a URL (the MCP endpoint defaults to `/mcp`).

```bash
# Run an HTTP MCP server at http://127.0.0.1:8000/mcp
MCP_NIXOS_TRANSPORT=http MCP_NIXOS_HOST=127.0.0.1 MCP_NIXOS_PORT=8000 mcp-nixos
```

STDIO (default):

```bash
MCP_NIXOS_TRANSPORT=stdio mcp-nixos
```

Custom path:

```bash
MCP_NIXOS_TRANSPORT=http MCP_NIXOS_PATH=/api/mcp mcp-nixos
```

Stateless HTTP (disables per-client session state):

```bash
MCP_NIXOS_TRANSPORT=http MCP_NIXOS_STATELESS_HTTP=1 mcp-nixos
```

## What Is This?

An MCP server providing accurate, real-time information about:

- **NixOS pac

## Links

- Repository: https://github.com/utensils/mcp-nixos
- Homepage: https://mcp-nixos.io/
