---
id: TIP-226
title: "Playwright CLI — browser via shell invece del MCP"
category: scripts
source_type: manual
risk_level: SAFE
quality_score: 8
ai_summary: "CLI ufficiale Microsoft (@playwright/cli) con SKILL.md che pilota il browser via shell on-demand, risparmiando i ~10k token fissi delle definizioni tool del Playwright MCP."
tags: [playwright, browser, testing, context-optimization, cli]
source: "https://github.com/microsoft/playwright-cli"
github_url: "https://github.com/microsoft/playwright-cli"
github_stars: "13000"
github_last_push: "2026-08"
date_added: 2026-08-29
validated: true
related_tips: []
use_cases:
  - "sostituire il Playwright MCP (mcp__playwright__*) per recuperare ~10k token fissi a sessione"
dependencies: ["npm (globale)", "browser binaries (già presenti in ~/AppData/Local/ms-playwright)"]
platform: all
claude_code_version: "any"
---

# Playwright CLI (microsoft/playwright-cli)

VALUTATO il 2026-08-29 — DECISIONE: SKIP come aggiunta. Motivi:
- Il Playwright MCP (executeautomation, ~33 tool) è già attivo in sessione.
- `browse` (gstack) copre QA/navigazione ed è mandatorio da CLAUDE.md.
- `ui-stress` ha già il suo stack Playwright autosufficiente.
- La SKILL.md ufficiale è già su disco dentro gstack:
  `~/.claude/skills/gstack/node_modules/playwright-core/lib/tools/skills/playwright-cli/SKILL.md`

Mossa futura sensata (decisione founder): "replace MCP" — disattivare
mcp__playwright__* e installare `@playwright/cli` + skill ufficiale per igiene
contesto (~10k token fissi recuperati). I browser binaries sono già installati,
non riscaricherebbe Chromium.

Nota frontmatter della skill ufficiale: `allowed-tools: Bash(playwright-cli:*)
Bash(npx:*) Bash(npm:*)` — wildcard npm/npx, da sapere se la si registra.
Skill community (lackeyjb ecc.): superate dall'ufficiale, non installare.
