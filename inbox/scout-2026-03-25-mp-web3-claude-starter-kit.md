---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code starter kit"
  quality_score: 71
  scoring_breakdown:
    stars: 16
    recency: 25
    docs: 20
    community: 10
github_data:
  full_name: "mp-web3/claude-starter-kit"
  url: "https://github.com/mp-web3/claude-starter-kit"
  description: "Turn Claude Code into a personal AI assistant that remembers you across sessions"
  stars: 67
  forks: 11
  open_issues: 1
  language: "Python"
  license: "MIT"
  last_push: "2026-03-18"
  created: "2026-03-05"
  topics: []
---

# mp-web3/claude-starter-kit

> Discovered by arsenal scout — awaiting manual triage

## Description

Turn Claude Code into a personal AI assistant that remembers you across sessions

## README Excerpt

# Claude Code Starter Kit

A pre-built configuration that gives Claude Code persistent memory, security guardrails, and structured workflows. Clone, run `setup.sh`, and your next session picks up where the last one left off.

## How It Works

Claude Code reads `~/.claude/` at startup. This kit installs minimal global config there — rules, security hooks, and a pointer to your workspace. The workspace (`~/claude-assistant/`) holds everything else: knowledge, skills, tasks, agents, and session history.

```
You run setup.sh ──> Phase 1: Minimal config to ~/.claude/
                     Phase 2: Full workspace at ~/claude-assistant/

~/.claude/ (global, every project)     ~/claude-assistant/ (workspace)
├── CLAUDE.md (pointer)                ├── .claude/CLAUDE.md (detailed)
├── settings.json (hooks)              ├── .claude/skills/ (6 skills)
├── rules/ (behavioral)               ├── knowledge/ (on-demand)
├── scripts/ (4 hook scripts)          ├── agents/ (4 definitions)
└── statusline.sh                      ├── scripts/ (db, learnings)
                                       ├── state/ (sessions, backlog)
                                       ├── MEMORY.md (200 lines)
                                       └── tasks.db (SQLite)
```

**Why the split?** `~/.claude/` is Claude Code's config directory — it should stay lean. Rules and hooks load every session regardless of project. Knowledge, tasks, and skills live in the workspace, loaded only when you're working there. This keeps `~/.claude/` clean and your assistant data in a proper, version-controlled workspace.

**On-demand loading is how this avoids context bloat.** The workspace CLAUDE.md contains a table of file paths and one-line descriptions. Claude sees the table at startup (~20-30 lines), then uses `Read` to open specific files when relevant. A typical session loads 3-5 files out of however many you have.

## What's Included

| Component | What It Does |
|---|---|
| `/onboard` | 20-30 min guided setup: profile, 12 Favorite Problems, goals, tasks |
| `/tasks` | SQLite-backed task management. Tasks connect to your goals and problems |
| `/plan` | 6-phase gated workflow: explore, discover tools, design, approve, implement, verify |
| `/reflect` | Extracts corrections and preferences from sessions, routes them to the right files |
| `/bootstrap` | Sets up any project's `.claude/` for agentic development |
| `/create-skill` | Scaffolds new skills with validation — extend the system with your own workflows |
| Security guard | Blocks secrets access, force-push, writes outside `$HOME`, `rm -rf`. Audit log at `~/.claude/state/guard-log.jsonl` |
| Session persistence | Pre-compact hook saves state, post-compact hook re-injects critical rules. Session reminders after 10 min |
| Delegation rules | Subagent orchestration: authority boundaries, knowledge flow, quality control |
| Agent definitions | 4 pre-built agents: code-reviewer, bug-fixer, implementer, researcher |
| Development standards | Code q

## Links

- Repository: https://github.com/mp-web3/claude-starter-kit
