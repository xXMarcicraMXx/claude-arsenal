---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 84
  scoring_breakdown:
    stars: 33
    recency: 20
    docs: 20
    community: 11
github_data:
  full_name: "idosal/git-mcp"
  url: "https://github.com/idosal/git-mcp"
  description: "Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project"
  stars: 7825
  forks: 680
  open_issues: 56
  language: "TypeScript"
  license: "Apache-2.0"
  last_push: "2026-03-13"
  created: "2025-03-29"
  topics: ["agentic-ai", "agents", "ai", "claude", "copilot", "cursor", "git", "llm", "mcp"]
---

# idosal/git-mcp

> Discovered by arsenal scout — awaiting manual triage

## Description

Put an end to code hallucinations! GitMCP is a free, open-source, remote MCP server for any GitHub project

## README Excerpt

# GitMCP

<p align="center">
  <img width="884" alt="image" src="https://github.com/user-attachments/assets/2bf3e3df-556c-49c6-ab7b-36c279d53bba" />
</p>

<p align="center">
  <a href="#-what-is-gitmcp">What is GitMCP</a> •
  <a href="#-features">Features</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-badge">Badge</a> •
  <a href="#-examples">Examples</a> •
  <a href="#-faq">FAQ</a> •
  <a href="#-privacy">Privacy</a> •
  <a href="#-contributing">Contributing</a> •
  <a href="#-license">License</a>
</p>
<div align="center">

[![GitMCP](https://img.shields.io/endpoint?url=https://gitmcp.io/badge/idosal/git-mcp)](https://gitmcp.io/idosal/git-mcp)
[![Twitter Follow](https://img.shields.io/twitter/follow/idosal1?style=social)](https://twitter.com/idosal1)
[![Twitter Follow](https://img.shields.io/twitter/follow/liadyosef?style=social)](https://twitter.com/liadyosef)
</div>

<div align="center">
  <a href="https://www.pulsemcp.com/servers/idosal-git-mcp"><img src="https://www.pulsemcp.com/badge/top-pick/idosal-git-mcp" width="400" alt="Pulse MCP Badge"></a>
</div>

## 🤔 What is GitMCP?
**Stop vibe-hallucinating and start vibe-coding!**

[GitMCP](https://gitmcp.io) is a free, open-source, remote [Model Context Protocol (MCP)](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) server that transforms **any** GitHub project (repositories or GitHub pages) into a documentation hub. It enables AI tools like Cursor to access up-to-date documentation and code, even if the LLM has never encountered them, thereby eliminating code hallucinations seamlessly.

GitMCP supports **two flavors** -

*   **Specific Repository (`gitmcp.io/{owner}/{repo}` or `{owner}.gitmcp.io/{repo}`):** Use these when you primarily work with a select number of libraries. This ensures your AI assistant always targets the correct project, enhancing security and relevance by preventing access to unintended repositories.
*   **Generic Server (`gitmcp.io/docs`):** Use this for maximum flexibility when you need to switch between different repositories frequently. The AI assistant will prompt you (or decide based on context) which repository to access for each request. Be mindful that this relies on correctly identifying the target repository each time.

**With GitMCP:**

*   AI assistants access the *latest* documentation and code directly from the source.
*   Get accurate API usage and reliable code examples.
*   Work effectively even with niche, new, or rapidly changing libraries.
*   Significantly reduced hallucinations and improved code correctness.

For example, this side-by-side comparison shows the result for the same one-shot prompt in Cursor when creating a [three.js](https://github.com/mrdoob/three.js) scene -

https://github.com/user-attachments/assets/fbf1b4a7-f9f0-4c0e-831c-4d64faae2c45

## ✨ Features

- 😎 **Latest Documentation on ANY GitHub Project**: Grant your AI assistant seamless access to the GitHub

## Links

- Repository: https://github.com/idosal/git-mcp
- Homepage: https://gitmcp.io
