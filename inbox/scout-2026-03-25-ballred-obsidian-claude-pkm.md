---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code starter kit"
  quality_score: 74
  scoring_breakdown:
    stars: 26
    recency: 15
    docs: 20
    community: 13
github_data:
  full_name: "ballred/obsidian-claude-pkm"
  url: "https://github.com/ballred/obsidian-claude-pkm"
  description: "A complete starter kit for an Obsidian + Claude Code personal knowledge management system."
  stars: 1267
  forks: 88
  open_issues: 9
  language: "Shell"
  license: "MIT"
  last_push: "2026-02-18"
  created: "2025-08-07"
  topics: ["ai-agents", "claude-code", "goal-tracking", "obsidian", "pkm", "productivity", "second-brain"]
---

# ballred/obsidian-claude-pkm

> Discovered by arsenal scout — awaiting manual triage

## Description

A complete starter kit for an Obsidian + Claude Code personal knowledge management system.

## README Excerpt

**📊 [Take the quick poll](https://github.com/ballred/obsidian-claude-pkm/discussions/4)** - Help shape what gets built next!

---

# Obsidian + Claude Code: AI Accountability System

**Not another PKM starter kit.** This is an execution system that connects your 3-year vision to what you do today — and holds you accountable with AI.

```
3-Year Vision ──→ Yearly Goals ──→ Projects ──→ Monthly Goals ──→ Weekly Review ──→ Daily Tasks
                                      ↑
                              /project new
                         (the bridge layer)
```

Every layer connects. `/daily` surfaces your ONE Big Thing from the weekly review. `/weekly` shows project progress. `/monthly` checks quarterly milestones. `/goal-tracking` knows which goals have no active project. Nothing falls through the cracks.

**v3.1** · Zero dependencies · MIT License

## The Cascade

The #1 reason people star this repo: **"I want goals → projects → daily notes → tasks to actually connect."**

| Layer | File | Skill | What It Does |
|-------|------|-------|-------------|
| Vision | `Goals/0. Three Year Goals.md` | `/goal-tracking` | Life areas, long-term direction |
| Annual | `Goals/1. Yearly Goals.md` | `/goal-tracking` | Measurable objectives, quarterly milestones |
| Projects | `Projects/*/CLAUDE.md` | `/project` | Active initiatives linked to goals |
| Monthly | `Goals/2. Monthly Goals.md` | `/monthly` | Roll up weekly reviews, check quarterly progress |
| Weekly | `Goals/3. Weekly Review.md` | `/weekly` | Reflect, realign, plan next week |
| Daily | `Daily Notes/YYYY-MM-DD.md` | `/daily` | Morning planning, evening reflection |

### How It Flows

**Morning** — `/daily` creates today's note, shows your week's ONE Big Thing and active project next-actions. You pick your focus.

**Evening** — `/daily` summarizes which goals and projects got attention today. Unlinked tasks get flagged.

**Sunday** — `/weekly` reads all your daily notes, scans project status, calculates goal progress, and helps you plan next week. Optional agent team mode parallelizes the collection.

**End of month** — `/monthly` rolls up the weekly reviews, checks quarterly milestones against yearly goals, and sets next month's priorities.

**Ad hoc** — `/project new` creates a project linked to a goal. `/project status` shows a dashboard. `/review` auto-detects the right review type based on context.

## Quick Start

### Prerequisites
- [Obsidian](https://obsidian.md/) installed
- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed
- Git installed

### Setup

```bash
# Clone and set up
git clone https://github.com/ballred/obsidian-claude-pkm.git
cd obsidian-claude-pkm
chmod +x scripts/setup.sh && ./scripts/setup.sh

# Open vault in Obsidian, then start Claude Code:
cd ~/your-vault-location
claude
```

On first run, you'll see a welcome message with the cascade visualization. Run `/onboard` to personalize your vault — it asks your name, preferred review day, and goal area

## Links

- Repository: https://github.com/ballred/obsidian-claude-pkm
