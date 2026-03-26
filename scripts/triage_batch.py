"""
triage_batch.py — Mechanical batch triage for scout inbox files.

Applies triage rules from scripts/triage.md automatically:
- Computes quality score from GitHub data
- Infers category from description/topics
- Assigns risk level based on category
- Writes library/{category}/TIP-NNN.md or rejected/TIP-NNN.md
- Updates catalog.md
- Deletes processed inbox files

Usage: python scripts/triage_batch.py [--dry-run] [--start-id NNN]
"""
import argparse
import math
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ARSENAL_DIR = Path(__file__).parent.parent
INBOX_DIR = ARSENAL_DIR / "inbox"
LIBRARY_DIR = ARSENAL_DIR / "library"
REJECTED_DIR = ARSENAL_DIR / "rejected"
CATALOG_PATH = ARSENAL_DIR / "catalog.md"

CATEGORIES = ["prompts", "configs", "scripts", "mcp-servers", "workflows", "software", "ideas"]

# Keywords for category inference (checked in order)
CATEGORY_RULES = [
    ("mcp-servers", ["mcp server", "mcp-server", "model context protocol server", " mcp ", "mcpserver"]),
    ("prompts",     ["prompt", "system prompt", "claude.md", "prompting", "proofreading"]),
    ("configs",     ["config", "settings", "setup", "configuration", "starter kit", "boilerplate", "dotfiles"]),
    ("scripts",     ["hook", "bash", "shell script", "automation", "alias", "audio", "notification"]),
    ("workflows",   ["agent", "skill", "workflow", "subagent", "plugin", "framework", "orchestrat", "multi-agent"]),
    ("software",    ["app", "tool", "desktop", "extension", "gui", "cli", "platform", "service"]),
    ("ideas",       ["awesome", "list", "catalog", "directory", "curated", "tutorial", "guide", "tips", "learn", "resource"]),
]

# Risk level by category
RISK_BY_CATEGORY = {
    "mcp-servers": "REVIEW",
    "prompts":     "SAFE",
    "configs":     "SAFE",  # most configs are just JSON/YAML
    "scripts":     "REVIEW",
    "workflows":   "REVIEW",
    "software":    "REVIEW",
    "ideas":       "SAFE",
}

# Override risk to SAFE for pure-markdown idea repos
FORCE_SAFE_KEYWORDS = ["awesome", "curated", "tips", "list", "guide", "tutorial", "learn", "resource", "catalog"]


def parse_inbox_file(path: Path) -> dict | None:
    """Parse YAML frontmatter + body from an inbox file."""
    text = path.read_text(encoding="utf-8")
    # Extract frontmatter between --- markers
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        return None
    try:
        fm = yaml.safe_load(match.group(1))
    except Exception:
        return None
    body = match.group(2)
    return {"frontmatter": fm, "body": body, "filename": path.name}


def days_since(date_str: str) -> int:
    """Days since a YYYY-MM-DD date string."""
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - d).days
    except Exception:
        return 999


def compute_quality_score(github_data: dict) -> int:
    """Compute 1-10 triage quality score from github_data."""
    stars = github_data.get("stars", 0)
    last_push = github_data.get("last_push", "2020-01-01")
    license_ = github_data.get("license")
    description = (github_data.get("description") or "").lower()

    # Stars base
    if stars >= 10000:
        score = 10
    elif stars >= 2000:
        score = 8
    elif stars >= 500:
        score = 6
    elif stars >= 100:
        score = 4
    else:
        score = 2

    # Recency
    d = days_since(last_push)
    if d <= 30:
        score += 2
    elif d <= 180:
        score += 1
    elif d > 365:
        score -= 2

    # License
    if license_ and license_ not in ("NOASSERTION", "OTHER", ""):
        score += 1

    # Rough docs/CI bonus: infer from star count as proxy
    if stars >= 1000:
        score += 1  # large repos usually have good docs

    return min(10, max(1, score))


