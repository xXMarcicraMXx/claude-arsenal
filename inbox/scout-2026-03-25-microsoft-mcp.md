---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 89
  scoring_breakdown:
    stars: 29
    recency: 25
    docs: 20
    community: 15
github_data:
  full_name: "microsoft/mcp"
  url: "https://github.com/microsoft/mcp"
  description: "Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration"
  stars: 2859
  forks: 434
  open_issues: 269
  language: "C#"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2025-04-09"
  topics: []
---

# microsoft/mcp

> Discovered by arsenal scout — awaiting manual triage

## Description

Catalog of official Microsoft MCP (Model Context Protocol) server implementations for AI-powered data access and tool integration

## README Excerpt

# 🌟 Microsoft MCP Servers


## 📘 What is MCP?

**Model Context Protocol (MCP)** is an open protocol that standardizes how applications provide context to large language models (LLMs). It allows AI applications to connect with various data sources and tools in a consistent manner, enhancing their capabilities and flexibility. MCP follows a client-server architecture:

- **MCP Hosts**: Applications like AI assistants or IDEs that initiate connections.
- **MCP Clients**: Connectors within the host application that maintain 1:1 connections with servers.
- **MCP Servers**: Services that provide context and capabilities through the standardized MCP.

For more details, visit the [official MCP website](https://modelcontextprotocol.io).

## 📁 Which MCP Servers are built from this repository?

This repository contains core libraries, test frameworks, engineering systems, pipelines, and tooling for Microsoft MCP Server contributors to unify engineering investments; and reduce duplication and divergence:

| MCP Server           |  README              | Source Code             |    CHANGELOG          | Releases             | Documentation             | Troubleshooting             | Support             |
|:---------------------|:--------------------:|:-----------------------:|:---------------------:|:--------------------:|:-------------------------:|:---------------------------:|:-------------------:|
| Azure MCP            | [Azure MCP README]   | [Azure MCP Source Code] | [Azure MCP CHANGELOG] | [Azure MCP Releases] | [Azure MCP Documentation] | [Azure MCP Troubleshooting] | [Azure MCP Support] |
| Microsoft Fabric MCP | [Fabric MCP README]  | [Fabric MCP Source Code] | [Fabric MCP CHANGELOG] | [Fabric MCP Releases] | [Fabric Documentation] | [Fabric MCP Troubleshooting] | [Fabric MCP Support] |

[Azure MCP README]: https://github.com/microsoft/mcp/blob/main/servers/Azure.Mcp.Server/README.md
[Azure MCP CHANGELOG]: https://github.com/microsoft/mcp/blob/main/servers/Azure.Mcp.Server/CHANGELOG.md
[Azure MCP Source Code]: https://github.com/microsoft/mcp/blob/main/servers/Azure.Mcp.Server
[Azure MCP Releases]: https://github.com/microsoft/mcp/releases?q=Azure.Mcp.Server-
[Azure MCP Documentation]: https://learn.microsoft.com/azure/developer/azure-mcp-server/
[Azure MCP Troubleshooting]: https://github.com/microsoft/mcp/blob/main/servers/Azure.Mcp.Server/TROUBLESHOOTING.md
[Azure MCP Support]: https://github.com/microsoft/mcp/blob/main/servers/Azure.Mcp.Server/SUPPORT.md

[Fabric MCP README]: https://github.com/microsoft/mcp/blob/main/servers/Fabric.Mcp.Server/README.md
[Fabric MCP CHANGELOG]: https://github.com/microsoft/mcp/blob/main/servers/Fabric.Mcp.Server/CHANGELOG.md
[Fabric MCP Source Code]: https://github.com/microsoft/mcp/blob/main/servers/Fabric.Mcp.Server
[Fabric MCP Releases]: https://github.com/microsoft/mcp/releases?q=Fabric.Mcp.Server-
[Fabric Documentation]: https://learn.microsoft.com/fabric/
[Fabric MCP Troubleshooting]: https://github.com/mic

## Links

- Repository: https://github.com/microsoft/mcp
