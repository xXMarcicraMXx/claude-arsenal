---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code skill"
  quality_score: 77
  scoring_breakdown:
    stars: 34
    recency: 8
    docs: 20
    community: 15
github_data:
  full_name: "diet103/claude-code-infrastructure-showcase"
  url: "https://github.com/diet103/claude-code-infrastructure-showcase"
  description: "Examples of my Claude Code infrastructure with skill auto-activation, hooks, and agents"
  stars: 9336
  forks: 1195
  open_issues: 15
  language: "Shell"
  license: "MIT"
  last_push: "2025-10-31"
  created: "2025-10-30"
  topics: []
---

# diet103/claude-code-infrastructure-showcase

> Discovered by arsenal scout — awaiting manual triage

## Description

Examples of my Claude Code infrastructure with skill auto-activation, hooks, and agents

## README Excerpt

# Claude Code Infrastructure Showcase

**A curated reference library of production-tested Claude Code infrastructure.**

Born from 6 months of real-world use managing a complex TypeScript microservices project, this showcase provides the patterns and systems that solved the "skills don't activate automatically" problem and scaled Claude Code for enterprise development.

> **This is NOT a working application** - it's a reference library. Copy what you need into your own projects.

---

## What's Inside

**Production-tested infrastructure for:**
- ✅ **Auto-activating skills** via hooks
- ✅ **Modular skill pattern** (500-line rule with progressive disclosure)
- ✅ **Specialized agents** for complex tasks
- ✅ **Dev docs system** that survives context resets
- ✅ **Comprehensive examples** using generic blog domain

**Time investment to build:** 6 months of iteration
**Time to integrate into your project:** 15-30 minutes

---

## Quick Start - Pick Your Path

### 🤖 Using Claude Code to Integrate?

**Claude:** Read [`CLAUDE_INTEGRATION_GUIDE.md`](CLAUDE_INTEGRATION_GUIDE.md) for step-by-step integration instructions tailored for AI-assisted setup.

### 🎯 I want skill auto-activation

**The breakthrough feature:** Skills that actually activate when you need them.

**What you need:**
1. The skill-activation hooks (2 files)
2. A skill or two relevant to your work
3. 15 minutes

**👉 [Setup Guide: .claude/hooks/README.md](.claude/hooks/README.md)**

### 📚 I want to add ONE skill

Browse the [skills catalog](.claude/skills/) and copy what you need.

**Available:**
- **backend-dev-guidelines** - Node.js/Express/TypeScript patterns
- **frontend-dev-guidelines** - React/TypeScript/MUI v7 patterns
- **skill-developer** - Meta-skill for creating skills
- **route-tester** - Test authenticated API routes
- **error-tracking** - Sentry integration patterns

**👉 [Skills Guide: .claude/skills/README.md](.claude/skills/README.md)**

### 🤖 I want specialized agents

10 production-tested agents for complex tasks:
- Code architecture review
- Refactoring assistance
- Documentation generation
- Error debugging
- And more...

**👉 [Agents Guide: .claude/agents/README.md](.claude/agents/README.md)**

---

## What Makes This Different?

### The Auto-Activation Breakthrough

**Problem:** Claude Code skills just sit there. You have to remember to use them.

**Solution:** UserPromptSubmit hook that:
- Analyzes your prompts
- Checks file context
- Automatically suggests relevant skills
- Works via `skill-rules.json` configuration

**Result:** Skills activate when you need them, not when you remember them.

### Production-Tested Patterns

These aren't theoretical examples - they're extracted from:
- ✅ 6 microservices in production
- ✅ 50,000+ lines of TypeScript
- ✅ React frontend with complex data grids
- ✅ Sophisticated workflow engine
- ✅ 6 months of daily Claude Code use

The patterns work because they solved real problems.

### Modular Skills (500-Line Rule)

Large skills hit con

## Links

- Repository: https://github.com/diet103/claude-code-infrastructure-showcase
