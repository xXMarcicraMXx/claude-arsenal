---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code configuration"
  quality_score: 81
  scoring_breakdown:
    stars: 27
    recency: 25
    docs: 20
    community: 9
github_data:
  full_name: "Piebald-AI/tweakcc"
  url: "https://github.com/Piebald-AI/tweakcc"
  description: "Customize Claude Code's system prompts, create custom toolsets, input pattern highlighters, themes/thinking verbs/spinners, customize input box & user message styling, support AGENTS.md, unlock private/unreleased features, and much more.  Supports both native/npm installs on all platforms."
  stars: 1416
  forks: 106
  open_issues: 39
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-24"
  created: "2025-07-20"
  topics: ["agentic", "anthropic", "bun", "claude-code", "claude-code-native", "claude-code-system-prompts", "claude-code-themes", "claude-code-ui", "command-line", "configuration", "customization", "developer-tools", "personalization", "refined-claude-code", "styling", "system-prompts", "terminal", "themes", "token-counter", "tweak"]
---

# Piebald-AI/tweakcc

> Discovered by arsenal scout — awaiting manual triage

## Description

Customize Claude Code's system prompts, create custom toolsets, input pattern highlighters, themes/thinking verbs/spinners, customize input box & user message styling, support AGENTS.md, unlock private/unreleased features, and much more.  Supports both native/npm installs on all platforms.

## README Excerpt

<div>
<div align="right">
<a href="https://piebald.ai"><img width="200" top="20" align="right" src="https://github.com/Piebald-AI/.github/raw/main/Wordmark.svg"></a>
</div>

<div align="left">

### Check out Piebald

We've released **Piebald**, the ultimate agentic AI developer experience. \
Download it and try it out for free! **https://piebald.ai/**

<a href="https://piebald.ai/discord"><img src="https://img.shields.io/badge/Join%20our%20Discord-5865F2?style=flat&logo=discord&logoColor=white" alt="Join our Discord"></a>
<a href="https://x.com/PiebaldAI"><img src="https://img.shields.io/badge/Follow%20%40PiebaldAI-000000?style=flat&logo=x&logoColor=white" alt="X"></a>

<sub>[**Scroll down for tweakcc.**](#tweakcc) :point_down:</sub>

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

# tweakcc

[![tweakcc on npm](https://img.shields.io/npm/v/tweakcc?color)](https://www.npmjs.com/package/tweakcc)
[![Mentioned in Awesome Claude Code](https://awesome.re/mentioned-badge.svg)](https://github.com/hesreallyhim/awesome-claude-code)
[![ClaudeLog - A comprehensive knowledge base for Claude.](https://claudelog.com/img/claude_log_badge.svg)](https://claudelog.com/)

**tweakcc is a CLI tool that upgrades your Claude Code experience.** Customize its system prompts, add custom themes, create toolsets, and personalize the UI. From the team behind [<img src="https://github.com/Piebald-AI/piebald/raw/main/assets/logo.svg" width="15"> **Piebald.**](https://piebald.ai/)

<!--
> [!note]
> ⭐ **If you find tweakcc useful, please consider [starring the repository](https://github.com/Piebald-AI/tweakcc) to show your support!** ⭐
-->

<img src="./assets/demo.gif" alt="Animated GIF demonstrating running `npx tweakcc`, creating a new theme, changing all of Claude Code's UI colors to purple, changing the thinking format from '<verb>ing...' to 'Claude is <verb>ing', changing the generating spinner style to a 50ms glow animation, applying the changes, running Claude, and using '/config' to switch to the new theme, and sending a message to see the new thinking verb format." width="800">

> [!IMPORTANT]
> **NEW in 4.0.0:** tweakcc now has an API; use `npm i tweakcc` to add to your project and see [API](#api)!
>
> **NEW in 4.0.0:** You can now create custom patches via sandboxed scripts! Works with native installations. No need to fork tweakcc just to make a quick patch! See [`tweakcc adhoc-patch`](#cli-commands).
>
> **NEW in 4.0.0:** You can also apply customizations from a remote URL to a config file. See [Remote Config](#remote-config).
>
> Also see `tweakcc --restore`, [`tweakcc unpack`](#cli-commands), and [`tweakcc repack`](#cli-commands).

> [!NOTE]
> **NEW:*

## Links

- Repository: https://github.com/Piebald-AI/tweakcc
