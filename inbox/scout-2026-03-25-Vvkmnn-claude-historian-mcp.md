---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "anthropic mcp server"
  quality_score: 76
  scoring_breakdown:
    stars: 20
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "Vvkmnn/claude-historian-mcp"
  url: "https://github.com/Vvkmnn/claude-historian-mcp"
  description: "📜 An MCP server for conversation history search and retrieval in Claude Code"
  stars: 217
  forks: 17
  open_issues: 4
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-23"
  created: "2025-07-14"
  topics: ["ai", "ai-tools", "anthropic", "claude", "claude-code", "context-retrieval", "conversation-history", "developer-tools", "inverted-index", "jsonl", "llm", "mcp", "mcp-server", "memory", "model-context-protocol", "nodejs", "npx", "search", "session", "typescript"]
---

# Vvkmnn/claude-historian-mcp

> Discovered by arsenal scout — awaiting manual triage

## Description

📜 An MCP server for conversation history search and retrieval in Claude Code

## README Excerpt

<img align="right" src="claude-historian.svg" alt="claude-historian-mcp" width="220">

# claude-historian-mcp

An [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server for searching your [Claude Code](https://docs.anthropic.com/en/docs/claude-code) conversation history. Find past solutions, track file changes, and learn from previous work.

<br clear="right">

![claude-historian-mcp](demo/demo.gif)

[![npm version](https://img.shields.io/npm/v/claude-historian-mcp.svg)](https://www.npmjs.com/package/claude-historian-mcp) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?logo=typescript&logoColor=white)](https://www.typescriptlang.org/) [![Node.js](https://img.shields.io/badge/node-%3E%3D20-brightgreen)](https://nodejs.org/) [![Claude](https://img.shields.io/badge/Claude-D97757?logo=claude&logoColor=fff)](#) [![GitHub stars](https://img.shields.io/github/stars/Vvkmnn/claude-historian-mcp?style=social)](https://github.com/Vvkmnn/claude-historian-mcp) ![CodeRabbit Pull Request Reviews](https://img.shields.io/coderabbit/prs/github/Vvkmnn/claude-historian-mcp?utm_source=oss&utm_medium=github&utm_campaign=Vvkmnn%2Fclaude-historian-mcp&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews)

---

## install

**Requirements:**

[![Claude Code](https://img.shields.io/badge/Claude_Code-555?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxOCAxMCIgc2hhcGUtcmVuZGVyaW5nPSJjcmlzcEVkZ2VzIj4KICA8IS0tIENsYXdkOiBDbGF1ZGUgQ29kZSBtYXNjb3QgLS0+CiAgPCEtLSBEZWNvZGVkIGZyb206IOKWkOKWm+KWiOKWiOKWiOKWnOKWjCAvIOKWneKWnOKWiOKWiOKWiOKWiOKWiOKWm+KWmCAvIOKWmOKWmCDilp3ilp0gLS0+CiAgPCEtLSBTdWItcGl4ZWxzIGFyZSAxIHdpZGUgeCAyIHRhbGwgdG8gbWF0Y2ggdGVybWluYWwgY2hhciBjZWxsIGFzcGVjdCByYXRpbyAtLT4KICA8cmVjdCBmaWxsPSIjZDk3NzU3IiB4PSIzIiAgeT0iMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjIiLz4KICA8cmVjdCBmaWxsPSIjZDk3NzU3IiB4PSIzIiAgeT0iMiIgd2lkdGg9IjIiICBoZWlnaHQ9IjIiLz4KICA8cmVjdCBmaWxsPSIjZDk3NzU3IiB4PSI2IiAgeT0iMiIgd2lkdGg9IjYiICBoZWlnaHQ9IjIiLz4KICA8cmVjdCBmaWxsPSIjZDk3NzU3IiB4PSIxMyIgeT0iMiIgd2lkdGg9IjIiICBoZWlnaHQ9IjIiLz4KICA8cmVjdCBmaWxsPSIjZDk3NzU3IiB4PSIxIiAgeT0iNCIgd2lkdGg9IjE2IiBoZWlnaHQ9IjIiLz4KICA8cmVjdCBmaWxsPSIjZDk3NzU3IiB4PSIzIiAgeT0iNiIgd2lkdGg9IjEyIiBoZWlnaHQ9IjIiLz4KICA8cmVjdCBmaWxsPSIjZDk3NzU3IiB4PSI0IiAgeT0iOCIgd2lkdGg9IjEiICBoZWlnaHQ9IjIiLz4KICA8cmVjdCBmaWxsPSIjZDk3NzU3IiB4PSI2IiAgeT0iOCIgd2lkdGg9IjEiICBoZWlnaHQ9IjIiLz4KICA8cmVjdCBmaWxsPSIjZDk3NzU3IiB4PSIxMSIgeT0iOCIgd2lkdGg9IjEiICBoZWlnaHQ9IjIiLz4KICA8cmVjdCBmaWxsPSIjZDk3NzU3IiB4PSIxMyIgeT0iOCIgd2lkdGg9IjEiICBoZWlnaHQ9IjIiLz4KPC9zdmc+Cg==)](https://claude.ai/code)

**From shell:**

```bash
claude mcp add claude-historian-mcp -- npx claude-historian-mcp
```

**From inside Claude** (restart required):

```
Add this to our global mcp config: npx claude-historian-mcp

Install this mcp: https://github.com/Vvkmnn/cla

## Links

- Repository: https://github.com/Vvkmnn/claude-historian-mcp
- Homepage: https://www.npmjs.com/package/claude-historian-mcp
