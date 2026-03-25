---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "anthropic mcp server"
  quality_score: 77
  scoring_breakdown:
    stars: 20
    recency: 25
    docs: 20
    community: 12
github_data:
  full_name: "Mng-dev-ai/agentrove"
  url: "https://github.com/Mng-dev-ai/agentrove"
  description: "Your own Claude Code UI, sandbox, in-browser VS Code, terminal, multi-provider support (Anthropic, OpenAI, GitHub Copilot, OpenRouter), custom skills, and MCP servers."
  stars: 248
  forks: 46
  open_issues: 2
  language: "TypeScript"
  license: "Apache-2.0"
  last_push: "2026-03-25"
  created: "2025-12-15"
  topics: ["agent", "anthropic", "claude", "claude-code", "code-execution", "fastapi", "llm", "python", "react", "sandbox", "typescript"]
---

# Mng-dev-ai/agentrove

> Discovered by arsenal scout — awaiting manual triage

## Description

Your own Claude Code UI, sandbox, in-browser VS Code, terminal, multi-provider support (Anthropic, OpenAI, GitHub Copilot, OpenRouter), custom skills, and MCP servers.

## README Excerpt

# Agentrove

Self-hosted Claude Code workspace with multi-provider routing, sandboxed execution, and a full web IDE.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![React 19](https://img.shields.io/badge/React-19-61DAFB.svg)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![Discord](https://img.shields.io/badge/Discord-5865F2.svg?logo=discord&logoColor=white)](https://discord.gg/HvkJU8dcBA)

> **Note:** Agentrove is under active development. Expect breaking changes between releases.

## Screenshots

![Chat Interface](screenshots/chat-interface.png)
![Agent Workflow](screenshots/agent-workflow.png)

## Community

Join the [Discord server](https://discord.gg/HvkJU8dcBA).

## Why Agentrove

- Claude Code as the execution harness, exposed through a self-hosted web UI
- One workflow across Anthropic, OpenAI, GitHub Copilot, OpenRouter, and custom Anthropic-compatible endpoints
- Anthropic Bridge routing for non-Anthropic providers while preserving Claude Code behavior
- Isolated sandbox backends (Docker, host)
- Extension surface: MCP servers, skills, agents, slash commands, prompts, and marketplace plugins
- Provider switching with shared working context

## Core Architecture

```text
React/Vite Frontend
  -> FastAPI Backend
  -> PostgreSQL + Redis (web/docker mode)
  -> SQLite + in-memory cache/pubsub (desktop mode)
  -> Sandbox runtime (Docker/Host)
  -> Claude Code CLI + claude-agent-sdk
```

### Claude Code harness

Agentrove runs chats through `claude-agent-sdk`, which drives the Claude Code CLI in the selected sandbox. This keeps Claude Code-native behavior for tools, session flow, permission modes, and MCP orchestration.

### Anthropic Bridge for non-Anthropic providers

For OpenAI, OpenRouter, and Copilot providers, Agentrove starts `anthropic-bridge` inside the sandbox and routes Claude Code requests through:

- `ANTHROPIC_BASE_URL=http://127.0.0.1:3456`
- provider-specific auth secrets such as `OPENROUTER_API_KEY` and `GITHUB_COPILOT_TOKEN`
- provider-scoped model IDs like `openai/gpt-5.2-codex`, `openrouter/moonshotai/kimi-k2.5`, `copilot/gpt-5.2-codex`

```text
Agentrove UI
  -> Claude Agent SDK + Claude Code CLI
  -> Anthropic-compatible request shape
  -> Anthropic Bridge (OpenAI/OpenRouter/Copilot)
  -> Target provider model
```

For Anthropic providers, Agentrove uses your Claude auth token directly. For custom providers, Agentrove calls your configured Anthropic-compatible `base_url`.

## Key Features

- Claude Code-native chat execution through `claude-agent-sdk`
- Anthropic Bridge provider routing with provider-scoped models (`openai/*`, `openrouter/*`, `copilot/*`)
- Workspace-based project organization with per-workspace sandboxes
- Multi-sandbox runtime (Docker/Host)
- MCP + custom ski

## Links

- Repository: https://github.com/Mng-dev-ai/agentrove
