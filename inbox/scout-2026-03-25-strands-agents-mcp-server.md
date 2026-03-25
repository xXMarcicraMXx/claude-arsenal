---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "anthropic mcp server"
  quality_score: 70
  scoring_breakdown:
    stars: 21
    recency: 20
    docs: 20
    community: 9
github_data:
  full_name: "strands-agents/mcp-server"
  url: "https://github.com/strands-agents/mcp-server"
  description: "This MCP server provides documentation about Strands Agents to your GenAI tools, so you can use your favorite AI coding assistant to vibe-code Strands Agents."
  stars: 266
  forks: 66
  open_issues: 4
  language: "Python"
  license: "Apache-2.0"
  last_push: "2026-03-11"
  created: "2025-05-14"
  topics: ["agentic", "agentic-ai", "agents", "ai", "anthropic", "autonomous-agents", "bedrock", "genai", "litellm", "llama", "llm", "machine-learning", "mcp", "multi-agent-systems", "ollama", "openai", "opentelemetry", "python", "strands-agents"]
---

# strands-agents/mcp-server

> Discovered by arsenal scout — awaiting manual triage

## Description

This MCP server provides documentation about Strands Agents to your GenAI tools, so you can use your favorite AI coding assistant to vibe-code Strands Agents.

## README Excerpt

<div align="center">
  <div>
    <a href="https://strandsagents.com">
      <img src="https://strandsagents.com/latest/assets/logo-github.svg" alt="Strands Agents" width="55px" height="105px">
    </a>
  </div>

  <h1>
    Strands Agents MCP Server
  </h1>

  <h2>
    A model-driven approach to building AI agents in just a few lines of code.
  </h2>

  <div align="center">
    <a href="https://github.com/strands-agents/mcp-server/graphs/commit-activity"><img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/m/strands-agents/mcp-server"/></a>
    <a href="https://github.com/strands-agents/mcp-server/issues"><img alt="GitHub open issues" src="https://img.shields.io/github/issues/strands-agents/mcp-server"/></a>
    <a href="https://github.com/strands-agents/mcp-server/pulls"><img alt="GitHub open pull requests" src="https://img.shields.io/github/issues-pr/strands-agents/mcp-server"/></a>
    <a href="https://github.com/strands-agents/mcp-server/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/strands-agents/mcp-server"/></a>
    <a href="https://pypi.org/project/strands-agents-mcp-server/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/strands-agents-mcp-server"/></a>
    <a href="https://python.org"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/strands-agents-mcp-server"/></a>
  </div>

  <p>
    <a href="https://strandsagents.com/">Documentation</a>
    ◆ <a href="https://github.com/strands-agents/samples">Samples</a>
    ◆ <a href="https://github.com/strands-agents/sdk-python">Python SDK</a>
    ◆ <a href="https://github.com/strands-agents/tools">Tools</a>
    ◆ <a href="https://github.com/strands-agents/agent-builder">Agent Builder</a>
    ◆ <a href="https://github.com/strands-agents/mcp-server">MCP Server</a>
  </p>
</div>

This MCP server provides curated documentation access to your GenAI tools via llms.txt files, enabling AI coding assistants to search and retrieve relevant documentation with intelligent ranking.

## Features

- **Smart Document Search**: TF-IDF based search with Markdown-aware scoring that prioritizes titles, headers, and code blocks
- **Section-Based Browsing**: Browse document structure via table of contents, then fetch only the section you need - more token-efficient than retrieving full pages
- **Curated Content**: Indexes documentation from llms.txt files with clean, human-readable titles
- **On-Demand Fetching**: Lazy-loads full document content only when needed for optimal performance
- **Snippet Generation**: Provides contextual snippets with relevance scoring for quick overview
- **Real URL Support**: Works with actual HTTPS URLs while maintaining backward compatibility

## Prerequisites

The usage methods below require [uv](https://github.com/astral-sh/uv) to be installed on your system. You can install it by following the [official installation instructions](https://github.com/astral-sh/uv#installation).

## Instal

## Links

- Repository: https://github.com/strands-agents/mcp-server
- Homepage: https://strandsagents.com
