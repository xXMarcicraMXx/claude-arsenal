---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 74
  scoring_breakdown:
    stars: 35
    recency: 8
    docs: 20
    community: 11
github_data:
  full_name: "BeehiveInnovations/pal-mcp-server"
  url: "https://github.com/BeehiveInnovations/pal-mcp-server"
  description: "The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one."
  stars: 11313
  forks: 969
  open_issues: 116
  language: "Python"
  license: "NOASSERTION"
  last_push: "2025-12-15"
  created: "2025-06-08"
  topics: []
---

# BeehiveInnovations/pal-mcp-server

> Discovered by arsenal scout — awaiting manual triage

## Description

The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one.

## README Excerpt

# PAL MCP: Many Workflows. One Context.

<div align="center">

  <em>Your AI's PAL – a Provider Abstraction Layer</em><br />
  <sub><a href="docs/name-change.md">Formerly known as Zen MCP</a></sub>

  [PAL in action](https://github.com/user-attachments/assets/0d26061e-5f21-4ab1-b7d0-f883ddc2c3da)

👉 **[Watch more examples](#-watch-tools-in-action)**

### Your CLI + Multiple Models = Your AI Dev Team

**Use the 🤖 CLI you love:**  
[Claude Code](https://www.anthropic.com/claude-code) · [Gemini CLI](https://github.com/google-gemini/gemini-cli) · [Codex CLI](https://github.com/openai/codex) · [Qwen Code CLI](https://qwenlm.github.io/qwen-code-docs/) · [Cursor](https://cursor.com) · _and more_

**With multiple models within a single prompt:**  
Gemini · OpenAI · Anthropic · Grok · Azure · Ollama · OpenRouter · DIAL · On-Device Model

</div>

---

## 🆕 Now with CLI-to-CLI Bridge

The new **[`clink`](docs/tools/clink.md)** (CLI + Link) tool connects external AI CLIs directly into your workflow:

- **Connect external CLIs** like [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Codex CLI](https://github.com/openai/codex), and [Claude Code](https://www.anthropic.com/claude-code) directly into your workflow
- **CLI Subagents** - Launch isolated CLI instances from _within_ your current CLI! Claude Code can spawn Codex subagents, Codex can spawn Gemini CLI subagents, etc. Offload heavy tasks (code reviews, bug hunting) to fresh contexts while your main session's context window remains unpolluted. Each subagent returns only final results.
- **Context Isolation** - Run separate investigations without polluting your primary workspace
- **Role Specialization** - Spawn `planner`, `codereviewer`, or custom role agents with specialized system prompts
- **Full CLI Capabilities** - Web search, file inspection, MCP tool access, latest documentation lookups
- **Seamless Continuity** - Sub-CLIs participate as first-class members with full conversation context between tools

```bash
# Codex spawns Codex subagent for isolated code review in fresh context
clink with codex codereviewer to audit auth module for security issues
# Subagent reviews in isolation, returns final report without cluttering your context as codex reads each file and walks the directory structure

# Consensus from different AI models → Implementation handoff with full context preservation between tools
Use consensus with gpt-5 and gemini-pro to decide: dark mode or offline support next
Continue with clink gemini - implement the recommended feature
# Gemini receives full debate context and starts coding immediately
```

👉 **[Learn more about clink](docs/tools/clink.md)**

---

## Why PAL MCP?

**Why rely on one AI model when you can orchestrate them all?**

A Model Context Protocol server that supercharges tools like [Claude Code](https://www.anthropic.com/claude-code), [Codex CLI](https://developers.openai.com/codex/cli), and IDE clients such
as [Cursor](https://cursor.com) or the [Claude Dev

## Links

- Repository: https://github.com/BeehiveInnovations/pal-mcp-server
