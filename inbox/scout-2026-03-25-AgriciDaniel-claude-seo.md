---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code skill"
  quality_score: 86
  scoring_breakdown:
    stars: 30
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "AgriciDaniel/claude-seo"
  url: "https://github.com/AgriciDaniel/claude-seo"
  description: "Universal SEO skill for Claude Code. 13 sub-skills, 7 subagents, extensions system with DataForSEO MCP integration. Technical SEO, E-E-A-T, schema, GEO/AEO, and strategic planning."
  stars: 3085
  forks: 477
  open_issues: 5
  language: "Python"
  license: "MIT"
  last_push: "2026-03-23"
  created: "2026-02-07"
  topics: ["ai-search", "ai-tools", "claude", "claude-code", "core-web-vitals", "dataforseo", "e-e-a-t", "geo", "mcp", "python", "schema-markup", "seo", "seo-audit", "seo-tools", "skill"]
---

# AgriciDaniel/claude-seo

> Discovered by arsenal scout — awaiting manual triage

## Description

Universal SEO skill for Claude Code. 13 sub-skills, 7 subagents, extensions system with DataForSEO MCP integration. Technical SEO, E-E-A-T, schema, GEO/AEO, and strategic planning.

## README Excerpt

<!-- Updated: 2026-03-06 -->

![Claude SEO](screenshots/cover-image.jpeg)

# Claude SEO - SEO Audit Skill for Claude Code

Comprehensive SEO analysis skill for Claude Code. Covers technical SEO, on-page analysis, content quality (E-E-A-T), schema markup, image optimization, sitemap architecture, AI search optimization (GEO), and strategic planning.

![SEO Command Demo](screenshots/seo-command-demo.gif)

[![CI](https://github.com/AgriciDaniel/claude-seo/actions/workflows/ci.yml/badge.svg)](https://github.com/AgriciDaniel/claude-seo/actions/workflows/ci.yml)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/claude-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/github/v/release/AgriciDaniel/claude-seo)](https://github.com/AgriciDaniel/claude-seo/releases)

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Commands](#commands)
- [Features](#features)
- [Architecture](#architecture)
- [Extensions](#extensions)
- [Ecosystem](#ecosystem)
- [Documentation](#documentation)
- [Requirements](#requirements)
- [Uninstall](#uninstall)
- [Contributing](#contributing)

## Installation

### Recommended Install (Unix/macOS/Linux)

```bash
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/install.sh
```

<details>
<summary>One-liner (curl)</summary>

```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh | bash
```

Or via [install.cat](https://install.cat):

```bash
curl -fsSL install.cat/AgriciDaniel/claude-seo | bash
```

Prefer to review the script before running?

```bash
curl -fsSL https://raw.githubusercontent.com/AgriciDaniel/claude-seo/main/install.sh > install.sh
cat install.sh        # review
bash install.sh       # run when satisfied
rm install.sh
```

</details>

### Windows (PowerShell)

```powershell
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
powershell -ExecutionPolicy Bypass -File claude-seo\install.ps1
```

> **Why git clone instead of `irm | iex`?** Claude Code's own security guardrails flag `irm ... | iex` as a supply chain risk (downloading and executing remote code with no verification). The git clone approach lets you inspect the script at `claude-seo\install.ps1` before running it.

## Quick Start

```bash
# Start Claude Code
claude

# Run a full site audit
/seo audit https://example.com

# Analyze a single page
/seo page https://example.com/about

# Check schema markup
/seo schema https://example.com

# Generate a sitemap
/seo sitemap generate

# Optimize for AI search
/seo geo https://example.com
```
### Demo:
[Watch the full demo on YouTube](https://www.youtube.com/watch?v=COMnNlUakQk)

**`/seo audit`: full site audit with parallel subagents:**

![SEO Audit Demo](screenshots/seo-audit-demo.gif)

## Commands

| Command | Description |
|---------|-------------|
| `/seo audit <url>` | Full webs

## Links

- Repository: https://github.com/AgriciDaniel/claude-seo
- Homepage: https://www.skool.com/ai-marketing-hub-pro
