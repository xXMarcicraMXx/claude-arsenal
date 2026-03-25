---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 93
  scoring_breakdown:
    stars: 37
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "modelcontextprotocol/python-sdk"
  url: "https://github.com/modelcontextprotocol/python-sdk"
  description: "The official Python SDK for Model Context Protocol servers and clients"
  stars: 22306
  forks: 3207
  open_issues: 367
  language: "Python"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2024-09-24"
  topics: []
---

# modelcontextprotocol/python-sdk

> Discovered by arsenal scout — awaiting manual triage

## Description

The official Python SDK for Model Context Protocol servers and clients

## README Excerpt

# MCP Python SDK

<div align="center">

<strong>Python implementation of the Model Context Protocol (MCP)</strong>

[![PyPI][pypi-badge]][pypi-url]
[![MIT licensed][mit-badge]][mit-url]
[![Python Version][python-badge]][python-url]
[![Documentation][docs-badge]][docs-url]
[![Protocol][protocol-badge]][protocol-url]
[![Specification][spec-badge]][spec-url]

</div>

<!-- TODO(v2): Replace this README with README.v2.md when v2 is released -->

> [!NOTE]
> **This README documents v1.x of the MCP Python SDK (the current stable release).**
>
> For v1.x code and documentation, see the [`v1.x` branch](https://github.com/modelcontextprotocol/python-sdk/tree/v1.x).
> For the upcoming v2 documentation (pre-alpha, in development on `main`), see [`README.v2.md`](README.v2.md).

<!-- omit in toc -->
## Table of Contents

- [MCP Python SDK](#mcp-python-sdk)
  - [Overview](#overview)
  - [Installation](#installation)
    - [Adding MCP to your python project](#adding-mcp-to-your-python-project)
    - [Running the standalone MCP development tools](#running-the-standalone-mcp-development-tools)
  - [Quickstart](#quickstart)
  - [What is MCP?](#what-is-mcp)
  - [Core Concepts](#core-concepts)
    - [Server](#server)
    - [Resources](#resources)
    - [Tools](#tools)
      - [Structured Output](#structured-output)
    - [Prompts](#prompts)
    - [Images](#images)
    - [Context](#context)
      - [Getting Context in Functions](#getting-context-in-functions)
      - [Context Properties and Methods](#context-properties-and-methods)
    - [Completions](#completions)
    - [Elicitation](#elicitation)
    - [Sampling](#sampling)
    - [Logging and Notifications](#logging-and-notifications)
    - [Authentication](#authentication)
    - [FastMCP Properties](#fastmcp-properties)
    - [Session Properties and Methods](#session-properties-and-methods)
    - [Request Context Properties](#request-context-properties)
  - [Running Your Server](#running-your-server)
    - [Development Mode](#development-mode)
    - [Claude Desktop Integration](#claude-desktop-integration)
    - [Direct Execution](#direct-execution)
    - [Streamable HTTP Transport](#streamable-http-transport)
      - [CORS Configuration for Browser-Based Clients](#cors-configuration-for-browser-based-clients)
    - [Mounting to an Existing ASGI Server](#mounting-to-an-existing-asgi-server)
      - [StreamableHTTP servers](#streamablehttp-servers)
        - [Basic mounting](#basic-mounting)
        - [Host-based routing](#host-based-routing)
        - [Multiple servers with path configuration](#multiple-servers-with-path-configuration)
        - [Path configuration at initialization](#path-configuration-at-initialization)
      - [SSE servers](#sse-servers)
  - [Advanced Usage](#advanced-usage)
    - [Low-Level Server](#low-level-server)
      - [Structured Output Support](#structured-output-support)
    - [Pagination (Advanced)](#pagination-advanced)
    - [Writing MCP Clients](#writing-mcp-clients)
    - [Client 

## Links

- Repository: https://github.com/modelcontextprotocol/python-sdk
- Homepage: https://modelcontextprotocol.github.io/python-sdk/
