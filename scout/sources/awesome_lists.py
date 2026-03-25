"""
Awesome-list source for the arsenal scout.
Downloads README.md from known awesome-lists and extracts GitHub repo links.
"""
import base64
import os
import re
import time

import requests

from sources.github_search import apply_hard_filters, build_repo_dict
from sources.scoring import compute_quality_score_detailed

GITHUB_LINK_RE = re.compile(r"github\.com/([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)")


def extract_github_links(readme_content: str) -> list:
    """Extract unique owner/repo slugs from markdown content."""
    matches = GITHUB_LINK_RE.findall(readme_content)
    seen = set()
    result = []
    for m in matches:
        slug = m.rstrip("/")
        if slug.endswith(".git"):
            slug = slug[:-4]
        if slug not in seen:
            seen.add(slug)
            result.append(slug)
    return result


class AwesomeListSource:
    BASE = "https://api.github.com"

    def __init__(self, config: dict, scoring_config: dict):
        self.config = config
        self.scoring_config = scoring_config
        token = os.environ.get("GITHUB_TOKEN", "")
        self.headers = {"Accept": "application/vnd.github+json"}
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def _get(self, url: str) -> requests.Response:
        resp = requests.get(url, headers=self.headers, timeout=30)
        remaining = int(resp.headers.get("X-RateLimit-Remaining", "100"))
        if remaining < 5:
            reset = int(resp.headers.get("X-RateLimit-Reset", time.time() + 60))
            sleep_secs = max(reset - time.time() + 5, 10)
            print(f"[awesome] Rate limit low ({remaining}), sleeping {sleep_secs:.0f}s")
            time.sleep(sleep_secs)
        return resp

    def _fetch_readme_content(self, list_repo: str) -> str:
        """Download and decode the README of an awesome-list repo."""
        try:
            resp = self._get(f"{self.BASE}/repos/{list_repo}/readme")
            if resp.status_code != 200:
                return ""
            data = resp.json()
            if data.get("encoding") == "base64":
                return base64.b64decode(data["content"].replace("\n", "")).decode(
                    "utf-8", errors="replace"
                )
        except Exception as e:
            print(f"[awesome] Failed to fetch {list_repo}: {e}")
        return ""

    def _fetch_repo_metadata(self, full_name: str) -> dict | None:
        try:
            resp = self._get(f"{self.BASE}/repos/{full_name}")
            if resp.status_code == 200:
                return resp.json()
        except Exception:
            pass
        return None

    def search(self, seen: set) -> list:
        """Scan all configured awesome-lists. Return new repos not in seen."""
        results = []
        seen_in_run = set()

        for list_repo in self.config.get("repos", []):
            print(f"[awesome] Scanning: {list_repo}")
            readme = self._fetch_readme_content(list_repo)
            if not readme:
                continue

            links = extract_github_links(readme)
            print(f"[awesome] Found {len(links)} GitHub links in {list_repo}")

            for slug in links:
                if slug in seen or slug in seen_in_run or slug == list_repo:
                    continue

                metadata = self._fetch_repo_metadata(slug)
                if not metadata:
                    continue

                if not apply_hard_filters(metadata, self.config):
                    continue

                readme_resp = None
                try:
                    r = self._get(f"{self.BASE}/repos/{slug}/readme")
                    if r.status_code == 200:
                        readme_resp = r.json()
                except Exception:
                    pass

                repo_dict = build_repo_dict(metadata, readme_resp)
                repo_dict["query_matched"] = f"awesome-list:{list_repo}"
                repo_dict["source"] = "awesome_list"

                breakdown = compute_quality_score_detailed(repo_dict, self.scoring_config)
                repo_dict["quality_score"] = breakdown["score"]
                repo_dict["_score_stars"] = breakdown["stars"]
                repo_dict["_score_recency"] = breakdown["recency"]
                repo_dict["_score_docs"] = breakdown["docs"]
                repo_dict["_score_community"] = breakdown["community"]

                results.append(repo_dict)
                seen_in_run.add(slug)
                time.sleep(0.5)

        return results