def should_reject(github_data: dict) -> str | None:
    """Return rejection reason string, or None if should be accepted."""
    stars = github_data.get("stars", 0)
    last_push = github_data.get("last_push", "2020-01-01")
    d = days_since(last_push)

    if stars < 50 and d > 180:
        return f"score below threshold — {stars} stars and {d} days since last push"

    return None


def infer_category(github_data: dict) -> str:
    """Infer category from description and topics."""
    description = (github_data.get("description") or "").lower()
    topics = " ".join(github_data.get("topics") or []).lower()
    full_name = (github_data.get("full_name") or "").lower()
    combined = f"{description} {topics} {full_name}"

    for category, keywords in CATEGORY_RULES:
        for kw in keywords:
            if kw in combined:
                return category
    return "software"


def infer_risk(category: str, github_data: dict) -> str:
    """Infer risk level. Override to SAFE for pure-markdown repos."""
    description = (github_data.get("description") or "").lower()
    full_name = (github_data.get("full_name") or "").lower()
    language = (github_data.get("language") or "").lower()

    base_risk = RISK_BY_CATEGORY.get(category, "REVIEW")

    # Force SAFE for idea/list repos (usually pure markdown)
    if category == "ideas":
        return "SAFE"

    # Force SAFE for configs if clearly markdown-only
    if category == "configs" and language in ("", "markdown", "html"):
        return "SAFE"

    # Check for SAFE override keywords in description
    for kw in FORCE_SAFE_KEYWORDS:
        if kw in description or kw in full_name:
            if category in ("ideas", "prompts"):
                return "SAFE"

    return base_risk


def generate_ai_summary(github_data: dict, category: str) -> str:
    """Generate a one-sentence functional description (paraphrase of description)."""
    description = github_data.get("description") or ""
    full_name = github_data.get("full_name") or ""

    # Strip marketing noise
    description = re.sub(r"[⭐️🔊🌟💡🚀✨🎮]", "", description).strip()
    description = re.sub(r"\[.*?\]", "", description)
    description = re.sub(r"\(.*?\)", "", description)
    description = re.sub(r"Stars make.*?!", "", description, flags=re.IGNORECASE)
    description = re.sub(r"Perfect for.*?\.", "", description, flags=re.IGNORECASE)
    description = re.sub(r"Trusted by.*?\.", "", description, flags=re.IGNORECASE)
    description = description.strip(" .,!-")

    if not description:
        parts = full_name.split("/")[-1].replace("-", " ").replace("_", " ")
        description = f"Tool related to {parts}"

    # Ensure ends with period
    if not description.endswith("."):
        description += "."

    # Capitalize first letter
    return description[0].upper() + description[1:]


def generate_tags(github_data: dict, category: str) -> list:
    """Generate up to 5 tags from topics + category + language."""
    tags = list(github_data.get("topics") or [])[:3]
    language = (github_data.get("language") or "").lower()
    if language and language not in tags:
        tags.append(language)
    if category not in tags:
        tags.append(category)
    return tags[:5]


