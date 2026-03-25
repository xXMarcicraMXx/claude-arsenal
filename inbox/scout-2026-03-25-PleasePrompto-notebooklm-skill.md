---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code skill"
  quality_score: 74
  scoring_breakdown:
    stars: 31
    recency: 8
    docs: 20
    community: 15
github_data:
  full_name: "PleasePrompto/notebooklm-skill"
  url: "https://github.com/PleasePrompto/notebooklm-skill"
  description: "Use this skill to enable Claude Code to communicate directly with your Google NotebookLM notebooks. Query your uploaded documents and get source-grounded, citation-backed answers from Gemini. Features browser automation, library management, persistent authentication, and answers exclusively from your own knowledge base."
  stars: 5008
  forks: 522
  open_issues: 17
  language: "Python"
  license: "MIT"
  last_push: "2025-11-21"
  created: "2025-10-19"
  topics: []
---

# PleasePrompto/notebooklm-skill

> Discovered by arsenal scout — awaiting manual triage

## Description

Use this skill to enable Claude Code to communicate directly with your Google NotebookLM notebooks. Query your uploaded documents and get source-grounded, citation-backed answers from Gemini. Features browser automation, library management, persistent authentication, and answers exclusively from your own knowledge base.

## README Excerpt

<div align="center">

# NotebookLM Claude Code Skill

**Let [Claude Code](https://github.com/anthropics/claude-code) chat directly with NotebookLM for source-grounded answers based exclusively on your uploaded documents**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-purple.svg)](https://www.anthropic.com/news/skills)
[![Based on](https://img.shields.io/badge/Based%20on-NotebookLM%20MCP-green.svg)](https://github.com/PleasePrompto/notebooklm-mcp)
[![GitHub](https://img.shields.io/github/stars/PleasePrompto/notebooklm-skill?style=social)](https://github.com/PleasePrompto/notebooklm-skill)

> Use this skill to query your Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed answers from Gemini. Browser automation, library management, persistent auth. Drastically reduced hallucinations - answers only from your uploaded documents.

[Installation](#installation) • [Quick Start](#quick-start) • [Why NotebookLM](#why-notebooklm-not-local-rag) • [How It Works](#how-it-works) • [MCP Alternative](https://github.com/PleasePrompto/notebooklm-mcp)

</div>

---

## ⚠️ Important: Local Claude Code Only

**This skill works ONLY with local [Claude Code](https://github.com/anthropics/claude-code) installations, NOT in the web UI.**

The web UI runs skills in a sandbox without network access, which this skill requires for browser automation. You must use [Claude Code](https://github.com/anthropics/claude-code) locally on your machine.

---

## The Problem

When you tell [Claude Code](https://github.com/anthropics/claude-code) to "search through my local documentation", here's what happens:
- **Massive token consumption**: Searching through documentation means reading multiple files repeatedly
- **Inaccurate retrieval**: Searches for keywords, misses context and connections between docs
- **Hallucinations**: When it can't find something, it invents plausible-sounding APIs
- **Manual copy-paste**: Switching between NotebookLM browser and your editor constantly

## The Solution

This Claude Code Skill lets [Claude Code](https://github.com/anthropics/claude-code) chat directly with [**NotebookLM**](https://notebooklm.google/) — Google's **source-grounded knowledge base** powered by Gemini 2.5 that provides intelligent, synthesized answers exclusively from your uploaded documents.

```
Your Task → Claude asks NotebookLM → Gemini synthesizes answer → Claude writes correct code
```

**No more copy-paste dance**: Claude asks questions directly and gets answers straight back in the CLI. It builds deep understanding through automatic follow-ups, getting specific implementation details, edge cases, and best practices.

---

## Why NotebookLM, Not Local RAG?

| Approach | Token Cost | Setup Time | Hallucinations | Answer Quality |
|----------|------------|------------|----------------|----------------|
| **Feed docs to Claude** 

## Links

- Repository: https://github.com/PleasePrompto/notebooklm-skill
