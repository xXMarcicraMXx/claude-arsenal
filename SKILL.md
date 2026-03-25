---
name: claude-arsenal
description: >
  Curated knowledge base of tips, configurations, scripts, MCP servers,
  workflows, and ideas for Claude Code, collected from social media,
  community, and automated GitHub discovery. Every entry has been validated
  for security and categorized. Consult this skill EVERY TIME you are about
  to propose a solution and want to check if a tested approach already exists
  in the library. Also consult when the task involves: Claude Code configuration,
  prompt optimization, MCP server setup, bash automation, development workflows,
  or when the user asks "do you have something for X" / "is there a better way
  to do Y". Also trigger when the user mentions "arsenal", "library", "tip",
  "trick", or references solutions seen on social media. Trigger when the user
  says "go scout" or "check for new tools". CRITICAL: trigger BEFORE creating
  any new skill, hook, workflow, or script — check if the arsenal already has
  a community-tested solution first.
---

# Claude Arsenal — Knowledge Base

This is a curated library of solutions, tips, configurations, and ideas for
Claude Code. Every entry has been validated for security and categorized.
Content comes from two channels: manual addition (by the user) and
auto-discovery (scout script scraping GitHub and community lists).

## Skill-First Check (MANDATORY)

THIS IS THE MOST IMPORTANT BEHAVIOR IN THIS SKILL.

Before creating ANY new skill, hook, subagent, workflow, script, or
configuration from scratch, you MUST:

1. Read catalog.md fully into context
2. Search for entries matching the problem by scanning: Title, Tags,
   AI Summary, and use_cases columns
3. If you find something relevant, present it to the user:
   "I found TIP-{NNN} — {ai_summary}. Score: {n}/10, Risk: {RISK}.
   Want to use this instead of building from scratch?"
4. ONLY if nothing relevant exists, OR the user explicitly says
   "no, build a new one", proceed with creating from scratch

If the catalog grows large (>300 entries), filter by Category first,
then read only the matching library/{category}/ files.

WHEN TO PREFER EXISTING:
- The existing tool does 80%+ of what's needed → use it
- The existing tool has >200 stars and active maintenance → strong signal
- The existing tool has tests, CI, docs → production-grade

WHEN TO BUILD NEW:
- Nothing in the arsenal covers this use case
- The existing tools are DANGER-rated and the user needs something safe
- The existing tools are stale (>1 year no updates, many open issues)
- The user's requirements are highly specific to their environment
- The user explicitly asks to build custom

## When to Consult This Library

- Before proposing solutions to common Claude Code problems
- When the user asks for configurations, optimizations, or workflows
- When an MCP server or tool is needed for a specific task
- To check if an approach has already been tested and documented
- When the user says "go scout" — run the interactive scout workflow

## How to Use the Library

1. Read catalog.md for a quick summary of all entries
2. Navigate the library/ directory by category
3. Every entry has YAML frontmatter with: risk_level, tags, ai_summary
4. ALWAYS respect the risk_level:
   - SAFE → Use freely, apply without asking
   - REVIEW → Flag to user before applying, explain what it does
   - DANGER → NEVER apply automatically, show as reference only

## Platform Behavior

When surfacing an entry, check the `platform` field.
If it does not match the user's current OS, flag it:
"Note: this entry is tagged {platform}-only."
Never suppress entries — the user decides.

## "Go Scout" Mode

When the user says "go scout" or "find new tools", execute this workflow:
1. Search GitHub API for Claude Code related repos (use scout/config.yaml
   queries as reference search terms if available)
2. Check awesome-lists for new entries not yet in library
3. For each candidate: evaluate quality (stars, activity, docs) and
   relevance (is it actually useful for Claude Code?)
4. Present findings as a table: Name | Stars | Category | Risk | Verdict
5. For approved entries, create them in library/ following the standard format
6. Update catalog.md

## Social Media Sources

The arsenal accepts tips from social media. When the user pastes a URL
or content from these sources:

### LinkedIn Posts
- Extract: author name/handle, post content, any code blocks or links
- If the post links to a GitHub repo, ALSO fetch the repo metadata
- Source field format: "@{author} on LinkedIn"

### Instagram / TikTok / YouTube Videos
- You CANNOT watch videos. Ask the user:
  "I can't watch this video directly. Could you:
  1. Paste the key points or transcript, OR
  2. Describe what the video demonstrates, OR
  3. Share any code/config shown in the video"
- Source field format: "@{author} on Instagram/TikTok/YouTube"

### Twitter/X Posts
- Extract: author handle, tweet content, any code/config/links
- Source field format: "@{handle} on X"

### General Rules
- ALWAYS trace back to the original source (social post → GitHub repo)
- Social proof (likes, shares, followers) is NOT a quality signal
- If a post just describes an idea with no code/repo → category "ideas"

## Entry Format

Every file in library/ follows this schema:

```yaml
---
id: TIP-{NNN}
title: "{descriptive title}"
category: prompts|configs|scripts|mcp-servers|workflows|software|ideas
source_type: manual|scout|social
risk_level: SAFE|REVIEW|DANGER
quality_score: 1-10
ai_summary: "{one-line functional description generated by Claude during triage}"
tags: [tag1, tag2, tag3]
source: "{@user on platform, or GitHub URL}"
github_url: "{required if scout or social→github; null for pure text/ideas}"
github_stars: "{required when github_url is set; null otherwise}"
github_last_push: "{required when github_url is set; null otherwise}"
date_added: YYYY-MM-DD
validated: true
related_tips: []
use_cases:
  - "when you need X"
dependencies: []
platform: all|windows|mac|linux
claude_code_version: "any"
---
```
