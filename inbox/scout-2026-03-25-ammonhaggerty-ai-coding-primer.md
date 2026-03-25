---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code starter kit"
  quality_score: 60
  scoring_breakdown:
    stars: 15
    recency: 20
    docs: 15
    community: 10
github_data:
  full_name: "ammonhaggerty/ai-coding-primer"
  url: "https://github.com/ammonhaggerty/ai-coding-primer"
  description: "An open-source guidebook and starter kit for building full-stack products with Claude Code and Cloudflare — for designers, founders, and anyone blocked by the technical wall"
  stars: 65
  forks: 6
  open_issues: 0
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-11"
  created: "2026-02-26"
  topics: ["ai-assisted-development", "beginners", "claude-code", "cloudflare-workers", "daisyui", "full-stack", "hono", "htmx"]
---

# ammonhaggerty/ai-coding-primer

> Discovered by arsenal scout — awaiting manual triage

## Description

An open-source guidebook and starter kit for building full-stack products with Claude Code and Cloudflare — for designers, founders, and anyone blocked by the technical wall

## README Excerpt

# Intro to Full-Stack AI Product Development

An open-source guidebook and starter kit for building real products with Claude Code and Cloudflare — written for designers, founders, PMs, researchers, hobbyists, and anyone with ideas who's been blocked by the technical wall.

[![AI Coding Primer Onboarding Video](https://github.com/user-attachments/assets/0a621b86-f898-487f-ac7d-d34a6c6aa3cc)](https://youtu.be/KPAlZ3Oni1A)
*☝️ This video walks through the entire onboarding and sample project*

I want to be clear - what I'm sharing is highly technical and the ideas shared have taken me years to learn and understand. What's changed is Claude, as helper, problem-solver, and guide, allows you to navigate nearly anything that comes your way. I tried to make the onboarding process as simple as I could, but my first dry-run was a complete failure - that said, Claude was able to figure out and correct for every issue. Once you have Claude running, just ask for help at any step. 

## Start Reading

**[Read the guidebook →](guidebook/)**

Or jump straight to the [TL;DR Fast Track](guidebook/00-tldr.md) if you want to start building now.

## What's Here

```
ai-coding-primer/
├── guidebook/       # The guidebook — one chapter per file, read it like a book
├── starter/         # Starter project template (what you'll clone)
├── assets/          # Images and diagrams
├── docs/            # Working notes and plans (project memory)
└── _authoring/      # Editorial materials (outlines, research, notes)
```

## The Guidebook

| # | Chapter | Description |
|---|---------|-------------|
| 00 | [TL;DR](guidebook/00-tldr.md) | Seven steps to a deployed app |
| 01 | [About the Author](guidebook/01-about-the-author.md) | Who wrote this and why |
| 02 | [The Landscape](guidebook/02-the-landscape.md) | What changed and the mental model |
| 03 | [Setting Up](guidebook/03-setting-up.md) | Installing your workshop |
| 04 | [The Cloud](guidebook/04-the-cloud.md) | Cloudflare and your first deploy |
| 05 | [Building](guidebook/05-building.md) | Your first feature, end to end |
| 06 | [Daily Practice](guidebook/06-daily-practice.md) | The ongoing rhythm of building |
| 07 | [Where This Is Going](guidebook/07-where-this-is-going.md) | What comes next |
| 08 | [Appendices](guidebook/08-appendices.md) | Claude Code features, AI models & pricing, Cloudflare free tier, links, glossary, troubleshooting |

## The Stack

This guide teaches one specific, opinionated stack:

- **Claude Code** (Opus 4.6) — Your AI coding partner, in the terminal
- **Cloudflare Workers** — Where your code runs (free tier gets you far)
- **Hono** — Web framework for the edge
- **Tailwind + DaisyUI** — Styling without writing CSS
- **HTMX + Alpine.js** — Interactivity without a framework
- **D1** — SQLite database, zero config
- **R2** — File storage, zero egress fees
- **Vectorize** — Vector database for smart search and RAG

## Status

The guidebook is in **active drafting**. All chapters have first drafts. 

## Links

- Repository: https://github.com/ammonhaggerty/ai-coding-primer
