"""
Pure quality scoring function for arsenal scout.
No I/O, no network calls, no LLM — only math.
"""
import math


def compute_quality_score(repo: dict, scoring: dict) -> int:
    """
    Compute a 0-100 quality score for a repo based purely on metrics.

    Args:
        repo: dict with keys: stars, days_since_push, readme_length,
              forks, has_issues, has_wiki
        scoring: dict with keys: stars_max_points, recency_max_points,
                 docs_max_points, community_max_points

    Returns:
        Integer score 0-100.
    """
    score = 0

    # Stars (0-stars_max_points) — logarithmic scale, 50k stars = max
    if repo.get("stars", 0) > 0:
        normalized = min(math.log(repo["stars"]) / math.log(50000), 1.0)
        score += round(normalized * scoring["stars_max_points"])

    # Recency (0-recency_max_points)
    days = repo.get("days_since_push", 999)
    if days <= 7:
        r = 1.0
    elif days <= 30:
        r = 0.8
    elif days <= 90:
        r = 0.6
    elif days <= 180:
        r = 0.3
    else:
        r = 0.0
    score += round(r * scoring["recency_max_points"])

    # Documentation (0-docs_max_points)
    readme_len = repo.get("readme_length", 0)
    if readme_len > 5000:
        d = 1.0
    elif readme_len > 2000:
        d = 0.75
    elif readme_len > 500:
        d = 0.4
    else:
        d = 0.0
    score += round(d * scoring["docs_max_points"])

    # Community (0-community_max_points)
    forks = repo.get("forks", 0)
    c = 0.0
    if forks > 0:
        c += min(math.log(forks) / math.log(500), 1.0) * 0.5
    if repo.get("has_issues", False):
        c += 0.25
    if repo.get("has_wiki", False):
        c += 0.25
    score += round(c * scoring["community_max_points"])

    return score
