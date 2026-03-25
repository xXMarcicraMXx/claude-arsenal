---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "anthropic mcp server"
  quality_score: 76
  scoring_breakdown:
    stars: 23
    recency: 20
    docs: 20
    community: 13
github_data:
  full_name: "wshobson/maverick-mcp"
  url: "https://github.com/wshobson/maverick-mcp"
  description: "MaverickMCP - Personal Stock Analysis MCP Server"
  stars: 444
  forks: 112
  open_issues: 9
  language: "Python"
  license: "MIT"
  last_push: "2026-03-16"
  created: "2025-08-24"
  topics: ["anthropic", "artificial-intelligence", "claude", "equities", "fastmcp", "finance", "financial-analysis", "fintech", "investing", "mcp", "mcp-server", "mcp-servers", "pandas", "python", "stock-market", "stocks", "technical-analysis", "tiingo", "tiingo-api", "trading"]
---

# wshobson/maverick-mcp

> Discovered by arsenal scout — awaiting manual triage

## Description

MaverickMCP - Personal Stock Analysis MCP Server

## README Excerpt

# MaverickMCP - Personal Stock Analysis MCP Server

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![FastMCP](https://img.shields.io/badge/FastMCP-2.0-green.svg)](https://github.com/jlowin/fastmcp)
[![GitHub Stars](https://img.shields.io/github/stars/wshobson/maverick-mcp?style=social)](https://github.com/wshobson/maverick-mcp)
[![GitHub Issues](https://img.shields.io/github/issues/wshobson/maverick-mcp)](https://github.com/wshobson/maverick-mcp/issues)
[![GitHub Forks](https://img.shields.io/github/forks/wshobson/maverick-mcp?style=social)](https://github.com/wshobson/maverick-mcp/network/members)

**MaverickMCP** is a personal-use FastMCP 2.0 server that provides professional-grade financial data analysis, technical indicators, and portfolio optimization tools directly to your Claude Desktop interface. Built for individual traders and investors, it offers comprehensive stock analysis capabilities without any authentication or billing complexity.

The server comes pre-seeded with all 520 S&P 500 stocks and provides advanced screening recommendations across multiple strategies. It runs locally with HTTP/SSE/STDIO transport options for seamless integration with Claude Desktop and other MCP clients.

## Why MaverickMCP?

MaverickMCP provides professional-grade financial analysis tools directly within your Claude Desktop interface. Perfect for individual traders and investors who want comprehensive stock analysis capabilities without the complexity of expensive platforms or commercial services.

**Key Benefits:**

- **No Setup Complexity**: Simple `make dev` command gets you running (or `uv sync` + `make dev`)
- **Modern Python Tooling**: Built with `uv` for lightning-fast dependency management
- **Claude Desktop Integration**: Native MCP support for seamless AI-powered analysis
- **Comprehensive Analysis**: 29+ financial tools covering technical indicators, screening, and portfolio optimization
- **Smart Caching**: Redis-powered performance with graceful fallbacks
- **Fast Development**: Hot reload, smart error handling, and parallel processing
- **Open Source**: MIT licensed, community-driven development
- **Educational Focus**: Perfect for learning financial analysis and MCP development

## Features

- **Pre-seeded Database**: 520 S&P 500 stocks with comprehensive screening recommendations
- **Advanced Backtesting**: VectorBT-powered engine with 15+ built-in strategies and ML algorithms
- **Fast Development**: Comprehensive Makefile, smart error handling, hot reload, and parallel processing
- **Stock Data Access**: Historical and real-time stock data with intelligent caching
- **Technical Analysis**: 20+ indicators including SMA, EMA, RSI, MACD, Bollinger Bands, and more
- **Stock Screening**: Multiple strategies (Maverick Bullish/Bearish, Trending Breakouts) with parallel processin

## Links

- Repository: https://github.com/wshobson/maverick-mcp
- Homepage: https://sethhobson.com
