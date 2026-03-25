---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 89
  scoring_breakdown:
    stars: 33
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "modelcontextprotocol/registry"
  url: "https://github.com/modelcontextprotocol/registry"
  description: "A community driven registry service for Model Context Protocol (MCP) servers."
  stars: 6590
  forks: 685
  open_issues: 147
  language: "Go"
  license: "NOASSERTION"
  last_push: "2026-03-23"
  created: "2025-02-05"
  topics: ["mcp", "mcp-servers"]
---

# modelcontextprotocol/registry

> Discovered by arsenal scout — awaiting manual triage

## Description

A community driven registry service for Model Context Protocol (MCP) servers.

## README Excerpt

# MCP Registry

The MCP registry provides MCP clients with a list of MCP servers, like an app store for MCP servers.

[**📤 Publish my MCP server**](docs/modelcontextprotocol-io/quickstart.mdx) | [**⚡️ Live API docs**](https://registry.modelcontextprotocol.io/docs) | [**👀 Ecosystem vision**](docs/design/ecosystem-vision.md) | 📖 **[Full documentation](./docs)**

## Development Status

**2025-10-24 update**: The Registry API has entered an **API freeze (v0.1)** 🎉. For the next month or more, the API will remain stable with no breaking changes, allowing integrators to confidently implement support. This freeze applies to v0.1 while development continues on v0. We'll use this period to validate the API in real-world integrations and gather feedback to shape v1 for general availability. Thank you to everyone for your contributions and patience—your involvement has been key to getting us here!

**2025-09-08 update**: The registry has launched in preview 🎉 ([announcement blog post](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/)). While the system is now more stable, this is still a preview release and breaking changes or data resets may occur. A general availability (GA) release will follow later. We'd love your feedback in [GitHub discussions](https://github.com/modelcontextprotocol/registry/discussions/new?category=ideas) or in the [#registry-dev Discord](https://discord.com/channels/1358869848138059966/1369487942862504016) ([joining details here](https://modelcontextprotocol.io/community/communication)).

Current key maintainers:
- **Adam Jones** (Anthropic) [@domdomegg](https://github.com/domdomegg)  
- **Tadas Antanavicius** (PulseMCP) [@tadasant](https://github.com/tadasant)
- **Toby Padilla** (GitHub) [@toby](https://github.com/toby)
- **Radoslav (Rado) Dimitrov** (Stacklok) [@rdimitrov](https://github.com/rdimitrov)

## Contributing

We use multiple channels for collaboration - see [modelcontextprotocol.io/community/communication](https://modelcontextprotocol.io/community/communication).

Often (but not always) ideas flow through this pipeline:

- **[Discord](https://modelcontextprotocol.io/community/communication)** - Real-time community discussions
- **[Discussions](https://github.com/modelcontextprotocol/registry/discussions)** - Propose and discuss product/technical requirements
- **[Issues](https://github.com/modelcontextprotocol/registry/issues)** - Track well-scoped technical work  
- **[Pull Requests](https://github.com/modelcontextprotocol/registry/pulls)** - Contribute work towards issues

### Quick start:

#### Pre-requisites

- **Docker**
- **Go 1.24.x**
- **ko** - Container image builder for Go ([installation instructions](https://ko.build/install/))
- **golangci-lint v2.4.0**

#### Running the server

```bash
# Start full development environment
make dev-compose
```

This starts the registry at [`localhost:8080`](http://localhost:8080) with PostgreSQL. The database uses ephemeral storage and is reset ea

## Links

- Repository: https://github.com/modelcontextprotocol/registry
- Homepage: https://github.com/modelcontextprotocol/registry/tree/main/docs
