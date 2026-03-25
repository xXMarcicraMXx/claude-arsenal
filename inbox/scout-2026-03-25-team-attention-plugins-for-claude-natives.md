---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code plugin"
  quality_score: 77
  scoring_breakdown:
    stars: 24
    recency: 20
    docs: 20
    community: 13
github_data:
  full_name: "team-attention/plugins-for-claude-natives"
  url: "https://github.com/team-attention/plugins-for-claude-natives"
  description: "Claude Code plugins for power users"
  stars: 690
  forks: 83
  open_issues: 7
  language: "Python"
  license: "MIT"
  last_push: "2026-03-12"
  created: "2026-01-01"
  topics: []
---

# team-attention/plugins-for-claude-natives

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Code plugins for power users

## README Excerpt

# Plugins for Claude Natives

A collection of Claude Code plugins for power users who want to extend Claude Code's capabilities beyond the defaults.

## Table of Contents

- [Quick Start](#quick-start)
- [Available Plugins](#available-plugins)
- [Plugin Details](#plugin-details)
  - [agent-council](#agent-council) - Get consensus from multiple AI models
  - [clarify](#clarify) - Transform vague requirements into specs
  - [dev](#dev) - Community scanning + technical decision-making
  - [doubt](#doubt) - Force Claude to re-validate responses
  - [interactive-review](#interactive-review) - Review plans with a web UI
  - [say-summary](#say-summary) - Hear responses via text-to-speech
  - [youtube-digest](#youtube-digest) - Summarize and quiz on YouTube videos
  - [gmail](#gmail) - Multi-account Gmail integration
  - [google-calendar](#google-calendar) - Multi-account calendar integration
  - [kakaotalk](#kakaotalk) - Send/read KakaoTalk messages on macOS
  - [session-wrap](#session-wrap) - Session wrap-up + history analysis toolkit
  - [team-assemble](#team-assemble) - Dynamic agent team orchestration
  - [podcast](#podcast) - Source-to-YouTube Korean podcast generator
- [Contributing](#contributing)
- [License](#license)

---

## Quick Start

```bash
# Add this marketplace to Claude Code
/plugin marketplace add team-attention/plugins-for-claude-natives

# Install any plugin
/plugin install <plugin-name>
```

---

## Available Plugins

| Plugin | Description |
|--------|-------------|
| [agent-council](./plugins/agent-council/) | Collect and synthesize opinions from multiple AI agents (Gemini, GPT, Codex) |
| [clarify](./plugins/clarify/) | Transform vague requirements into precise specifications through iterative questioning |
| [dev](./plugins/dev/) | Developer workflow: community opinion scanning and technical decision analysis |
| [doubt](./plugins/doubt/) | Force Claude to re-validate its response when `!rv` is in your prompt |
| [interactive-review](./plugins/interactive-review/) | Interactive markdown review with web UI for visual plan/document approval |
| [say-summary](./plugins/say-summary/) | Speaks a short summary of Claude's response using macOS TTS (Korean/English) |
| [youtube-digest](./plugins/youtube-digest/) | Summarize YouTube videos with transcript, insights, Korean translation, and quizzes |
| [gmail](./plugins/gmail/) | Multi-account Gmail integration with email reading, searching, sending, and management |
| [google-calendar](./plugins/google-calendar/) | Multi-account Google Calendar integration with parallel querying and conflict detection |
| [kakaotalk](./plugins/kakaotalk/) | Send and read KakaoTalk messages on macOS using Accessibility API |
| [session-wrap](./plugins/session-wrap/) | Session wrap-up, history analysis, and session validation toolkit |
| [team-assemble](./plugins/team-assemble/) | Dynamically assemble expert agent teams for complex tasks using Claude Code's agent teams feature |
| [podcast](./plugins/podc

## Links

- Repository: https://github.com/team-attention/plugins-for-claude-natives
