---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 75
  scoring_breakdown:
    stars: 32
    recency: 8
    docs: 20
    community: 15
github_data:
  full_name: "executeautomation/mcp-playwright"
  url: "https://github.com/executeautomation/mcp-playwright"
  description: "Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌"
  stars: 5351
  forks: 481
  open_issues: 22
  language: "TypeScript"
  license: "MIT"
  last_push: "2025-12-13"
  created: "2024-12-03"
  topics: []
---

# executeautomation/mcp-playwright

> Discovered by arsenal scout — awaiting manual triage

## Description

Playwright Model Context Protocol Server - Tool to automate Browsers and APIs in Claude Desktop, Cline, Cursor IDE and More 🔌

## README Excerpt

<div align="center" markdown="1">
  <table>
    <tr>
      <td align="center" valign="middle">
        <a href="https://mseep.ai/app/executeautomation-mcp-playwright">
          <img src="https://mseep.net/pr/executeautomation-mcp-playwright-badge.png" alt="MseeP.ai Security Assessment Badge" height="80"/>
        </a>
      </td>
    </tr>
    <tr>
      <td align="center"><sub>MseeP.ai Security Assessment</sub></td>
    </tr>
  </table>
</div>
<hr>

# Playwright MCP Server 🎭

[![Trust Score](https://archestra.ai/mcp-catalog/api/badge/quality/executeautomation/mcp-playwright)](https://archestra.ai/mcp-catalog/executeautomation__mcp-playwright)
[![smithery badge](https://smithery.ai/badge/@executeautomation/playwright-mcp-server)](https://smithery.ai/server/@executeautomation/playwright-mcp-server)

A Model Context Protocol server that provides browser automation capabilities using Playwright. This server enables LLMs to interact with web pages, take screenshots, generate test code, web scrapes the page and execute JavaScript in a real browser environment.

<a href="https://glama.ai/mcp/servers/yh4lgtwgbe"><img width="380" height="200" src="https://glama.ai/mcp/servers/yh4lgtwgbe/badge" alt="mcp-playwright MCP server" /></a>

## ✨ What's New in v1.0.10

### 🎯 Device Emulation with 143 Real Device Presets!

Test your web applications on **real device profiles** with a simple command:

```javascript
// Test on iPhone 13 with automatic user-agent, touch support, and device pixel ratio
await playwright_resize({ device: "iPhone 13" });

// Switch to iPad with landscape orientation
await playwright_resize({ device: "iPad Pro 11", orientation: "landscape" });

// Test desktop view
await playwright_resize({ device: "Desktop Chrome" });
```

**Natural Language Support for AI Assistants:**
- "Test on iPhone 13" 
- "Switch to iPad view"
- "Rotate to landscape"

**Supports 143 devices:** iPhone, iPad, Pixel, Galaxy, and Desktop browsers with proper emulation of viewport, user-agent, touch events, and device pixel ratios.

📚 [View Device Quick Reference](https://executeautomation.github.io/mcp-playwright/docs/playwright-web/Device-Quick-Reference) | [Prompt Guide](https://executeautomation.github.io/mcp-playwright/docs/playwright-web/Resize-Prompts-Guide)

## Screenshot
![Playwright + Claude](image/playwright_claude.png)

## [Documentation](https://executeautomation.github.io/mcp-playwright/) | [API reference](https://executeautomation.github.io/mcp-playwright/docs/playwright-web/Supported-Tools)

## Installation

You can install the package using either npm, mcp-get, or Smithery:

Using npm:
```bash
npm install -g @executeautomation/playwright-mcp-server
```

Using mcp-get:
```bash
npx @michaellatman/mcp-get@latest install @executeautomation/playwright-mcp-server
```
Using Smithery

To install Playwright MCP for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@executeautomation/playwright-mcp-server):

```bash
npx @smithery/cli install

## Links

- Repository: https://github.com/executeautomation/mcp-playwright
- Homepage: https://executeautomation.github.io/mcp-playwright/
