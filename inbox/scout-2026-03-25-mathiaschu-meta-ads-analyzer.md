---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code mcp server"
  quality_score: 68
  scoring_breakdown:
    stars: 21
    recency: 20
    docs: 15
    community: 12
github_data:
  full_name: "mathiaschu/meta-ads-analyzer"
  url: "https://github.com/mathiaschu/meta-ads-analyzer"
  description: "Meta Ads Analyzer skill + MCP server for Claude Code. Breakdown Effect, Learning Phase, and expert-level campaign diagnosis."
  stars: 272
  forks: 38
  open_issues: 2
  language: "Shell"
  license: "MIT"
  last_push: "2026-02-26"
  created: "2026-02-26"
  topics: []
---

# mathiaschu/meta-ads-analyzer

> Discovered by arsenal scout — awaiting manual triage

## Description

Meta Ads Analyzer skill + MCP server for Claude Code. Breakdown Effect, Learning Phase, and expert-level campaign diagnosis.

## README Excerpt

# Meta Ads Analyzer for Claude Code

A Claude Code skill + MCP server setup for expert-level Meta Ads campaign analysis. Includes the **Breakdown Effect** framework, Learning Phase diagnostics, and 9 reference documents from Meta's official documentation.

## What It Does

When installed, Claude Code can:

- Analyze campaign, ad set, and ad-level performance data
- Identify root causes of performance issues using Meta's system mechanics
- Explain the **Breakdown Effect** (why Meta allocates budget to seemingly "worse" segments)
- Diagnose Learning Phase, Auction Overlap, Pacing, and Creative Fatigue issues
- Generate structured analysis reports with actionable recommendations
- Connect directly to Meta's API to pull live campaign data (via MCP)

## Components

| Component | What it does |
|---|---|
| **Skill** (`skill/`) | Analysis framework with 9 reference docs that Claude loads as context |
| **MCP Server** (`mcp/`) | Connects Claude Code to Meta's Marketing API for live data |
| **Scripts** (`scripts/`) | Setup and token refresh helpers |

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- [Node.js](https://nodejs.org/) v18+
- A Meta App with Marketing API access ([create one here](https://developers.facebook.com/apps/))

## Installation

### 1. Install the Skill

Copy the `skill/` folder into your Claude Code project:

```bash
# From your Claude Code project root
mkdir -p .claude/skills/meta-ads-analyzer
cp -r skill/* .claude/skills/meta-ads-analyzer/
```

The skill is now active. Claude will automatically use it when you ask about Meta Ads analysis.

### 2. Set Up the MCP Server (optional, for live data)

The MCP server lets Claude pull live campaign data from Meta's API. Skip this if you only want to analyze exported data (CSV, screenshots).

#### a) Create a Meta App

1. Go to [developers.facebook.com](https://developers.facebook.com/apps/)
2. Create a new app (type: **Business**)
3. Add the **Marketing API** product
4. Note your **App ID** and **App Secret**

#### b) Generate an Access Token

1. Go to [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
2. Select your app
3. Add permissions: `ads_read`, `ads_management`, `business_management`
4. Click **Generate Access Token** and authorize
5. Exchange for a long-lived token (60 days) using the setup script:

```bash
bash scripts/setup.sh
```

#### c) Configure Claude Code

Copy the MCP config template and add your credentials:

```bash
cp mcp/mcp.json.example .mcp.json
```

Edit `.mcp.json` and replace the placeholders with your actual token and app secret.

Then restart Claude Code for the MCP server to connect.

### 3. Verify

Ask Claude: **"Analyze my Meta Ads campaigns"** — it should connect to your ad account and start analyzing.

## Token Refresh

Meta long-lived tokens expire after ~60 days. To refresh:

```bash
bash scripts/refresh_token.sh
```

If the token already expired, generate a new one from the [Graph API Explor

## Links

- Repository: https://github.com/mathiaschu/meta-ads-analyzer
