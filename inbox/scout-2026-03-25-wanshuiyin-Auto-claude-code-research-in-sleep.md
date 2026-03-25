---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code skill"
  quality_score: 90
  scoring_breakdown:
    stars: 31
    recency: 25
    docs: 20
    community: 14
github_data:
  full_name: "wanshuiyin/Auto-claude-code-research-in-sleep"
  url: "https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep"
  description: "ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea discovery, and experiment automation. No framework, no lock-in — works with Claude Code, Codex, OpenClaw, or any LLM agent."
  stars: 3973
  forks: 317
  open_issues: 11
  language: "Python"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2026-03-10"
  topics: ["ai-research", "ai-tools", "aris", "autonomous-agent", "claude", "claude-code", "claude-code-skills", "codex", "deep-learning", "gpt", "idea-generation", "llm", "machine-learning", "mcp", "mcp-server", "ml-research", "openai", "paper-review", "paper-writing", "research-automation"]
---

# wanshuiyin/Auto-claude-code-research-in-sleep

> Discovered by arsenal scout — awaiting manual triage

## Description

ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea discovery, and experiment automation. No framework, no lock-in — works with Claude Code, Codex, OpenClaw, or any LLM agent.

## README Excerpt

# Auto-claude-code-research-in-sleep (ARIS ⚔️🌙)

![ARIS Logo](docs/aris_logo.svg)

![Hero](docs/hero_combined.svg)

[中文版 README](README_CN.md) | English

![Score Progression](docs/auto_review_score_curve.png)

> 🌙 **Let Claude Code do research while you sleep.** Wake up to find your paper scored, weaknesses identified, experiments run, and narrative rewritten — autonomously.
>
> 🪶 **Radically lightweight — zero dependencies, zero lock-in.** The entire system is plain Markdown files. No framework to learn, no database to maintain, no Docker to configure, no daemon to babysit. Every skill is a single `SKILL.md` readable by any LLM — swap Claude Code for [Codex CLI](skills/skills-codex/), [OpenClaw](docs/OPENCLAW_ADAPTATION.md), [Cursor](docs/CURSOR_ADAPTATION.md), [Trae](docs/TRAE_ARIS_RUNBOOK_EN.md), [Antigravity](docs/ANTIGRAVITY_ADAPTATION.md), Windsurf, or your own agent and the workflows still work. Fork it, rewrite it, adapt it to your stack.
>
> *💡 ARIS is a methodology, not a platform. What matters is the research workflow — take it wherever you go. 🌱*

[![Featured on PaperWeekly](https://img.shields.io/badge/Featured%20on-PaperWeekly-red?style=flat)](https://mp.weixin.qq.com/s/tDniVryVGjDkkkWl-5sTkQ) · [![PaperWeekly — MiniMax-M2.7](https://img.shields.io/badge/PaperWeekly-MiniMax--M2.7-red?style=flat)](https://mp.weixin.qq.com/s/KLFU74lAL2FAIc9K6i1Kqg) · [![Featured in awesome-agent-skills](https://img.shields.io/badge/Featured%20in-awesome--agent--skills-blue?style=flat&logo=github)](https://github.com/VoltAgent/awesome-agent-skills) · [![AI Digital Crew - Project of the Day](https://img.shields.io/badge/AI%20Digital%20Crew-Project%20of%20the%20Day%20(2026.03.14)-orange?style=flat)](https://aidigitalcrew.com) · [💬 Join Community](#-community) · [![Cite](https://img.shields.io/badge/📖_Cite_Us-BibTeX-green?style=flat)](#-citation)

Custom [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skills for autonomous ML research workflows. These skills orchestrate **cross-model collaboration** — Claude Code drives the research while an external LLM (via [Codex MCP](https://github.com/openai/codex)) acts as a critical reviewer. 🔀 **Also supports [alternative model combinations](#-alternative-model-combinations) (Kimi, LongCat, DeepSeek, etc.) — no Claude or OpenAI API required.** For example, [MiniMax-M2.7 + GLM-5 or GLM-5 + MiniMax-M2.7](docs/MiniMax-GLM-Configuration.md). 🤖 **[Codex CLI native](skills/skills-codex/)** — full skill set also available for OpenAI Codex. 🖱️ **[Cursor](docs/CURSOR_ADAPTATION.md)** — works in Cursor too. 🖥️ **[Trae](docs/TRAE_ARIS_RUNBOOK_EN.md)** — ByteDance AI IDE. 🚀 **[Antigravity](docs/ANTIGRAVITY_ADAPTATION.md)** — Google's agent-first IDE. 🆓 **[Free tier via ModelScope](docs/MODELSCOPE_GUIDE.md) — zero cost, zero lock-in.**

> 💭 **Why not self-play with a single model?** Using Claude Code subagents or agent teams for both execution and review is technically possible, but tends to fall into **local min

## Links

- Repository: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
