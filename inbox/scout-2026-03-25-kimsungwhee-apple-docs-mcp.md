---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 78
  scoring_breakdown:
    stars: 26
    recency: 20
    docs: 20
    community: 12
github_data:
  full_name: "kimsungwhee/apple-docs-mcp"
  url: "https://github.com/kimsungwhee/apple-docs-mcp"
  description: "MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants"
  stars: 1170
  forks: 48
  open_issues: 7
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-17"
  created: "2025-07-15"
  topics: ["ai-assistant", "api-documentation", "apple", "apple-developer-docs-mcp", "apple-developer-documentation", "apple-docs-mcp", "apple-documentation", "claude", "claude-code", "cursor", "documentation", "ios-development", "macos-development", "mcp", "model-context-protocol", "objective-c", "swift", "swift-mcp", "swiftui"]
---

# kimsungwhee/apple-docs-mcp

> Discovered by arsenal scout — awaiting manual triage

## Description

MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants

## README Excerpt

# Apple Docs MCP - Apple Developer Documentation Model Context Protocol Server

[![npm version](https://badge.fury.io/js/@kimsungwhee%2Fapple-docs-mcp.svg)](https://badge.fury.io/js/@kimsungwhee%2Fapple-docs-mcp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Apple Developer Documentation MCP Server - Access Apple's official developer docs, frameworks, APIs, SwiftUI, UIKit, and WWDC videos through Model Context Protocol. Search iOS, macOS, watchOS, tvOS, and visionOS documentation with AI-powered natural language queries. Get instant access to Swift/Objective-C code examples, API references, and technical guides directly in Claude, Cursor, or any MCP-compatible AI assistant.

**English** | [日本語](README.ja.md) | [한국어](README.ko.md) | [简体中文](README.zh-CN.md)

## ✨ Features

- 🔍 **Smart Search**: Intelligent search across Apple Developer Documentation for SwiftUI, UIKit, Foundation, CoreData, ARKit, and more
- 📚 **Complete Documentation Access**: Full access to Apple's JSON API for Swift, Objective-C, and framework documentation
- 🔧 **Framework Index**: Browse hierarchical API structures for iOS, macOS, watchOS, tvOS, visionOS frameworks
- 📋 **Technology Catalog**: Explore Apple technologies including SwiftUI, UIKit, Metal, Core ML, Vision, and ARKit
- 📰 **Documentation Updates**: Track WWDC 2024/2025 announcements, iOS 26, macOS 26, and latest SDK releases
- 🎯 **Technology Overviews**: Comprehensive guides for Swift, SwiftUI, UIKit, and all Apple development platforms
- 💻 **Sample Code Library**: Swift and Objective-C code examples for iOS, macOS, and cross-platform development
- 🎥 **WWDC Video Library**: Search WWDC 2014-2025 sessions with transcripts, Swift/SwiftUI code examples, and resources
- 🔗 **Related APIs Discovery**: Find SwiftUI views, UIKit controllers, and framework-specific API relationships
- 📊 **Platform Compatibility**: iOS 13+, macOS 10.15+, watchOS 6+, tvOS 13+, visionOS compatibility analysis
- ⚡ **High Performance**: Optimized for Xcode, Swift Playgrounds, and AI-powered development environments
- 🔄 **Smart UserAgent Pool**: Intelligent UserAgent rotation system with automatic failure recovery and performance monitoring
- 🌐 **Multi-Platform**: Complete iOS, iPadOS, macOS, watchOS, tvOS, and visionOS documentation support
- 🏷️ **Beta & Status Tracking**: iOS 26 beta APIs, deprecated UIKit methods, new SwiftUI features tracking

## 🚀 Quick Start

### Claude Desktop (Recommended)

Add this to your Claude Desktop configuration:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "apple-docs": {
      "command": "npx",
      "args": ["-y", "@kimsungwhee/apple-docs-mcp"]
    }
  }
}
```

> **Note**: If you encounter issues with an old version being used, add `@latest` to force the latest version:
> ```json
> "args": ["-y", "@kimsungwhee/apple-docs-mcp@lat

## Links

- Repository: https://github.com/kimsungwhee/apple-docs-mcp
- Homepage: https://www.npmjs.com/package/@kimsungwhee/apple-docs-mcp
