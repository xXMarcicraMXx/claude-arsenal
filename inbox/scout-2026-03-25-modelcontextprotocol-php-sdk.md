---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "model context protocol server"
  quality_score: 82
  scoring_breakdown:
    stars: 27
    recency: 25
    docs: 20
    community: 10
github_data:
  full_name: "modelcontextprotocol/php-sdk"
  url: "https://github.com/modelcontextprotocol/php-sdk"
  description: "The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboration with The PHP Foundation."
  stars: 1425
  forks: 125
  open_issues: 29
  language: "PHP"
  license: "NOASSERTION"
  last_push: "2026-03-23"
  created: "2025-07-15"
  topics: []
---

# modelcontextprotocol/php-sdk

> Discovered by arsenal scout — awaiting manual triage

## Description

The official PHP SDK for Model Context Protocol servers and clients. Maintained in collaboration with The PHP Foundation.

## README Excerpt

# MCP PHP SDK

The official PHP SDK for Model Context Protocol (MCP). It provides a framework-agnostic API for implementing MCP servers
and clients in PHP.

This project represents a collaboration between [the PHP Foundation](https://thephp.foundation/) and the [Symfony project](https://symfony.com/). It adopts
development practices and standards from the Symfony project, including [Coding Standards](https://symfony.com/doc/current/contributing/code/standards.html) and the
[Backward Compatibility Promise](https://symfony.com/doc/current/contributing/code/bc.html).

Until the first major release, this SDK is considered [experimental](https://symfony.com/doc/current/contributing/code/experimental.html), please see the [roadmap](./ROADMAP.md) for
planned next steps and features.

## Installation

```bash
composer require mcp/sdk
```

## Quick Start

This example demonstrates the most common usage pattern - a STDIO server using attribute discovery.

### 1. Define Your MCP Elements

Create a class with MCP capabilities using attributes:

```php
<?php

namespace App;

use Mcp\Capability\Attribute\McpTool;
use Mcp\Capability\Attribute\McpResource;

class CalculatorElements
{
    /**
     * Adds two numbers together.
     * 
     * @param int $a The first number
     * @param int $b The second number
     * @return int The sum of the two numbers
     */
    #[McpTool]
    public function add(int $a, int $b): int
    {
        return $a + $b;
    }

    /**
     * Performs basic arithmetic operations.
     */
    #[McpTool(name: 'calculate')]
    public function calculate(float $a, float $b, string $operation): float|string
    {
        return match($operation) {
            'add' => $a + $b,
            'subtract' => $a - $b,
            'multiply' => $a * $b,
            'divide' => $b != 0 ? $a / $b : 'Error: Division by zero',
            default => 'Error: Unknown operation'
        };
    }

    #[McpResource(
        uri: 'config://calculator/settings',
        name: 'calculator_config',
        mimeType: 'application/json'
    )]
    public function getSettings(): array
    {
        return ['precision' => 2, 'allow_negative' => true];
    }
}
```

### 2. Create the Server Script

Create your MCP server:

```php
#!/usr/bin/env php
<?php

declare(strict_types=1);

require_once __DIR__ . '/vendor/autoload.php';

use Mcp\Server;
use Mcp\Server\Transport\StdioTransport;

$server = Server::builder()
    ->setServerInfo('Calculator Server', '1.0.0')
    ->setDiscovery(__DIR__, ['.'])
    ->build();

$transport = new StdioTransport();

$server->run($transport);
```

### 3. Configure Your MCP Client

Add to your client configuration (e.g., Claude Desktop's `mcp.json`):

```json
{
    "mcpServers": {
        "php-calculator": {
            "command": "php",
            "args": ["/absolute/path/to/your/server.php"]
        }
    }
}
```

### 4. Test Your Server

```bash
# Test with MCP Inspector
npx @modelcontextprotocol/inspector php /path/to/server.php



## Links

- Repository: https://github.com/modelcontextprotocol/php-sdk
- Homepage: https://php.sdk.modelcontextprotocol.io
