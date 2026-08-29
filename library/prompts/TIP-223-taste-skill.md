---
id: TIP-223
title: "Taste Skill — anti-slop frontend design framework"
category: prompts
source_type: manual
risk_level: SAFE
quality_score: 8
ai_summary: "Framework markdown anti-slop per landing/portfolio/redesign: brief inference, dial di varianza, direttive tipografia/colore/layout, checklist pre-flight 75+ voci."
tags: [design, frontend, anti-slop, landing-page, skill]
source: "https://github.com/Leonxlnx/taste-skill"
github_url: "https://github.com/Leonxlnx/taste-skill"
github_stars: "82200"
github_last_push: "2026-08-24"
date_added: 2026-08-29
validated: true
related_tips: [TIP-224, TIP-225]
use_cases:
  - "quando devi costruire una landing page, un portfolio o un redesign che non sembri templated"
  - "quando l'output di design dell'LLM collassa nei default (Inter + gradiente viola + 3 card)"
dependencies: []
platform: all
claude_code_version: "any"
---

# Taste Skill (Leonxlnx/taste-skill)

Il repo virale (~82k★, MIT) di skill di design per agenti. INSTALLATO il 2026-08-29:
- `~/.claude/skills/taste-skill/SKILL.md` (87 KB, nome frontmatter `design-taste-frontend`)
- `~/.claude/skills/image-to-code/SKILL.md` (36 KB, dallo stesso repo, skill `image-to-code-skill`)

Contenuto: brief inference obbligatoria prima del codice ("Design Read" in una riga),
3 dial 1-10 (DESIGN_VARIANCE 8, MOTION_INTENSITY 6, VISUAL_DENSITY 4), selezione
design system ufficiali (Material/Fluent/Carbon/shadcn/GOV.UK), lista di "AI tells"
vietati, dark mode, a11y, checklist pre-flight.

Security audit (2026-08-29): SKILL.md puro markdown, zero exec/fetch/credenziali.
Gli script del repo (`skill.sh`, `scripts/*.mjs`) sono tooling di build, letti e
innocui, NON copiati in locale.

Cautele d'uso:
- 87 KB pesano in contesto: invocare solo per lavoro di design vero.
- Default 8/6/4 spinge verso l'artsy/kinetic — per L'Agente tarare i dial più bassi.
- Scope dichiarato: landing/portfolio/redesign, NON dashboard o product UI multi-step.
