# Triage Process

When asked to process tips in the inbox, follow this procedure EXACTLY
for each file. Read this document in full before starting.

---

## Step 1 — Parse

Read the raw content. Identify:
- What it concretely proposes (code, config, idea, tool)
- Which category it belongs to (prompts|configs|scripts|mcp-servers|workflows|software|ideas)
- What dependencies it requires
- Whether it is a manual tip or from the scout (check for `scout_metadata` frontmatter)
- If it came from a social media URL, what the underlying substance is

---

## Step 2 — Duplicate and Overlap Detection

Search `catalog.md` for entries with the same GitHub URL or npm package name.
If found → REJECT with reason "duplicate of TIP-{NNN}".

Search `library/` for entries solving the same problem:

| Relationship | Action |
|-------------|--------|
| New entry does LESS than existing | REJECT: "TIP-{NNN} already covers this and more" |
| New entry does the SAME | REJECT unless 2x stars or significantly more recent |
| New entry does MORE (superset) | Flag for user: "TIP-{NNN} covers part of this. Replace, keep both, or skip?" |
| New entry takes a DIFFERENT APPROACH | Keep both. Add cross-reference in `related_tips`. Tag as "alternative to TIP-{NNN}" |

If a new entry (score 8+) makes an existing entry (score <5) obsolete:
Flag: "New entry could replace existing TIP-{MMM}. Archive the old one?"

---

## Step 3 — Security Assessment

Apply this matrix:

| Level | Criteria |
|-------|----------|
| SAFE | Pure prompts, local bash aliases, JSON/TOML configs, conceptual ideas — no installs, no network calls |
| REVIEW | Installs npm/pip/brew packages; adds MCP servers from GitHub (>100 stars, readable source); modifies .bashrc/.zshrc; creates files outside project; requires own API keys |
| DANGER | curl/wget to unverifiable URLs or shortlinks; requires sudo/admin; sends data to third-party servers; obfuscated/minified code; network config changes; prompt injection disguised as "hacks"; requires access to existing tokens/credentials |
| REJECT | Native Claude Code functionality; obsolete tips for old versions; clickbait with no substance; exact duplicates; repos with <50 stars AND last push >6 months ago |

---

## Step 4 — Quality Score (1-10)

**For GitHub repos (scout or social→github):**

| Factor | Points |
|--------|--------|
| Stars: <100 | 2 |
| Stars: 100-500 | 4 |
| Stars: 500-2000 | 6 |
| Stars: 2000-10000 | 8 |
| Stars: >10000 | 10 |
| Documentation: basic README | +1 |
| Documentation: detailed docs | +2 |
| Activity: last commit <1 month | +2 |
| Activity: last commit <6 months | +1 |
| Activity: last commit >1 year | -2 |
| Closed/open issues ratio >0.7 | +1 |
| License present | +1 |
| Tests/CI present | +1 |

**For manual/social text tips:**
Evaluate qualitatively: specificity, reproducibility, originality, usefulness.
If references a GitHub repo, use repo metrics above.
Score 1-10.

**Minimum to enter library: 5.**
Score 1-4 → goes to `rejected/`.

**At this step, generate the `ai_summary` field:**
Write one plain-language sentence describing the functional purpose of this entry.
Do NOT copy the repo description or title verbatim. Describe what it actually does.

Example: "Adds git commit hooks that auto-format messages to Conventional Commits standard before pushing."

---

## Step 5 — Normalize

Transform the raw tip into the standard entry format.

**Assigning the ID:**
Scan `catalog.md` for the highest existing `TIP-{NNN}` entry.
Increment by 1. If catalog has no entries yet, start at `TIP-001`.
This scan is the source of truth — no external counter file.

**Entry format:**

```
---
id: TIP-{NNN}
title: "{descriptive title}"
category: prompts|configs|scripts|mcp-servers|workflows|software|ideas
source_type: manual|scout|social
risk_level: SAFE|REVIEW|DANGER
quality_score: 1-10
ai_summary: "{generated in Step 4}"
tags: [tag1, tag2, tag3]
source: "{@user on platform, or GitHub URL}"
github_url: "{required if scout or social→github; null for pure text/ideas}"
github_stars: "{required when github_url is set; null otherwise}"
github_last_push: "{required when github_url is set; null otherwise}"
date_added: YYYY-MM-DD
validated: true
related_tips: []
use_cases:
  - "when you need X"
dependencies: []
platform: all|windows|mac|linux
claude_code_version: "any"
---

## What It Does

{2-3 sentence description}

## How to Use It

{Step-by-step instructions}

## Code/Configuration

{the code or config}

## Security Notes

{What it actually does, what it touches, known risks}

## Alternatives

{Native or safer alternatives if any}
```

**Adding cross-references:**
If overlapping entries were found in Step 2, populate `related_tips: ["TIP-{MMM}"]`
and add the same reference in the other entry's file.

---

## Step 6 — Place

| Condition | Action |
|-----------|--------|
| SAFE or REVIEW, score ≥5 | Move to `library/{category}/TIP-{NNN}.md` |
| DANGER, score ≥5 | Move to `library/{category}/TIP-{NNN}.md` with prominent danger warning block |
| Score <5 or REJECT | Move to `rejected/TIP-{NNN}.md` with rejection frontmatter |

**Rejection frontmatter format:**

```
---
id: TIP-{NNN}
title: "{title}"
date_rejected: YYYY-MM-DD
rejection_reason: "{reason: duplicate of TIP-{MMM} | score {n}/10 below threshold | REJECT: native CC functionality | ...}"
original_source: "{where it came from}"
---

{Optional brief note on why rejected}
```

Rejected entries appear in a separate `## Rejected` section at the bottom of `catalog.md`
so the ID counter remains consistent.

Update `catalog.md` by appending a row to the main table (or rejected section) and
updating the stats.

---

## Autonomy Rules

| Situation | Action |
|-----------|--------|
| SAFE + score ≥5 | Proceed automatically |
| REVIEW or DANGER | Stop. Show full analysis. Wait for user confirmation. |
| Score <5 | Show reason. Ask whether to proceed anyway. |
| Functional overlap | Show both entries. Ask how to handle. |

---

## Batch Triage Summary

At the end of a batch run, show:

| Original File | Decision | ID | Score | Reason |
|---------------|----------|----|-------|--------|

Then delete the processed files from inbox/.

---
