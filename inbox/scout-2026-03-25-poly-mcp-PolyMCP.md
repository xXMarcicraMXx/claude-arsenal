---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "anthropic mcp server"
  quality_score: 66
  scoring_breakdown:
    stars: 19
    recency: 20
    docs: 20
    community: 7
github_data:
  full_name: "poly-mcp/PolyMCP"
  url: "https://github.com/poly-mcp/PolyMCP"
  description: "Polymcp provides a simple and efficient way to interact with MCP servers using custom agents"
  stars: 162
  forks: 10
  open_issues: 1
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-02"
  created: "2025-10-10"
  topics: ["agent-framework", "ai-agent", "anthropic", "code-mode-mcp", "llm-integration", "mcp", "mcp-client", "mcp-inspector", "mcp-server", "model-context-protocol", "ollama", "open-source", "openai", "polymcp", "python", "skills", "stdio-mcp", "tool-orchestration", "typescript", "wasm"]
---

# poly-mcp/PolyMCP

> Discovered by arsenal scout — awaiting manual triage

## Description

Polymcp provides a simple and efficient way to interact with MCP servers using custom agents

## README Excerpt

<p align="center">
  <img src="poly-mcp.png" alt="PolymCP Logo" width="500"/>
</p>

<p align="center">
  <a href="https://pypi.org/project/polymcp/"><img src="https://img.shields.io/pypi/v/polymcp.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/polymcp/"><img src="https://img.shields.io/pypi/pyversions/polymcp.svg" alt="Python Versions"></a>
  <a href="LICENSE"><img src="https://img.shields.io/pypi/l/polymcp.svg" alt="License"></a>
  <a href="https://github.com/llm-use/polymcp/stargazers"><img src="https://img.shields.io/github/stars/llm-use/polymcp?style=social" alt="GitHub stars"></a>
  <a href="https://pepy.tech/project/polymcp"><img src="https://img.shields.io/pepy/dt/polymcp" alt="PyPI downloads"></a>
</p>

> Universal MCP toolkit and agent framework for Python and TypeScript.

## Overview

PolyMCP gives teams one consistent way to expose tools, connect MCP servers, and run agents that orchestrate those tools. It ships in Python and TypeScript, plus a standalone Inspector and an MCP Apps SDK.

Version: 1.3.8

## What You Can Build

- MCP servers from normal functions
- MCP clients over HTTP, stdio, or in-process transports
- Agents that orchestrate one or more MCP servers
- 🦞 Autonomous OpenClaw-style execution agent workflows with PolyClaw (Docker-first)
- Skills via skills.sh for tool selection and capability packaging
- UI-based MCP Apps with HTML resources and tool bridges

## Project Map

- `polymcp/` Python package (tools, agents, auth, sandbox, CLI)
- `polymcp-ts/` TypeScript implementation
- `polymcp-ts/use_cases/` TypeScript runnable B2B/B2C use cases
- `polymcp-inspector/` standalone Inspector app
- `polymcp_website/` marketing/docs website
- `use_cases/` Python runnable B2B/B2C use cases
- `polymcp_sdk_mcp_apps/` MCP Apps SDK
- `polymcp/cli/` CLI documentation
- `examples/` runnable examples
- `tests/` Python tests
- `registry/` sample registry files
- `my-project/` scaffold output from `polymcp init`

## Quick Start (Python)

Requirements: Python 3.8+

```bash
pip install polymcp
```

Create an MCP HTTP server from plain functions:

```python
from polymcp import expose_tools_http


def add(a: int, b: int) -> int:
    return a + b


app = expose_tools_http(
    tools=[add],
    title="Math Server",
    description="MCP tools over HTTP",
)
```

Run:

```bash
uvicorn server:app --host 0.0.0.0 --port 8000
```

## Quick Start (TypeScript)

Requirements: Node.js 18+

```bash
cd polymcp-ts
npm install
npm run build
```

## Skills (skills.sh)

PolyMCP delegates skills management to the skills.sh CLI.
PolyAgent and UnifiedPolyAgent automatically inject relevant skills into prompts
to improve tool selection and planning.

```bash
npx skills --help

# Install in current project (./.agents/skills)
npx skills add vercel-labs/agent-skills

# Install globally (~/.agents/skills)
npx skills add vercel-labs/agent-skills -g

npx skills list
npx skills list -g
```

Python helper:

```python
from polymcp import run_skills_cli

run_sk

## Links

- Repository: https://github.com/poly-mcp/PolyMCP
