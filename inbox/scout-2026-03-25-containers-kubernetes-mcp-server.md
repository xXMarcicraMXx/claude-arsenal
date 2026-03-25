---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 86
  scoring_breakdown:
    stars: 27
    recency: 25
    docs: 20
    community: 14
github_data:
  full_name: "containers/kubernetes-mcp-server"
  url: "https://github.com/containers/kubernetes-mcp-server"
  description: "Model Context Protocol (MCP) server for Kubernetes and OpenShift"
  stars: 1333
  forks: 293
  open_issues: 79
  language: "Go"
  license: "Apache-2.0"
  last_push: "2026-03-25"
  created: "2025-02-11"
  topics: ["containers", "context", "kubernetes", "kubernetes-mcp", "mcp", "model", "modelcontextprotocol", "openshift", "protocol"]
---

# containers/kubernetes-mcp-server

> Discovered by arsenal scout — awaiting manual triage

## Description

Model Context Protocol (MCP) server for Kubernetes and OpenShift

## README Excerpt

# Kubernetes MCP Server

[![GitHub License](https://img.shields.io/github/license/containers/kubernetes-mcp-server)](https://github.com/containers/kubernetes-mcp-server/blob/main/LICENSE)
[![npm](https://img.shields.io/npm/v/kubernetes-mcp-server)](https://www.npmjs.com/package/kubernetes-mcp-server)
[![PyPI - Version](https://img.shields.io/pypi/v/kubernetes-mcp-server)](https://pypi.org/project/kubernetes-mcp-server/)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/containers/kubernetes-mcp-server?sort=semver)](https://github.com/containers/kubernetes-mcp-server/releases/latest)
[![Build](https://github.com/containers/kubernetes-mcp-server/actions/workflows/build.yaml/badge.svg)](https://github.com/containers/kubernetes-mcp-server/actions/workflows/build.yaml)

[✨ Features](#features) | [🚀 Getting Started](#getting-started) | [🎥 Demos](#demos) | [⚙️ Configuration](#configuration) | [🛠️ Tools](#tools-and-functionalities) | [💬 Community](#community) | [🧑‍💻 Development](#development)

https://github.com/user-attachments/assets/be2b67b3-fc1c-4d11-ae46-93deba8ed98e

## ✨ Features <a id="features"></a>

A powerful and flexible Kubernetes [Model Context Protocol (MCP)](https://blog.marcnuri.com/model-context-protocol-mcp-introduction) server implementation with support for **Kubernetes** and **OpenShift**.

- **✅ Configuration**:
  - Automatically detect changes in the Kubernetes configuration and update the MCP server.
  - **View** and manage the current [Kubernetes `.kube/config`](https://blog.marcnuri.com/where-is-my-default-kubeconfig-file) or in-cluster configuration.
- **✅ Generic Kubernetes Resources**: Perform operations on **any** Kubernetes or OpenShift resource.
  - Any CRUD operation (Create or Update, Get, List, Delete).
- **✅ Pods**: Perform Pod-specific operations.
  - **List** pods in all namespaces or in a specific namespace.
  - **Get** a pod by name from the specified namespace.
  - **Delete** a pod by name from the specified namespace.
  - **Show logs** for a pod by name from the specified namespace.
  - **Top** gets resource usage metrics for all pods or a specific pod in the specified namespace.
  - **Exec** into a pod and run a command.
  - **Run** a container image in a pod and optionally expose it.
- **✅ Namespaces**: List Kubernetes Namespaces.
- **✅ Events**: View Kubernetes events in all namespaces or in a specific namespace.
- **✅ Projects**: List OpenShift Projects.
- **☸️ Helm**:
  - **Install** a Helm chart in the current or provided namespace.
  - **List** Helm releases in all namespaces or in a specific namespace.
  - **Uninstall** a Helm release in the current or provided namespace.
- **🔭 Observability**: Optional OpenTelemetry distributed tracing and metrics with custom sampling rates. Includes `/stats` endpoint for real-time statistics. See [OTEL.md](docs/OTEL.md).

Unlike other Kubernetes MCP server implementations, this **IS NOT** just a wrapper around `kubectl` or `helm` command-line t

## Links

- Repository: https://github.com/containers/kubernetes-mcp-server
