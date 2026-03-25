"""
GitHub REST API search source for the arsenal scout.
No LLM calls. Uses only the GitHub public API.
"""
import base64
import os
import time
from datetime import datetime, timezone

import requests

from sources.scoring import compute_quality_score_detailed


def _days_since(iso_date: str) -> int:
    """Return days elapsed since an ISO-8601 UTC timestamp."""
    dt = datetime.strptime(iso_date, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - dt).days


def apply_hard_filters(repo: dict, config: dict) -> bool:
    """Return True if repo passes all hard filters from config."""
    if config.get("exclude_forks") and repo.get("fork"):
        return False
    if config.get("exclude_archived") and repo.get("archived"):
        return False
    if repo.get("stargazers_count", 0) < config.get("min_stars", 0):
        return False
    days = _days_since(repo["pushed_at"])
    if days > config.get("max_days_since_last_push", 180):
        return False
    if config.get("must_have_license") and not repo.get("license"):
        return False
    return True


def build_repo_dict(repo: dict, readme_response: dict | None) -> dict:
    """Build a normalized repo dict from GitHub API response + README response."""
    readme_content = ""
    readme_length = 0
    if readme_response and readme_response.get("encoding") == "base64":
        try:
            raw = base64.b64decode(readme_response["content"].replace("\n", "")).decode(
                "utf-8", errors="replace"
            )
            readme_content = raw[:3000]
            readme_length = len(raw)
        except Exception:
            pass

    days_since_push = _days_since(repo["pushed_at"])

    return {
        "full_name": repo["full_name"],
        "description": repo.get("description") or "",
        "url": repo["html_url"],
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "open_issues": repo["open_issues_count"],
        "language": repo.get("language") or "",
        "license": repo.get("license", {}).get("spdx_id") if repo.get("license") else None,
        "last_push": repo["pushed_at"][:10],
        "created": repo["created_at"][:10],
        "topics": repo.get("topics") or [],
        "homepage": repo.get("homepage") or "",
        "has_issues": repo.get("has_issues", False),
        "has_wiki": repo.get("has_wiki", False),
        "days_since_push": days_since_push,
        "readme_length": readme_length,
        "readme_excerpt": readme_content,
        "source": "github_search",
    }


class GitHubSearchSource:
    BASE = "https://api.github.com"

    def __init__(self, config: dict, scoring_config: dict):
        self.config = config
        self.scoring_config = scoring_config
        token = os.environ.get(config.get("token_env", "GITHUB_TOKEN"), "")
        self.headers = {"Accept": "application/vnd.github+json"}
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def _get(self, url: str, params: dict = None) -> requests.Response:
        resp = requests.get(url, headers=self.headers, params=params, timeout=30)
        remaining = int(resp.headers.get("X-RateLimit-Remaining", "100"))
        if remaining < 5:
            reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
            sleep_secs = max(reset - time.time() + 5, 10)
            print(f"[github] Rate limit low ({remaining}), sleeping {sleep_secs:.0f}s")
            time.sleep(sleep_secs)
        return resp

    def _fetch_readme(self, full_name: str) -> dict | None:
        try:
            resp = self._get(f"{self.BASE}/repos/{full_name}/readme")
            if resp.status_code == 200:
                return resp.json()
        except Exception:
            pass
        return None

    def search(self, seen: set) -> list[dict]:
        """Search GitHub for all configured queries. Return passing repos not in seen."""
        results = []
        seen_in_run = set()

        for query in self.config.get("search_queries", []):
            print(f"[github] Searching: {query}")
            try:
                resp = self._get(
                    f"{self.BASE}/search/repositories",
                    params={
                        "q": query,
                        "sort": "stars",
                        "order": "desc",
                        "per_page": self.config.get("results_per_query", 30),
                    },
                )
                if resp.status_code != 200:
                    print(f"[github] Error {resp.status_code} for query: {query}")
                    continue

                items = resp.json().get("items", [])
                for item in items:
                    full_name = item["full_name"]
                    if full_name in seen or full_name in seen_in_run:
                        continue
                    if not apply_hard_filters(item, self.config):
                        continue

                    readme = self._fetch_readme(full_name)
                    repo_dict = build_repo_dict(item, readme)
                    repo_dict["query_matched"] = query

                    if self.config.get("must_have_readme") and repo_dict.get("readme_length", 0) == 0:
                        continue

                    breakdown = compute_quality_score_detailed(repo_dict, self.scoring_config)
                    repo_dict["quality_score"] = breakdown["score"]
                    repo_dict["_score_stars"] = breakdown["stars"]
                    repo_dict["_score_recency"] = breakdown["recency"]
                    repo_dict["_score_docs"] = breakdown["docs"]
                    repo_dict["_score_community"] = breakdown["community"]

                    results.append(repo_dict)
                    seen_in_run.add(full_name)

                time.sleep(1)

            except Exception as e:
                print(f"[github] Exception for query '{query}': {e}")

        return results
