---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "awesome claude code"
  quality_score: 78
  scoring_breakdown:
    stars: 21
    recency: 25
    docs: 20
    community: 12
github_data:
  full_name: "LimHyungTae/awesome-claudecode-paper-proofreading"
  url: "https://github.com/LimHyungTae/awesome-claudecode-paper-proofreading"
  description: "Claude Code-driven research paper proofreading prompt"
  stars: 271
  forks: 31
  open_issues: 1
  language: ""
  license: "MIT"
  last_push: "2026-03-20"
  created: "2026-03-09"
  topics: []
---

# LimHyungTae/awesome-claudecode-paper-proofreading

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Code-driven research paper proofreading prompt

## README Excerpt

<div align="center">
    <h1>Awesome Claude Code / Codex — Paper Proofreading</h1>
    <a href="https://github.com/LimHyungTae/awesome-claudecode-paper-proofreading"><img src="https://img.shields.io/badge/Claude_Code_+_Codex-Dual_Compatible-2b6cb0" /></a>
    <br />
    <br />
    <p align="center"><img src="https://github.com/user-attachments/assets/b2a97cb8-8535-4beb-b6af-2f641d1962c9" alt="Demo" width="95%"/></p>
    <p><strong><em>Detect first. Fix with confidence.</em></strong></p>
</div>

______________________________________________________________________

## :rocket: Overview

This repository is designed to work with **both Claude Code and Codex** while preserving the original proofreading philosophy.

The detailed instructions live in two prompt files. You can use them directly in a session, or copy/merge them into Codex-oriented workspace instructions such as `AGENTS.md`.

The workflow remains **two-phase**: the agent detects and lists all issues with unique numbers `[1]`, `[2]`, `[3]`..., then waits. The user selects which issues to fix or discard before any file is modified.

______________________________________________________________________

## :bust_in_silhouette: About the Author

<p align="center"><img src="https://github.com/user-attachments/assets/4af4b29f-ce85-47a0-9472-406f2ca95572" alt="Hyungtae Lim" width="75%"/></p>

These prompts are distilled from years of hands-on paper reviewing and mentoring experience by **[Hyungtae Lim](https://github.com/LimHyungTae)**, a researcher in robotics and 3D perception.

- 📝 **[Associate Editor](https://www.ieee-ras.org/publications/ra-l/editorial-board/)**, IEEE Robotics and Automation Letters (RA-L)
- 🌟 **[RSS Pioneer 2024](https://sites.google.com/view/rsspioneers2024/participants)**
- 🎖️ **[ICRA 2025 Outstanding Reviewer](https://2025.ieee-icra.org/program/awards-and-finalists/#outstandingreviewer)** — selected from 7,400+ reviewers
- 📄 **Conducted 100+ paper reviews** across top robotics and CV venues

The review rules in these prompts reflect the standards expected at top robotics and computer vision venues, refined through real paper reviews and publications across ICRA, IROS, RSS, CVPR, ICCV, NeurIPS, AAAI, RA-L, T-RO, IJRR, T-PAMI, T-IV, etc.

______________________________________________________________________

## :page_facing_up: Files

### [`AGENTS.md`](AGENTS.md)

Optional Codex coordinator instructions for the workflow:

- detects first and waits before editing
- chooses between workspace audit and paper proofreading
- reads the full LaTeX workspace recursively
- applies only approved fixes in Phase 2
- points Codex to the authoritative prompt files

### [`prompts/01_latex_workspace_review.md`](prompts/01_latex_workspace_review.md)

**LaTeX infrastructure audit** — detailed checklist for workspace-level errors before submission.

| Check | Description |
|-------|-------------|
| C1 | Preamble configuration (`hyperref`, `cleveref`, `caption` setup) |
| C2 | Package loa

## Links

- Repository: https://github.com/LimHyungTae/awesome-claudecode-paper-proofreading
