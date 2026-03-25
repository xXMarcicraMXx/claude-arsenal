---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 76
  scoring_breakdown:
    stars: 23
    recency: 25
    docs: 20
    community: 8
github_data:
  full_name: "samvallad33/vestige"
  url: "https://github.com/samvallad33/vestige"
  description: "Cognitive memory for AI agents — FSRS-6 spaced repetition, 29 brain modules, 3D dashboard, single 22MB Rust binary. MCP server for Claude, Cursor, VS Code, Xcode, JetBrains."
  stars: 445
  forks: 39
  open_issues: 6
  language: "Rust"
  license: "AGPL-3.0"
  last_push: "2026-03-17"
  created: "2026-01-25"
  topics: ["ai-memory", "claude", "cognitive-science", "cursor", "embeddings", "fsrs", "long-term-memory", "mcp", "mcp-server", "neuroscience", "onnx", "rust", "spaced-repetition", "sqlite", "sveltekit", "threejs", "vscode", "webgpu"]
---

# samvallad33/vestige

> Discovered by arsenal scout — awaiting manual triage

## Description

Cognitive memory for AI agents — FSRS-6 spaced repetition, 29 brain modules, 3D dashboard, single 22MB Rust binary. MCP server for Claude, Cursor, VS Code, Xcode, JetBrains.

## README Excerpt

<div align="center">

# Vestige

### The cognitive engine that gives AI a brain.

[![GitHub stars](https://img.shields.io/github/stars/samvallad33/vestige?style=social)](https://github.com/samvallad33/vestige)
[![Release](https://img.shields.io/github/v/release/samvallad33/vestige)](https://github.com/samvallad33/vestige/releases/latest)
[![Tests](https://img.shields.io/badge/tests-1238%20passing-brightgreen)](https://github.com/samvallad33/vestige/actions)
[![License](https://img.shields.io/badge/license-AGPL--3.0-blue)](LICENSE)
[![MCP Compatible](https://img.shields.io/badge/MCP-compatible-green)](https://modelcontextprotocol.io)

**Your AI forgets everything between sessions. Vestige fixes that.**

Built on 130 years of memory research — FSRS-6 spaced repetition, prediction error gating, synaptic tagging, spreading activation, memory dreaming — all running in a single Rust binary with a 3D neural visualization dashboard. 100% local. Zero cloud.

[Quick Start](#quick-start) | [Dashboard](#-3d-memory-dashboard) | [How It Works](#-the-cognitive-science-stack) | [Tools](#-21-mcp-tools) | [Docs](docs/)

</div>

---

## What's New in v2.0 "Cognitive Leap"

- **3D Memory Dashboard** — SvelteKit + Three.js neural visualization with real-time WebSocket events, bloom post-processing, force-directed graph layout. Watch your AI's mind in real-time.
- **WebSocket Event Bus** — Every cognitive operation broadcasts events: memory creation, search, dreaming, consolidation, retention decay
- **HyDE Query Expansion** — Template-based Hypothetical Document Embeddings for dramatically improved search quality on conceptual queries
- **Nomic v2 MoE (experimental)** — fastembed 5.11 with optional Nomic Embed Text v2 MoE (475M params, 8 experts) + Metal GPU acceleration. Default: v1.5 (8192 token context)
- **Command Palette** — `Cmd+K` navigation, keyboard shortcuts, responsive mobile layout, PWA installable
- **FSRS Decay Visualization** — SVG retention curves with predicted decay at 1d/7d/30d, endangered memory alerts
- **29 cognitive modules** — 1,238 tests, 79,600+ LOC

---

## Quick Start

```bash
# 1. Install (macOS Apple Silicon)
curl -L https://github.com/samvallad33/vestige/releases/latest/download/vestige-mcp-aarch64-apple-darwin.tar.gz | tar -xz
sudo mv vestige-mcp vestige vestige-restore /usr/local/bin/

# 2. Connect to Claude Code
claude mcp add vestige vestige-mcp -s user

# 3. Test it
# "Remember that I prefer TypeScript over JavaScript"
# ...new session...
# "What are my coding preferences?"
# → "You prefer TypeScript over JavaScript."
```

<details>
<summary>Other platforms & install methods</summary>

**macOS (Intel):**
```bash
curl -L https://github.com/samvallad33/vestige/releases/latest/download/vestige-mcp-x86_64-apple-darwin.tar.gz | tar -xz
sudo mv vestige-mcp vestige vestige-restore /usr/local/bin/
```

**Linux (x86_64):**
```bash
curl -L https://github.com/samvallad33/vestige/releases/latest/download/vestige-mcp-x86_64-unknown-linux-gnu.ta

## Links

- Repository: https://github.com/samvallad33/vestige
- Homepage: https://github.com/samvallad33/vestige
