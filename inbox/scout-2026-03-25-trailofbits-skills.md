---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code skill"
  quality_score: 87
  scoring_breakdown:
    stars: 31
    recency: 25
    docs: 20
    community: 11
github_data:
  full_name: "trailofbits/skills"
  url: "https://github.com/trailofbits/skills"
  description: "Trail of Bits Claude Code skills for security research, vulnerability detection, and audit workflows"
  stars: 3897
  forks: 322
  open_issues: 23
  language: "Python"
  license: "CC-BY-SA-4.0"
  last_push: "2026-03-24"
  created: "2026-01-14"
  topics: ["agent-skills"]
---

# trailofbits/skills

> Discovered by arsenal scout — awaiting manual triage

## Description

Trail of Bits Claude Code skills for security research, vulnerability detection, and audit workflows

## README Excerpt

# Trail of Bits Skills Marketplace

A Claude Code plugin marketplace from Trail of Bits providing skills to enhance AI-assisted security analysis, testing, and development workflows.

> Also see: [claude-code-config](https://github.com/trailofbits/claude-code-config) · [skills-curated](https://github.com/trailofbits/skills-curated) · [claude-code-devcontainer](https://github.com/trailofbits/claude-code-devcontainer) · [dropkit](https://github.com/trailofbits/dropkit)

## Installation

### Claude Code Marketplace

```
/plugin marketplace add trailofbits/skills
```

### Browse and Install Plugins

```
/plugin menu
```

### Codex

Codex-native skill discovery is supported via the sidecar `.codex/skills/` tree in this repository.

Install with:

```sh
git clone https://github.com/trailofbits/skills.git ~/.codex/trailofbits-skills
~/.codex/trailofbits-skills/.codex/scripts/install-for-codex.sh
```

See [`.codex/INSTALL.md`](.codex/INSTALL.md) for additional details.

### Local Development

To add the marketplace locally (e.g., for testing or development), navigate to the **parent directory** of this repository:

```
cd /path/to/parent  # e.g., if repo is at ~/projects/skills, be in ~/projects
/plugins marketplace add ./skills
```

## Available Plugins

### Smart Contract Security

| Plugin | Description |
|--------|-------------|
| [building-secure-contracts](plugins/building-secure-contracts/) | Smart contract security toolkit with vulnerability scanners for 6 blockchains |
| [entry-point-analyzer](plugins/entry-point-analyzer/) | Identify state-changing entry points in smart contracts for security auditing |

### Code Auditing

| Plugin | Description |
|--------|-------------|
| [agentic-actions-auditor](plugins/agentic-actions-auditor/) | Audit GitHub Actions workflows for AI agent security vulnerabilities |
| [audit-context-building](plugins/audit-context-building/) | Build deep architectural context through ultra-granular code analysis |
| [burpsuite-project-parser](plugins/burpsuite-project-parser/) | Search and extract data from Burp Suite project files |
| [differential-review](plugins/differential-review/) | Security-focused differential review of code changes with git history analysis |
| [fp-check](plugins/fp-check/) | Systematic false positive verification for security bug analysis with mandatory gate reviews |
| [insecure-defaults](plugins/insecure-defaults/) | Detect insecure default configurations, hardcoded credentials, and fail-open security patterns |
| [semgrep-rule-creator](plugins/semgrep-rule-creator/) | Create and refine Semgrep rules for custom vulnerability detection |
| [semgrep-rule-variant-creator](plugins/semgrep-rule-variant-creator/) | Port existing Semgrep rules to new target languages with test-driven validation |
| [sharp-edges](plugins/sharp-edges/) | Identify error-prone APIs, dangerous configurations, and footgun designs |
| [static-analysis](plugins/static-analysis/) | Static analysis toolkit with CodeQL, Semgrep,

## Links

- Repository: https://github.com/trailofbits/skills
