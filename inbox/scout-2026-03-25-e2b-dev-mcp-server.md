---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 59
  scoring_breakdown:
    stars: 22
    recency: 20
    docs: 8
    community: 9
github_data:
  full_name: "e2b-dev/mcp-server"
  url: "https://github.com/e2b-dev/mcp-server"
  description: "Giving Claude ability to run code with E2B via MCP (Model Context Protocol)"
  stars: 384
  forks: 67
  open_issues: 4
  language: "JavaScript"
  license: "Apache-2.0"
  last_push: "2026-02-28"
  created: "2024-12-01"
  topics: ["anthropic", "claude", "claude-3-5-sonnet", "claude-ai", "model-context-protocol"]
---

# e2b-dev/mcp-server

> Discovered by arsenal scout — awaiting manual triage

## Description

Giving Claude ability to run code with E2B via MCP (Model Context Protocol)

## README Excerpt

![E2B MCP Server Preview Light](/readme-assets/mcp-server-light.png#gh-light-mode-only)
![E2B MCP Server Preview Dark](/readme-assets/mcp-server-dark.png#gh-dark-mode-only)

# E2B MCP Server

[![smithery badge](https://smithery.ai/badge/e2b)](https://smithery.ai/server/e2b)

This repository contains the source code for the [E2B](https://e2b.dev) MCP server.

The E2B MCP server allows you to add [code interpreting capabilities](https://github.com/e2b-dev/code-interpreter) to your Claude Desktop app via the E2B Sandbox. See demo [here](https://x.com/mishushakov/status/1863286108433317958).


Available in two editions:

- [JavaScript](packages/js/README.md)

- [Python](packages/python/README.md)


### Installing via Smithery

You can also install E2B for Claude Desktop automatically via [Smithery](https://smithery.ai/server/e2b):

```bash
npx @smithery/cli install e2b --client claude
```


## Links

- Repository: https://github.com/e2b-dev/mcp-server
