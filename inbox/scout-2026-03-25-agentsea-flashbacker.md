---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code agent subagent"
  quality_score: 56
  scoring_breakdown:
    stars: 15
    recency: 15
    docs: 20
    community: 6
github_data:
  full_name: "agentsea/flashbacker"
  url: "https://github.com/agentsea/flashbacker"
  description: "Claude Code state management with session continuity and AI personas, subagents and agent discussion"
  stars: 55
  forks: 6
  open_issues: 3
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-01-14"
  created: "2025-08-06"
  topics: []
---

# agentsea/flashbacker

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Code state management with session continuity and AI personas, subagents and agent discussion

## README Excerpt

```
███████╗██╗      █████╗ ███████╗██╗  ██╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║     ██╔══██╗██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
█████╗  ██║     ███████║███████╗███████║██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══╝  ██║     ██╔══██║╚════██║██╔══██║██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║     ███████╗██║  ██║███████║██║  ██║██████╔╝██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                          
         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
       ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
     ░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░
   ░░▒▒▓▓██████████████████████████████████████████████████████████████████▓▓▒▒░░
 ░░▒▒▓▓████  M E M O R I E S   F L O A T I N G   B A C K   I N   T I M E  ████▓▓▒▒░░
   ░░▒▒▓▓██████████████████████████████████████████████████████████████████▓▓▒▒░░
     ░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░
       ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
         ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```

> **Claude Code state management with session continuity and AI personas**

**Flashbacker provides:** 

1) Session continuity for Claude Code through intelligent state management memory commands
2) Specialized AI personas accessed via `/fb:` slash commands
3) Dedicated agents accessed via @agent-{AGENT-NAME} commands
4) Agent discussion system for complex issues
5) A code task management system for complex issues
6) A code quality and fix system for complex issues

**Current Status: v2.4.1** - 🚧 **ALPHA** - Complete workflow system with 20 total specialists. PM2 daemon foundation with per-project ecosystem generation and CLI management. Status line: robust model detection, stateful output, JSONL fallback, session-aware cache, and repository-root state persistence. Restored `/fb:create-issue` command for comprehensive issue documentation.

## 🚀 Quick Start

### Prerequisites

- **Node.js**: 18.x, 20.x, or 22.x LTS (recommended: 22.x)
- **npm**: 9.x or later

#### Quick Prerequisites Installation
```bash
# Option 1: Use our automated installer script
npm run setup:prereqs

# Option 2: Manual nvm installation (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
nvm install 22
nvm use 22

# Option 3: Download from https://nodejs.org/ (LTS version)
```

### Quick Installation

**Option 1: NPM Package (RECOMMENDED)**
```bash
# Install globally from npm registry
npm install -g flashbacker

# Initialize in your project with MCP servers
cd /path/to/your/project
flashback init --mcp              # Includes context7, playwright, sequential-thinking
```

**Option 2: Automated Insta

## Links

- Repository: https://github.com/agentsea/flashbacker
