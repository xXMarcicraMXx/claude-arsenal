---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 76
  scoring_breakdown:
    stars: 27
    recency: 15
    docs: 20
    community: 14
github_data:
  full_name: "MiniMax-AI/MiniMax-MCP"
  url: "https://github.com/MiniMax-AI/MiniMax-MCP"
  description: "Official MiniMax Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech, image generation and video generation APIs."
  stars: 1349
  forks: 237
  open_issues: 14
  language: "Python"
  license: "MIT"
  last_push: "2026-01-07"
  created: "2025-04-10"
  topics: ["image-generation", "image-to-video", "mcp", "mcp-server", "mcp-tools", "text-to-image", "text-to-speech", "text-to-video", "video-generation", "voice-cloning"]
---

# MiniMax-AI/MiniMax-MCP

> Discovered by arsenal scout — awaiting manual triage

## Description

Official MiniMax Model Context Protocol (MCP) server that enables interaction with powerful Text to Speech, image generation and video generation APIs.

## README Excerpt

![export](https://github.com/MiniMax-AI/MiniMax-01/raw/main/figures/MiniMaxLogo-Light.png)

<div align="center" style="line-height: 1;">
  <a href="https://www.minimax.io" target="_blank" style="margin: 2px; color: var(--fgColor-default);">
    <img alt="Homepage" src="https://img.shields.io/badge/_Homepage-MiniMax-FF4040?style=flat-square&labelColor=2C3E50&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgNDkwLjE2IDQxMS43Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2ZmZjt9PC9zdHlsZT48L2RlZnM+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMjMzLjQ1LDQwLjgxYTE3LjU1LDE3LjU1LDAsMSwwLTM1LjEsMFYzMzEuNTZhNDAuODIsNDAuODIsMCwwLDEtODEuNjMsMFYxNDVhMTcuNTUsMTcuNTUsMCwxLDAtMzUuMDksMHY3OS4wNmE0MC44Miw0MC44MiwwLDAsMS04MS42MywwVjE5NS40MmExMS42MywxMS42MywwLDAsMSwyMy4yNiwwdjI4LjY2YTE3LjU1LDE3LjU1LDAsMCwwLDM1LjEsMFYxNDVBNDAuODIsNDAuODIsMCwwLDEsMTQwLDE0NVYzMzEuNTZhMTcuNTUsMTcuNTUsMCwwLDAsMzUuMSwwVjIxNy41aDBWNDAuODFhNDAuODEsNDAuODEsMCwxLDEsODEuNjIsMFYyODEuNTZhMTEuNjMsMTEuNjMsMCwxLDEtMjMuMjYsMFptMjE1LjksNjMuNEE0MC44Niw0MC44NiwwLDAsMCw0MDguNTMsMTQ1VjMwMC44NWExNy41NSwxNy41NSwwLDAsMS0zNS4wOSwwdi0yNjBhNDAuODIsNDAuODIsMCwwLDAtODEuNjMsMFYzNzAuODlhMTcuNTUsMTcuNTUsMCwwLDEtMzUuMSwwVjMzMGExMS42MywxMS42MywwLDEsMC0yMy4yNiwwdjQwLjg2YTQwLjgxLDQwLjgxLDAsMCwwLDgxLjYyLDBWNDAuODFhMTcuNTUsMTcuNTUsMCwwLDEsMzUuMSwwdjI2MGE0MC44Miw0MC44MiwwLDAsMCw4MS42MywwVjE0NWExNy41NSwxNy41NSwwLDEsMSwzNS4xLDBWMjgxLjU2YTExLjYzLDExLjYzLDAsMCwwLDIzLjI2LDBWMTQ1QTQwLjg1LDQwLjg1LDAsMCwwLDQ0OS4zNSwxMDQuMjFaIi8+PC9zdmc+&logoWidth=20" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://arxiv.org/abs/2501.08313" target="_blank" style="margin: 2px;">
    <img alt="Paper" src="https://img.shields.io/badge/📖_Paper-MiniMax--01-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
   <a href="https://chat.minimax.io/" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="https://img.shields.io/badge/_MiniMax_Chat-FF4040?style=flat-square&labelColor=2C3E50&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgNDkwLjE2IDQxMS43Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2ZmZjt9PC9zdHlsZT48L2RlZnM+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMjMzLjQ1LDQwLjgxYTE3LjU1LDE3LjU1LDAsMSwwLTM1LjEsMFYzMzEuNTZhNDAuODIsNDAuODIsMCwwLDEtODEuNjMsMFYxNDVhMTcuNTUsMTcuNTUsMCwxLDAtMzUuMDksMHY3OS4wNmE0MC44Miw0MC44MiwwLDAsMS04MS42MywwVjE5NS40MmExMS42MywxMS42MywwLDAsMSwyMy4yNiwwdjI4LjY2YTE3LjU1LDE3LjU1LDAsMCwwLDM1LjEsMFYxNDVBNDAuODIsNDAuODIsMCwwLDEsMTQwLDE0NVYzMzEuNTZhMTcuNTUsMTcuNTUsMCwwLDAsMzUuMSwwVjIxNy41aDBWNDAuODFhNDAuODEsNDAuODEsMCwxLDEsODEuNjIsMFYyODEuNTZhMTEuNjMsMTEuNjMsMCwxLDEtMjMuMjYsMFptMjE1LjksNjMuNEE0MC44Niw0MC44NiwwLDAsMCw0MDguNTMsMTQ1VjMwMC44NWExNy41NSwxNy41NSwwLDAsMS0zNS4wOSwwdi0yNjBhNDAuODIsNDAuODIsMCwwLDAtODEuNjMsMFYzNzAuODlhMTcuNTUsMTcuNTUsMCwwLDEtMzUuMSwwVjMzMGExMS

## Links

- Repository: https://github.com/MiniMax-AI/MiniMax-MCP
- Homepage: https://www.minimax.io/platform
