---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code agent subagent"
  quality_score: 58
  scoring_breakdown:
    stars: 16
    recency: 15
    docs: 20
    community: 7
github_data:
  full_name: "tony/claude-code-riper-5"
  url: "https://github.com/tony/claude-code-riper-5"
  description: "Claude Code (Sub-agent, Custom Commands) for RIPER-5"
  stars: 73
  forks: 10
  open_issues: 2
  language: ""
  license: "MIT"
  last_push: "2026-02-08"
  created: "2025-09-05"
  topics: ["claude-code", "claude-subagents", "riper", "riper-5", "subagent", "subagents"]
---

# tony/claude-code-riper-5

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Code (Sub-agent, Custom Commands) for RIPER-5

## README Excerpt

# RIPER Workflow for Claude Code

**R**esearch • **I**nnovate • **P**lan • **E**xecute • **R**eview

A structured, context-efficient development workflow for [Claude Code](https://github.com/anthropics/claude-code/) using [custom slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands#custom-slash-commands) and [subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents).

## 🎯 Overview

RIPER creates a controlled, guided flow that enforces separation between research, planning, and execution phases. This helps:

- Reduce context usage through specialized agents
- Prevent premature implementation before understanding
- Maintain clear documentation of decisions
- Enable reproducible development processes

## 🚀 Quick Start

### Installation

1. Copy the `.claude` directory to your project root:

```bash
cp -r .claude /path/to/your/project/
```

2. Update `.claude/project-info.md` with your project details

3. Customize `.claude/riper-config.json` with your tech stack and paths

4. Optional: Add `.claude/memory-bank/` to `.gitignore` to keep plans and reviews private:

   ```bash
   echo ".claude/memory-bank/" >> .gitignore
   ```

   Or selectively ignore just plans and reviews while keeping memory bank structure:

   ```bash
   echo ".claude/memory-bank/*/plans/" >> .gitignore
   ```

   ```bash
   echo ".claude/memory-bank/*/reviews/" >> .gitignore
   ```

   Note: If you accidentally commit these, remove them before merging:

   ```bash
   git rebase -i HEAD~n  # where n is number of commits to review
   ```

### Basic Usage

Start a guided RIPER session:

```
/riper:strict
```

Then use the workflow commands:

1. **Research** - Investigate the codebase

   ```
   /riper:research analyze authentication system
   ```

2. **Plan** - Create technical specifications

   ```
   /riper:plan add OAuth2 support
   ```

3. **Execute** - Implement the approved plan

   ```
   /riper:execute
   ```

   Or execute a specific substep:

   ```
   /riper:execute 2.3
   ```

4. **Review** - Validate implementation
   ```
   /riper:review
   ```

## 📚 Commands Reference

### RIPER Workflow Commands

| Command                 | Description                        | Mode Restrictions           |
| ----------------------- | ---------------------------------- | --------------------------- |
| `/riper:strict`         | Enable strict protocol enforcement | None                        |
| `/riper:research`       | Enter research mode (read-only)    | Read only                   |
| `/riper:innovate`       | Brainstorm approaches (optional)   | Read only                   |
| `/riper:plan`           | Create technical specifications    | Read + Write to memory bank |
| `/riper:execute`        | Implement approved plan            | Full access                 |
| `/riper:execute <step>` | Execute specific plan step         | Full access                 |
| `/riper:review`         | Validate against plan              | Read + Test execution 

## Links

- Repository: https://github.com/tony/claude-code-riper-5
