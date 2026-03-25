---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 76
  scoring_breakdown:
    stars: 24
    recency: 20
    docs: 20
    community: 12
github_data:
  full_name: "SixHq/Overture"
  url: "https://github.com/SixHq/Overture"
  description: "Overture is an open-source, locally running web interface delivered as an MCP (Model Context Protocol) server that visually maps out the execution plan of any AI coding agent as an interactive flowchart/graph before the agent begins writing code. "
  stars: 602
  forks: 57
  open_issues: 3
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-08"
  created: "2026-02-17"
  topics: ["ai-agent", "ai-coding", "automation", "claude", "claude-code", "codex", "copilot", "cursor", "deepseek", "developer-tools", "gemini", "generative-ai", "gpt", "llm", "mcp", "mcp-server", "openclaw", "planning", "typescript", "vscode"]
---

# SixHq/Overture

> Discovered by arsenal scout — awaiting manual triage

## Description

Overture is an open-source, locally running web interface delivered as an MCP (Model Context Protocol) server that visually maps out the execution plan of any AI coding agent as an interactive flowchart/graph before the agent begins writing code. 

## README Excerpt

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/SixHq/Overture/main/assets/overture-logo-dark.png">
    <img src="https://raw.githubusercontent.com/SixHq/Overture/main/assets/overture-logo-light.png" alt="Overture" width="400">
  </picture>
</p>

<p align="center">
  <strong>See the plan before the code. Approve it. Then watch it execute.</strong>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/overture-mcp"><img src="https://img.shields.io/npm/v/overture-mcp?style=for-the-badge&color=blue" alt="npm version"></a>
  <a href="https://github.com/SixHq/Overture/actions"><img src="https://img.shields.io/github/actions/workflow/status/SixHq/Overture/ci.yml?branch=main&style=for-the-badge" alt="CI status"></a>
  <a href="https://www.npmjs.com/package/overture-mcp"><img src="https://img.shields.io/npm/dm/overture-mcp?style=for-the-badge&color=orange" alt="npm downloads"></a>
  <a href="https://github.com/SixHq/Overture/discussions"><img src="https://img.shields.io/github/discussions/SixHq/Overture?style=for-the-badge&color=purple" alt="Discussions"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="MIT License"></a>
</p>

<p align="center">
  <a href="#-the-problem">Problem</a> •
  <a href="#-the-solution">Solution</a> •
  <a href="#-installation">Install</a> •
  <a href="#-features">Features</a> •
  <a href="#-mcp-marketplace">Marketplace</a> •
  <a href="#-configuration">Config</a> •
  <a href="https://github.com/SixHq/Overture/discussions">Discussions</a>
</p>

<br>

<p align="center">

https://github.com/user-attachments/assets/eeb9c4cb-c80d-42da-bf63-c0c4ecb1e5d6

</p>

---

## 🔥 The Problem

Every AI coding agent today — **Cursor**, **Claude Code**, **Cline**, **Copilot** — works the same way:

<table>
<tr>
<td width="50%">

### What Happens Now

1. You type a prompt
2. Agent **immediately starts writing code**
3. You have **zero visibility** into what it's doing
4. You realize it misunderstood your request
5. **Hundreds of lines of code** need to be discarded
6. You've wasted tokens, time, and patience

</td>
<td width="50%">

### Text Plans Don't Help

Some agents show plans as text in chat. But text fails to show:

- **Dependencies** — which tasks depend on what?
- **Branch points** — what alternative approaches exist?
- **Context requirements** — which files, APIs, or secrets are needed?
- **Complexity** — which steps are risky?
- **Progress** — what's done, what's next?

</td>
</tr>
</table>

<p align="center">
  <img src="https://raw.githubusercontent.com/SixHq/Overture/main/assets/problem-illustration.png" alt="The Problem" width="700">
</p>

---

## ✨ The Solution

**Overture** intercepts your AI agent's planning phase and renders it as an **interactive visual flowchart** — before any code is written.

<p align="center">
  <img src="https://raw.githubusercontent.com/SixHq/Overture/main/ass

## Links

- Repository: https://github.com/SixHq/Overture
