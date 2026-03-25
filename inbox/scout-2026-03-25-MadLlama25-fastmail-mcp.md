---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude desktop extension"
  quality_score: 74
  scoring_breakdown:
    stars: 17
    recency: 25
    docs: 20
    community: 12
github_data:
  full_name: "MadLlama25/fastmail-mcp"
  url: "https://github.com/MadLlama25/fastmail-mcp"
  description: "A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data. Includes a DXT (desktop extension) for Claude Desktop."
  stars: 88
  forks: 37
  open_issues: 5
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-03-21"
  created: "2025-06-15"
  topics: ["dxt", "fastmail", "fastmail-api", "mcp-server"]
---

# MadLlama25/fastmail-mcp

> Discovered by arsenal scout — awaiting manual triage

## Description

A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data. Includes a DXT (desktop extension) for Claude Desktop.

## README Excerpt

# Fastmail MCP Server

A Model Context Protocol (MCP) server that provides access to the Fastmail API, enabling AI assistants to interact with email, contacts, and calendar data.

## Features

### Core Email Operations
- List mailboxes and get mailbox statistics
- List, search, and filter emails with advanced criteria
- Get specific emails by ID with full content
- Send emails (text and HTML) with proper draft/sent handling
- Reply to emails with proper threading (In-Reply-To, References headers)
- Create and save email drafts (with or without threading)
- Email management: mark read/unread, delete, move between folders

### Advanced Email Features
- **Attachment Handling**: List and download email attachments
- **Threading Support**: Get complete conversation threads
- **Advanced Search**: Multi-criteria filtering (sender, date range, attachments, read status)
- **Bulk Operations**: Process multiple emails simultaneously
- **Statistics & Analytics**: Account summaries and mailbox statistics

### Contacts Operations
- List all contacts with full contact information
- Get specific contacts by ID
- Search contacts by name or email

### Calendar Operations
- List all calendars and calendar events
- Get specific calendar events by ID
- Create new calendar events with participants and details

### Label vs Move Operations
- **move_email/bulk_move**: Replaces ALL mailboxes for an email (folder behavior)
- **add_labels/remove_labels**: Adds/removes SPECIFIC mailboxes while preserving others (label behavior)

### Identity & Account Management
- List available sending identities
- Account summary with comprehensive statistics

## Setup

### Prerequisites
- Node.js 18+ 
- A Fastmail account with API access
- Fastmail API token

### Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   npm install
   ```

3. Build the project:
   ```bash
   npm run build
   ```

### Configuration

1. Get your Fastmail API token:
   - Log in to Fastmail web interface
   - Go to Settings → Privacy & Security
   - Find "Connected apps & API tokens" section
   - Click "Manage API tokens"
   - Click "New API token"
   - Copy the generated token

2. Set environment variables:
   ```bash
   export FASTMAIL_API_TOKEN="your_api_token_here"
   # Optional: customize base URL (defaults to https://api.fastmail.com)
   export FASTMAIL_BASE_URL="https://api.fastmail.com"
   ```

### Running the Server

Start the MCP server:
```bash
npm start
```

For development with auto-reload:
```bash
npm run dev
```

### Run via npx (GitHub)

Default to `main` branch:

```bash
FASTMAIL_API_TOKEN="your_token" FASTMAIL_BASE_URL="https://api.fastmail.com" \
  npx --yes github:MadLlama25/fastmail-mcp fastmail-mcp
```

Windows PowerShell:

```powershell
$env:FASTMAIL_API_TOKEN="your_token"
$env:FASTMAIL_BASE_URL="https://api.fastmail.com"
npx --yes github:MadLlama25/fastmail-mcp fastmail-mcp
```

Pin to a tagged release:

```bash
FASTMAIL_API_TOKEN="your_token" \
  npx -

## Links

- Repository: https://github.com/MadLlama25/fastmail-mcp
