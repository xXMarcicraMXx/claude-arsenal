---
id: TIP-225
title: "Web Design Guidelines — review UI ufficiale Vercel"
category: prompts
source_type: manual
risk_level: REVIEW
quality_score: 8
ai_summary: "Skill ufficiale Vercel che fa review di UI contro le Web Interface Guidelines (100+ regole a11y/focus/form/motion/dark-mode); fetcha le regole da GitHub a ogni run."
tags: [design, review, accessibility, vercel, skill]
source: "https://github.com/vercel-labs/agent-skills"
github_url: "https://github.com/vercel-labs/agent-skills"
github_stars: "30600"
github_last_push: "2026-08"
date_added: 2026-08-29
validated: true
related_tips: [TIP-223]
use_cases:
  - "review di codice UI contro best practice (a11y, focus, form, animazioni, dark mode)"
  - "già installata in ~/.claude/skills/web-design-guidelines (v1.0.0, allineata upstream)"
dependencies: []
platform: all
claude_code_version: "any"
---

# Web Design Guidelines (vercel-labs/agent-skills)

GIÀ INSTALLATA e verificata il 2026-08-29: copia locale identica byte-per-byte
all'upstream v1.0.0. Un solo file SKILL.md, nessuno script.

Motivo del REVIEW (non SAFE): a ogni invocazione la skill istruisce l'agente a
fetchare via WebFetch le regole correnti da
`raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md`
— contenuto remoto non versionato iniettato a runtime. Oggi pulito (verificato)
e il proprietario è Vercel Labs, ma chi controlla quel branch può cambiare le
istruzioni future.

Mitigazione se serve portarla a SAFE: vendoring di command.md in locale o pin
dell'URL a uno SHA di commit, perdendo l'auto-aggiornamento.
