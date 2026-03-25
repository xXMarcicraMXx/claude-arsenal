---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 72
  scoring_breakdown:
    stars: 21
    recency: 20
    docs: 20
    community: 11
github_data:
  full_name: "laraben/laravel-claude-code-setup"
  url: "https://github.com/laraben/laravel-claude-code-setup"
  description: "One-command setup for AI-powered Laravel development with Claude Code and MCP servers"
  stars: 279
  forks: 26
  open_issues: 4
  language: "Shell"
  license: "MIT"
  last_push: "2026-03-05"
  created: "2025-07-02"
  topics: []
---

# laraben/laravel-claude-code-setup

> Discovered by arsenal scout — awaiting manual triage

## Description

One-command setup for AI-powered Laravel development with Claude Code and MCP servers

## README Excerpt

# Laravel Claude Code Setup 🚀

**One-command setup** for Claude Code with Laravel development. Automatically configures all MCP servers for the ultimate AI-powered Laravel development experience with **Figma integration**.

## 🎯 What This Does

Installs and configures Claude Code with a complete development ecosystem:

### 🌐 Global MCP Servers (shared across all projects)
- ✅ **GitHub integration** - Access all your repositories, manage PRs (with automatic token configuration!)
- ✅ **GitLab integration** - Access all your repositories, manage MRs, issues, and projects (with automatic token configuration!)
- ✅ **Memory system** - Remember decisions across all projects
- ✅ **Context7** - Latest Laravel/PHP documentation access
- ✅ **Web fetch** - Access external APIs and resources
- ✅ **Figma integration** - Design-to-code workflows with automatic design token extraction

### 📁 Project-Specific MCP Servers
- ✅ **Filesystem access** - Read/write your specific Laravel project files
- ✅ **Database integration** - Direct access to your project's database
- ✅ **Laravel DebugBar** - Real-time debugging (if installed)

### 🎨 **NEW: Figma Design Integration**
- **Design-to-code workflows** - Convert Figma designs directly to Laravel/Livewire components
- **Automatic design token extraction** - Colors, typography, and spacing for Tailwind CSS
- **Component specifications** - Get precise implementation details from Figma designs
- **Seamless integration** - Works with your existing Laravel + Livewire + Filament + Tailwind stack

The installer intelligently sets up global servers once and adds project-specific servers for each Laravel project.

## 🚀 Quick Install

### Option 1: Direct Installation (Recommended)

Run this single command from your Laravel project root:

```bash
curl -fsSL https://raw.githubusercontent.com/laraben/laravel-claude-code-setup/main/install.sh | bash
```

### Option 2: With Tokens Pre-configured

If you want to skip the interactive prompts:

```bash
export GITHUB_TOKEN="your_github_personal_access_token"
export GITLAB_TOKEN="your_gitlab_personal_access_token"
export FIGMA_ACCESS_TOKEN="your_figma_access_token"
curl -fsSL https://raw.githubusercontent.com/laraben/laravel-claude-code-setup/main/install.sh | bash
```

### Option 3: Download and Run

For more control or if you prefer to review the script first:

```bash
# Download the script
curl -fsSL https://raw.githubusercontent.com/laraben/laravel-claude-code-setup/main/install.sh -o setup.sh

# Make it executable
chmod +x setup.sh

# Run it
./setup.sh
```

## 📋 Prerequisites

Before running the installer, make sure you have:

1. **Claude Code** installed ([Download here](https://claude.ai/code))
2. **Node.js & npm** installed
3. **Go 1.22+** installed (for database MCP server)
4. **A Laravel project** with `.env` file configured
5. **GitHub Personal Access Token** (the installer will guide you)
6. **GitLab Personal Access Token** (optional, for GitLab integration)
7. **Figma Persona

## Links

- Repository: https://github.com/laraben/laravel-claude-code-setup
