---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code hook"
  quality_score: 67
  scoring_breakdown:
    stars: 21
    recency: 15
    docs: 20
    community: 11
github_data:
  full_name: "karanb192/claude-code-hooks"
  url: "https://github.com/karanb192/claude-code-hooks"
  description: "🪝 A growing collection of useful Claude Code hooks. Copy, paste, customize."
  stars: 299
  forks: 18
  open_issues: 3
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-01-26"
  created: "2026-01-24"
  topics: ["ai-tools", "anthropic", "automation", "claude", "claude-code", "claude-code-hooks", "cli", "developer-tools", "hooks", "notifications", "security"]
---

# karanb192/claude-code-hooks

> Discovered by arsenal scout — awaiting manual triage

## Description

🪝 A growing collection of useful Claude Code hooks. Copy, paste, customize.

## README Excerpt

# claude-code-hooks

🪝 Ready-to-use hooks for Claude Code — safety, automation, notifications, and more.

[![GitHub stars](https://img.shields.io/github/stars/karanb192/claude-code-hooks?style=social)](https://github.com/karanb192/claude-code-hooks)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://img.shields.io/badge/tests-262%20passing-brightgreen)](hook-scripts/tests)

### 🎬 Quick Demo

<table>
  <tr>
    <th align="center">Protecting Secrets</th>
    <th align="center">Blocking Dangerous Commands</th>
  </tr>
  <tr>
    <td valign="bottom" align="center"><img src="assets/block-secrets.png" alt="Hook blocking .env read" width="400"></td>
    <td valign="bottom" align="center"><img src="assets/block-dangerous-commands.png" alt="Hook blocking dangerous commands" width="400"></td>
  </tr>
</table>

A growing collection of tested, documented hooks you can copy, paste, and customize.

---

## 📑 Table of Contents

- [Hooks](#-hooks)
- [Quick Start](#-quick-start)
- [Safety Levels](#-safety-levels)
- [Testing](#-testing)
- [Contributing](#-contributing)

---

## 🪝 Hooks

### Pre-Tool-Use

Runs **before** Claude executes a tool. Can block or modify the operation.

| Hook | Matcher | Description |
|------|---------|-------------|
| [block-dangerous-commands](hook-scripts/pre-tool-use/block-dangerous-commands.js) | `Bash` | Blocks dangerous shell commands (rm -rf ~, fork bombs, curl\|sh) |
| [protect-secrets](hook-scripts/pre-tool-use/protect-secrets.js) | `Read\|Edit\|Write\|Bash` | Prevents reading/modifying/exfiltrating sensitive files |

### Post-Tool-Use

Runs **after** Claude executes a tool. Can react to results.

| Hook | Matcher | Description |
|------|---------|-------------|
| [auto-stage](hook-scripts/post-tool-use/auto-stage.js) | `Edit\|Write` | Automatically git stages files after Claude modifies them |

### Notification

Fires when Claude needs user attention.

| Hook | Matcher | Description |
|------|---------|-------------|
| [notify-permission](hook-scripts/notification/notify-permission.js) | `permission_prompt\|idle_prompt` | Sends Slack alerts when Claude needs input |

### Utils

Tools to help you build and debug hooks.

| Tool | Language | Description |
|------|----------|-------------|
| [event-logger](hook-scripts/utils/event-logger.py) | Python | Logs all hook events to inspect payload structures |

> 💡 **Building a new hook?** Use `event-logger.py` to discover what data Claude Code provides for each event before writing your own hooks.

---

## 🚀 Quick Start

**1. Copy the hook script:**
```bash
mkdir -p ~/.claude/hooks
cp hook-scripts/pre-tool-use/block-dangerous-commands.js ~/.claude/hooks/
```

**2. Add to `.claude/settings.json`:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "node ~/.claude/hooks/block-dangerous-commands.js"
    

## Links

- Repository: https://github.com/karanb192/claude-code-hooks
