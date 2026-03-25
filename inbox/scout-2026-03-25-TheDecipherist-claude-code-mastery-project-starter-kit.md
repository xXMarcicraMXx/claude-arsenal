---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code starter kit"
  quality_score: 68
  scoring_breakdown:
    stars: 20
    recency: 20
    docs: 20
    community: 8
github_data:
  full_name: "TheDecipherist/claude-code-mastery-project-starter-kit"
  url: "https://github.com/TheDecipherist/claude-code-mastery-project-starter-kit"
  description: "The definitive starting point for Claude Code projects. Based on Claude Code Mastery Guides V1-V5."
  stars: 255
  forks: 32
  open_issues: 1
  language: "Shell"
  license: "MIT"
  last_push: "2026-03-04"
  created: "2026-02-13"
  topics: []
---

# TheDecipherist/claude-code-mastery-project-starter-kit

> Discovered by arsenal scout — awaiting manual triage

## Description

The definitive starting point for Claude Code projects. Based on Claude Code Mastery Guides V1-V5.

## README Excerpt

# Claude Code Starter Kit

[![CI](https://github.com/TheDecipherist/claude-code-mastery-project-starter-kit/actions/workflows/ci.yml/badge.svg)](https://github.com/TheDecipherist/claude-code-mastery-project-starter-kit/actions/workflows/ci.yml)

> ## [View the Full Interactive Guide →](https://thedecipherist.github.io/claude-code-mastery-project-starter-kit/)
>
> The GitHub Pages site has the complete documentation with syntax highlighting, navigation, and visual examples.

> The definitive starting point for Claude Code projects.
> Based on [Claude Code Mastery Guides V1-V5](https://github.com/TheDecipherist/claude-code-mastery) by TheDecipherist.

---

## What Is This?

This is a **scaffold template**, not a runnable application. It provides the infrastructure (commands, hooks, skills, agents, documentation templates) that makes Claude Code dramatically more effective. You use it to **create** projects, not run it directly.

### Three Ways to Use It

**A. Scaffold a new project (most common):**
```bash
/new-project my-app clean    # or: /new-project my-app default
cd ~/projects/my-app
/setup
```
This creates a new project directory with all the Claude Code tooling pre-configured. Run `/quickstart` for a guided walkthrough.

**B. Convert an existing project:**
```bash
/convert-project-to-starter-kit ~/projects/my-existing-app
```
Non-destructive merge — brings all starter kit infrastructure (commands, hooks, skills, agents, CLAUDE.md rules) into your existing project while preserving everything you already have. Creates a safety commit first so you can `git revert HEAD` to undo.

**C. Customize the template itself:**
Clone this repo and modify the commands, hooks, skills, and rules to match your team's standards. Then use your customized version as the source for `/new-project`.

> **What NOT to do:** Don't clone this repo and run `pnpm dev` expecting a working app. This is the *template* that creates apps — it's not an app itself. If you're looking to build something, start with option A above.

## Learning Path

Progress through these phases at your own pace. Each builds on the previous one.

The starter kit supports two development workflows:
- **Classic** — `/review`, `/commit`, `/create-api`, `/create-e2e` (individual commands, you drive)
- **MDD** — `/mdd` (structured Document → Test → Code workflow, Claude drives with your approval)

Both use the same hooks, rules, and quality gates. MDD adds structured documentation and audit capabilities on top.

```
Phase 1                Phase 2              Phase 3              Phase 4              Phase 5
INITIAL SETUP          BUILD FEATURES       QUALITY & TESTING    DEPLOYMENT           ADVANCED
(5 minutes)

/install-global   -->  /mdd <feature>  -->  /mdd audit      -->  /optimize-docker -->  /refactor
/new-project           /review              /mdd status          /security-check       /what-is-my-ai-doing
cd my-app              /commit              /create-e2e          deploy                /

## Links

- Repository: https://github.com/TheDecipherist/claude-code-mastery-project-starter-kit
- Homepage: https://thedecipherist.github.io/claude-code-mastery-project-starter-kit/
