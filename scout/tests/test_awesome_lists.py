import base64
from unittest.mock import MagicMock, patch

import pytest

from sources.awesome_lists import AwesomeListSource, extract_github_links


def make_readme_response(content: str):
    encoded = base64.b64encode(content.encode()).decode()
    resp = MagicMock()
    resp.status_code = 200
    resp.json.return_value = {"content": encoded + "\n", "encoding": "base64"}
    resp.headers = {"X-RateLimit-Remaining": "100"}
    return resp


README_WITH_LINKS = """
# Awesome Claude Code

## Tools

- [Cool MCP Server](https://github.com/alice/cool-mcp) - A great tool
- [Another Tool](https://github.com/bob/another-tool) - Another great one
- [Not GitHub](https://example.com/tool) - This should be ignored
- [Duplicate](https://github.com/alice/cool-mcp) - Already listed above
"""


def test_extract_github_links_finds_repos():
    links = extract_github_links(README_WITH_LINKS)
    assert "alice/cool-mcp" in links
    assert "bob/another-tool" in links


def test_extract_github_links_excludes_non_github():
    links = extract_github_links(README_WITH_LINKS)
    assert not any("example.com" in l for l in links)


def test_extract_github_links_deduplicates():
    links = extract_github_links(README_WITH_LINKS)
    assert links.count("alice/cool-mcp") == 1


def test_awesome_list_source_skips_seen():
    config = {
        "repos": ["hesreallyhim/awesome-claude-code"],
        "min_stars": 30,
        "max_days_since_last_push": 180,
        "must_have_license": True,
        "exclude_forks": True,
        "exclude_archived": True,
    }
    scoring_config = {
        "stars_max_points": 40,
        "recency_max_points": 25,
        "docs_max_points": 20,
        "community_max_points": 15,
    }
    seen = {"alice/cool-mcp", "bob/another-tool"}

    readme_resp = make_readme_response(README_WITH_LINKS)

    with patch("sources.awesome_lists.requests.get", return_value=readme_resp):
        source = AwesomeListSource(config, scoring_config)
        results = source.search(seen)

    assert len(results) == 0
