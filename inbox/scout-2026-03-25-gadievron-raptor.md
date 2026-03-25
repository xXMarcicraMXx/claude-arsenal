---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 86
  scoring_breakdown:
    stars: 27
    recency: 25
    docs: 20
    community: 14
github_data:
  full_name: "gadievron/raptor"
  url: "https://github.com/gadievron/raptor"
  description: "Raptor turns Claude Code into a general-purpose AI offensive/defensive security agent. By using Claude.md and creating rules, sub-agents, and skills, and orchestrating security tool usage, we configure the agent for adversarial thinking, and perform research or attack/defense operations."
  stars: 1513
  forks: 194
  open_issues: 12
  language: "Python"
  license: "MIT"
  last_push: "2026-03-24"
  created: "2025-10-17"
  topics: []
---

# gadievron/raptor

> Discovered by arsenal scout — awaiting manual triage

## Description

Raptor turns Claude Code into a general-purpose AI offensive/defensive security agent. By using Claude.md and creating rules, sub-agents, and skills, and orchestrating security tool usage, we configure the agent for adversarial thinking, and perform research or attack/defense operations.

## README Excerpt

```text
╔═══════════════════════════════════════════════════════════════════════════╗ 
║                                                                           ║
║             ██████╗  █████╗ ██████╗ ████████╗ ██████╗ ██████╗             ║ 
║             ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗            ║ 
║             ██████╔╝███████║██████╔╝   ██║   ██║   ██║██████╔╝            ║ 
║             ██╔══██╗██╔══██║██╔═══╝    ██║   ██║   ██║██╔══██╗            ║ 
║             ██║  ██║██║  ██║██║        ██║   ╚██████╔╝██║  ██║            ║ 
║             ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝            ║ 
║                                                                           ║ 
║             Autonomous Offensive/Defensive Research Framework             ║
║             Based on Claude Code - v1.0-beta                              ║
║                                                                           ║ 
║             By Gadi Evron, Daniel Cuthbert                                ║
║                Thomas Dullien (Halvar Flake)                              ║
║                Michael Bargury                                            ║ 
║                John Cartwright                                            ║ 
║                                                                           ║ 
╚═══════════════════════════════════════════════════════════════════════════╝ 

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣀⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠿⠿⠟
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣤⣴⣶⣶⣶⣤⣿⡿⠁⠀⠀⠀
⣀⠤⠴⠒⠒⠛⠛⠛⠛⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⣿⣿⣿⡟⠻⢿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢿⣿⠟⠀⠸⣊⡽⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⡁⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⣿⣧⠀ Get them bugs.....⠀⠀⠀⠀⠀⠀⠀⠀
                                                 
```

# RAPTOR - Autonomous Offensive/Defensive Security Research Framework, based on Claude Code

[![Run in Smithery](https://smithery.ai/badge/skills/gadievron)](https://smithery.ai/skills?ns=gadievron&utm_source=github&utm_medium=badge)
[![CodeQL](https://github.com/gadievron/raptor/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/gadievron/raptor/actions/workflows/github-code-scanning/codeql)


**Authors:** Gadi Evron, Daniel Cuthbert, Thomas Dullien (Halvar Flake), Michael Bargury & John Cartwright
(@gadievron, @danielcuthbert, @thomasdullien, @mbrg & @grokjc)

**License:** MIT (see LICENSE file)

**Repository:** https://github.com/gadievron/raptor

**Dependencies:** See DEPENDENCIES.md for external tools and licenses

---

## What is RAPTOR?

RAPTOR is an **autonomous offensive/defensive security research framework**, based on
**Claude Code**. It empowers security research with agentic workflows and automation.

RAPTOR stands for Recursive Autonomous Penetration Testing and Observation Robot.
(We really wanted to name it RAPTOR)

**RAPTOR autonomously**:
1. **Scans** your code with Semgrep and CodeQL and tries dataflow validation
2. **Fuzzes** your binaries with American Fuzzy Lop (AFL)
3. **Analyses** vulnerabilities using adva

## Links

- Repository: https://github.com/gadievron/raptor
