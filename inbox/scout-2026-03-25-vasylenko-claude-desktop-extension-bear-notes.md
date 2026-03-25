---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude desktop extension"
  quality_score: 65
  scoring_breakdown:
    stars: 18
    recency: 20
    docs: 20
    community: 7
github_data:
  full_name: "vasylenko/claude-desktop-extension-bear-notes"
  url: "https://github.com/vasylenko/claude-desktop-extension-bear-notes"
  description: "Claude Desktop extension with bundled MCP Server for Bear note taking app"
  stars: 145
  forks: 12
  open_issues: 11
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-14"
  created: "2025-08-31"
  topics: ["bear", "bear-notes", "claude", "claude-ai", "claude-desktop", "gtd-applications", "mcp-bundle", "mcp-server", "notes", "notetaking", "productivity", "second-brain", "writing"]
---

# vasylenko/claude-desktop-extension-bear-notes

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Desktop extension with bundled MCP Server for Bear note taking app

## README Excerpt

[![Supply Chain](https://github.com/vasylenko/claude-desktop-extension-bear-notes/actions/workflows/ci.yml/badge.svg)](https://github.com/vasylenko/claude-desktop-extension-bear-notes/actions/workflows/ci.yml)
[![Snyk](https://snyk.io/test/github/vasylenko/claude-desktop-extension-bear-notes/badge.svg)](https://snyk.io/test/github/vasylenko/claude-desktop-extension-bear-notes)
[![Verified on MseeP](https://mseep.ai/badge.svg)](https://mseep.ai/app/34d7b12a-3983-40a3-876f-3cdd2ccfe3f2)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/vasylenko/claude-desktop-extension-bear-notes)

# Bear Notes Claude Extension (aka MCP Bundle)

Search, read, create, and update your Bear Notes directly from Claude conversations.

This **local-only** extension reads Bear's SQLite database for fast search with OCR support, and uses Bear's native API for writes. Complete privacy: no external connections, all processing on your Mac.

Example prompts:

> Summarize our conversation and create a new Bear note with it

> Interview me about my side project idea and capture the key points in a Bear note

> Help me restructure the outline in my "Product Launch" note

> Let's brainstorm blog post ideas — save the best ones to my Bear note and refine them as we go

![](./docs/demo.gif)

## ✨ Key Features

- **10 MCP tools** for searching, reading, creating, updating, tagging, and archiving notes
- **OCR search** — finds text inside attached images and PDFs
- **Date-based search** with relative dates ("yesterday", "last week", "start of last month")
- **Tag management** — list tags as a tree, find untagged notes, add tags to notes
- **New note convention** (opt-in) — place tags right after the title instead of at the bottom
- **Content replacement** (opt-in) — replace the full note body or a specific section
- **Local-only** — no network calls, all data stays on your Mac

> [!NOTE]
> Complete privacy (except the data you send to your AI provider when using an AI assistant such as Claude, of course): this extension makes no external connections. All processing happens locally on your Mac using Bear's own database and API. There is no extra telemetry, usage statistics or anything like that.

## 📦 Installation

### Claude Desktop Extension

**Prerequisites**: [Bear app](https://bear.app/) must be installed and [Claude Desktop](https://claude.ai/download) must be installed.

1. Download the latest `bear-notes-mcpb.mcpb` extension from releases
2. Make sure your Claude Desktop is running (start if not)
3. Doubleclick on the extension file – Claude Desktop should show you the installation prompt

    If doubleclick does not work for some reason, then open Claude -> Settings -> Extensions -> Advanced Settings -> click "Install Extension".

4. DONE!

Ask Claude to search your Bear notes with a query like "Search my Bear notes for 'meeting'" - you should see your notes appear in the response!

### Standalone MCP Server

Want to use this Bear Notes MCP server with Cl

## Links

- Repository: https://github.com/vasylenko/claude-desktop-extension-bear-notes
