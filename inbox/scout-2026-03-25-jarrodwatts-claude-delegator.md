---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code plugin"
  quality_score: 73
  scoring_breakdown:
    stars: 25
    recency: 20
    docs: 20
    community: 8
github_data:
  full_name: "jarrodwatts/claude-delegator"
  url: "https://github.com/jarrodwatts/claude-delegator"
  description: "Delegate tasks to Codex and Gemini directly from within Claude Code."
  stars: 921
  forks: 45
  open_issues: 2
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-03-09"
  created: "2026-01-08"
  topics: ["ai-agents", "claude", "claude-code", "codex", "gpt", "mcp", "plugin"]
---

# jarrodwatts/claude-delegator

> Discovered by arsenal scout — awaiting manual triage

## Description

Delegate tasks to Codex and Gemini directly from within Claude Code.

## README Excerpt

# Claude Delegator

GPT expert subagents for Claude Code. Five specialists that can analyze AND implement—architecture, security, code review, and more.

[![License](https://img.shields.io/github/license/jarrodwatts/claude-delegator?v=2)](LICENSE)
[![Stars](https://img.shields.io/github/stars/jarrodwatts/claude-delegator?v=2)](https://github.com/jarrodwatts/claude-delegator/stargazers)

![Claude Delegator in action](claude-delegator.png)

## Install

Inside a Claude Code instance, run the following commands:

**Step 1: Add the marketplace**
```
/plugin marketplace add jarrodwatts/claude-delegator
```

**Step 2: Install the plugin**
```
/plugin install claude-delegator
```

**Step 3: Run setup**
```
/claude-delegator:setup
```

Done! Claude now routes complex tasks to GPT experts automatically.

> **Note**: Requires [Codex CLI](https://github.com/openai/codex) or [Gemini CLI](https://github.com/google/gemini-cli). Setup guides you through installation.

---

## What is Claude Delegator?

Claude gains a team of GPT and Gemini specialists via native MCP. Each expert has a distinct specialty and can advise OR implement.

**Note:** You can use either provider (GPT or Gemini), or both. The plugin will automatically detect which one is configured and route tasks accordingly.

| What You Get | Why It Matters |
|--------------|----------------|
| **5 domain experts** | Right specialist for each problem type |
| **GPT or Gemini** | Use your preferred model provider |
| **Dual mode** | Experts can analyze (read-only) or implement (write) |
| **Auto-routing** | Claude detects when to delegate based on your request |
| **Synthesized responses** | Claude interprets expert output, never raw passthrough |

### The Experts

| Expert | What They Do | Example Triggers |
|--------|--------------|------------------|
| **Architect** | System design, tradeoffs, complex debugging | "How should I structure this?" / "What are the tradeoffs?" |
| **Plan Reviewer** | Validate plans before you start | "Review this migration plan" / "Is this approach sound?" |
| **Scope Analyst** | Catch ambiguities early | "What am I missing?" / "Clarify the scope" |
| **Code Reviewer** | Find bugs, improve quality | "Review this PR" / "What's wrong with this?" |
| **Security Analyst** | Vulnerabilities, threat modeling | "Is this secure?" / "Harden this endpoint" |

### When Experts Help Most

- **Architecture decisions** — "Should I use Redis or in-memory caching?"
- **Stuck debugging** — After 2+ failed attempts, get a fresh perspective
- **Pre-implementation** — Validate your plan before writing code
- **Security concerns** — "Is this auth flow safe?"
- **Code quality** — Get a second opinion on your implementation

### When NOT to Use Experts

- Simple file operations (Claude handles these directly)
- First attempt at any fix (try yourself first)
- Trivial questions (no need to delegate)

---

## How It Works

```
You: "Is this authentication flow secure?"
                    ↓
Claude: 

## Links

- Repository: https://github.com/jarrodwatts/claude-delegator
