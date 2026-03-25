---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code workflow"
  quality_score: 76
  scoring_breakdown:
    stars: 27
    recency: 15
    docs: 20
    community: 14
github_data:
  full_name: "CloudAI-X/claude-workflow-v2"
  url: "https://github.com/CloudAI-X/claude-workflow-v2"
  description: "Universal Claude Code workflow plugin with agents, skills, hooks, and commands"
  stars: 1302
  forks: 186
  open_issues: 2
  language: "Python"
  license: "MIT"
  last_push: "2026-02-14"
  created: "2026-01-01"
  topics: ["agent-skills", "ai", "ai-agents", "claude-code", "codex", "cursor", "skills", "workflow"]
---

# CloudAI-X/claude-workflow-v2

> Discovered by arsenal scout — awaiting manual triage

## Description

Universal Claude Code workflow plugin with agents, skills, hooks, and commands

## README Excerpt

# project-starter

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-v1.0.33+-blue.svg)](https://code.claude.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/CloudAI-X/claude-workflow-v2/pulls)

A universal Claude Code workflow plugin with specialized agents, skills, hooks, and output styles for any software project. Compatible with [skills.sh](https://skills.sh) — works with Claude Code, Cursor, Codex, and 35+ AI agents.

---

## Quick Start

### Option 1: skills.sh (Recommended — Any Agent)

```bash
npx skills add CloudAI-X/claude-workflow-v2
```

Installs skills to Claude Code, Cursor, Codex, Windsurf, Cline, and 35+ other AI agents automatically.

### Option 2: npx (Claude Code — Full Plugin)

```bash
npx install-claude-workflow-v2@latest
```

Installs the complete plugin: agents, commands, skills, and hooks.

### Option 3: CLI (Per-Session)

```bash
# Clone the plugin
git clone https://github.com/CloudAI-X/claude-workflow-v2.git

# Run Claude Code with the plugin
claude --plugin-dir ./claude-workflow-v2
```

### Option 4: Agent SDK

```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

for await (const message of query({
  prompt: "Hello",
  options: {
    plugins: [{ type: "local", path: "./claude-workflow-v2" }],
  },
})) {
  // Plugin commands, agents, and skills are now available
}
```

### Option 5: Install Permanently

```bash
# Install from marketplace (when available)
claude plugin install project-starter

# Or install from local directory
claude plugin install ./claude-workflow-v2
```

### Verify Installation

After loading the plugin, verify it's working:

```
> /plugin
```

Tab to **Installed** - you should see `project-starter` listed.
Tab to **Errors** - should be empty (no errors).

These commands become available:

```
/project-starter:architect    # Architecture-first mode
/project-starter:rapid        # Ship fast mode
/project-starter:commit       # Auto-generate commit message
/project-starter:verify-changes  # Multi-agent verification
```

---

## What's Included

| Component    | Count | Description                                                             |
| ------------ | ----- | ----------------------------------------------------------------------- |
| **Agents**   | 7     | Specialized subagents for code review, debugging, security, etc.        |
| **Commands** | 26    | Slash commands for workflows, output styles, planning, and onboarding   |
| **Skills**   | 14    | Knowledge domains with on-demand context loading                        |
| **Hooks**    | 14    | Automation scripts for formatting, security, metrics, and notifications |

---

## Usage Examples

### Commands in Action

**Auto-commit your changes:**

```
> /project-starter:commit

Looking at staged changes...
✓ Created commit: feat(auth): add JWT refresh token endpoin

## Links

- Repository: https://github.com/CloudAI-X/claude-workflow-v2
