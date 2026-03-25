---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 89
  scoring_breakdown:
    stars: 33
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "Piebald-AI/claude-code-system-prompts"
  url: "https://github.com/Piebald-AI/claude-code-system-prompts"
  description: "All parts of Claude Code's system prompt, 18 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact,  statusline, magic docs, WebFetch, Bash cmd, security review, agent creation).  Updated for each Claude Code version."
  stars: 6622
  forks: 898
  open_issues: 2
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-03-21"
  created: "2025-11-18"
  topics: ["claude-code", "claude-code-system-prompts", "system-prompts"]
---

# Piebald-AI/claude-code-system-prompts

> Discovered by arsenal scout — awaiting manual triage

## Description

All parts of Claude Code's system prompt, 18 builtin tool descriptions, sub agent prompts (Plan/Explore/Task), utility prompts (CLAUDE.md, compact,  statusline, magic docs, WebFetch, Bash cmd, security review, agent creation).  Updated for each Claude Code version.

## README Excerpt

<div>
<div align="right">
<a href="https://piebald.ai"><img width="200" top="20" align="right" src="https://github.com/Piebald-AI/.github/raw/main/Wordmark.svg"></a>
</div>

<div align="left">

### Check out Piebald
We've released **Piebald**, the ultimate agentic AI developer experience. \
Download it and try it out for free!  **https://piebald.ai/**

<a href="https://piebald.ai/discord"><img src="https://img.shields.io/badge/Join%20our%20Discord-5865F2?style=flat&logo=discord&logoColor=white" alt="Join our Discord"></a>
<a href="https://x.com/PiebaldAI"><img src="https://img.shields.io/badge/Follow%20%40PiebaldAI-000000?style=flat&logo=x&logoColor=white" alt="X"></a>

<sub>[**Scroll down for Claude Code's system prompts.**](#claude-code-system-prompts) :point_down:</sub>

</div>
</div>

<div align="left">
<a href="https://piebald.ai">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://piebald.ai/screenshot-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="https://piebald.ai/screenshot-light.png">
  <img alt="hero" width="800" src="https://piebald.ai/screenshot-light.png">
</picture>
</a>
</div>

# Claude Code System Prompts

[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)

> [!important]
> **NEW (January 23, 2026): We've added all of Claude Code's ~40 system reminders to this list&mdash;see [System Reminders](#system-reminders).**

This repository contains an up-to-date list of all Claude Code's various system prompts and their associated token counts as of **[Claude Code v2.1.81](https://www.npmjs.com/package/@anthropic-ai/claude-code/v/2.1.81) (March 20th, 2026).**  It also contains a [**CHANGELOG.md**](./CHANGELOG.md) for the system prompts across 131 versions since v2.0.14.  From the team behind [<img src="https://github.com/Piebald-AI/piebald/raw/main/assets/logo.svg" width="15"> **Piebald.**](https://piebald.ai/)

**This repository is updated within minutes of each Claude Code release.  See the [changelog](./CHANGELOG.md), and follow [@PiebaldAI](https://x.com/PiebaldAI) on X for a summary of the system prompt changes in each release.**

> [!note]
> ⭐ **Star** this repository to get notified about new Claude Code versions.  For each new Claude Code version, we create a release on GitHub, which will notify all users who've starred the repository.

---

Why multiple "system prompts?"

**Claude Code doesn't just have one single string for its system prompt.**

Instead, there are:
- Large portions conditionally added depending on the environment and various configs.
- Descriptions for builtin tools like `Write`, `Bash`, and `TodoWrite`, and some are fairly large.
- Separate system prompts for builtin agents like Explore and Plan.
- Numerous AI-powered utility functions, such as conversation compaction, `CLAUDE.md` generation, session title generation, etc. featuring their own systems prompts.

The result&mdash;110+ strings

## Links

- Repository: https://github.com/Piebald-AI/claude-code-system-prompts