def library_entry(tip_id: str, github_data: dict, category: str, risk: str, score: int) -> str:
    """Generate full library entry markdown."""
    full_name = github_data.get("full_name", "")
    url = github_data.get("url") or f"https://github.com/{full_name}"
    stars = github_data.get("stars", 0)
    last_push = github_data.get("last_push", "unknown")
    language = github_data.get("language") or "unknown"
    license_ = github_data.get("license") or "unknown"

    ai_summary = generate_ai_summary(github_data, category)
    tags = generate_tags(github_data, category)
    tags_str = ", ".join(tags)

    # Infer use cases from category
    use_case_map = {
        "mcp-servers":  f"when you need {full_name.split('/')[-1].replace('-', ' ')} capabilities in Claude Code",
        "prompts":      "when you need structured prompts or CLAUDE.md templates",
        "configs":      "when setting up a new project's Claude Code configuration",
        "scripts":      "when automating Claude Code interactions via shell hooks",
        "workflows":    "when you need a multi-agent or multi-step workflow",
        "software":     f"when you need the {full_name.split('/')[-1].replace('-', ' ')} tool",
        "ideas":        "when researching Claude Code patterns, tools, or methodologies",
    }
    use_case = use_case_map.get(category, "when you need this capability")

    danger_block = ""
    if risk == "DANGER":
        danger_block = "\n> ⚠️ **DANGER**: This entry has elevated risk — review source carefully before use.\n"

    entry = f"""---
id: {tip_id}
title: "{full_name.split('/')[-1].replace('-', ' ').replace('_', ' ').title()}"
category: {category}
source_type: scout
risk_level: {risk}
quality_score: {score}
ai_summary: "{ai_summary}"
tags: [{tags_str}]
source: "{url}"
github_url: "{url}"
github_stars: {stars}
github_last_push: "{last_push}"
date_added: 2026-03-25
validated: true
related_tips: []
use_cases:
  - "{use_case}"
dependencies: [{language}]
platform: all
claude_code_version: "any"
---
{danger_block}
## What It Does

{ai_summary}

## How to Use It

See the repository README at {url} for full installation and usage instructions.

## Security Notes

{'Requires installation of ' + language + ' packages. Review the source before adding to global Claude Code settings.' if risk == 'REVIEW' else 'Safe to use — no installation or network calls required beyond the repo itself.'}

## Alternatives

See catalog.md for related entries in the {category} category.
"""
    return entry.strip()


def rejected_entry(tip_id: str, github_data: dict, reason: str) -> str:
    full_name = github_data.get("full_name", "")
    url = github_data.get("url") or f"https://github.com/{full_name}"
    return f"""---
id: {tip_id}
title: "{full_name}"
date_rejected: 2026-03-25
rejection_reason: "{reason}"
original_source: "{url}"
---
""".strip()


def scan_highest_tip(catalog_text: str) -> int:
    """Scan catalog.md for highest TIP-NNN number."""
    matches = re.findall(r"TIP-(\d{3,})", catalog_text)
    if not matches:
        return 0
    return max(int(m) for m in matches)


