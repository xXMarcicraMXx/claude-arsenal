---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "awesome claude code"
  quality_score: 74
  scoring_breakdown:
    stars: 31
    recency: 8
    docs: 20
    community: 15
github_data:
  full_name: "vijaythecoder/awesome-claude-agents"
  url: "https://github.com/vijaythecoder/awesome-claude-agents"
  description: "An orchestrated sub agent dev team powered by claude code"
  stars: 4091
  forks: 480
  open_issues: 28
  language: ""
  license: "MIT"
  last_push: "2025-10-30"
  created: "2025-07-26"
  topics: []
---

# vijaythecoder/awesome-claude-agents

> Discovered by arsenal scout — awaiting manual triage

## Description

An orchestrated sub agent dev team powered by claude code

## README Excerpt

# Awesome Claude Agents - AI Development Team 🚀

**Supercharge Claude Code with a team of specialized AI agents** that work together to build complete features, debug complex issues, and handle any technology stack with expert-level knowledge.

## ⚠️ Important Notice

**This project is experimental and token-intensive.** I'm actively testing these agents with Claude subscription - expect high token consumption during complex workflows. Multi-agent orchestration can consume 10-50k tokens per complex feature. Use with caution and monitor your usage.

## 🚀 Quick Start (3 Minutes)

### Prerequisites
- **Claude Code CLI** installed and authenticated
- **Claude subscription** - required for intensive agent workflows
- Active project directory with your codebase
- **Optional**: [Context7 MCP](docs/dependencies.md) for enhanced documentation access

### 1. Install the Agents
```bash
git clone https://github.com/vijaythecoder/awesome-claude-agents.git
```

#### Option A: Symlink (Recommended - auto-updates)

**macOS/Linux:**
```bash
# Create agents directory if it doesn't exist (preserves existing agents)
mkdir -p ~/.claude/agents

# Symlink the awesome-claude-agents collection
ln -sf "$(pwd)/awesome-claude-agents/agents/" ~/.claude/agents/awesome-claude-agents
```

**Windows (PowerShell):**
```powershell
# Create agents directory
New-Item -Path "$env:USERPROFILE\.claude\agents" -ItemType Directory -Force

# Create symlink
cmd /c mklink /D "$env:USERPROFILE\.claude\agents\awesome-claude-agents" "$(Get-Location)\awesome-claude-agents\agents"
```

#### Option B: Copy (Static - no auto-updates)
```bash
# Create agents directory if it doesn't exist
mkdir -p ~/.claude/agents

# Copy all agents
cp -r awesome-claude-agents/agents ~/.claude/agents/awesome-claude-agents
```

### 2. Verify Installation
```bash
claude /agents
# Should show all 24 agents.
```

### 3. Initialize Your Project
**Navigate** to your **project directory** and run the following command to configure your AI team:

```bash
claude "use @agent-team-configurator and optimize my project to best use the available subagents."
```

### 4. Start Building
```bash
claude "use @agent-tech-lead-orchestrator and build a user authentication system"
```

Your AI team will automatically detect your stack and use the right specialists!

## 🎯 How Auto-Configuration Works

The @agent-team-configurator automatically sets up your perfect AI development team. When invoked, it:

1. **Locates CLAUDE.md** - Finds existing project configuration and preserves all your custom content outside the "AI Team Configuration" section
2. **Detects Technology Stack** - Inspects package.json, composer.json, requirements.txt, go.mod, Gemfile, and build configs to understand your project
3. **Discovers Available Agents** - Scans ~/.claude/agents/ and .claude/ folders, building a capability table of all available specialists
4. **Selects Specialists** - Prefers framework-specific agents over universal ones, always includes @agent-co

## Links

- Repository: https://github.com/vijaythecoder/awesome-claude-agents
- Homepage: https://x.com/vijaytupakula
