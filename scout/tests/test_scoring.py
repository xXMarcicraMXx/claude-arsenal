import pytest
from sources.scoring import compute_quality_score, compute_quality_score_detailed

SCORING_CONFIG = {
    "stars_max_points": 40,
    "recency_max_points": 25,
    "docs_max_points": 20,
    "community_max_points": 15,
}


def make_repo(**overrides):
    base = {
        "stars": 100,
        "days_since_push": 30,
        "readme_length": 3000,
        "forks": 10,
        "has_issues": True,
        "has_wiki": False,
    }
    base.update(overrides)
    return base


def test_zero_stars_contributes_zero():
    repo = make_repo(stars=0, forks=0, has_issues=False, has_wiki=False, readme_length=0, days_since_push=999)
    score = compute_quality_score(repo, SCORING_CONFIG)
    assert score == 0


def test_high_stars_approaches_max():
    repo = make_repo(stars=50000, days_since_push=1, readme_length=6000, forks=500, has_issues=True, has_wiki=True)
    score = compute_quality_score(repo, SCORING_CONFIG)
    assert score == 100


def test_recency_recent_push():
    repo = make_repo(days_since_push=3, stars=0, readme_length=0, forks=0, has_issues=False, has_wiki=False)
    score = compute_quality_score(repo, SCORING_CONFIG)
    assert score == 25


def test_recency_old_push():
    repo = make_repo(days_since_push=200, stars=0, readme_length=0, forks=0, has_issues=False, has_wiki=False)
    score = compute_quality_score(repo, SCORING_CONFIG)
    assert score == 0


def test_docs_long_readme():
    repo = make_repo(readme_length=6000, stars=0, days_since_push=999, forks=0, has_issues=False, has_wiki=False)
    score = compute_quality_score(repo, SCORING_CONFIG)
    assert score == 20


def test_docs_short_readme():
    repo = make_repo(readme_length=100, stars=0, days_since_push=999, forks=0, has_issues=False, has_wiki=False)
    score = compute_quality_score(repo, SCORING_CONFIG)
    assert score == 0


def test_community_has_issues_and_wiki():
    repo = make_repo(forks=0, has_issues=True, has_wiki=True, stars=0, days_since_push=999, readme_length=0)
    score = compute_quality_score(repo, SCORING_CONFIG)
    assert 7 <= score <= 8


def test_returns_integer():
    repo = make_repo()
    score = compute_quality_score(repo, SCORING_CONFIG)
    assert isinstance(score, int)


def test_score_never_exceeds_100():
    repo = make_repo(stars=1_000_000, days_since_push=1, readme_length=100_000, forks=100_000, has_issues=True, has_wiki=True)
    score = compute_quality_score(repo, SCORING_CONFIG)
    assert score <= 100


# ── compute_quality_score_detailed tests ─────────────────────────────────────

def test_detailed_returns_dict_with_all_keys():
    repo = make_repo()
    result = compute_quality_score_detailed(repo, SCORING_CONFIG)
    assert isinstance(result, dict)
    for key in ("score", "stars", "recency", "docs", "community"):
        assert key in result


def test_detailed_score_matches_compute_quality_score():
    repo = make_repo()
    assert compute_quality_score_detailed(repo, SCORING_CONFIG)["score"] == compute_quality_score(repo, SCORING_CONFIG)


def test_detailed_components_are_non_negative():
    repo = make_repo()
    result = compute_quality_score_detailed(repo, SCORING_CONFIG)
    assert result["stars"] >= 0
    assert result["recency"] >= 0
    assert result["docs"] >= 0
    assert result["community"] >= 0


def test_detailed_zero_repo_all_zeros():
    repo = make_repo(stars=0, forks=0, has_issues=False, has_wiki=False, readme_length=0, days_since_push=999)
    result = compute_quality_score_detailed(repo, SCORING_CONFIG)
    assert result == {"score": 0, "stars": 0, "recency": 0, "docs": 0, "community": 0}


def test_detailed_components_sum_to_score():
    repo = make_repo()
    result = compute_quality_score_detailed(repo, SCORING_CONFIG)
    assert result["stars"] + result["recency"] + result["docs"] + result["community"] == result["score"]
