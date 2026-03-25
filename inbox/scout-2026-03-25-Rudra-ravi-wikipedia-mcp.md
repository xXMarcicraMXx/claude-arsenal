---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "anthropic mcp server"
  quality_score: 72
  scoring_breakdown:
    stars: 20
    recency: 20
    docs: 20
    community: 12
github_data:
  full_name: "Rudra-ravi/wikipedia-mcp"
  url: "https://github.com/Rudra-ravi/wikipedia-mcp"
  description: "A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs."
  stars: 211
  forks: 44
  open_issues: 5
  language: "Python"
  license: "MIT"
  last_push: "2026-03-12"
  created: "2025-03-08"
  topics: ["anthropic", "llm", "mcp-server", "open-source", "wikipedia", "wikipedia-api", "wikipedia-mcp", "wikipedia-mcp-server"]
---

# Rudra-ravi/wikipedia-mcp

> Discovered by arsenal scout — awaiting manual triage

## Description

A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to LLMs.

## README Excerpt

# Wikipedia MCP Server

[![smithery badge](https://smithery.ai/badge/@Rudra-ravi/wikipedia-mcp)](https://smithery.ai/server/@Rudra-ravi/wikipedia-mcp)

A Model Context Protocol (MCP) server that retrieves information from Wikipedia to provide context to Large Language Models (LLMs). This tool helps AI assistants access factual information from Wikipedia to ground their responses in reliable sources.

<a href="https://glama.ai/mcp/servers/@Rudra-ravi/wikipedia-mcp">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@Rudra-ravi/wikipedia-mcp/badge" alt="Wikipedia Server MCP server" />
</a>

![image](https://github.com/user-attachments/assets/e41382f7-111a-4105-97f3-7851c906843e)

## Overview

The Wikipedia MCP server provides real-time access to Wikipedia information through a standardized Model Context Protocol interface. This allows LLMs to retrieve accurate and up-to-date information directly from Wikipedia to enhance their responses.

## Verified By

[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/rudra-ravi-wikipedia-mcp-badge.png)](https://mseep.ai/app/rudra-ravi-wikipedia-mcp)

## Features

- **Search Wikipedia**: Find articles matching specific queries with enhanced diagnostics
- **Retrieve Article Content**: Get full article text with all information
- **Article Summaries**: Get concise summaries of articles
- **Section Extraction**: Retrieve specific sections from articles
- **Link Discovery**: Find links within articles to related topics
- **Related Topics**: Discover topics related to a specific article
- **Multi-language Support**: Access Wikipedia in different languages by specifying the `--language` or `-l` argument when running the server (e.g., `wikipedia-mcp --language ta` for Tamil).
- **Country/Locale Support**: Use intuitive country codes like `--country US`, `--country China`, or `--country TW` instead of language codes. Automatically maps to appropriate Wikipedia language variants.
- **Language Variant Support**: Support for language variants such as Chinese traditional/simplified (e.g., `zh-hans` for Simplified Chinese, `zh-tw` for Traditional Chinese), Serbian scripts (`sr-latn`, `sr-cyrl`), and other regional variants.
- **Optional caching**: Cache API responses for improved performance using --enable-cache
- **Modern MCP Transport Support**: Supports `stdio`, `http`, and `streamable-http` (with legacy `sse` compatibility).
- **Optional MCP Transport Auth**: Secure network transports with `--auth-mode static` or `--auth-mode jwt`.
- **Google ADK Compatibility**: Fully compatible with Google ADK agents and other AI frameworks that use strict function calling schemas

## Installation

### Using pipx (Recommended for Claude Desktop)

The best way to install for Claude Desktop usage is with pipx, which installs the command globally:

```bash
# Install pipx if you don't have it
pip install pipx
pipx ensurepath

# Install the Wikipedia MCP server
pipx install wikipedia-mcp
```

This ensures the `wikip

## Links

- Repository: https://github.com/Rudra-ravi/wikipedia-mcp
- Homepage: https://pypi.org/project/wikipedia-mcp/
