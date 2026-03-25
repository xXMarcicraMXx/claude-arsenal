---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "anthropic mcp server"
  quality_score: 88
  scoring_breakdown:
    stars: 29
    recency: 25
    docs: 20
    community: 14
github_data:
  full_name: "bytebase/dbhub"
  url: "https://github.com/bytebase/dbhub"
  description: "Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Server, MariaDB, SQLite."
  stars: 2409
  forks: 194
  open_issues: 8
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-24"
  created: "2025-03-09"
  topics: ["agents", "ai", "anthropic", "claude", "claude-ai", "codex", "cursor", "database", "dify", "llm", "mariadb", "mcp", "mcp-server", "mssql", "mysql", "postgres", "postgresql", "sql", "sqlite", "sqlserver"]
---

# bytebase/dbhub

> Discovered by arsenal scout — awaiting manual triage

## Description

Zero-dependency, token-efficient database MCP server for Postgres, MySQL, SQL Server, MariaDB, SQLite.

## README Excerpt

> [!NOTE]  
> Brought to you by [Bytebase](https://www.bytebase.com/), open-source database DevSecOps platform.

<p align="center">
<a href="https://dbhub.ai/" target="_blank">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/bytebase/dbhub/main/docs/images/logo/full-dark.svg" width="75%">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/bytebase/dbhub/main/docs/images/logo/full-light.svg" width="75%">
  <img src="https://raw.githubusercontent.com/bytebase/dbhub/main/docs/images/logo/full-light.svg" width="75%" alt="DBHub Logo">
</picture>
</a>
</p>

```bash
            +------------------+    +--------------+    +------------------+
            |                  |    |              |    |                  |
            |                  |    |              |    |                  |
            |  Claude Desktop  +--->+              +--->+    PostgreSQL    |
            |                  |    |              |    |                  |
            |  Claude Code     +--->+              +--->+    SQL Server    |
            |                  |    |              |    |                  |
            |  Cursor          +--->+    DBHub     +--->+    SQLite        |
            |                  |    |              |    |                  |
            |  VS Code         +--->+              +--->+    MySQL         |
            |                  |    |              |    |                  |
            |  Copilot CLI     +--->+              +--->+    MariaDB       |
            |                  |    |              |    |                  |
            |                  |    |              |    |                  |
            +------------------+    +--------------+    +------------------+
                 MCP Clients           MCP Server             Databases
```

DBHub is a zero-dependency, token efficient MCP server implementing the Model Context Protocol (MCP) server interface. This lightweight gateway allows MCP-compatible clients to connect to and explore different databases:

- **Local Development First**: Zero dependency, token efficient with just two MCP tools to maximize context window
- **Multi-Database**: PostgreSQL, MySQL, MariaDB, SQL Server, and SQLite through a single interface
- **Multi-Connection**: Connect to multiple databases simultaneously with TOML configuration
- **Guardrails**: Read-only mode, row limiting, and query timeout to prevent runaway operations
- **Secure Access**: SSH tunneling and SSL/TLS encryption

## Supported Databases

PostgreSQL, MySQL, SQL Server, MariaDB, and SQLite.

## MCP Tools

DBHub implements MCP tools for database operations:

- **[execute_sql](https://dbhub.ai/tools/execute-sql)**: Execute SQL queries with transaction support and safety controls
- **[search_objects](https://dbhub.ai/tools/search-objects)**: Search and explore database schemas, tables, columns, indexes, and procedures with progressive dis

## Links

- Repository: https://github.com/bytebase/dbhub
- Homepage: https://dbhub.ai
