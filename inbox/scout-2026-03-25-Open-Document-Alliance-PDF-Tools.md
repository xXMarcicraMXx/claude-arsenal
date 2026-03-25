---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude desktop extension"
  quality_score: 73
  scoring_breakdown:
    stars: 17
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "Open-Document-Alliance/PDF-Tools"
  url: "https://github.com/Open-Document-Alliance/PDF-Tools"
  description: "PDF Filler for Claude Desktop (using Claude Desktop Extensions)"
  stars: 113
  forks: 15
  open_issues: 1
  language: "HTML"
  license: "MIT"
  last_push: "2026-03-24"
  created: "2025-06-26"
  topics: ["claude", "pdf-filler"]
---

# Open-Document-Alliance/PDF-Tools

> Discovered by arsenal scout — awaiting manual triage

## Description

PDF Filler for Claude Desktop (using Claude Desktop Extensions)

## README Excerpt

# PDF Tools - Fill, Analyze, Extract, View

The complete PDF toolkit for Claude Desktop. Work with PDFs already on your computer — fill forms, analyze documents, extract data, and view them interactively without uploading.

## Features

### Interactive PDF Viewer
- View any PDF with page navigation, zoom, and fullscreen
- Search text across all pages with highlighted results
- Select and copy text directly from PDFs
- Form field sidebar shows all fields with fill status

### Fill Forms & Automate
- Fill out W-9, 1099, I-9, rental applications, and any fillable PDF
- Bulk fill hundreds of PDFs from CSV data
- Save reusable profiles for common forms
- Validate required fields before submission

### Analyze & Extract
- Analyze research papers and academic documents
- Extract tables and structured data to CSV
- Compare contract versions
- Summarize 300+ page reports
- OCR support for scanned documents

### Works with any PDF type
Scientific papers, legal contracts, technical manuals, financial statements, invoices, and forms. Handles fillable forms, scanned documents, and encrypted PDFs.

## Installation

### Claude Desktop Extension

#### Quick Install
1. **[Download the latest .mcpb file from Releases](https://github.com/Open-Document-Alliance/PDF-Tools/releases/latest)**
2. Double-click the `.mcpb` file to install in Claude Desktop

The extension is also available in the Claude Extensions directory.

#### Build from Source
```bash
git clone https://github.com/Open-Document-Alliance/PDF-Tools
cd PDF-Tools
npm install
npm run build:ui
npm install -g @anthropic-ai/mcpb
mcpb pack
# Install the generated .mcpb file in Claude Desktop
```

### Cursor / Other MCP Hosts

```bash
git clone https://github.com/Open-Document-Alliance/PDF-Tools
cd PDF-Tools
npm install

# Add to your MCP client config:
{
  "mcpServers": {
    "pdf-tools": {
      "command": "node",
      "args": ["/full/path/to/PDF-Tools/server/index.js"]
    }
  }
}
```

## Usage

Ask Claude to:

### View PDFs
*"Open my W-9 and show me the fields"*
*"Display the contract PDF in my Documents folder"*

### Fill Forms
*"Fill this W-9 with my business info: Company Name LLC, 123 Main St, Tax ID 12-3456789"*
*"Use my 'work' profile to fill this application"*

### Merge, Split & Organize
*"Merge these three contracts into one PDF"*
*"Split this report into chapters — every 10 pages"*
*"Rotate page 3 by 90 degrees"*
*"Reorder the pages so page 5 comes first"*

### Analyze Documents
*"Summarize this research paper"*
*"What does this contract say about payment terms?"*
*"Extract all text from this scanned invoice"* (OCR)

### Bulk Processing
*"Fill 50 contract PDFs using the client data from contracts.csv"*
*"Extract data from all PDFs in this folder to summary.csv"*

### Password-Protected PDFs
*"Read the fields from this encrypted PDF using password 'mypassword123'"*

## Available Tools

| Tool | Description |
|------|-------------|
| `display_pdf` | Interactive PDF viewer with search, navigation, zo

## Links

- Repository: https://github.com/Open-Document-Alliance/PDF-Tools
- Homepage: https://www.opendocuments.ai/
