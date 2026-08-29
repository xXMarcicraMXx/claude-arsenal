---
id: TIP-224
title: "Awesome Design Skills — 67 skill di stile auto-contenute"
category: prompts
source_type: manual
risk_level: SAFE
quality_score: 8
ai_summary: "67 skill di stile (glassmorphism, brutalism, bento, editorial…) con token colore, scala tipografica, do/don't e WCAG 2.2 AA — clonate come libreria locale, da attivare a richiesta."
tags: [design, styles, ui, library, skill]
source: "https://github.com/bergside/awesome-design-skills"
github_url: "https://github.com/bergside/awesome-design-skills"
github_stars: "2581"
github_last_push: "2026-06-28"
date_added: 2026-08-29
validated: true
related_tips: [TIP-223]
use_cases:
  - "quando serve una direzione estetica precisa (es. brutalism, bento, claymorphism) con token pronti"
  - "per attivare uno stile: copiare skills/<slug>/ da ~/.claude/design-library/awesome-design-skills in ~/.claude/skills/"
dependencies: []
platform: all
claude_code_version: "any"
---

# Awesome Design Skills (bergside)

CLONATO il 2026-08-29 in `~/.claude/design-library/awesome-design-skills/` (68 slug
sotto `skills/`). NON registrato come skill: 67 voci inquinerebbero il listing —
si attiva il singolo stile copiando la cartella in `~/.claude/skills/` quando serve.

Ogni stile: SKILL.md ~86 righe + DESIGN.md (token colore, scala tipografica,
do/don't, criteri WCAG 2.2 AA) + PNG di anteprima.

Security audit (2026-08-29): zero file eseguibili nel clone (solo md/png/json +
LICENSE). NON usare il canale `npx typeui.sh pull <slug>` del README (CLI npm di
terze parti non auditata) — la copia manuale basta.

Alternativa scartata: VoltAgent/awesome-claude-design (3.6k★) è solo un indice di
link a design system su getdesign.md, non installabile.
