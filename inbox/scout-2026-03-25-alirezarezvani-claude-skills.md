---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code skill"
  quality_score: 93
  scoring_breakdown:
    stars: 33
    recency: 25
    docs: 20
    community: 15
github_data:
  full_name: "alirezarezvani/claude-skills"
  url: "https://github.com/alirezarezvani/claude-skills"
  description: "+192 Claude Code skills & agent plugins for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — engineering, marketing, product, compliance, C-level advisory."
  stars: 6851
  forks: 812
  open_issues: 7
  language: "Python"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2025-10-19"
  topics: ["agent-plugins", "agent-skills", "agentic-ai", "ai-coding-agent", "anthropic-claude", "claude-ai", "claude-code", "claude-code-plugins", "claude-code-skills", "claude-skills", "codex-skills", "coding-agent-plugins", "cursor-skills", "developer-tools", "gemini-cli-skills", "openai-codex", "openclaw", "openclaw-plugins", "openclaw-skills", "prompt-engineering"]
---

# alirezarezvani/claude-skills

> Discovered by arsenal scout — awaiting manual triage

## Description

+192 Claude Code skills & agent plugins for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — engineering, marketing, product, compliance, C-level advisory.

## README Excerpt

# Claude Code Skills & Plugins — Agent Skills for Every Coding Tool

**205 production-ready Claude Code skills, plugins, and agent skills for 11 AI coding tools.**

The most comprehensive open-source library of Claude Code skills and agent plugins — also works with OpenAI Codex, Gemini CLI, Cursor, and 7 more coding agents. Reusable expertise packages covering engineering, DevOps, marketing, compliance, C-level advisory, and more.

**Works with:** Claude Code · OpenAI Codex · Gemini CLI · OpenClaw · Cursor · Aider · Windsurf · Kilo Code · OpenCode · Augment · Antigravity

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/Skills-205-brightgreen?style=for-the-badge)](#skills-overview)
[![Agents](https://img.shields.io/badge/Agents-16-blue?style=for-the-badge)](#agents)
[![Personas](https://img.shields.io/badge/Personas-3-purple?style=for-the-badge)](#personas)
[![Commands](https://img.shields.io/badge/Commands-19-orange?style=for-the-badge)](#commands)
[![Stars](https://img.shields.io/github/stars/alirezarezvani/claude-skills?style=for-the-badge)](https://github.com/alirezarezvani/claude-skills/stargazers)
[![SkillCheck Validated](https://img.shields.io/badge/SkillCheck-Validated-4c1?style=for-the-badge)](https://getskillcheck.com)

> **5,200+ GitHub stars** — the most comprehensive open-source Claude Code skills & agent plugins library.

---

## What Are Claude Code Skills & Agent Plugins?

Claude Code skills (also called agent skills or coding agent plugins) are modular instruction packages that give AI coding agents domain expertise they don't have out of the box. Each skill includes:

- **SKILL.md** — structured instructions, workflows, and decision frameworks
- **Python tools** — 268 CLI scripts (all stdlib-only, zero pip installs)
- **Reference docs** — templates, checklists, and domain-specific knowledge

**One repo, eleven platforms.** Works natively as Claude Code plugins, Codex agent skills, Gemini CLI skills, and converts to 8 more tools via `scripts/convert.sh`. All 268 Python tools run anywhere Python runs.

### Skills vs Agents vs Personas

| | Skills | Agents | Personas |
|---|---|---|---|
| **Purpose** | How to execute a task | What task to do | Who is thinking |
| **Scope** | Single domain | Single domain | Cross-domain |
| **Voice** | Neutral | Professional | Personality-driven |
| **Example** | "Follow these steps for SEO" | "Run a security audit" | "Think like a startup CTO" |

All three work together. See [Orchestration](#orchestration) for how to combine them.

---

## Quick Install

### Gemini CLI (New)

```bash
# Clone the repository
git clone https://github.com/alirezarezvani/claude-skills.git
cd claude-skills

# Run the setup script
./scripts/gemini-install.sh

# Start using skills
> activate_skill(name="senior-architect")
```

### Claude Code (Recommended)

```bash
# Add the marketplace
/plugin marketplace add

## Links

- Repository: https://github.com/alirezarezvani/claude-skills
- Homepage: https://alirezarezvani.medium.com/
