---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 72
  scoring_breakdown:
    stars: 17
    recency: 25
    docs: 20
    community: 10
github_data:
  full_name: "agent-sh/agnix"
  url: "https://github.com/agent-sh/agnix"
  description: "The missing linter and lsp for AI coding assistants. Validate CLAUDE.md, AGENTS.md, SKILL.md, hooks, MCP. Plugin for all major IDEs included, with autofixes."
  stars: 105
  forks: 11
  open_issues: 0
  language: "Rust"
  license: "Apache-2.0"
  last_push: "2026-03-23"
  created: "2026-01-30"
  topics: ["agent", "ai", "ai-agents", "ai-coding-assistant", "claude", "cli", "code-quality", "codex", "copilot", "cursor", "devtools", "linter", "llm", "lsp", "mcp", "opencode", "rust", "skills", "vscode", "vscode-extension"]
---

# agent-sh/agnix

> Discovered by arsenal scout — awaiting manual triage

## Description

The missing linter and lsp for AI coding assistants. Validate CLAUDE.md, AGENTS.md, SKILL.md, hooks, MCP. Plugin for all major IDEs included, with autofixes.

## README Excerpt

<div align="center">
  <img src="editors/vscode/icon.png" alt="agnix" width="128">
  <h1>agnix</h1>
  <p><strong>Lint agent configurations before they break your workflow</strong></p>
  <p>
    <a href="https://www.npmjs.com/package/agnix"><img src="https://img.shields.io/npm/v/agnix.svg?color=3C873A" alt="npm"></a>
    <a href="https://crates.io/crates/agnix-cli"><img src="https://img.shields.io/crates/v/agnix-cli.svg?color=E57324" alt="Crates.io"></a>
    <a href="https://github.com/agent-sh/agnix/releases"><img src="https://img.shields.io/github/v/release/agent-sh/agnix?color=0A7E8C" alt="Release"></a>
    <a href="https://github.com/agent-sh/agnix/actions/workflows/ci.yml"><img src="https://github.com/agent-sh/agnix/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
    <a href="LICENSE-MIT"><img src="https://img.shields.io/badge/license-MIT%2FApache--2.0-64748B.svg" alt="License"></a>
  </p>
</div>

<p align="center">Catch broken agent configs before your AI tools silently ignore them.<br>342 rules across Claude Code, Codex CLI, OpenCode, Cursor, Copilot, and more -<br>validating CLAUDE.md, SKILL.md, hooks, MCP configs, and other agent files.</p>

<p align="center"><strong>Auto-fix</strong> | <strong><a href="https://github.com/marketplace/actions/agnix-ci">GitHub Action</a></strong> | <strong><a href="https://marketplace.visualstudio.com/items?itemName=avifenesh.agnix">VS Code</a> + <a href="https://plugins.jetbrains.com/plugin/30087-agnix">JetBrains</a> + <a href="https://github.com/agent-sh/agnix.nvim">Neovim</a> + <a href="https://zed.dev/extensions?query=agnix">Zed</a></strong></p>

<p align="center">
  <a href="https://agent-sh.github.io/agnix/"><img src="https://img.shields.io/badge/Docs-Website-2563EB?style=for-the-badge" alt="Website"></a>
  <a href="https://agent-sh.github.io/agnix/playground"><img src="https://img.shields.io/badge/Try_it-Playground-E91E63?style=for-the-badge" alt="Playground"></a>
  <a href="https://dev.to/avifenesh/your-ai-agent-configs-are-probably-broken-and-you-dont-know-it-16n1"><img src="https://img.shields.io/badge/Blog-Post-0A0A0A?style=for-the-badge&logo=dev.to" alt="Blog Post"></a>
</p>

<p align="center"><em>New rules and tool support ship constantly. Follow for real-time updates:</em></p>
<p align="center">
  <a href="https://x.com/avi_fenesh"><img src="https://img.shields.io/badge/Follow-@avi__fenesh-1DA1F2?style=for-the-badge&logo=x&logoColor=white" alt="Follow on X"></a>
</p>

## Why agnix?

**Your skills don't trigger.** Vercel's research found skills [invoke at 0%](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals) without correct syntax. One wrong field and your skill is invisible.

**"Almost right" is the worst outcome.** [66% of developers](https://survey.stackoverflow.co/2025/ai) cite it as their biggest AI frustration. Misconfigured agents produce exactly this.

**Multi-tool stacks fail silently.** Cursor + Claude Code + Copilot each want different formats. A config that 

## Links

- Repository: https://github.com/agent-sh/agnix
