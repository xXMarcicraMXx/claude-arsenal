"""
Claude Arsenal Scout — Main Orchestrator
Searches GitHub, npm, and awesome-lists for Claude Code tools.
Deposits candidates in inbox/ for manual triage.
NO LLM calls. Pure Python + free APIs.
"""
import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

from sources.github_search import GitHubSearchSource
from sources.awesome_lists import AwesomeListSource
from sources.npm_registry import NpmRegistrySource

SCOUT_DIR = Path(__file__).parent
ARSENAL_DIR = SCOUT_DIR.parent
CONFIG_PATH = SCOUT_DIR / "config.yaml"
STATE_PATH = SCOUT_DIR / "state.json"


# ── State helpers ────────────────────────────────────────────────────────────

def load_state(path: Path) -> dict:
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            pass
    return {
        "last_run": None,
        "repos": {},
        "npm_packages": {},
        "run_stats": {
            "total_runs": 0,
            "total_discovered": 0,
            "total_passed_filters": 0,
            "total_deposited": 0,
        },
    }


def save_state(state: dict, path: Path) -> None:
    path.write_text(json.dumps(state, indent=2, default=str))


def should_skip(repo: dict, state: dict, min_score: int = 0) -> bool:
    full_name = repo.get("full_name", "")
    if full_name.startswith("npm:"):
        npm_name = full_name[4:]
        if npm_name in state.get("npm_packages", {}):
            return True
    else:
        if full_name in state.get("repos", {}):
            return True
    if repo.get("quality_score", 0) < min_score:
        return True
    return False


# ── Inbox file generation ────────────────────────────────────────────────────

def generate_inbox_entry(repo: dict) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    score = repo.get("quality_score", 0)
    source = repo.get("source", "unknown")
    query = repo.get("query_matched", "")
    full_name = repo.get("full_name", "unknown")

    # Use actual scoring breakdown if available, otherwise estimate
    stars_pts = repo.get("_score_stars", 0)
    recency_pts = repo.get("_score_recency", 0)
    docs_pts = repo.get("_score_docs", 0)
    community_pts = repo.get("_score_community", 0)

    github_block = ""
    if not full_name.startswith("npm:"):
        github_block = f"""github_data:
  full_name: "{full_name}"
  url: "{repo.get('url', '')}"
  description: "{repo.get('description', '').replace('"', "'")}"
  stars: {repo.get('stars', 0)}
  forks: {repo.get('forks', 0)}
  open_issues: {repo.get('open_issues', 0)}
  language: "{repo.get('language', '')}"
  license: "{repo.get('license', '')}"
  last_push: "{repo.get('last_push', '')}"
  created: "{repo.get('created', '')}"
  topics: {json.dumps(repo.get('topics', []))}"""
    else:
        github_block = f"""npm_data:
  name: "{repo.get('npm_name', full_name[4:])}"
  weekly_downloads: {repo.get('weekly_downloads', 0)}
  version: "{repo.get('version', '')}"
  published: "{repo.get('published', '')}"""

    homepage = repo.get("homepage", "")
    homepage_line = f"\n- Homepage: {homepage}" if homepage else ""
    npm_url = (
        f"\n- npm: https://www.npmjs.com/package/{repo.get('npm_name', '')}"
        if repo.get("npm_name")
        else ""
    )

    return f"""---
scout_metadata:
  discovered_at: "{now}"
  source: {source}
  query_matched: "{query}"
  quality_score: {score}
  scoring_breakdown:
    stars: {stars_pts}
    recency: {recency_pts}
    docs: {docs_pts}
    community: {community_pts}
{github_block}
---

# {full_name}

> Discovered by arsenal scout — awaiting manual triage

## Description

{repo.get('description', 'No description available.')}

## README Excerpt

{repo.get('readme_excerpt', 'No README available.')[:3000]}

## Links

- Repository: {repo.get('url', 'N/A')}{homepage_line}{npm_url}
"""


# ── Git auto-commit ──────────────────────────────────────────────────────────

