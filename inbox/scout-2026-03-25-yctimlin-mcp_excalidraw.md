---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 80
  scoring_breakdown:
    stars: 27
    recency: 20
    docs: 20
    community: 13
github_data:
  full_name: "yctimlin/mcp_excalidraw"
  url: "https://github.com/yctimlin/mcp_excalidraw"
  description: "MCP server and Claude Code skill for Excalidraw — programmatic canvas toolkit to create, edit, and export diagrams via AI agents with real-time canvas sync."
  stars: 1540
  forks: 143
  open_issues: 26
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-03-06"
  created: "2025-03-16"
  topics: []
---

# yctimlin/mcp_excalidraw

> Discovered by arsenal scout — awaiting manual triage

## Description

MCP server and Claude Code skill for Excalidraw — programmatic canvas toolkit to create, edit, and export diagrams via AI agents with real-time canvas sync.

## README Excerpt

# Excalidraw MCP Server & Agent Skill

[![CI](https://github.com/yctimlin/mcp_excalidraw/actions/workflows/ci.yml/badge.svg)](https://github.com/yctimlin/mcp_excalidraw/actions/workflows/ci.yml)
[![Docker Build & Push](https://github.com/yctimlin/mcp_excalidraw/actions/workflows/docker.yml/badge.svg)](https://github.com/yctimlin/mcp_excalidraw/actions/workflows/docker.yml)
[![NPM Version](https://img.shields.io/npm/v/mcp-excalidraw-server)](https://www.npmjs.com/package/mcp-excalidraw-server)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Run a live Excalidraw canvas and control it from AI agents. This repo provides:

- **MCP Server**: Connect via Model Context Protocol (Claude Desktop, Cursor, Codex CLI, etc.)
- **Agent Skill**: Portable skill for Claude Code, Codex CLI, and other skill-enabled agents

Keywords: Excalidraw agent skill, Excalidraw MCP server, AI diagramming, Claude Code skill, Codex CLI skill, Claude Desktop MCP, Cursor MCP, Mermaid to Excalidraw.

## Demo

![MCP Excalidraw Demo](demo.gif)

*AI agent creates a complete architecture diagram from a single prompt (4x speed). [Watch full video on YouTube](https://youtu.be/ufW78Amq5qA)*

## Table of Contents

- [Demo](#demo)
- [What It Is](#what-it-is)
- [How We Differ from the Official Excalidraw MCP](#how-we-differ-from-the-official-excalidraw-mcp)
- [What's New](#whats-new)
- [Quick Start (Local)](#quick-start-local)
- [Quick Start (Docker)](#quick-start-docker)
- [Configure MCP Clients](#configure-mcp-clients)
  - [Claude Desktop](#claude-desktop)
  - [Claude Code](#claude-code)
  - [Cursor](#cursor)
  - [Codex CLI](#codex-cli)
  - [OpenCode](#opencode)
  - [Antigravity (Google)](#antigravity-google)
- [Agent Skill (Optional)](#agent-skill-optional)
- [MCP Tools (26 Total)](#mcp-tools-26-total)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Known Issues / TODO](#known-issues--todo)
- [Development](#development)

## What It Is

This repo contains two separate processes:

- Canvas server: web UI + REST API + WebSocket updates (default `http://localhost:3000`)
- MCP server: exposes MCP tools over stdio; syncs to the canvas via `EXPRESS_SERVER_URL`

## How We Differ from the Official Excalidraw MCP

Excalidraw now has an [official MCP](https://github.com/excalidraw/excalidraw-mcp) — it's great for quick, prompt-to-diagram generation rendered inline in chat. We solve a different problem.

| | Official Excalidraw MCP | This Project |
|---|---|---|
| **Approach** | Prompt in, diagram out (one-shot) | Programmatic element-level control (26 tools) |
| **State** | Stateless — each call is independent | Persistent live canvas with real-time sync |
| **Element CRUD** | No | Full create / read / update / delete per element |
| **AI sees the canvas** | No | `describe_scene` (structured text) + `get_canvas_screenshot` (image) |
| **Iterative refinement** | No — regenerate the whole diagram | Draw → look → adjust → look again, element by element |
| **La

## Links

- Repository: https://github.com/yctimlin/mcp_excalidraw
