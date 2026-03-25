---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "anthropic mcp server"
  quality_score: 72
  scoring_breakdown:
    stars: 20
    recency: 20
    docs: 20
    community: 12
github_data:
  full_name: "ilhamfp/pasal"
  url: "https://github.com/ilhamfp/pasal"
  description: "Pasal.id - The first open, AI-native Indonesian legal platform. MCP server + REST API + web app giving AI grounded access Indonesian laws."
  stars: 196
  forks: 29
  open_issues: 18
  language: "TypeScript"
  license: "AGPL-3.0"
  last_push: "2026-03-01"
  created: "2026-02-11"
  topics: ["ai-native", "anthropic", "claude", "codex", "full-text-search", "hackathon", "hukum", "indonesia", "indonesian-law", "law", "legal-tech", "mcp", "mcp-server", "nextjs", "open-data", "supabase"]
---

# ilhamfp/pasal

> Discovered by arsenal scout — awaiting manual triage

## Description

Pasal.id - The first open, AI-native Indonesian legal platform. MCP server + REST API + web app giving AI grounded access Indonesian laws.

## README Excerpt

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="logo/lockup-dark-bg.svg" />
    <img src="logo/lockup-primary.svg" alt="Pasal.id" height="64" />
  </picture>
</p>

<h3 align="center">The First Open, AI-Native Platform for Indonesian Law</h3>

<p align="center">
  <a href="https://www.loom.com/share/da211318bbe14c4396840b97f5ab8603">Demo Video</a> ·
  <a href="https://pasal.id">Website</a> ·
  <a href="https://pasal.id/connect">Connect to Claude</a> ·
  <a href="https://pasal.id/api">REST API</a> ·
  <a href="LICENSE">AGPL-3.0 License</a>
</p>

<p align="center">
  <a href="https://pasal.id"><img src="https://img.shields.io/badge/Legal_Data-Pasal.id-2B6150?style=flat" alt="Legal Data by Pasal.id" /></a>
  <a href="https://pasal.id/connect"><img src="https://img.shields.io/badge/MCP-Server-blue?style=flat" alt="MCP Server" /></a>
  <img src="https://img.shields.io/badge/Built_with-Opus_4.6-cc785c?style=flat&logo=anthropic&logoColor=white" alt="Built with Opus 4.6" />
  <img src="https://img.shields.io/badge/Next.js-16-black?logo=nextdotjs" alt="Next.js" />
  <img src="https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E?logo=supabase" alt="Supabase" />
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL--3.0-blue?style=flat" alt="License: AGPL-3.0" /></a>
</p>

---

## The Problem

**280 million Indonesians** have no practical way to read their own laws. The official legal database ([peraturan.go.id](https://peraturan.go.id)) offers **only PDF downloads**: no search, no structure, no API. When you ask AI about Indonesian law, you get **hallucinated articles and wrong citations** because no grounded data source exists.

## Try It Now

Connect Claude to real Indonesian legal data in one command:

```bash
claude mcp add --transport http pasal-id https://pasal-mcp-server-production.up.railway.app/mcp
```

Then ask:

> *"Apa saja hak pekerja kontrak menurut UU Ketenagakerjaan?"* (What are contract worker rights under the Labor Law?)
> *"Jelaskan pasal tentang perlindungan data pribadi"* (Explain articles on personal data protection)
> *"Apakah UU Perkawinan 1974 masih berlaku?"* (Is the 1974 Marriage Law still in force?)

Claude searches **40,000+ regulations and 937,000+ structured articles**, cites specific Pasal (articles), and gives grounded answers. No hallucination.

Or browse the web app at **[pasal.id](https://pasal.id)**.

## What We Built

| | Feature | Description |
|---|---|---|
| **Search** | Full-Text Legal Search | Indonesian stemmer + 3-tier fallback across 937,000+ articles |
| **Read** | Structured Reader | Three-column law reader with TOC, amendment timeline, and verification badges |
| **AI** | MCP Server | 4 grounded tools giving Claude access to actual legislation with exact citations |
| **API** | REST API | Public JSON endpoints for search, browsing, and article retrieval |
| **Correct** | Crowd-Sourced Corrections | Anyone can submit corrections; AI verifies before a

## Links

- Repository: https://github.com/ilhamfp/pasal
- Homepage: https://pasal.id
