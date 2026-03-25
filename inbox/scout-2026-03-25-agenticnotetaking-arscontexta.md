---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code plugin"
  quality_score: 79
  scoring_breakdown:
    stars: 29
    recency: 20
    docs: 20
    community: 10
github_data:
  full_name: "agenticnotetaking/arscontexta"
  url: "https://github.com/agenticnotetaking/arscontexta"
  description: "Claude Code plugin that generates individualized knowledge systems from conversation. You describe how you think and work, have a conversation and get a complete second brain as markdown files you own."
  stars: 2849
  forks: 182
  open_issues: 21
  language: "Shell"
  license: "MIT"
  last_push: "2026-02-24"
  created: "2026-02-15"
  topics: ["claude-code", "claude-code-plugin", "knowledge-base", "knowledge-management", "markdown", "second-brain"]
---

# agenticnotetaking/arscontexta

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Code plugin that generates individualized knowledge systems from conversation. You describe how you think and work, have a conversation and get a complete second brain as markdown files you own.

## README Excerpt

# Ars Contexta

**A second brain for your agent.**

A Claude Code plugin that generates complete knowledge systems from conversation.
You describe how you think and work. The engine derives a cognitive architecture
-- folder structure, context files, processing pipeline, hooks, navigation maps,
and note templates -- tailored to your domain and backed by 249 research claims.

No templates. No configuration. Just conversation.

**v0.8.0** · Claude Code plugin · MIT

---

## Installation

1. Add the marketplace to Claude Code:
   ```
   /plugin marketplace add agenticnotetaking/arscontexta
   ```

2. Install the plugin:
   ```
   /plugin install arscontexta@agenticnotetaking
   ```

3. Restart Claude Code, then run:
   ```
   /arscontexta:setup
   ```

4. Answer 2-4 questions about your domain (~20 minutes -- token-intensive but one-time)

5. The engine generates your complete knowledge system

6. Restart Claude Code again to activate generated hooks and skills

7. Run `/arscontexta:help` to see everything available

---

## What It Does

Most AI tools start every session blank. Ars Contexta changes that by generating
a persistent thinking system derived from how you actually work.

**What you get:**

- **A vault** -- plain markdown files connected by wiki links, forming a traversable
  knowledge graph. No database, no cloud, no lock-in.
- **A processing pipeline** -- skills that extract insights, find connections, update
  old notes with new context, and verify quality.
- **Automation** -- hooks that enforce structure on every write, detect maintenance
  needs, capture session state, and auto-commit.
- **Navigation** -- Maps of Content (MOCs) at hub, domain, and topic levels.
- **Templates** -- note templates with `_schema` blocks as single source of truth.
- **A user manual** -- 7 pages of domain-native documentation generated alongside.

**The key differentiator:** derivation, not templating. Every choice traces to
specific research claims. The engine reasons from principles about what your
domain needs and why.

---

## The Setup Flow

`/arscontexta:setup` runs a 6-phase process:

| Phase | What Happens |
|-------|-------------|
| **Detection** | Detects Claude Code environment and capabilities |
| **Understanding** | 2-4 conversation turns where you describe your domain |
| **Derivation** | Maps signals to eight configuration dimensions with confidence scoring |
| **Proposal** | Shows what will be generated and why, in your vocabulary |
| **Generation** | Produces all files: context file, folders, templates, skills, hooks, manual |
| **Validation** | Checks all 15 kernel primitives, runs pipeline smoke test |

The whole process takes about 20 minutes. It's token-intensive because the engine
reads research claims, reasons about your domain, and generates substantial output.
This is a one-time investment -- after setup, your agent remembers.

For advanced users: `/arscontexta:setup --advanced` to configure dimensions directly.

---

## Three-Spac

## Links

- Repository: https://github.com/agenticnotetaking/arscontexta
- Homepage: https://arscontexta.org
