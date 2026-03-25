---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code plugin"
  quality_score: 94
  scoring_breakdown:
    stars: 34
    recency: 25
    docs: 20
    community: 15
github_data:
  full_name: "EveryInc/compound-engineering-plugin"
  url: "https://github.com/EveryInc/compound-engineering-plugin"
  description: "Office Compound Engineering plugin for Claude Code, Codex, and more"
  stars: 11088
  forks: 874
  open_issues: 62
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2025-10-09"
  topics: ["compound", "engineering"]
---

# EveryInc/compound-engineering-plugin

> Discovered by arsenal scout — awaiting manual triage

## Description

Office Compound Engineering plugin for Claude Code, Codex, and more

## README Excerpt

# Compound Marketplace

[![Build Status](https://github.com/EveryInc/compound-engineering-plugin/actions/workflows/ci.yml/badge.svg)](https://github.com/EveryInc/compound-engineering-plugin/actions/workflows/ci.yml)
[![npm](https://img.shields.io/npm/v/@every-env/compound-plugin)](https://www.npmjs.com/package/@every-env/compound-plugin)

A Claude Code plugin marketplace featuring the **Compound Engineering Plugin** — tools that make each unit of engineering work easier than the last.

## Claude Code Install

```bash
/plugin marketplace add EveryInc/compound-engineering-plugin
/plugin install compound-engineering
```

## Cursor Install

```text
/add-plugin compound-engineering
```

## OpenCode, Codex, Droid, Pi, Gemini, Copilot, Kiro, Windsurf, OpenClaw & Qwen (experimental) Install

This repo includes a Bun/TypeScript CLI that converts Claude Code plugins to OpenCode, Codex, Factory Droid, Pi, Gemini CLI, GitHub Copilot, Kiro CLI, Windsurf, OpenClaw, and Qwen Code.

```bash
# convert the compound-engineering plugin into OpenCode format
bunx @every-env/compound-plugin install compound-engineering --to opencode

# convert to Codex format
bunx @every-env/compound-plugin install compound-engineering --to codex

# convert to Factory Droid format
bunx @every-env/compound-plugin install compound-engineering --to droid

# convert to Pi format
bunx @every-env/compound-plugin install compound-engineering --to pi

# convert to Gemini CLI format
bunx @every-env/compound-plugin install compound-engineering --to gemini

# convert to GitHub Copilot format
bunx @every-env/compound-plugin install compound-engineering --to copilot

# convert to Kiro CLI format
bunx @every-env/compound-plugin install compound-engineering --to kiro

# convert to OpenClaw format
bunx @every-env/compound-plugin install compound-engineering --to openclaw

# convert to Windsurf format (global scope by default)
bunx @every-env/compound-plugin install compound-engineering --to windsurf

# convert to Windsurf workspace scope
bunx @every-env/compound-plugin install compound-engineering --to windsurf --scope workspace

# convert to Qwen Code format
bunx @every-env/compound-plugin install compound-engineering --to qwen

# auto-detect installed tools and install to all
bunx @every-env/compound-plugin install compound-engineering --to all
```

### Local Development

When developing and testing local changes to the plugin:

**Claude Code** — add a shell alias so your local copy loads alongside your normal plugins:

```bash
# add to ~/.zshrc or ~/.bashrc
alias claude-dev-ce='claude --plugin-dir ~/code/compound-engineering-plugin/plugins/compound-engineering'
```

One-liner to append it:

```bash
echo "alias claude-dev-ce='claude --plugin-dir ~/code/compound-engineering-plugin/plugins/compound-engineering'" >> ~/.zshrc
```

Then run `claude-dev-ce` instead of `claude` to test your changes. Your production install stays untouched.

**Codex** — point the install command at your local path:

```bash

## Links

- Repository: https://github.com/EveryInc/compound-engineering-plugin
- Homepage: https://every.to/guides/compound-engineering
