---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 60
  scoring_breakdown:
    stars: 21
    recency: 8
    docs: 20
    community: 11
github_data:
  full_name: "elusznik/mcp-server-code-execution-mode"
  url: "https://github.com/elusznik/mcp-server-code-execution-mode"
  description: "An MCP server that executes Python code in isolated rootless containers with optional MCP server proxying. Implementation of Anthropic's and Cloudflare's ideas for reducing MCP tool definitions context bloat."
  stars: 319
  forks: 27
  open_issues: 4
  language: "Python"
  license: "GPL-3.0"
  last_push: "2025-12-05"
  created: "2025-11-10"
  topics: ["agentic-ai", "agents", "anthropic", "claude", "claude-code", "code-execution", "docker", "mcp", "model-context-protocol", "orchestration", "podman", "python", "token-optimization"]
---

# elusznik/mcp-server-code-execution-mode

> Discovered by arsenal scout — awaiting manual triage

## Description

An MCP server that executes Python code in isolated rootless containers with optional MCP server proxying. Implementation of Anthropic's and Cloudflare's ideas for reducing MCP tool definitions context bloat.

## README Excerpt

# MCP Code Execution Server: Zero-Context Discovery for 100+ MCP Tools

[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/elusznik-mcp-server-code-execution-mode-badge.png)](https://mseep.ai/app/elusznik-mcp-server-code-execution-mode)

**Stop paying 30,000 tokens per query.** This bridge implements Anthropic's discovery pattern with rootless security—reducing MCP context from 30K to 200 tokens while proxying any stdio server.

[![Anthropic Engineering](https://img.shields.io/badge/Anthropic-Engineering-orange)](https://www.anthropic.com/engineering/code-execution-with-mcp)
[![Cloudflare Blog](https://img.shields.io/badge/Cloudflare-Code_Mode-orange)](https://blog.cloudflare.com/code-mode/)
[![Docker MCP Gateway](https://img.shields.io/badge/Docker-MCP_Gateway-blue)](https://www.docker.com/blog/dynamic-mcps-stop-hardcoding-your-agents-world/)
[![Apple Machine Learning](https://img.shields.io/badge/Apple_Machine_Learning-CodeAct?logo=apple&style=flat-square)](https://machinelearning.apple.com/research/codeact)
[![MCP Protocol](https://img.shields.io/badge/MCP-Documentation-green)](https://modelcontextprotocol.io/)
[![Verified on MseeP](https://mseep.ai/badge.svg)](https://mseep.ai/app/4a84c349-1795-41fc-a299-83d4a29feee8)

## Overview

This bridge implements the **"Code Execution with MCP"** pattern, a convergence of ideas from industry leaders:

- **Apple's [CodeAct](https://machinelearning.apple.com/research/codeact)**: "Your LLM Agent Acts Better when Generating Code."
- **Anthropic's [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)**: "Building more efficient agents."
- **Cloudflare's [Code Mode](https://blog.cloudflare.com/code-mode/)**: "LLMs are better at writing code to call MCP, than at calling MCP directly."
- **Docker's [Dynamic MCPs](https://www.docker.com/blog/dynamic-mcps-stop-hardcoding-your-agents-world/)**: "Stop Hardcoding Your Agents’ World."
- **[Terminal Bench](https://www.tbench.ai)'s [Terminus](https://www.tbench.ai/terminus)**: "A realistic terminal environment for evaluating LLM agents."

Instead of exposing hundreds of individual tools to the LLM (which consumes massive context and confuses the model), this bridge exposes **one** tool: `run_python`. The LLM writes Python code to discover, call, and compose other tools.

### Why This vs. JS "Code Mode"?

While there are JavaScript-based alternatives (like [`universal-tool-calling-protocol/code-mode`](https://github.com/universal-tool-calling-protocol/code-mode)), this project is built for **Data Science** and **Security**:

| Feature | This Project (Python) | JS Code Mode (Node.js) |
| :--- | :--- | :--- |
| **Native Language** | **Python** (The language of AI/ML) | TypeScript/JavaScript |
| **Data Science** | **Native** (`pandas`, `numpy`, `scikit-learn`) | Impossible / Hacky |
| **Isolation** | **Hard** (Podman/Docker Containers) | Soft (Node.js VM) |
| **Security** | **Enterprise** (Rootless, No Net, Read-Only) | Process

## Links

- Repository: https://github.com/elusznik/mcp-server-code-execution-mode
