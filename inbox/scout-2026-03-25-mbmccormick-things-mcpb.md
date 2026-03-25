---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude desktop extension"
  quality_score: 48
  scoring_breakdown:
    stars: 14
    recency: 8
    docs: 20
    community: 6
github_data:
  full_name: "mbmccormick/things-mcpb"
  url: "https://github.com/mbmccormick/things-mcpb"
  description: "Claude Desktop Extension for Things, the award-winning personal task manager"
  stars: 44
  forks: 9
  open_issues: 6
  language: "JavaScript"
  license: "MIT"
  last_push: "2025-11-05"
  created: "2025-07-16"
  topics: []
---

# mbmccormick/things-mcpb

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Desktop Extension for Things, the award-winning personal task manager

## README Excerpt

# Things MCPB - Claude Desktop Extension

A comprehensive Claude Desktop Extension that provides seamless integration with Things 3, enabling you to manage your complete task workflow directly from Claude conversations using AppleScript via secure JavaScript for Automation (JXA).

## Download

### [⬇️ Download Latest Release](https://github.com/mbmccormick/things-mcpb/releases/latest)

## Quick Start

1. **Install Dependencies**: `npm install`
2. **Run Tests**: `npm test` (optional but recommended)
3. **Package Extension**: `mcpb pack .`
4. **Install in Claude Desktop**: Follow Claude Desktop's extension installation process
5. **Launch Things 3**: Ensure Things 3 is running before using commands

> **💡 Pro Tip**: Use `when` for scheduling (when to work on) and `deadline` for final due dates.

## Recent Improvements

### Version 1.4.0
- **📦 MCPB Format Migration**: Updated from DXT to the new MCPB (MCP Bundle) format specification v0.2
- **📦 Package Updates**: Updated @modelcontextprotocol/sdk to v1.20.1 and esbuild to v0.25.11
- **🔧 Tooling**: Migrated from `dxt` CLI to `mcpb` CLI for packaging
- **📝 Documentation**: Updated all documentation and references to reflect MCPB naming
- **✅ Compatibility**: Maintained full backward compatibility with all existing functionality

### Version 1.3.0
- **🏗️ Complete Architecture Overhaul**: Migrated from AppleScript to modular JavaScript for Automation (JXA)
- **🔒 Security-First Design**: Eliminated shell injection risks with `execFile` and JSON parameter passing
- **📦 Modular Build System**: ES6 modules compiled with esbuild for maintainable, modern code
- **⚡ Performance**: Pre-built bundled scripts for faster execution
- **🧪 Comprehensive Testing**: Unit, integration, and regression test suites
- **🔧 Better Error Handling**: Enhanced error messages and timeout protection
- **📚 Developer Experience**: Improved debugging, logging, and development workflow

## Features

### 🎯 Core Functionality
- **Complete Task Management**: Create, read, update, and search todos and projects
- **Smart List Access**: Work with all Things 3 lists (Inbox, Today, Upcoming, Anytime, Someday)
- **Project & Area Organization**: Full project and area management capabilities
- **Advanced Search**: Multiple search types across all your Things data

### 🔍 Discovery & Navigation  
- **Tag Management**: Get all tags and find items by specific tags
- **Logbook Access**: View completed tasks with flexible time periods
- **Trash Management**: Access and review trashed items
- **Recent Items**: Find recently modified items

### 🛠️ Advanced Features
- **Flexible Updates**: Modify existing tasks and projects with full parameter control
- **Data Integrity**: Comprehensive input validation and error handling
- **Security**: Built-in AppleScript injection protection and safe execution
- **User-Friendly Parameters**: Intuitive date terminology and parameter mapping

## API Reference

### 📝 Creation Tools

#### `add_todo` - Create a new to-do


## Links

- Repository: https://github.com/mbmccormick/things-mcpb
