---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code hook"
  quality_score: 70
  scoring_breakdown:
    stars: 23
    recency: 20
    docs: 15
    community: 12
github_data:
  full_name: "blader/taskmaster"
  url: "https://github.com/blader/taskmaster"
  description: "Stop hook for Claude Code that keeps the agent working until all plans and user requests are 100% complete"
  stars: 488
  forks: 31
  open_issues: 4
  language: "Shell"
  license: "MIT"
  last_push: "2026-03-11"
  created: "2026-02-10"
  topics: []
---

# blader/taskmaster

> Discovered by arsenal scout — awaiting manual triage

## Description

Stop hook for Claude Code that keeps the agent working until all plans and user requests are 100% complete

## README Excerpt

# Taskmaster

Taskmaster is a completion guard for coding agents.

It addresses a common failure mode: the agent makes partial progress, writes a
summary, and stops before the user goal is actually finished.

## Philosophy

Taskmaster is built around one idea: progress is not completion.

- Evidence over narrative:
  The agent should not be allowed to stop based on a convincing summary alone.
  Completion must be explicit and machine-checkable.
- Same-session recovery:
  When a turn is incomplete, the right move is to continue in the same running
  session, not restart from scratch.
- Goal re-anchoring:
  Compliance prompts force the model back to the user’s actual request, not its
  own local notion of “good enough”.
- Automation-safe signaling:
  A deterministic done token makes completion parseable for wrappers and
  CI-style flows.

## Core Contract

A run is complete only when the assistant emits:

```text
TASKMASTER_DONE::<session_id>
```

If that token is missing at stop time, Taskmaster blocks stop and pushes the
current turn to continue. Codex monitoring stays active for later turns in the
same long-lived session.

### Enforcement Prompt

Taskmaster uses one shared compliance prompt for both Codex and Claude.

- Codex: the wrapper/injector path injects this shared prompt back into the
  same running session when stop conditions are not met.
- Claude: the Stop hook returns this same shared prompt as the block reason.

The shared prompt source lives in `taskmaster-compliance-prompt.sh`.

## How It Works

- Codex path:
  - Runs through a wrapper (`codex` shim / `codex-taskmaster` launcher).
  - Enables Codex session logs.
  - Watches `task_complete` / `turn_complete` events.
  - If done token is missing, injects a continuation prompt into the same
    running Codex process via expect PTY.
  - A done token suppresses injection for that completed turn only; it does
    not permanently disable Taskmaster for future turns in the same session.
- Claude path:
  - Registers a `Stop` command hook.
  - Hook runs `check-completion.sh`.
  - If done token is missing, the stop is blocked with corrective feedback.

## Install

```bash
bash ~/.codex/skills/taskmaster/install.sh
```

Auto-detection behavior:
- Installs Codex integration when `codex` or `~/.codex` exists.
- Installs Claude integration when `claude` or `~/.claude` exists.
- If both are present, installs both.
- If neither is detected, defaults to both.

Optional target override:

```bash
TASKMASTER_INSTALL_TARGET=codex bash ~/.codex/skills/taskmaster/install.sh
TASKMASTER_INSTALL_TARGET=claude bash ~/.codex/skills/taskmaster/install.sh
TASKMASTER_INSTALL_TARGET=both bash ~/.codex/skills/taskmaster/install.sh
```

Installed artifacts:
- Codex:
  - `~/.codex/skills/taskmaster/`
  - `~/.codex/bin/codex-taskmaster`
  - `~/.codex/bin/codex` (shim to Taskmaster wrapper)
- Claude:
  - `~/.claude/skills/taskmaster/`
  - `~/.claude/hooks/taskmaster-check-completion.sh`
  - Stop-hook entry added to `~

## Links

- Repository: https://github.com/blader/taskmaster
