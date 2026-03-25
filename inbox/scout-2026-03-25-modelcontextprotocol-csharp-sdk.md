---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 82
  scoring_breakdown:
    stars: 31
    recency: 25
    docs: 15
    community: 11
github_data:
  full_name: "modelcontextprotocol/csharp-sdk"
  url: "https://github.com/modelcontextprotocol/csharp-sdk"
  description: "The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft."
  stars: 4131
  forks: 664
  open_issues: 149
  language: "C#"
  license: "NOASSERTION"
  last_push: "2026-03-25"
  created: "2025-03-10"
  topics: []
---

# modelcontextprotocol/csharp-sdk

> Discovered by arsenal scout — awaiting manual triage

## Description

The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft.

## README Excerpt

# MCP C# SDK

[![NuGet version](https://img.shields.io/nuget/v/ModelContextProtocol.svg)](https://www.nuget.org/packages/ModelContextProtocol)

The official C# SDK for the [Model Context Protocol](https://modelcontextprotocol.io/), enabling .NET applications, services, and libraries to implement and interact with MCP clients and servers. Please visit the [API documentation](https://csharp.sdk.modelcontextprotocol.io/api/ModelContextProtocol.html) for more details on available functionality.

## Packages

This SDK consists of three main packages:

- **[ModelContextProtocol.Core](https://www.nuget.org/packages/ModelContextProtocol.Core)** [![NuGet version](https://img.shields.io/nuget/v/ModelContextProtocol.Core.svg)](https://www.nuget.org/packages/ModelContextProtocol.Core) - For projects that only need to use the client or low-level server APIs and want the minimum number of dependencies.

- **[ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)** [![NuGet version](https://img.shields.io/nuget/v/ModelContextProtocol.svg)](https://www.nuget.org/packages/ModelContextProtocol) - The main package with hosting and dependency injection extensions. References `ModelContextProtocol.Core`. This is the right fit for most projects that don't need HTTP server capabilities.

- **[ModelContextProtocol.AspNetCore](https://www.nuget.org/packages/ModelContextProtocol.AspNetCore)** [![NuGet version](https://img.shields.io/nuget/v/ModelContextProtocol.AspNetCore.svg)](https://www.nuget.org/packages/ModelContextProtocol.AspNetCore) - The library for HTTP-based MCP servers. References `ModelContextProtocol`.

## Getting Started

To get started, see the [Getting Started](https://csharp.sdk.modelcontextprotocol.io/concepts/getting-started.html) guide in the conceptual documentation for installation instructions, package-selection guidance, and complete examples for both clients and servers.

You can also browse the [samples](samples) directory and the [API documentation](https://csharp.sdk.modelcontextprotocol.io/api/ModelContextProtocol.html) for more details on available functionality.

## About MCP

The Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context to Large Language Models (LLMs). It enables secure integration between LLMs and various data sources and tools.

For more information about MCP:

- [Official MCP Documentation](https://modelcontextprotocol.io/)
- [MCP C# SDK Documentation](https://csharp.sdk.modelcontextprotocol.io/)
- [Protocol Specification](https://modelcontextprotocol.io/specification/)
- [GitHub Organization](https://github.com/modelcontextprotocol)

## License

This project is licensed under the [Apache License 2.0](LICENSE).


## Links

- Repository: https://github.com/modelcontextprotocol/csharp-sdk
- Homepage: https://modelcontextprotocol.github.io/csharp-sdk/
