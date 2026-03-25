import json
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from scout import generate_inbox_entry, load_state, save_state, should_skip


def test_load_state_returns_empty_on_missing_file():
    with tempfile.TemporaryDirectory() as d:
        state = load_state(Path(d) / "state.json")
    assert state["repos"] == {}
    assert state["npm_packages"] == {}


def test_load_state_reads_existing_file():
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "state.json"
        data = {"repos": {"a/b": {"status": "deposited"}}, "npm_packages": {}, "run_stats": {}}
        path.write_text(json.dumps(data))
        state = load_state(path)
    assert "a/b" in state["repos"]


def test_save_state_writes_file():
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "state.json"
        state = {"repos": {"a/b": {}}, "npm_packages": {}, "run_stats": {}, "last_run": None}
        save_state(state, path)
        loaded = json.loads(path.read_text())
    assert "a/b" in loaded["repos"]


def test_should_skip_seen_repo():
    state = {"repos": {"owner/repo": {"status": "deposited"}}, "npm_packages": {}}
    repo = {"full_name": "owner/repo"}
    assert should_skip(repo, state) is True


def test_should_skip_new_repo():
    state = {"repos": {}, "npm_packages": {}}
    repo = {"full_name": "owner/new-repo"}
    assert should_skip(repo, state) is False


def test_should_skip_below_min_score():
    state = {"repos": {}, "npm_packages": {}}
    repo = {"full_name": "owner/repo", "quality_score": 10}
    assert should_skip(repo, state, min_score=35) is True


def test_generate_inbox_entry_contains_required_sections():
    repo = {
        "full_name": "owner/repo",
        "description": "A test repo",
        "url": "https://github.com/owner/repo",
        "stars": 500,
        "forks": 20,
        "open_issues": 5,
        "language": "Python",
        "license": "MIT",
        "last_push": "2026-03-20",
        "created": "2025-01-01",
        "topics": ["mcp"],
        "homepage": "",
        "quality_score": 55,
        "source": "github_search",
        "query_matched": "claude mcp",
        "readme_excerpt": "This is a readme",
    }
    entry = generate_inbox_entry(repo)
    assert "scout_metadata:" in entry
    assert "github_data:" in entry
    assert "README Excerpt" in entry
    assert "owner/repo" in entry


def test_should_skip_seen_npm():
    state = {"repos": {}, "npm_packages": {"my-package": {"status": "deposited"}}}
    repo = {"full_name": "npm:my-package"}
    assert should_skip(repo, state) is True
