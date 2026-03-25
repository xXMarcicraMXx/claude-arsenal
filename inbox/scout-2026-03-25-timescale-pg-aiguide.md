---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 81
  scoring_breakdown:
    stars: 27
    recency: 25
    docs: 20
    community: 9
github_data:
  full_name: "timescale/pg-aiguide"
  url: "https://github.com/timescale/pg-aiguide"
  description: "MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code."
  stars: 1647
  forks: 83
  open_issues: 15
  language: "Python"
  license: "Apache-2.0"
  last_push: "2026-03-23"
  created: "2025-07-23"
  topics: ["ai", "ai-agents", "ai-coding", "claude-code-plugin", "claude-code-plugins", "claude-code-plugins-marketplace", "claude-marketplace", "claude-plugin", "claude-skills", "docs", "documentation", "mcp", "mcp-server", "postgres", "postgresql", "skills"]
---

# timescale/pg-aiguide

> Discovered by arsenal scout — awaiting manual triage

## Description

MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code.

## README Excerpt

# pg-aiguide

**AI-optimized PostgreSQL expertise for coding assistants**

pg-aiguide helps AI coding tools write dramatically better PostgreSQL code. It provides:

- **Semantic search** across the official PostgreSQL manual (version-aware)
- **AI-optimized “skills”** — curated, opinionated Postgres best practices used automatically by AI agents
- **Extension ecosystem docs**, starting with TimescaleDB, with more coming soon

Use it either as:

- a **public MCP server** that can be used with any AI coding agent, or
- a **Claude Code plugin** optimized for use with Claude's native skill support.

## ⭐ Why pg-aiguide?

AI coding tools often generate Postgres code that is:

- outdated
- missing constraints and indexes
- unaware of modern PG features
- inconsistent with real-world best practices

pg-aiguide fixes that by giving AI agents deep, versioned PostgreSQL knowledge and proven patterns.

### See the difference

https://github.com/user-attachments/assets/5a426381-09b5-4635-9050-f55422253a3d

<details>
<summary>Video Transcript </summary>

Prompt given to Claude Code:

> Please describe the schema you would create for an e-commerce website two times, first with the tiger mcp server disabled, then with the tiger mcp server enabled. For each time, write the schema to its own file in the current working directory. Then compare the two files and let me know which approach generated the better schema, using both qualitative and quantitative reasons. For this example, only use standard Postgres.

Result (summarized):

- **4× more constraints**
- **55% more indexes** (including partial/expression indexes)
- **PG17-recommended patterns**
- **Modern features** (`GENERATED ALWAYS AS IDENTITY`, `NULLS NOT DISTINCT`)
- **Cleaner naming & documentation**

Conclusion: _pg-aiguide produces more robust, performant, maintainable schemas._

</details>

## 🚀 Quickstart

pg-aiguide is available as a **public MCP server**:

[https://mcp.tigerdata.com/docs](https://mcp.tigerdata.com/docs)

<details> 
<summary>Manual MCP configuration using JSON</summary>

```json
{
  "mcpServers": {
    "pg-aiguide": {
      "url": "https://mcp.tigerdata.com/docs"
    }
  }
}
```

</details>

Or it can be used as a **Claude Code Plugin**:

```bash
claude plugin marketplace add timescale/pg-aiguide
claude plugin install pg@aiguide
```

### Install by environment

#### One-click installs

[![Install in Cursor](https://img.shields.io/badge/Install_in-Cursor-000000?style=flat-square&logoColor=white)](https://cursor.com/en/install-mcp?name=pg-aiguide&config=eyJuYW1lIjoicGctYWlndWlkZSIsInR5cGUiOiJodHRwIiwidXJsIjoiaHR0cHM6Ly9tY3AudGlnZXJkYXRhLmNvbS9kb2NzIn0=)
[![Install in VS Code](https://img.shields.io/badge/Install_in-VS_Code-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=pg-aiguide&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.tigerdata.com%2Fdocs%22%7D)
[![Install in VS Code Insiders](https://img.shi

## Links

- Repository: https://github.com/timescale/pg-aiguide