def update_catalog(catalog_path: Path, library_entries: list, rejected_entries: list) -> None:
    """Rewrite catalog.md with all new entries appended."""
    existing = catalog_path.read_text(encoding="utf-8")

    # Count existing stats
    safe_count = existing.count("| SAFE |")
    review_count = existing.count("| REVIEW |")
    danger_count = existing.count("| DANGER |")

    # Add new entries
    new_library_rows = []
    for e in library_entries:
        row = f"| {e['id']} | {e['title']} | {e['category']} | {e['risk']} | {e['score']} | {e['github_url']} | {e['tags']} | 2026-03-25 | {e['ai_summary'][:80]}... |"
        new_library_rows.append(row)
        if e['risk'] == 'SAFE':
            safe_count += 1
        elif e['risk'] == 'REVIEW':
            review_count += 1
        elif e['risk'] == 'DANGER':
            danger_count += 1

    new_rejected_rows = []
    for e in rejected_entries:
        row = f"| {e['id']} | {e['title']} | 2026-03-25 | {e['reason']} |"
        new_rejected_rows.append(row)

    total_library = safe_count + review_count + danger_count
    total_rejected = len(rejected_entries)
    scout_count = total_library + total_rejected

    # Build new catalog
    # Find and replace the placeholder rows
    lines = existing.splitlines()
    new_lines = []
    in_main_table = False
    in_rejected_table = False
    inserted_library = False
    inserted_rejected = False

    for line in lines:
        if line.startswith("| ID | Title | Category |"):
            new_lines.append(line)
            in_main_table = True
            in_rejected_table = False
            continue
        if line.startswith("| ID | Title | Date Rejected |"):
            new_lines.append(line)
            in_main_table = False
            in_rejected_table = True
            continue
        if line.startswith("|-") and in_main_table:
            new_lines.append(line)
            if not inserted_library:
                for row in new_library_rows:
                    new_lines.append(row)
                inserted_library = True
            continue
        if line.startswith("|-") and in_rejected_table:
            new_lines.append(line)
            if not inserted_rejected:
                new_lines.append("| TIP-001 | JDArmy/Evasion-SubAgents | 2026-03-25 | REJECT: malware tooling — shellcode loader and AV evasion framework |")
                for row in new_rejected_rows:
                    new_lines.append(row)
                inserted_rejected = True
            continue
        # Skip existing placeholder rows
        if line.startswith("| — |"):
            continue
        # Update header stats
        if line.startswith("> Last updated:"):
            new_lines.append(f"> Last updated: 2026-03-25")
            continue
        if line.startswith("> Total entries:"):
            new_lines.append(f"> Total entries: {total_library} | SAFE: {safe_count} | REVIEW: {review_count} | DANGER: {danger_count}")
            continue
        if line.startswith("> Sources:"):
            new_lines.append(f"> Sources: Manual: 0 | Scout: {scout_count} | Social: 0")
            continue
        # Update stats by category and risk
        if line.startswith("| prompts"):
            c = sum(1 for e in library_entries if e['category'] == 'prompts')
            scores = [e['score'] for e in library_entries if e['category'] == 'prompts']
            avg = f"{sum(scores)/len(scores):.1f}" if scores else "—"
            new_lines.append(f"| prompts     | {c}     | {avg}         |")
            continue
        if line.startswith("| configs"):
            c = sum(1 for e in library_entries if e['category'] == 'configs')
            scores = [e['score'] for e in library_entries if e['category'] == 'configs']
            avg = f"{sum(scores)/len(scores):.1f}" if scores else "—"
            new_lines.append(f"| configs     | {c}     | {avg}         |")
            continue
        if line.startswith("| scripts"):
            c = sum(1 for e in library_entries if e['category'] == 'scripts')
            scores = [e['score'] for e in library_entries if e['category'] == 'scripts']
            avg = f"{sum(scores)/len(scores):.1f}" if scores else "—"
            new_lines.append(f"| scripts     | {c}     | {avg}         |")
            continue
        if line.startswith("| mcp-servers"):
            c = sum(1 for e in library_entries if e['category'] == 'mcp-servers')
            scores = [e['score'] for e in library_entries if e['category'] == 'mcp-servers']
            avg = f"{sum(scores)/len(scores):.1f}" if scores else "—"
            new_lines.append(f"| mcp-servers | {c}     | {avg}         |")
            continue
        if line.startswith("| workflows"):
            c = sum(1 for e in library_entries if e['category'] == 'workflows')
            scores = [e['score'] for e in library_entries if e['category'] == 'workflows']
            avg = f"{sum(scores)/len(scores):.1f}" if scores else "—"
            new_lines.append(f"| workflows   | {c}     | {avg}         |")
            continue
        if line.startswith("| software"):
            c = sum(1 for e in library_entries if e['category'] == 'software')
            scores = [e['score'] for e in library_entries if e['category'] == 'software']
            avg = f"{sum(scores)/len(scores):.1f}" if scores else "—"
            new_lines.append(f"| software    | {c}     | {avg}         |")
            continue
        if line.startswith("| ideas"):
            c = sum(1 for e in library_entries if e['category'] == 'ideas')
            scores = [e['score'] for e in library_entries if e['category'] == 'ideas']
            avg = f"{sum(scores)/len(scores):.1f}" if scores else "—"
            new_lines.append(f"| ideas       | {c}     | {avg}         |")
            continue
        if line.startswith("| SAFE"):
            new_lines.append(f"| SAFE    | {safe_count}     |")
            continue
        if line.startswith("| REVIEW"):
            new_lines.append(f"| REVIEW  | {review_count}     |")
            continue
        if line.startswith("| DANGER"):
            new_lines.append(f"| DANGER  | {danger_count}     |")
            continue
        new_lines.append(line)

    catalog_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--start-id", type=int, default=None,
                        help="Starting TIP number (default: auto from catalog)")
    args = parser.parse_args()

    # Determine starting ID
    catalog_text = CATALOG_PATH.read_text(encoding="utf-8")
    if args.start_id is not None:
        next_id = args.start_id
    else:
        next_id = scan_highest_tip(catalog_text) + 1
        if next_id < 2:
            next_id = 2  # TIP-001 is reserved for JDArmy reject

    print(f"Starting at TIP-{next_id:03d}")

    inbox_files = sorted(INBOX_DIR.glob("scout-*.md"))
    print(f"Found {len(inbox_files)} inbox files to process")

    library_meta = []   # For catalog update
    rejected_meta = []  # For catalog update
    processed_files = []

    for inbox_path in inbox_files:
        data = parse_inbox_file(inbox_path)
        if not data:
            print(f"  SKIP (parse failed): {inbox_path.name}")
            continue

        fm = data["frontmatter"]
        github_data = fm.get("github_data", {})
        if not github_data:
            print(f"  SKIP (no github_data): {inbox_path.name}")
            continue

        tip_id = f"TIP-{next_id:03d}"
        next_id += 1

        # Check reject conditions
        reject_reason = should_reject(github_data)
        if reject_reason:
            print(f"  REJECT {tip_id}: {github_data.get('full_name')} — {reject_reason}")
            if not args.dry_run:
                content = rejected_entry(tip_id, github_data, reject_reason)
                out_path = REJECTED_DIR / f"{tip_id}.md"
                out_path.write_text(content, encoding="utf-8")
            rejected_meta.append({
                "id": tip_id,
                "title": github_data.get("full_name", ""),
                "reason": reject_reason,
            })
            processed_files.append(inbox_path)
            continue

        # Classify and score
        category = infer_category(github_data)
        risk = infer_risk(category, github_data)
        score = compute_quality_score(github_data)

        if score < 5:
            reason = f"score {score}/10 — below threshold"
            print(f"  REJECT {tip_id} (low score): {github_data.get('full_name')} — {reason}")
            if not args.dry_run:
                content = rejected_entry(tip_id, github_data, reason)
                out_path = REJECTED_DIR / f"{tip_id}.md"
                out_path.write_text(content, encoding="utf-8")
            rejected_meta.append({
                "id": tip_id,
                "title": github_data.get("full_name", ""),
                "reason": reason,
            })
            processed_files.append(inbox_path)
            continue

        # Write library entry
        full_name = github_data.get("full_name", "")
        url = github_data.get("url") or f"https://github.com/{full_name}"
        ai_summary = generate_ai_summary(github_data, category)
        tags = generate_tags(github_data, category)
        print(f"  ACCEPT {tip_id} [{category}/{risk}/{score}]: {full_name}")

        if not args.dry_run:
            out_dir = LIBRARY_DIR / category
            out_dir.mkdir(parents=True, exist_ok=True)
            content = library_entry(tip_id, github_data, category, risk, score)
            out_path = out_dir / f"{tip_id}.md"
            out_path.write_text(content, encoding="utf-8")

        library_meta.append({
            "id": tip_id,
            "title": full_name.split("/")[-1].replace("-", " ").replace("_", " ").title(),
            "category": category,
            "risk": risk,
            "score": score,
            "github_url": url,
            "tags": ", ".join(tags),
            "ai_summary": ai_summary,
        })
        processed_files.append(inbox_path)

    print(f"\nSummary: {len(library_meta)} accepted, {len(rejected_meta)} rejected")

    if not args.dry_run:
        print("Updating catalog.md...")
        update_catalog(CATALOG_PATH, library_meta, rejected_meta)

        print("Deleting processed inbox files...")
        for f in processed_files:
            f.unlink()

        print("Done.")
    else:
        print("[dry-run] No files written.")


if __name__ == "__main__":
    main()
