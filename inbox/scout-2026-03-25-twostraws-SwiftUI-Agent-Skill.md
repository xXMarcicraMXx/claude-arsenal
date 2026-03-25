---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code skill"
  quality_score: 83
  scoring_breakdown:
    stars: 30
    recency: 20
    docs: 20
    community: 13
github_data:
  full_name: "twostraws/SwiftUI-Agent-Skill"
  url: "https://github.com/twostraws/SwiftUI-Agent-Skill"
  description: "SwiftUI agent skill for Claude Code, Codex, and other AI tools."
  stars: 3049
  forks: 99
  open_issues: 8
  language: ""
  license: "MIT"
  last_push: "2026-03-11"
  created: "2026-03-05"
  topics: []
---

# twostraws/SwiftUI-Agent-Skill

> Discovered by arsenal scout — awaiting manual triage

## Description

SwiftUI agent skill for Claude Code, Codex, and other AI tools.

## README Excerpt

<p align="center">
    <img src="assets/logo.svg" alt="SwiftUI Pro - Agent Skill for Claude Code, Codex, and Gemini" height="100" />
</p>

<h1 align="center">SwiftUI Agent Skill for AI Coding Assistants</h1>

<p align="center">
    <img src="https://img.shields.io/badge/iOS-26+-2980b9.svg" alt="Designed for iOS 26 and later." />
    <img src="https://img.shields.io/badge/swift-6.2+-8e44ad.svg" alt="Designed for Swift 6.2 and later." />
    <a href="https://twitter.com/twostraws">
        <img src="https://img.shields.io/badge/Contact-@twostraws-95a5a6.svg?style=flat" alt="Twitter: @twostraws" />
    </a>
</p>

An agent skill that helps AI coding assistants write smarter, simpler, and more modern SwiftUI, including guidance on API usage, design, performance, and accessibility. Covers navigation, layout, animations, state management, VoiceOver, deprecated API, and more, targeting the mistakes LLMs actually make.

Also available:

- [SwiftData Pro](https://github.com/twostraws/SwiftData-Agent-Skill)
- [Swift Concurrency Pro](https://github.com/twostraws/Swift-Concurrency-Agent-Skill)
- [Swift Testing Pro](https://github.com/twostraws/Swift-Testing-Agent-Skill)

Find more agent skills for Swift and Apple platform development at [Swift Agent Skills](https://github.com/twostraws/Swift-Agent-Skills).

The skill builds upon my existing [AGENTS.md](https://github.com/twostraws/SwiftAgents) file, meaning that you can bring years of knowledge and practical experience into your coding agent of choice in just a few minutes. It uses the [Agent Skills](https://agentskills.io/home) format, so it works smoothly with Claude Code, Codex, Gemini, Cursor, and more.


## Installing SwiftUI Pro

You can install this skill into Claude Code, Codex, Gemini, Cursor, and more by using `npx`:

```bash
npx skills add https://github.com/twostraws/swiftui-agent-skill --skill swiftui-pro
```

If you get the error `npx: command not found`, it means you don’t currently have Node installed. You need to run this command to install Node through Homebrew:

```bash
brew install node
```

And if *that* fails it usually means you need to [install Homebrew](https://brew.sh) first.

When using `npx`, you can select exactly which agents you want to use during the installation. You can also select whether the skill should be installed just for one project, or whether it should be made available for all your projects.

Alternatively, you can clone this whole repository and install it however you want.

If you're using Xcode, watch the YouTube video on [How to Install and Use Agent Skills in Xcode](https://www.youtube.com/watch?v=nKVZBKoB6P4) for a walkthrough.


## Using SwiftUI Pro

The skill is called SwiftUI Pro, and can be triggered in various ways. For example, in Claude Code you would use this:

> /swiftui-pro

And in Codex you would use this:

> $swiftui-pro

In both cases you can provide specific instructions if you want only a partial review. For example, `/swiftui-pro Check for depr

## Links

- Repository: https://github.com/twostraws/SwiftUI-Agent-Skill
