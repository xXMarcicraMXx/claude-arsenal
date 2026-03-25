import base64
from datetime import datetime, timedelta, timezone
from unittest.mock import MagicMock, patch

import pytest

from sources.github_search import GitHubSearchSource, apply_hard_filters, build_repo_dict


def utc_days_ago(n):
    return (datetime.now(timezone.utc) - timedelta(days=n)).strftime("%Y-%m-%dT%H:%M:%SZ")


SAMPLE_REPO = {
    "full_name": "owner/repo",
    "description": "A great tool",
    "html_url": "https://github.com/owner/repo",
    "stargazers_count": 500,
    "forks_count": 30,
    "open_issues_count": 5,
    "pushed_at": utc_days_ago(10),
    "created_at": utc_days_ago(200),
    "license": {"spdx_id": "MIT"},
    "language": "Python",
    "topics": ["mcp", "claude"],
    "homepage": None,
    "fork": False,
    "archived": False,
    "has_issues": True,
    "has_wiki": False,
}

FILTER_CONFIG = {
    "min_stars": 30,
    "max_days_since_last_push": 180,
    "must_have_readme": True,
    "must_have_license": True,
    "exclude_forks": True,
    "exclude_archived": True,
}


def test_apply_hard_filters_passes_valid_repo():
    repo = dict(SAMPLE_REPO)
    assert apply_hard_filters(repo, FILTER_CONFIG) is True


def test_apply_hard_filters_rejects_fork():
    repo = dict(SAMPLE_REPO, fork=True)
    assert apply_hard_filters(repo, FILTER_CONFIG) is False


def test_apply_hard_filters_rejects_archived():
    repo = dict(SAMPLE_REPO, archived=True)
    assert apply_hard_filters(repo, FILTER_CONFIG) is False


def test_apply_hard_filters_rejects_low_stars():
    repo = dict(SAMPLE_REPO, stargazers_count=5)
    assert apply_hard_filters(repo, FILTER_CONFIG) is False


def test_apply_hard_filters_rejects_stale():
    repo = dict(SAMPLE_REPO, pushed_at=utc_days_ago(200))
    assert apply_hard_filters(repo, FILTER_CONFIG) is False


def test_apply_hard_filters_rejects_no_license():
    repo = dict(SAMPLE_REPO, license=None)
    assert apply_hard_filters(repo, FILTER_CONFIG) is False


def test_build_repo_dict_extracts_fields():
    readme_content = "x" * 3000
    encoded = base64.b64encode(readme_content.encode()).decode()
    readme_response = {"content": encoded + "\n", "encoding": "base64"}
    result = build_repo_dict(SAMPLE_REPO, readme_response)

    assert result["full_name"] == "owner/repo"
    assert result["stars"] == 500
    assert result["forks"] == 30
    assert result["readme_length"] == 3000
    assert result["has_issues"] is True
    assert "days_since_push" in result
    assert result["days_since_push"] >= 10


def test_build_repo_dict_handles_missing_readme():
    result = build_repo_dict(SAMPLE_REPO, None)
    assert result["readme_length"] == 0
    assert result["readme_excerpt"] == ""


SCORING_CONFIG = {
    "stars_max_points": 40,
    "recency_max_points": 25,
    "docs_max_points": 20,
    "community_max_points": 15,
}


def test_github_search_source_skips_seen_repos():
    config = {
        "token_env": "GITHUB_TOKEN",
        "search_queries": ["claude mcp"],
        "results_per_query": 5,
        **FILTER_CONFIG,
    }
    seen = {"owner/repo"}

    mock_search_response = MagicMock()
    mock_search_response.status_code = 200
    mock_search_response.headers = {"X-RateLimit-Remaining": "100"}
    mock_search_response.json.return_value = {"items": [SAMPLE_REPO]}

    with patch("sources.github_search.requests.get", return_value=mock_search_response):
        source = GitHubSearchSource(config, SCORING_CONFIG)
        results = source.search(seen)

    assert len(results) == 0


def _make_search_response(items):
    mock = MagicMock()
    mock.status_code = 200
    mock.headers = {"X-RateLimit-Remaining": "100"}
    mock.json.return_value = {"items": items}
    return mock


def _make_readme_response(content: str):
    encoded = base64.b64encode(content.encode()).decode()
    mock = MagicMock()
    mock.status_code = 200
    mock.headers = {"X-RateLimit-Remaining": "100"}
    mock.json.return_value = {"content": encoded, "encoding": "base64"}
    return mock


def test_search_result_has_scoring_breakdown_fields():
    config = {
        "token_env": "GITHUB_TOKEN",
        "search_queries": ["claude mcp"],
        "results_per_query": 5,
        **FILTER_CONFIG,
    }

    search_mock = _make_search_response([SAMPLE_REPO])
    readme_mock = _make_readme_response("x" * 3000)

    with patch("sources.github_search.requests.get", side_effect=[search_mock, readme_mock]):
        source = GitHubSearchSource(config, SCORING_CONFIG)
        results = source.search(set())

    assert len(results) == 1
    repo = results[0]
    for key in ("_score_stars", "_score_recency", "_score_docs", "_score_community"):
        assert key in repo, f"Missing key: {key}"
        assert repo[key] >= 0, f"{key} should be non-negative"


def test_must_have_readme_filters_out_empty_readme():
    config = {
        "token_env": "GITHUB_TOKEN",
        "search_queries": ["claude mcp"],
        "results_per_query": 5,
        "must_have_readme": True,
        "min_stars": 0,
        "max_days_since_last_push": 365,
        "exclude_forks": False,
        "exclude_archived": False,
        "must_have_license": False,
    }

    search_mock = _make_search_response([SAMPLE_REPO])
    # README fetch returns 404
    no_readme_mock = MagicMock()
    no_readme_mock.status_code = 404
    no_readme_mock.headers = {"X-RateLimit-Remaining": "100"}

    with patch("sources.github_search.requests.get", side_effect=[search_mock, no_readme_mock]):
        source = GitHubSearchSource(config, SCORING_CONFIG)
        results = source.search(set())

    assert len(results) == 0


def test_must_have_readme_false_allows_empty_readme():
    config = {
        "token_env": "GITHUB_TOKEN",
        "search_queries": ["claude mcp"],
        "results_per_query": 5,
        "must_have_readme": False,
        "min_stars": 0,
        "max_days_since_last_push": 365,
        "exclude_forks": False,
        "exclude_archived": False,
        "must_have_license": False,
    }

    search_mock = _make_search_response([SAMPLE_REPO])
    no_readme_mock = MagicMock()
    no_readme_mock.status_code = 404
    no_readme_mock.headers = {"X-RateLimit-Remaining": "100"}

    with patch("sources.github_search.requests.get", side_effect=[search_mock, no_readme_mock]):
        source = GitHubSearchSource(config, SCORING_CONFIG)
        results = source.search(set())

    assert len(results) == 1
