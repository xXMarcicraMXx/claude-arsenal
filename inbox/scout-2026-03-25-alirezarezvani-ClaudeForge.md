---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 68
  scoring_breakdown:
    stars: 21
    recency: 15
    docs: 20
    community: 12
github_data:
  full_name: "alirezarezvani/ClaudeForge"
  url: "https://github.com/alirezarezvani/ClaudeForge"
  description: "A CLAUDE.md Generator and Maintenance tool for for Claude Code to create high-quality CLAUDE.md instruction files — aligned with Anthropic’s best practices for Claude Code."
  stars: 324
  forks: 39
  open_issues: 1
  language: "Python"
  license: "MIT"
  last_push: "2026-02-15"
  created: "2025-11-12"
  topics: ["agentic-ai", "agentic-workflow", "claude-code", "claude-skill", "claude-subagents"]
---

# alirezarezvani/ClaudeForge

> Discovered by arsenal scout — awaiting manual triage

## Description

A CLAUDE.md Generator and Maintenance tool for for Claude Code to create high-quality CLAUDE.md instruction files — aligned with Anthropic’s best practices for Claude Code.

## README Excerpt

# ClaudeForge

> **Automated CLAUDE.md creation, enhancement, and maintenance for Claude Code projects**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/alirezarezvani/ClaudeForge/releases)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1.4%2B-purple.svg)](https://claude.com/claude-code)
[![CI/CD](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF.svg)](https://github.com/alirezarezvani/ClaudeForge/actions)
[![Quality Gates](https://img.shields.io/badge/Quality_Gates-Automated-success.svg)](docs/GITHUB_WORKFLOWS.md)

ClaudeForge is a comprehensive toolkit that eliminates the tedious process of manually creating and maintaining CLAUDE.md files. With intelligent analysis, automated generation, and background maintenance, your CLAUDE.md files stay perfectly synchronized with your codebase.

---

## 🆕 New in v2.0 (Claude Code v2.1.4+ Support)

- **Lifecycle Hooks**: Guardian agent automatically checks for updates at session start using SessionStart hooks
- **Modern Permissions**: All components now use `permissions:` syntax for fine-grained control
- **Hot-Reload**: Skills automatically reload when modified (no restart needed)
- **Fork-Safe Mode**: Guardian runs independently with `fork_safe: true` without blocking operations
- **Version Detection**: Installers validate Claude Code version and ensure compatibility
- **Auto-Migration**: Seamless upgrade from v1.x with automatic backups

👉 **Upgrading from v1.x?** See [docs/MIGRATION_V2.md](docs/MIGRATION_V2.md) for migration guide.

---

## ✨ Features

- 🚀 **Interactive Initialization** - Explores your repository, detects project context, and creates customized CLAUDE.md files through conversational workflow
- ✅ **Intelligent Analysis** - Scans and evaluates existing CLAUDE.md files with quality scoring (0-100) and actionable recommendations
- 🔧 **Smart Enhancement** - Adds missing sections and improves structure automatically
- 🛡️ **Background Maintenance** - Guardian agent keeps CLAUDE.md synchronized with codebase changes
- 📦 **Modular Architecture** - Supports complex projects with context-specific files (backend/, frontend/, database/)
- 🎯 **100% Native Format** - All generated files follow official Claude Code format with project structure diagrams, setup instructions, and architecture sections
- 🛠️ **Tech Stack Customization** - Tailors guidelines to TypeScript, Python, Go, React, Vue, FastAPI, and more
- 👥 **Team Size Adaptation** - Adjusts complexity based on team size (solo, small, medium, large)

---

## 📦 What's Included

### 1. **Skill** (`claudeforge-skill`)
Core capability for CLAUDE.md analysis, generation, validation, and enhancement

### 2. **Slash Command** (`/enhance-claude-md`)
Interactive interface with multi-phase discovery workflow

### 3. **Guardian Agent** (`claude-md-guardian`)
Background agent for automatic CLAUD

## Links

- Repository: https://github.com/alirezarezvani/ClaudeForge
