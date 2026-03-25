---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 66
  scoring_breakdown:
    stars: 15
    recency: 20
    docs: 20
    community: 11
github_data:
  full_name: "aakashg/pm-claude-code-setup"
  url: "https://github.com/aakashg/pm-claude-code-setup"
  description: "Ready-to-use CLAUDE.md and starter skill for product managers using Claude Code."
  stars: 56
  forks: 15
  open_issues: 0
  language: ""
  license: "MIT"
  last_push: "2026-03-04"
  created: "2026-02-27"
  topics: ["ai", "ai-tools", "claude", "claude-code", "pm-os", "prd", "product-management", "productivity"]
---

# aakashg/pm-claude-code-setup

> Discovered by arsenal scout — awaiting manual triage

## Description

Ready-to-use CLAUDE.md and starter skill for product managers using Claude Code.

## README Excerpt

# PM Claude Code Setup

[![Stars](https://img.shields.io/github/stars/aakashg/pm-claude-code-setup?style=flat-square)](https://github.com/aakashg/pm-claude-code-setup/stargazers)
[![License](https://img.shields.io/github/license/aakashg/pm-claude-code-setup?style=flat-square)](LICENSE)

A production-ready Claude Code configuration for product managers. Drop these files into your project and Claude Code immediately understands PM work.

Includes a `CLAUDE.md` context file, 6 PM skills, and 4 templates. Takes 60 seconds to set up.

**This setup works standalone. The full PM Operating System goes further: 41+ skills, 7 sub-agent perspectives, a complete context library, launch templates, and sprint planning workflows refined over 100+ iterations.**

**[Get the full PM Operating System →](https://www.news.aakashg.com/p/pm-os)**

---

## What's Inside

```
pm-claude-code-setup/
├── CLAUDE.md                           # Master context file — drop in your project root
├── templates/
│   ├── prd-template.md                 # Blank PRD structure
│   ├── launch-plan.md                  # Launch planning template
│   ├── okr-template.md                 # OKR scorecard
│   └── sprint-review.md               # Sprint review template
└── .claude/
    └── skills/
        ├── prd-writer/                 # "write a PRD" → structured PRD with clarifying questions
        ├── competitive-analysis/       # "analyze competitor" → smart/weak/implications framework
        ├── launch-checklist/           # "launch checklist" → risk-scaled pre/post launch plan
        ├── metrics-definer/            # "define metrics" → primary, guardrail, and anti-metrics
        ├── sprint-planner/             # "plan sprint" → capacity-checked sprint with risks
        └── user-research/              # "synthesize research" → evidence-ranked findings
```

## Quick Setup

**Step 1:** Copy `CLAUDE.md` to your project root:
```bash
cp CLAUDE.md /path/to/your/project/
```

**Step 2:** Copy the skills folder:
```bash
cp -r .claude/ /path/to/your/project/
```

**Step 3:** Open Claude Code in your project. It loads automatically.

Done. Claude now knows you're a PM, follows your writing style, and writes PRDs on command.

## What the CLAUDE.md Does

`CLAUDE.md` is a lean config file — not a manual. It tells Claude who you are, how to write, and what rules to follow. Fill in the `[FILL IN]` fields at the top (~2 minutes), and the rest works immediately:

- **Your context** — role, product, metrics, OKRs, terminology
- **Writing rules** — enforced tone, banned words, output standards
- **Sub-agent roles** — 6 reviewers in a table (engineer, designer, executive, skeptic, customer, data analyst)
- **Output standards** — clarifying questions before generating, metrics with baselines, risks with mitigations
- **Skills reference** — points to `.claude/skills/` without duplicating their logic
- **MCP connections** — your integrations (Notion, Jira, Slack, etc.)

The file is intentionally under 60 l

## Links

- Repository: https://github.com/aakashg/pm-claude-code-setup
- Homepage: https://www.news.aakashg.com/p/pm-os
