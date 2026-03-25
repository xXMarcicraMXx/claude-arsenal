---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code workflow"
  quality_score: 87
  scoring_breakdown:
    stars: 28
    recency: 25
    docs: 20
    community: 14
github_data:
  full_name: "sdi2200262/agentic-project-management"
  url: "https://github.com/sdi2200262/agentic-project-management"
  description: "A framework for managing complex projects with structured multi-agent workflows. Integrates to AI Assistants like Cursor, Claude Code, GitHub Copilot and more."
  stars: 2132
  forks: 207
  open_issues: 2
  language: "JavaScript"
  license: "NOASSERTION"
  last_push: "2026-03-23"
  created: "2025-05-12"
  topics: []
---

# sdi2200262/agentic-project-management

> Discovered by arsenal scout — awaiting manual triage

## Description

A framework for managing complex projects with structured multi-agent workflows. Integrates to AI Assistants like Cursor, Claude Code, GitHub Copilot and more.

## README Excerpt

# Agentic Project Management (APM)

[![License: MPL-2.0](https://img.shields.io/badge/License-MPL_2.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0) [![Version](https://img.shields.io/badge/version-v0.5.4-blue)](https://github.com/sdi2200262/agentic-project-management/releases/tag/v0.5.4) [![Website](https://img.shields.io/badge/website-agentic--project--management.dev-blue)](https://agentic-project-management.dev)

*Manage complex projects with a team of AI assistants, smoothly and efficiently.*

## What is APM?

**Agentic Project Management (APM)** is a AI workflow framework that brings real-world project management principles into your AI-assisted workflows. It addresses a fundamental challenge of LLMs: **context window limitations**. 

APM uses various context retention techniques, coordinating a team of specialized AI agents in a structured way so that you can maintain productive AI-assisted work for longer periods before facing model hallucinations and needing to start over. When context window does fill up, APM ensures a smooth transition to a "fresh" chat session without important context loss.

Think of it like having a project manager, developers, ad-hoc specialists, and a setup/configuration expert all powered by AI and working together under your guidance.

<p align="center">
  <img src="assets/apm-banner.png" alt="apm-banner" style="border-radius: 16px; display: block; margin-left: auto; margin-right: auto;" />
</p>

## Installation

Install APM CLI globally via NPM:

```bash
npm install -g agentic-pm
```

Or install locally in your project:

```bash
npm install agentic-pm
```

<details>
<summary><strong>Supported AI Assistants</strong></summary>

APM supports the following AI assistants and IDEs:

| Assistant           | Type                    | Format   | Command Directory      |
|---------------------|-------------------------|----------|------------------------|
| Cursor              | IDE & CLI               | Markdown | `.cursor/commands`     |
| Claude Code         | IDE & CLI               | Markdown | `.claude/commands`     |
| GitHub Copilot      | IDE                     | Markdown | `.github/prompts`      |
| Windsurf            | IDE                     | Markdown | `.windsurf/workflows`  |
| Roo Code            | IDE                     | Markdown | `.roo/commands`        |
| Kilo Code           | IDE                     | Markdown | `.kilocode/workflows`  |
| Qwen Code           | CLI                     | TOML     | `.qwen/commands`       |
| opencode            | CLI                     | Markdown | `.opencode/command`    |
| Gemini CLI          | CLI                     | TOML     | `.gemini/commands`     |
| Auggie CLI          | CLI                     | Markdown | `.augment/commands`    |
| Google Antigravity  | IDE                     | Markdown | `.agent/workflows`     |

When you run `apm init`, simply select your AI assistant from the list, and APM will automatically configure the appropriate com

## Links

- Repository: https://github.com/sdi2200262/agentic-project-management
- Homepage: http://agentic-project-management.dev/
