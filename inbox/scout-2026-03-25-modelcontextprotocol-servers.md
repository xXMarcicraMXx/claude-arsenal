---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 96
  scoring_breakdown:
    stars: 40
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "modelcontextprotocol/servers"
  url: "https://github.com/modelcontextprotocol/servers"
  description: "Model Context Protocol Servers"
  stars: 82032
  forks: 10067
  open_issues: 590
  language: "TypeScript"
  license: "NOASSERTION"
  last_push: "2026-03-17"
  created: "2024-11-19"
  topics: []
---

# modelcontextprotocol/servers

> Discovered by arsenal scout — awaiting manual triage

## Description

Model Context Protocol Servers

## README Excerpt

# Model Context Protocol servers

This repository is a collection of *reference implementations* for the [Model Context Protocol](https://modelcontextprotocol.io/) (MCP), as well as references to community-built servers and additional resources.

> [!IMPORTANT]
> If you are looking for a list of MCP servers, you can browse published servers on [the MCP Registry](https://registry.modelcontextprotocol.io/). The repository served by this README is dedicated to housing just the small number of reference servers maintained by the MCP steering group.

> [!WARNING]
> The servers in this repository are intended as **reference implementations** to demonstrate MCP features and SDK usage. They are meant to serve as educational examples for developers building their own MCP servers, not as production-ready solutions. Developers should evaluate their own security requirements and implement appropriate safeguards based on their specific threat model and use case.

The servers in this repository showcase the versatility and extensibility of MCP, demonstrating how it can be used to give Large Language Models (LLMs) secure, controlled access to tools and data sources.
Typically, each MCP server is implemented with an MCP SDK:

- [C# MCP SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Go MCP SDK](https://github.com/modelcontextprotocol/go-sdk)
- [Java MCP SDK](https://github.com/modelcontextprotocol/java-sdk)
- [Kotlin MCP SDK](https://github.com/modelcontextprotocol/kotlin-sdk)
- [PHP MCP SDK](https://github.com/modelcontextprotocol/php-sdk)
- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Ruby MCP SDK](https://github.com/modelcontextprotocol/ruby-sdk)
- [Rust MCP SDK](https://github.com/modelcontextprotocol/rust-sdk)
- [Swift MCP SDK](https://github.com/modelcontextprotocol/swift-sdk)
- [TypeScript MCP SDK](https://github.com/modelcontextprotocol/typescript-sdk)

## 🌟 Reference Servers

These servers aim to demonstrate MCP features and the official SDKs.

- **[Everything](src/everything)** - Reference / test server with prompts, resources, and tools.
- **[Fetch](src/fetch)** - Web content fetching and conversion for efficient LLM usage.
- **[Filesystem](src/filesystem)** - Secure file operations with configurable access controls.
- **[Git](src/git)** - Tools to read, search, and manipulate Git repositories.
- **[Memory](src/memory)** - Knowledge graph-based persistent memory system.
- **[Sequential Thinking](src/sequentialthinking)** - Dynamic and reflective problem-solving through thought sequences.
- **[Time](src/time)** - Time and timezone conversion capabilities.

### Archived

The following reference servers are now archived and can be found at [servers-archived](https://github.com/modelcontextprotocol/servers-archived).

- **[AWS KB Retrieval](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/aws-kb-retrieval-server)** - Retrieval from AWS Knowledge Base using Bedrock Agent Runtime.
- **[Brave Searc

## Links

- Repository: https://github.com/modelcontextprotocol/servers
- Homepage: https://modelcontextprotocol.io
