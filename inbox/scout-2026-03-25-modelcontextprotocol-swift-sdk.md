---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 82
  scoring_breakdown:
    stars: 27
    recency: 25
    docs: 20
    community: 10
github_data:
  full_name: "modelcontextprotocol/swift-sdk"
  url: "https://github.com/modelcontextprotocol/swift-sdk"
  description: "The official Swift SDK for Model Context Protocol servers and clients."
  stars: 1322
  forks: 175
  open_issues: 49
  language: "Swift"
  license: "NOASSERTION"
  last_push: "2026-03-24"
  created: "2025-02-05"
  topics: ["mcp", "swift"]
---

# modelcontextprotocol/swift-sdk

> Discovered by arsenal scout — awaiting manual triage

## Description

The official Swift SDK for Model Context Protocol servers and clients.

## README Excerpt

# MCP Swift SDK

Official Swift SDK for the [Model Context Protocol][mcp] (MCP).

## Overview

The Model Context Protocol (MCP) defines a standardized way
for applications to communicate with AI and ML models.
This Swift SDK implements both client and server components
according to the [2025-11-25][mcp-spec-2025-11-25] (latest) version
of the MCP specification.

## Table of contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Client Usage](#client-usage)
  - [Basic Client Setup](#basic-client-setup)
  - [Transport Options for Clients](#transport-options-for-clients)
  - [Tools](#tools)
  - [Resources](#resources)
  - [Prompts](#prompts)
  - [Completions](#completions)
  - [Sampling](#sampling)
  - [Elicitation](#elicitation)
  - [Roots](#roots)
  - [Logging](#logging)
  - [Error Handling](#error-handling)
  - [Cancellation](#cancellation)
  - [Progress Tracking](#progress-tracking)
  - [Advanced Client Features](#advanced-client-features)
- [Server Usage](#server-usage)
  - [Basic Server Setup](#basic-server-setup)
  - [Tools](#tools-1)
  - [Resources](#resources-1)
  - [Prompts](#prompts-1)
  - [Completions](#completions-1)
  - [Sampling](#sampling-1)
  - [Elicitations](#elicitations)
  - [Roots](#roots-1)
  - [Logging](#logging-1)
  - [Progress Tracking](#progress-tracking-1)
  - [Initialize Hook](#initialize-hook)
  - [Graceful Shutdown](#graceful-shutdown)
- [Transports](#transports)
- [Authentication](#authentication)
  - [Client: Client Credentials Flow](#client-client-credentials-flow)
  - [Client: Authorization Code Flow](#client-authorization-code-flow)
  - [Client: Custom Token Provider](#client-custom-token-provider)
  - [Client: Custom Token Storage](#client-custom-token-storage)
  - [Client: private\_key\_jwt Authentication](#client-private_key_jwt-authentication)
  - [Client: Endpoint Overrides](#client-endpoint-overrides)
  - [Server: Serving Protected Resource Metadata](#server-serving-protected-resource-metadata)
  - [Server: Validating Bearer Tokens](#server-validating-bearer-tokens)
- [Platform Availability](#platform-availability)
- [Debugging and Logging](#debugging-and-logging)
- [Additional Resources](#additional-resources)
- [Changelog](#changelog)
- [License](#license)

## Requirements

- Swift 6.0+ (Xcode 16+)

See the [Platform Availability](#platform-availability) section below
for platform-specific requirements.

## Installation

### Swift Package Manager

Add the following to your `Package.swift` file:

```swift
dependencies: [
    .package(url: "https://github.com/modelcontextprotocol/swift-sdk.git", from: "0.11.0")
]
```

Then add the dependency to your target:

```swift
.target(
    name: "YourTarget",
    dependencies: [
        .product(name: "MCP", package: "swift-sdk")
    ]
)
```

## Client Usage

The client component allows your application to connect to MCP servers.

### Basic Client Setup

```swift
import MCP

// Initialize the client
let client = Client(name: "MyApp", version: "1.0

## Links

- Repository: https://github.com/modelcontextprotocol/swift-sdk
