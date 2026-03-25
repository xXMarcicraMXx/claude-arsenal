# Claude Arsenal

A personal knowledge management system that makes Claude Code smarter over time.
Collects, validates, and serves curated tips, tools, MCP servers, configurations,
and workflows — so Claude Code surfaces tested community solutions instead of
building from scratch every time.

---

## What It Does

**Before creating anything from scratch, Claude checks this arsenal.**
If a community-tested tool exists that covers 80%+ of the need, Claude presents it
and asks if you want to use it instead. A repo with 500 stars and active maintenance
beats a one-off skill drafted in a single session.

**Two intake channels:**
1. **Manual** — paste a tip from LinkedIn, Instagram, Twitter/X, or raw text
2. **Scout (Phase 2)** — Python script runs weekly on VPS, deposits candidates automatically

**After intake, triage evaluates:**
- Duplicate detection (exact URL + functional overlap)
- Security risk (SAFE / REVIEW / DANGER / REJECT)
- Quality score (1-10, based on GitHub metrics + qualitative evaluation)
- AI Summary (one plain-language sentence describing what it actually does)

**LinkedIn content creation:**
Turn any arsenal finding into a professional LinkedIn post (3 tone variants),
or reference a video with your professional context layer on top.

---

## Directory Structure

```
claude-arsenal/
├── SKILL.md                    # Main skill — Claude Code reads this
├── catalog.md                  # Master table: all validated entries + AI summaries
├── inbox/                      # Staging area for raw tips awaiting triage
├── library/
│   ├── prompts/                # Prompt engineering for Claude Code
│   ├── configs/                # TOML, settings, .claude configurations
│   ├── scripts/                # Bash aliases, shell scripts, automations
│   ├── mcp-servers/            # Evaluated MCP servers
│   ├── workflows/              # Multi-step workflows and pipelines
│   ├── software/               # Standalone tools and solutions
│   └── ideas/                  # Ideas, patterns, conceptual approaches
├── rejected/                   # Entries that failed triage (with reason)
├── scripts/
│   └── triage.md               # Triage process instructions (read by Claude)
├── prompts/
│   └── linkedin-templates.md   # LinkedIn content creation reference
└── scout/
    └── README.md               # Phase 2: auto-discovery system spec
```

---

## How to Add Tips

### From social media

Open Claude Code in the claude-arsenal directory, then say:

```
Arsenal quick add — process this:

[paste LinkedIn post / tweet / Instagram URL / raw text here]

Source: @whoever on LinkedIn
```

### Triage the inbox (after scout runs — Phase 2)

```bash
git pull   # get scout deposits
```

Then say:
```
Read scripts/triage.md and process ALL files in the inbox/ directory.
```

---

## Risk Levels

| Level | Meaning | Behavior |
|-------|---------|----------|
| SAFE | Pure prompts, local configs, no installs | Applied automatically |
| REVIEW | Installs packages, adds MCP servers | Requires your confirmation |
| DANGER | Network calls, sudo, external data | Reference only, never auto-applied |
| REJECT | Duplicate, obsolete, clickbait, native CC | Discarded with reason |

---

## Supported Social Sources

| Platform | What Claude can do |
|----------|--------------------|
| LinkedIn | Extract post content, author, GitHub links |
| Twitter/X | Extract handle, text, code, links |
| Instagram/TikTok/YouTube | Cannot watch — asks you for key points |
| GitHub URL | Fetches repo metadata directly |
| Raw text | Parses and evaluates as-is |

---

## Global Installation (Windows)

The skill is available in all Claude Code projects via a Windows junction point:

```cmd
mklink /J C:\Users\mbern\.claude\skills\claude-arsenal C:\Users\mbern\claude-arsenal
```

Claude Code reads `SKILL.md` when relevant context is detected.

---

## LinkedIn Content Creation

Open Claude Code in the arsenal directory and say:

```
I want to create a LinkedIn post about TIP-042.
Give me 3 variants: discovery angle, how-I-use-it angle, bigger picture.
```

See `prompts/linkedin-templates.md` for the full template reference.

---

## Scout (Phase 2)

Automated discovery via Python cron on VPS `5.161.213.45`. See `scout/README.md`.
Zero LLM calls — all AI evaluation happens when you run triage manually.

---

## Cost

| Component | Cost |
|-----------|------|
| Scout (cron) | $0 — free APIs only |
| Triage + LinkedIn posts | $0 — your Max subscription |
| VPS | $0 — your existing server |
| **Total** | **$0 beyond existing subscription** |

---
