---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 57
  scoring_breakdown:
    stars: 13
    recency: 15
    docs: 20
    community: 9
github_data:
  full_name: "solanabr/solana-claude-config"
  url: "https://github.com/solanabr/solana-claude-config"
  description: "Claude Code configs for the expert Solana builder. CLAUDE.md, agents, commands, hooks, rules, skills and settings across Web, Anchor, Pinnochio, Unity, Mobile and more."
  stars: 33
  forks: 5
  open_issues: 0
  language: ""
  license: "MIT"
  last_push: "2026-01-17"
  created: "2026-01-13"
  topics: ["anchor", "claude-agent", "claude-code", "claude-commands", "claude-md", "claude-skills", "claude-subagents", "pinocchio", "playsolana", "solana", "solana-agents", "solana-engineer", "solana-mobile-stack", "solana-program", "trident", "unity-csharp"]
---

# solanabr/solana-claude-config

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Code configs for the expert Solana builder. CLAUDE.md, agents, commands, hooks, rules, skills and settings across Web, Anchor, Pinnochio, Unity, Mobile and more.

## README Excerpt

# Solana Claude Configuration

Production-ready Claude Code configuration for full-stack Solana development. Combines best practices from multiple sources into an agent-optimized, token-efficient config you can copy over and adapt to your specific project.

Current multi-agent workflow favors monorepos, so we use a single CLAUDE.md/config for the whole project while leveraging agents and context-specific skills to solve each step of builder flow.

The idea here is to provide a generic CLAUDE.md that relies on subagents to plan and execute actions, dynamically loading markdown files for context, saving tokens in the end of the day.

Remember to rename ./CLAUDE-solana.md back to ./CLAUDE.md, as the current top-level CLAUDE.md file is focused on maintaining the repo itself.

## What This Is

A complete `.claude/` configuration that turns Claude into a Solana development expert with:

- **Specialized agents** for different tasks (architecture, Anchor, Pinocchio, frontend, backend, QA, docs, Unity games)
- **Workflow commands** for building, testing, deploying, and committing (Rust, TypeScript, Unity/C#)
- **Progressive skill loading** that only loads context when needed (saves tokens)
- **Auto-loading rules** that enforce best practices based on file patterns

## Quick Start

```bash
# Copy to your Solana project
cp -r .claude /path/to/your-project/
cp CLAUDE-solana.md /path/to/your-project/CLAUDE.md

# Or clone and use as template
git clone https://github.com/solanabr/solana-claude-config
```

## Key Features

### Agent-Ready Architecture

Each agent loads its own specialized context on invocation:

```
"Use solana-architect to design the vault program"
"Use anchor-engineer to implement the deposit instruction"  
"Use solana-qa-engineer to write comprehensive tests"
```

Claude will spawn each specialized agent by itself based on context.

### Token-Efficient Design

- Skills load progressively (not all at once)
- Agents reference skills instead of duplicating content
- Rules auto-load only for matching file patterns
- Decision frameworks live in agents, not global context

### Modern Stack (2026)

| Layer | Stack |
|-------|-------|
| Programs | Anchor 0.31+, Pinocchio, Rust 1.82+ |
| Testing | Mollusk, LiteSVM, Surfpool, Trident |
| Frontend | @solana/kit, Next.js 15, React 19 |
| Backend | Axum 0.8+, Tokio 1.40+, sqlx |
| Unity Games | Solana.Unity-SDK, .NET 9, C# 13 |
| PlaySolana | PSG1 console, PlayDex, SvalGuard |

## Repository Structure

```
.
├── CLAUDE.md                    # Main hub - Claude reads this first
├── README.md                    # This file
├── LICENSE                      # MIT
└── .claude/
    ├── agents/                      # 11 specialized agents
    │   ├── solana-architect.md          # System design, PDAs, architecture
    │   ├── anchor-engineer.md           # Anchor framework development
    │   ├── pinocchio-engineer.md        # CU optimization, zero-copy
    │   ├── solana-frontend-engineer.md  # React/Next.js, w

## Links

- Repository: https://github.com/solanabr/solana-claude-config