def git_commit_and_push(count: int, dry_run: bool) -> None:
    if dry_run or count == 0:
        return
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    try:
        subprocess.run(["git", "add", "inbox/", "scout/state.json"], cwd=ARSENAL_DIR, check=True)
        result = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ARSENAL_DIR)
        if result.returncode != 0:
            subprocess.run(
                ["git", "commit", "-m", f"scout: discovered {count} new candidates ({date})"],
                cwd=ARSENAL_DIR,
                check=True,
            )
            subprocess.run(["git", "push", "origin", "master"], cwd=ARSENAL_DIR, check=True)
            print(f"[scout] Committed and pushed {count} new candidates.")
    except subprocess.CalledProcessError as e:
        print(f"[scout] Git error: {e}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Claude Arsenal Scout")
    parser.add_argument("--dry-run", action="store_true", help="No writes, no git commit")
    parser.add_argument("--source", choices=["github", "awesome", "npm"], help="Run only one source")
    parser.add_argument("--force-rescan", action="store_true", help="Ignore state.json")
    parser.add_argument("--verbose", action="store_true", help="Print scoring breakdown")
    args = parser.parse_args()

    config = yaml.safe_load(CONFIG_PATH.read_text())
    state = load_state(STATE_PATH)
    if args.force_rescan:
        state["repos"] = {}
        state["npm_packages"] = {}

    seen_repos = set(state["repos"].keys())
    seen_npm = set(state["npm_packages"].keys())
    min_score = config["quality"]["min_score"]
    scoring_cfg = config["quality"]["scoring"]
    inbox_path = ARSENAL_DIR / "inbox"

    all_candidates = []

    if not args.source or args.source == "github":
        source = GitHubSearchSource(config["github"], scoring_cfg)
        candidates = source.search(seen_repos)
        print(f"[scout] GitHub: {len(candidates)} candidates")
        all_candidates.extend(candidates)

    if not args.source or args.source == "awesome":
        source = AwesomeListSource(config["awesome_lists"], scoring_cfg)
        candidates = source.search(seen_repos)
        print(f"[scout] Awesome-lists: {len(candidates)} candidates")
        all_candidates.extend(candidates)

    if not args.source or args.source == "npm":
        source = NpmRegistrySource(config["npm_registry"], scoring_cfg)
        candidates = source.search(seen_repos, seen_npm)
        print(f"[scout] npm: {len(candidates)} candidates")
        all_candidates.extend(candidates)

    state["run_stats"]["total_discovered"] = (
        state["run_stats"].get("total_discovered", 0) + len(all_candidates)
    )

    deposited = 0
    for repo in all_candidates:
        if should_skip(repo, state, min_score):
            continue

        full_name = repo.get("full_name", "")
        score = repo.get("quality_score", 0)

        if args.verbose:
            print(f"[scout] {full_name} — score: {score}")

        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        slug = full_name.replace("/", "-").replace(":", "-")
        filename = f"scout-{date_str}-{slug}.md"
        entry = generate_inbox_entry(repo)

        if not args.dry_run:
            (inbox_path / filename).write_text(entry, encoding="utf-8")
            if full_name.startswith("npm:"):
                state["npm_packages"][full_name[4:]] = {
                    "first_seen": date_str,
                    "version_at_discovery": repo.get("version", ""),
                    "status": "deposited",
                }
            else:
                state["repos"][full_name] = {
                    "first_seen": date_str,
                    "stars_at_discovery": repo.get("stars", 0),
                    "quality_score": score,
                    "status": "deposited",
                    "source": repo.get("source", "unknown"),
                }
        else:
            print(f"[dry-run] Would deposit: {filename} (score: {score})")

        deposited += 1

    state["run_stats"]["total_deposited"] = (
        state["run_stats"].get("total_deposited", 0) + deposited
    )
    state["run_stats"]["total_runs"] = state["run_stats"].get("total_runs", 0) + 1
    state["last_run"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    if not args.dry_run:
        save_state(state, STATE_PATH)

    print(f"[scout] Done. Deposited: {deposited} | Dry-run: {args.dry_run}")
    git_commit_and_push(deposited, args.dry_run)


if __name__ == "__main__":
    main()
