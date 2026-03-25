# Scout — Auto-Discovery System (Phase 2)

> **Status: Implemented. Run setup.sh on the VPS to deploy.**
> All 34 tests passing. Deployed via cron every Monday at 06:00 UTC.
> See git history for the complete implementation spec.

---

## What the Scout Will Do

A lightweight Python script that runs on the VPS (`5.161.213.45`) every Monday
at 06:00 UTC via cron. It searches GitHub, npm, and community awesome-lists for
high-quality Claude Code tools and deposits raw candidates into `inbox/` for
manual triage.

**Critical design constraint:** zero LLM calls. No Anthropic API, no AI.
Pure Python + free public APIs (GitHub REST, npm registry, HTTP).
All AI evaluation happens when the user manually runs triage in Claude Code.

---

## Planned Architecture

```
scout/
├── scout.py                # Main entry point
├── sources/
│   ├── github_search.py    # GitHub API search by keyword
│   ├── awesome_lists.py    # Parse awesome-lists for new entries
│   └── npm_registry.py     # Search npm for MCP server packages
├── config.yaml             # Search queries, thresholds, awesome-list sources
├── state.json              # Persistent state (repos already seen)
├── requirements.txt        # requests>=2.31.0, pyyaml>=6.0
└── setup.sh                # VPS auto-setup + cron registration
```

---

## Planned Sources

| Source | Method | Filter |
|--------|--------|--------|
| GitHub search | REST API `/search/repositories` | ≥30 stars, <180 days since push, has README + license |
| Awesome-lists | Parse README.md via GitHub API | 7 community lists (see spec) |
| npm registry | `/v1/search` + download stats | ≥50 weekly downloads, ≥14 days old |

---

## Planned Cron Schedule

```bash
0 6 * * 1   # Every Monday at 06:00 UTC
```

Deposits 5-15 candidates per run into `inbox/`. Commits and pushes automatically.

---

## Full Spec Reference

The complete implementation spec (PROMPT 4) covers: config.yaml content, quality
scoring algorithm (pure metrics, no LLM), inbox output format, setup.sh content,
and CLI flags (--dry-run, --verbose, --source, --force-rescan).

After writing, verify:
```bash
grep "Phase 2\|Not yet implemented\|scout.py" /c/Users/mbern/claude-arsenal/scout/README.md | wc -l
```

Expected: 3+ matches.
