from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

import pytest

from sources.npm_registry import NpmRegistrySource, passes_npm_filters


def utc_days_ago(n):
    return (datetime.now(timezone.utc) - timedelta(days=n)).isoformat()


SAMPLE_PACKAGE = {
    "package": {
        "name": "mcp-server-example",
        "description": "An example MCP server",
        "links": {"repository": "https://github.com/owner/mcp-server-example"},
        "publisher": {"username": "alice"},
        "date": utc_days_ago(30),
        "version": "1.0.0",
    }
}


def test_passes_npm_filters_valid():
    assert passes_npm_filters(SAMPLE_PACKAGE["package"], min_weekly_downloads=50, min_age_days=14, weekly_downloads=200) is True


def test_passes_npm_filters_too_few_downloads():
    assert passes_npm_filters(SAMPLE_PACKAGE["package"], min_weekly_downloads=50, min_age_days=14, weekly_downloads=10) is False


def test_passes_npm_filters_too_new():
    new_pkg = dict(SAMPLE_PACKAGE["package"], date=utc_days_ago(5))
    assert passes_npm_filters(new_pkg, min_weekly_downloads=50, min_age_days=14, weekly_downloads=200) is False


def test_npm_source_skips_seen_packages():
    config = {
        "search_keywords": ["mcp-server"],
        "min_weekly_downloads": 50,
        "min_age_days": 14,
    }
    scoring_config = {
        "stars_max_points": 40,
        "recency_max_points": 25,
        "docs_max_points": 20,
        "community_max_points": 15,
    }
    seen_npm = {"mcp-server-example"}

    search_resp = MagicMock()
    search_resp.status_code = 200
    search_resp.json.return_value = {"objects": [SAMPLE_PACKAGE]}

    dl_resp = MagicMock()
    dl_resp.status_code = 200
    dl_resp.json.return_value = {"downloads": 500}

    with patch("sources.npm_registry.requests.get") as mock_get:
        mock_get.side_effect = [search_resp, dl_resp]
        source = NpmRegistrySource(config, scoring_config)
        results = source.search(set(), seen_npm)

    assert len(results) == 0
