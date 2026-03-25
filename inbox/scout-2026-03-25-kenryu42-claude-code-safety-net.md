---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code hook"
  quality_score: 83
  scoring_breakdown:
    stars: 26
    recency: 25
    docs: 20
    community: 12
github_data:
  full_name: "kenryu42/claude-code-safety-net"
  url: "https://github.com/kenryu42/claude-code-safety-net"
  description: "A coding agent hook that acts as a safety net, catching destructive git and filesystem commands before they execute."
  stars: 1186
  forks: 53
  open_issues: 1
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2025-12-25"
  topics: ["claude", "claude-code", "claude-code-plugin", "destructive-commands", "hook", "security"]
---

# kenryu42/claude-code-safety-net

> Discovered by arsenal scout — awaiting manual triage

## Description

A coding agent hook that acts as a safety net, catching destructive git and filesystem commands before they execute.

## README Excerpt

# Claude Code Safety Net

[![CI](https://github.com/kenryu42/claude-code-safety-net/actions/workflows/ci.yml/badge.svg)](https://github.com/kenryu42/claude-code-safety-net/actions/workflows/ci.yml)
[![codecov](https://codecov.io/github/kenryu42/claude-code-safety-net/branch/main/graph/badge.svg?token=C9QTION6ZF)](https://codecov.io/github/kenryu42/claude-code-safety-net)
[![Version](https://img.shields.io/github/v/tag/kenryu42/claude-code-safety-net?label=version&color=blue)](https://github.com/kenryu42/claude-code-safety-net)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-D27656)](#claude-code-installation)
[![OpenCode](https://img.shields.io/badge/OpenCode-black)](#opencode-installation)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-678AE3)](#gemini-cli-installation)
[![Copilot CLI](https://img.shields.io/badge/Copilot%20CLI-4EA5C9)](#github-copilot-cli-installation)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)

<div align="center">

[![CC Safety Net](./.github/assets/cc-safety-net.png)](./.github/assets/cc-safety-net.png)

</div>

A Claude Code plugin that acts as a safety net, catching destructive git and filesystem commands before they execute.

## Contents

- [Why This Exists](#why-this-exists)
- [Why Use This Instead of Permission Deny Rules?](#why-use-this-instead-of-permission-deny-rules)
- [What About Sandboxing?](#what-about-sandboxing)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
  - [Claude Code Installation](#claude-code-installation)
  - [OpenCode Installation](#opencode-installation)
  - [Gemini CLI Installation](#gemini-cli-installation)
  - [GitHub Copilot CLI Installation](#github-copilot-cli-installation)
- [Status Line Integration](#status-line-integration)
  - [Setup via Slash Command](#setup-via-slash-command)
  - [Manual Setup](#manual-setup)
  - [Emoji Mode Indicators](#emoji-mode-indicators)
- [Diagnostics](#diagnostics)
- [Explain (Debug Analysis)](#explain-debug-analysis)
- [Commands Blocked](#commands-blocked)
- [Commands Allowed](#commands-allowed)
- [What Happens When Blocked](#what-happens-when-blocked)
- [Testing the Hook](#testing-the-hook)
- [Development](#development)
- [Custom Rules (Experimental)](#custom-rules-experimental)
  - [Config File Location](#config-file-location)
  - [Rule Schema](#rule-schema)
  - [Matching Behavior](#matching-behavior)
  - [Examples](#examples)
  - [Error Handling](#error-handling)
- [Advanced Features](#advanced-features)
  - [Strict Mode](#strict-mode)
  - [Paranoid Mode](#paranoid-mode)
  - [Shell Wrapper Detection](#shell-wrapper-detection)
  - [Interpreter One-Liner Detection](#interpreter-one-liner-detection)
  - [Secret Redaction](#secret-redaction)
  - [Audit Logging](#audit-logging)
- [License](#license)

## Why This Exists

We learned the [hard way](https://www.reddit.com/r/ClaudeAI/comments/1pgxckk/claude_cli_deleted_my_entire_home_directory_wiped/) that instructions a

## Links

- Repository: https://github.com/kenryu42/claude-code-safety-net
