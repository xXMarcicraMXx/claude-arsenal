---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 91
  scoring_breakdown:
    stars: 35
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "modelcontextprotocol/typescript-sdk"
  url: "https://github.com/modelcontextprotocol/typescript-sdk"
  description: "The official TypeScript SDK for Model Context Protocol servers and clients"
  stars: 11956
  forks: 1703
  open_issues: 362
  language: "TypeScript"
  license: "NOASSERTION"
  last_push: "2026-03-25"
  created: "2024-09-24"
  topics: []
---

# modelcontextprotocol/typescript-sdk

> Discovered by arsenal scout — awaiting manual triage

## Description

The official TypeScript SDK for Model Context Protocol servers and clients

## README Excerpt

# MCP TypeScript SDK

> [!IMPORTANT] **This is the `main` branch which contains v2 of the SDK (currently in development, pre-alpha).**
>
> We anticipate a stable v2 release in Q1 2026. Until then, **v1.x remains the recommended version** for production use. v1.x will continue to receive bug fixes and security updates for at least 6 months after v2 ships to give people time to upgrade.
>
> For v1 documentation, see the [V1 API docs](https://ts.sdk.modelcontextprotocol.io/). For v2 API docs, see [`/v2/`](https://ts.sdk.modelcontextprotocol.io/v2/).

![NPM Version](https://img.shields.io/npm/v/%40modelcontextprotocol%2Fserver) ![NPM Version](https://img.shields.io/npm/v/%40modelcontextprotocol%2Fclient) ![MIT licensed](https://img.shields.io/npm/l/%40modelcontextprotocol%2Fserver)

<details>
<summary>Table of Contents</summary>

- [Overview](#overview)
- [Packages](#packages)
- [Installation](#installation)
- [Quick Start (runnable examples)](#quick-start-runnable-examples)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

</details>

## Overview

The Model Context Protocol (MCP) allows applications to provide context for LLMs in a standardized way, separating the concerns of providing context from the actual LLM interaction.

This repository contains the TypeScript SDK implementation of the MCP specification. It runs on **Node.js**, **Bun**, and **Deno**, and ships:

- MCP **server** libraries (tools/resources/prompts, Streamable HTTP, stdio, auth helpers)
- MCP **client** libraries (transports, high-level helpers, OAuth helpers)
- Optional **middleware packages** for specific runtimes/frameworks (Express, Hono, Node.js HTTP)
- Runnable **examples** (under [`examples/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/examples))

## Packages

This monorepo publishes split packages:

- **`@modelcontextprotocol/server`**: build MCP servers
- **`@modelcontextprotocol/client`**: build MCP clients

Both packages have a **required peer dependency** on `zod` for schema validation. The SDK uses Zod v4.

### Middleware packages (optional)

The SDK also publishes small "middleware" packages under [`packages/middleware/`](https://github.com/modelcontextprotocol/typescript-sdk/tree/main/packages/middleware) that help you **wire MCP into a specific runtime or web framework**.

They are intentionally thin adapters: they should not introduce new MCP functionality or business logic. See [`packages/middleware/README.md`](packages/middleware/README.md) for details.

- **`@modelcontextprotocol/node`**: Node.js Streamable HTTP transport wrapper for `IncomingMessage` / `ServerResponse`
- **`@modelcontextprotocol/express`**: Express helpers (app defaults + Host header validation)
- **`@modelcontextprotocol/hono`**: Hono helpers (app defaults + JSON body parsing hook + Host header validation)

## Installation

### Server

```bash
npm install @modelcontextprotocol/server zod
# or
bun add @modelcontextprotocol/server z

## Links

- Repository: https://github.com/modelcontextprotocol/typescript-sdk
- Homepage: https://modelcontextprotocol.io
