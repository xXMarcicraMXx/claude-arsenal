---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code workflow"
  quality_score: 85
  scoring_breakdown:
    stars: 30
    recency: 25
    docs: 20
    community: 10
github_data:
  full_name: "entireio/cli"
  url: "https://github.com/entireio/cli"
  description: "Entire is a new developer platform that hooks into your git workflow to capture AI agent sessions on every push, unifying your code with its context and reasoning."
  stars: 3752
  forks: 267
  open_issues: 121
  language: "Go"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2026-01-02"
  topics: ["agents", "ai", "claude", "developer", "developer-platform", "gemini"]
---

# entireio/cli

> Discovered by arsenal scout — awaiting manual triage

## Description

Entire is a new developer platform that hooks into your git workflow to capture AI agent sessions on every push, unifying your code with its context and reasoning.

## README Excerpt

# Entire CLI

Entire hooks into your Git workflow to capture AI agent sessions as you work. Sessions are indexed alongside commits, creating a searchable record of how code was written in your repo.

With Entire, you can:

- **Understand why code changed** — see the full prompt/response transcript and files touched
- **Recover instantly** — rewind to a known-good checkpoint when an agent goes sideways and resume seamlessly
- **Keep Git history clean** — preserve agent context on a separate branch
- **Onboard faster** — show the path from prompt → change → commit
- **Maintain traceability** — support audit and compliance requirements when needed

## Why Entire

- **Understand why code changed, not just what** — Transcripts, prompts, files touched, token usage, tool calls, and more are captured alongside every commit.
- **Rewind and resume from any checkpoint** — Go back to any previous agent session and pick up exactly where you or a coworker left off.
- **Full context preserved and searchable** — A versioned record of every AI interaction tied to your git history, with nothing lost.
- **Zero context switching** — Git-native, two-step setup, works with Claude Code, Gemini, and more.

## Table of Contents

- [Why Entire](#why-entire)
- [Quick Start](#quick-start)
- [Typical Workflow](#typical-workflow)
- [Key Concepts](#key-concepts)
  - [How It Works](#how-it-works)
  - [Strategy](#strategy)
- [Local Device Auth Testing](#local-device-auth-testing)
- [Commands Reference](#commands-reference)
- [Configuration](#configuration)
- [Security & Privacy](#security--privacy)
- [Troubleshooting](#troubleshooting)
- [Development](#development)
- [Getting Help](#getting-help)
- [License](#license)

## Requirements

- Git
- macOS or Linux (Windows via WSL)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [OpenCode](https://opencode.ai/docs/cli/), [Cursor](https://www.cursor.com/), [Factory AI Droid](https://www.factory.ai/), or [GitHub Copilot CLI](https://docs.github.com/en/copilot) installed and authenticated

## Quick Start

```bash
# Install via Homebrew
brew tap entireio/tap
brew install entireio/tap/entire

# Or install via Go
go install github.com/entireio/cli/cmd/entire@latest

# Linux: Add Go binaries to PATH (add to ~/.zshrc or ~/.bashrc if not already configured)
export PATH="$HOME/go/bin:$PATH"

# Enable in your project
cd your-project && entire enable

# Check status
entire status
```

## Typical Workflow

### 1. Enable Entire in Your Repository

```
entire enable
```

This installs agent and git hooks to work with your AI agent (Claude Code, Gemini CLI, OpenCode, Cursor, Factory AI Droid, or Copilot CLI). You'll be prompted to select which agents to enable. To enable a specific agent non-interactively, use `entire enable --agent <name>` (e.g., `entire enable --agent cursor`).

The hooks capture session data as you work. Checkpoints are created when you or the agent make a

## Links

- Repository: https://github.com/entireio/cli
- Homepage: https://entire.io
