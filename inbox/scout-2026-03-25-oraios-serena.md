---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 93
  scoring_breakdown:
    stars: 37
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "oraios/serena"
  url: "https://github.com/oraios/serena"
  description: "A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & other integrations)"
  stars: 22055
  forks: 1475
  open_issues: 93
  language: "Python"
  license: "MIT"
  last_push: "2026-03-24"
  created: "2025-03-23"
  topics: ["agent", "ai", "ai-coding", "claude", "claude-code", "language-server", "llms", "mcp-server", "programming", "vibe-coding"]
---

# oraios/serena

> Discovered by arsenal scout — awaiting manual triage

## Description

A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & other integrations)

## README Excerpt

<p align="center" style="text-align:center">
  <img src="resources/serena-logo.svg#gh-light-mode-only" style="width:500px">
  <img src="resources/serena-logo-dark-mode.svg#gh-dark-mode-only" style="width:500px">
</p>

* :rocket: Serena is a powerful **coding agent toolkit** capable of turning an LLM into a fully-featured agent that works **directly on your codebase**.
  Unlike most other tools, it is not tied to an LLM, framework or an interface, making it easy to use it in a variety of ways.
* :wrench: Serena provides essential **semantic code retrieval and editing tools** that are akin to an IDE's capabilities, extracting code entities at the symbol level and exploiting relational structure. When combined with an existing coding agent, these tools greatly enhance (token) efficiency.
* :free: Serena is **free & open-source**, enhancing the capabilities of LLMs you already have access to free of charge.

You can think of Serena as providing IDE-like tools to your LLM/coding agent. 
With it, the agent no longer needs to read entire files, perform grep-like searches or basic string replacements to find the right parts of the code and to edit code. 
Instead, it can use code-centric tools like `find_symbol`, `find_referencing_symbols` and `insert_after_symbol`.

<p align="center">
  <em>Serena is under active development! See the latest updates, upcoming features, and lessons learned to stay up to date.</em>
</p>

<p align="center">
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/Updates-1e293b?style=flat&logo=rss&logoColor=white&labelColor=1e293b" alt="Changelog" /></a>
  <a href="lessons_learned.md"><img src="https://img.shields.io/badge/Lessons-Learned-7c4700?style=flat&logo=readthedocs&logoColor=white&labelColor=7c4700" alt="Lessons Learned" /></a>
</p>

> [!TIP]
> The [**Serena JetBrains plugin**](#the-serena-jetbrains-plugin) has been released!

## LLM Integration

Serena provides the necessary [tools](https://oraios.github.io/serena/01-about/035_tools.html) for coding workflows, but an LLM is required to do the actual work,
orchestrating tool use.

In general, Serena can be integrated with an LLM in several ways:

* by using the **model context protocol (MCP)**.
  Serena provides an MCP server which integrates with
    * Claude Code and Claude Desktop,
    * terminal-based clients like Codex, Gemini-CLI, Qwen3-Coder, rovodev, OpenHands CLI and others,
    * IDEs like VSCode, Cursor or IntelliJ,
    * Extensions like Cline or Roo Code
    * Local clients like [OpenWebUI](https://docs.openwebui.com/openapi-servers/mcp), [Jan](https://jan.ai/docs/mcp-examples/browser/browserbase#enable-mcp), [Agno](https://docs.agno.com/introduction/playground) and others
* by using [mcpo to connect it to ChatGPT](docs/03-special-guides/serena_on_chatgpt.md) or other clients that don't support MCP but do support tool calling via OpenAPI.
* by incorporating Serena's tools into an agent framework of your choice, as illustrated [here](docs/03-special

## Links

- Repository: https://github.com/oraios/serena
- Homepage: https://oraios.github.io/serena
