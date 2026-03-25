---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 81
  scoring_breakdown:
    stars: 30
    recency: 20
    docs: 20
    community: 11
github_data:
  full_name: "modelcontextprotocol/java-sdk"
  url: "https://github.com/modelcontextprotocol/java-sdk"
  description: "The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI"
  stars: 3304
  forks: 844
  open_issues: 271
  language: "Java"
  license: "MIT"
  last_push: "2026-03-13"
  created: "2025-01-20"
  topics: []
---

# modelcontextprotocol/java-sdk

> Discovered by arsenal scout — awaiting manual triage

## Description

The official Java SDK for Model Context Protocol servers and clients. Maintained in collaboration with Spring AI

## README Excerpt

# MCP Java SDK
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/license/MIT)
[![Build Status](https://github.com/modelcontextprotocol/java-sdk/actions/workflows/publish-snapshot.yml/badge.svg)](https://github.com/modelcontextprotocol/java-sdk/actions/workflows/publish-snapshot.yml)
[![Maven Central](https://img.shields.io/maven-central/v/io.modelcontextprotocol.sdk/mcp.svg?label=Maven%20Central)](https://central.sonatype.com/artifact/io.modelcontextprotocol.sdk/mcp)
[![Java Version](https://img.shields.io/badge/Java-17%2B-orange)](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html)


A set of projects that provide Java SDK integration for the [Model Context Protocol](https://modelcontextprotocol.io/docs/concepts/architecture). 
This SDK enables Java applications to interact with AI models and tools through a standardized interface, supporting both synchronous and asynchronous communication patterns.

## 📚 Reference Documentation 

#### MCP Java SDK documentation
For comprehensive guides and SDK API documentation

- [Features](https://modelcontextprotocol.github.io/java-sdk/#features) - Overview the features provided by the Java MCP SDK
- [Architecture](https://modelcontextprotocol.github.io/java-sdk/#architecture) - Java MCP SDK architecture overview.
- [Java Dependencies / BOM](https://modelcontextprotocol.github.io/java-sdk/quickstart/#dependencies) - Java dependencies and BOM.
- [Java MCP Client](https://modelcontextprotocol.github.io/java-sdk/client/) - Learn how to use the MCP client to interact with MCP servers.
- [Java MCP Server](https://modelcontextprotocol.github.io/java-sdk/server/) - Learn how to implement and configure a MCP servers.

#### Spring AI MCP documentation
[Spring AI MCP](https://docs.spring.io/spring-ai/reference/2.0-SNAPSHOT/api/mcp/mcp-overview.html) extends the MCP Java SDK with Spring Boot integration, providing both [client](https://docs.spring.io/spring-ai/reference/2.0-SNAPSHOT/api/mcp/mcp-client-boot-starter-docs.html) and [server](https://docs.spring.io/spring-ai/reference/2.0-SNAPSHOT/api/mcp/mcp-server-boot-starter-docs.html) starters. 
The [MCP Annotations](https://docs.spring.io/spring-ai/reference/2.0-SNAPSHOT/api/mcp/mcp-annotations-overview.html) - provides annotation-based method handling for MCP servers and clients in Java.
The [MCP Security](https://docs.spring.io/spring-ai/reference/2.0-SNAPSHOT/api/mcp/mcp-security.html) - provides comprehensive OAuth 2.0 and API key-based security support for Model Context Protocol implementations in Spring AI.
Bootstrap your AI applications with MCP support using [Spring Initializer](https://start.spring.io).

## Development

### Building from Source

```bash
./mvnw clean install -DskipTests
```

### Running Tests

To run the tests you have to pre-install `Docker` and `npx`.

```bash
./mvnw test
```

## Contributing

Contributions are welcome!
Please follow the [Contributing Guidelines](CONTRIBUTING.md)

## Links

- Repository: https://github.com/modelcontextprotocol/java-sdk
- Homepage: https://java.sdk.modelcontextprotocol.io/latest/
