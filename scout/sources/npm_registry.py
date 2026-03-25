"""
npm registry source for the arsenal scout.
Searches npm for MCP server packages and fetches GitHub data when available.
"""
import time
from datetime import datetime, timezone

import requests

from sources.github_search import build_repo_dict
from sources.scoring import compute_quality_score_detailed

NPM_SEARCH = "https://registry.npmjs.org/-/v1/search"
NPM_DOWNLOADS = "https://api.npmjs.org/downloads/point/last-week/{name}"
GITHUB_API = "https://api.github.com"


def _age_days(date_str: str) -> int:
    """Return days since an ISO-8601 date string."""
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return (datetime.now(timezone.utc) - dt).days
    except Exception:
        return 0


def passes_npm_filters(pkg: dict, min_weekly_downloads: int, min_age_days: int, weekly_downloads: int) -> bool:
    """Return True if npm package passes all hard filters."""
    if weekly_downloads < min_weekly_downloads:
        return False
    age = _age_days(pkg.get("date", ""))
    if age < min_age_days:
        return False
    return True


class NpmRegistrySource:
    def __init__(self, config: dict, scoring_config: dict):
        self.config = config
        self.scoring_config = scoring_config
        self.github_headers = {"Accept": "application/vnd.github+json"}

    def _get_downloads(self, name: str) -> int:
        try:
            resp = requests.get(NPM_DOWNLOADS.format(name=name), timeout=15)
            if resp.status_code == 200:
                return resp.json().get("downloads", 0)
        except Exception:
            pass
        return 0

    def _fetch_github_metadata(self, full_name: str) -> dict | None:
        try:
            resp = requests.get(
                f"{GITHUB_API}/repos/{full_name}",
                headers=self.github_headers,
                timeout=30,
            )
            if resp.status_code == 200:
                return resp.json()
        except Exception:
            pass
        return None

    def _github_slug_from_url(self, url: str) -> str | None:
        """Extract owner/repo from a GitHub URL."""
        if not url or "github.com" not in url:
            return None
        parts = url.rstrip("/").split("github.com/")[-1].split("/")
        if len(parts) >= 2:
            return f"{parts[0]}/{parts[1]}"
        return None

    def search(self, seen_repos: set, seen_npm: set) -> list:
        """Search npm for all configured keywords. Return passing packages."""
        results = []
        seen_in_run = set()

        min_downloads = self.config.get("min_weekly_downloads", 50)
        min_age = self.config.get("min_age_days", 14)

        for keyword in self.config.get("search_keywords", []):
            print(f"[npm] Searching: {keyword}")
            try:
                resp = requests.get(NPM_SEARCH, params={"text": keyword, "size": 50}, timeout=30)
                if resp.status_code != 200:
                    continue

                objects = resp.json().get("objects", [])
                for obj in objects:
                    pkg = obj.get("package", {})
                    name = pkg.get("name", "")

                    if not name or name in seen_npm or name in seen_in_run:
                        continue

                    downloads = self._get_downloads(name)
                    if not passes_npm_filters(pkg, min_downloads, min_age, downloads):
                        continue

                    github_url = pkg.get("links", {}).get("repository", "")
                    slug = self._github_slug_from_url(github_url)

                    if slug and (slug in seen_repos or slug in seen_in_run):
                        continue

                    entry = {
                        "npm_name": name,
                        "description": pkg.get("description", ""),
                        "weekly_downloads": downloads,
                        "version": pkg.get("version", ""),
                        "published": pkg.get("date", "")[:10],
                        "source": "npm_registry",
                        "query_matched": keyword,
                    }

                    if slug:
                        metadata = self._fetch_github_metadata(slug)
                        if metadata:
                            readme_resp = None
                            try:
                                r = requests.get(
                                    f"{GITHUB_API}/repos/{slug}/readme",
                                    headers=self.github_headers,
                                    timeout=30,
                                )
                                if r.status_code == 200:
                                    readme_resp = r.json()
                            except Exception:
                                pass
                            github_entry = build_repo_dict(metadata, readme_resp)
                            github_entry.update(entry)
                            github_entry["source"] = "npm_registry"
                            breakdown = compute_quality_score_detailed(github_entry, self.scoring_config)
                            github_entry["quality_score"] = breakdown["score"]
                            github_entry["_score_stars"] = breakdown["stars"]
                            github_entry["_score_recency"] = breakdown["recency"]
                            github_entry["_score_docs"] = breakdown["docs"]
                            github_entry["_score_community"] = breakdown["community"]
                            results.append(github_entry)
                            seen_in_run.add(slug)
                        else:
                            entry["stars"] = 0
                            entry["days_since_push"] = 0
                            entry["readme_length"] = 0
                            entry["forks"] = 0
                            entry["has_issues"] = False
                            entry["has_wiki"] = False
                            entry["quality_score"] = 20
                            entry["full_name"] = f"npm:{name}"
                            results.append(entry)
                    else:
                        entry["stars"] = 0
                        entry["days_since_push"] = 0
                        entry["readme_length"] = 0
                        entry["forks"] = 0
                        entry["has_issues"] = False
                        entry["has_wiki"] = False
                        entry["quality_score"] = 20
                        entry["full_name"] = f"npm:{name}"
                        results.append(entry)

                    seen_in_run.add(name)
                    time.sleep(0.3)

            except Exception as e:
                print(f"[npm] Exception for keyword '{keyword}': {e}")

        return results
