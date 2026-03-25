---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code configuration"
  quality_score: 62
  scoring_breakdown:
    stars: 16
    recency: 20
    docs: 20
    community: 6
github_data:
  full_name: "fubak/ferret-scan"
  url: "https://github.com/fubak/ferret-scan"
  description: "Security scanner for LLM CLI (Claude Code, Codex, Gemini, Droid, Opencode, etc) configurations and MD files - detect prompt injections, credential leaks, and malicious patterns"
  stars: 73
  forks: 5
  open_issues: 1
  language: "TypeScript"
  license: "MIT"
  last_push: "2026-02-22"
  created: "2026-01-31"
  topics: []
---

# fubak/ferret-scan

> Discovered by arsenal scout — awaiting manual triage

## Description

Security scanner for LLM CLI (Claude Code, Codex, Gemini, Droid, Opencode, etc) configurations and MD files - detect prompt injections, credential leaks, and malicious patterns

## README Excerpt

<p align="center">
<pre>
⠀⡠⢂⠔⠚⠟⠓⠒⠒⢂⠐⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣷⣧⣀⠀⢀⣀⣤⣄⠈⢢⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣿⣭⣿⣿⣿⣿⣽⣹⣧⠈⣾⢱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⢿⠋⢸⠂⠈⠹⢿⣿⡿⠀⢸⡷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⣆⠉⢇⢁⠶⠈⠀⠉⠀⢀⣾⣇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢑⣦⣤⣤⣤⣤⣴⣶⣿⡿⢨⠃⠀⠀⠀███████╗███████╗██████╗ ██████╗ ███████╗████████╗
⠀⢰⣿⣿⣟⣯⡿⣽⣻⣾⣽⣇⠏⠀⠀⠀⠀██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
⠀⢿⣿⣟⣾⣽⣻⣽⢷⣻⣾⢿⣄⣀⣀⡀⠀█████╗  █████╗  ██████╔╝██████╔╝█████╗     ██║
⠀⢸⣿⣟⣷⣯⢿⣽⣻⣟⣾⡟⠁⠀⠀⠀⠀██╔══╝  ██╔══╝  ██╔══██╗██╔══██╗██╔══╝     ██║
⠀⠈⣿⣿⣷⣻⣯⣟⣷⣯⣿⠀⠀⠀⠀⠀⠀██║     ███████╗██║  ██║██║  ██║███████╗   ██║
⠀⠀⠘⢿⣿⣷⣯⣿⣞⡷⣿⣇⠀⠀⠀⠀⠀╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝
⠀⠀⠀⠈⣿⣿⣿⣷⣟⣿⣳⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⡿⠉⠛⣿⡷⣯⡿⢀⣀⣀⣣⣸⣿⣽⣟⡿⣷⣟⣯⣷⣿⣽⣿⡆⠀⠀⠀
⠀⠀⠀⢰⣿⣿⠇⠀⠀⣿⣿⣹⠁⠀⠀⢉⣹⣿⣿⣿⣿⠿⣿⣿⣏⣿⣷⣿⣿⣿⣷⣄⠀
⠀⠀⢾⣿⣿⠟⠀⠀⣰⣿⣷⠏⠀⠀⠺⠿⠿⠿⠛⢉⣠⣴⣿⣿⣿⡻⠏⣋⣿⣿⣿⣷⣇
⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡾⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠻⠻⠁⣠⢦⣷⣟⡿⣞⣯⣿⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣟⣿⣿⠿⣿⡿⠟⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠯⠝⠋⠀⠀⠀⠀
</pre>
<strong>Security Scanner for AI CLI Configurations</strong>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/ferret-scan"><img src="https://img.shields.io/npm/v/ferret-scan?style=flat-square&color=blue" alt="npm version"></a>
  <a href="https://www.npmjs.com/package/ferret-scan"><img src="https://img.shields.io/npm/dm/ferret-scan?style=flat-square&color=green" alt="npm downloads"></a>
  <a href="https://github.com/fubak/ferret-scan/blob/main/LICENSE"><img src="https://img.shields.io/npm/l/ferret-scan?style=flat-square" alt="license"></a>
  <a href="https://github.com/fubak/ferret-scan/actions"><img src="https://img.shields.io/github/actions/workflow/status/fubak/ferret-scan/ci.yml?style=flat-square" alt="build status"></a>
  <a href="https://github.com/fubak/ferret-scan"><img src="https://img.shields.io/github/stars/fubak/ferret-scan?style=flat-square" alt="GitHub stars"></a>
</p>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#supported-ai-clis">Supported CLIs</a> •
  <a href="#what-it-detects">Detection</a> •
  <a href="#cicd-integration">CI/CD</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#contributing">Contributing</a>
</p>

---

**Ferret** is a security scanner purpose-built for AI assistant configurations. It detects prompt injections, credential leaks, jailbreak attempts, and malicious patterns in your AI CLI setup before they become problems.

Threat intelligence uses a local indicator database by default (no external feeds unless you add indicators).

```
$ ferret scan .

 ⡠⢂⠔⠚⠟⠓⠒⠒⢂⠐⢄
 ⣷⣧⣀⠀⢀⣀⣤⣄⠈⢢⢸⡀   ███████╗███████╗██████╗ ██████╗ ███████╗████████╗
⢀⣿⣭⣿⣿⣿⣿⣽⣹⣧⠈⣾⢱⡀  ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝╚══██╔══╝
⢸⢿⠋⢸⠂⠈⠹⢿⣿⡿⠀⢸⡷⡇  █████╗  █████╗  ██████╔╝██████╔╝█████╗     ██║
⠈⣆⠉⢇⢁⠶⠈⠀⠉⠀⢀⣾⣇⡇  ██╔══╝  ██╔══╝  ██╔══██╗██╔══██╗██╔══╝     ██║
  ⢑⣦⣤⣤⣤⣤⣴⣶⣿⡿⢨⠃  ██║     ███████╗██║  ██║██║  ██║███████╗   ██║
 ⢰⣿⣿⣟⣯⡿⣽⣻⣾⣽⣇⠏   ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝

 Security Scanner for AI CLI Configs

 Scanning: /home/user/my-project
 Found: 24 configuration files

 FINDINGS

 CRITICAL  CRED-005  Hardcoded API Keys
           .claude/se

## Links

- Repository: https://github.com/fubak/ferret-scan
