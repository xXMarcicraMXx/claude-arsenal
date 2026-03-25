---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code agent subagent"
  quality_score: 57
  scoring_breakdown:
    stars: 18
    recency: 8
    docs: 20
    community: 11
github_data:
  full_name: "shintaro-sprech/agent-orchestrator-template"
  url: "https://github.com/shintaro-sprech/agent-orchestrator-template"
  description: "A self-evolving subagent system for Claude Code"
  stars: 120
  forks: 20
  open_issues: 0
  language: ""
  license: "MIT"
  last_push: "2025-12-05"
  created: "2025-12-04"
  topics: []
---

# shintaro-sprech/agent-orchestrator-template

> Discovered by arsenal scout — awaiting manual triage

## Description

A self-evolving subagent system for Claude Code

## README Excerpt

# Autonomous Orchestration Ecosystem

A self-evolving sub-agent management system for Claude Code. Instead of using pre-defined abstract agents, let the orchestrator dynamically create, integrate, and evolve agents based on actual task requirements.

> **Original concept by [@shintaro_sprech](https://x.com/shintaro_sprech)**

![Autonomous Orchestration Ecosystem](docs/images/orchestration-flow.jpg)

## Concept

The system implements an **Infinite Evolution Cycle**:

```
Implementation → Initial Sub-agent Pool → Orchestrator Engine
                                              ↓
                                    Specialized Sub-agents
                                              ↓
                                    1st Gen Integration
                                              ↓
                                    2nd Gen Integration
                                              ↓
                                    Hyper-Elite Integration
                                              ↓
                                    Ultimate Elite Integration
                                              ↓
                                    Hyper-Elite Integrated Entity
                                              ↓
                                    ← Infinite Evolution Cycle →
```

## Key Features

- **Task-driven agent creation**: Agents are born from real task requirements, not abstract definitions
- **Dynamic integration**: Merges agents when synergy improves outcomes
- **Continuous evolution**: Strong agents evolve through generations, weak ones fade
- **Elite promotion**: High-performing agents are promoted to elite status
- **Lineage tracking**: Integrated agents remember their parents, enabling evolution chains

## Usage: Slash Command

**Use the `/task` slash command to activate the orchestration system.**

```
/task Create a REST API endpoint for user authentication
```

This command triggers the full orchestration workflow:
1. Reads `orchestrator.md`
2. Scans `pool/` for existing agents
3. Calculates coverage against task requirements
4. Creates/integrates/selects the optimal agent
5. Executes the task
6. Updates metrics in `manifests/`
7. Promotes high-performers to `elite/`

### Why Slash Command?

Without the slash command, the orchestration system will **not automatically activate**. The `/task` command ensures:
- Orchestrator logic is always read first
- Agent pool is scanned before execution
- Metrics are updated after completion
- Evolution cycle continues

## How It Works

### 1. Task Analysis

When `/task` is invoked, the orchestrator:
- Scans the existing agent pool
- Calculates coverage rate against task requirements

### 2. Decision Matrix

| Coverage Rate | Action |
|---------------|--------|
| **90%+** | Use existing agent directly |
| **60-90%** | Create integrated agent from multiple sources |
| **Below 60%** | Create new specialized agent |

### 3. Evolution Tracking

After task completion:
- Update agent metrics (usage

## Links

- Repository: https://github.com/shintaro-sprech/agent-orchestrator-template
