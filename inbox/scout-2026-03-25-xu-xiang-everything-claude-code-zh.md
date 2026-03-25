---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code hook"
  quality_score: 72
  scoring_breakdown:
    stars: 20
    recency: 20
    docs: 20
    community: 12
github_data:
  full_name: "xu-xiang/everything-claude-code-zh"
  url: "https://github.com/xu-xiang/everything-claude-code-zh"
  description: "everything-claude-code 中文翻译项目：完整的 Claude Code 配置集合（agents, skills, hooks, commands, rules, MCPs）。源自 Anthropic 黑客松获胜者的实战配置，助力中文工程师高效理解与使用 Claude Code。"
  stars: 222
  forks: 48
  open_issues: 1
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-03-05"
  created: "2026-01-27"
  topics: ["ai-agents", "anthropic", "claude", "claude-code", "developer-tools", "everything-claude-code", "llm", "mcp", "oneskill", "productivity"]
---

# xu-xiang/everything-claude-code-zh

> Discovered by arsenal scout — awaiting manual triage

## Description

everything-claude-code 中文翻译项目：完整的 Claude Code 配置集合（agents, skills, hooks, commands, rules, MCPs）。源自 Anthropic 黑客松获胜者的实战配置，助力中文工程师高效理解与使用 Claude Code。

## README Excerpt

**语言:** [English](README.md) | **简体中文** | [繁體中文](docs/zh-TW/README.md)

# Everything Claude Code

[![Stars](https://img.shields.io/github/stars/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/stargazers)
[![Forks](https://img.shields.io/github/forks/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/network/members)
[![Contributors](https://img.shields.io/github/contributors/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/graphs/contributors)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Shell](https://img.shields.io/badge/-Shell-4EAA25?logo=gnu-bash&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Go](https://img.shields.io/badge/-Go-00ADD8?logo=go&logoColor=white)
![Java](https://img.shields.io/badge/-Java-ED8B00?logo=openjdk&logoColor=white)
![Markdown](https://img.shields.io/badge/-Markdown-000000?logo=markdown&logoColor=white)

> **50K+ stars** | **6K+ forks** | **30 contributors** | **6 种语言支持** | **Anthropic 黑客松获胜者**

---

<div align="center">

**🌐 Language / 语言 / 語言**

[**English**](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md)

</div>

---

**为 AI 智能体（Agent）框架打造的性能优化系统。源自 Anthropic 黑客松获胜作品。**

这不仅仅是配置文件。它是一个完整的系统：包含技能（Skills）、本能（Instincts）、内存优化、持续学习、安全扫描以及研究优先的开发模式。这些生产级的智能体（Agents）、钩子（Hooks）、命令（Commands）、规则（Rules）以及 MCP 配置，是在构建真实产品的 10 个多月高强度日常使用中演化而来的。

适用于 **Claude Code**, **Codex**, **Cowork** 以及其他 AI 智能体框架。

---

## 指南 (The Guides)

本仓库仅包含原始代码。指南部分解释了所有细节。

<table>
<tr>
<td width="50%">
<a href="https://x.com/affaanmustafa/status/2012378465664745795">
<img src="https://github.com/user-attachments/assets/1a471488-59cc-425b-8345-5245c7efbcef" alt="Everything Claude Code 简明指南" />
</a>
</td>
<td width="50%">
<a href="https://x.com/affaanmustafa/status/2014040193557471352">
<img src="https://github.com/user-attachments/assets/c9ca43bc-b149-427f-b551-af6840c368f0" alt="Everything Claude Code 详细指南" />
</a>
</td>
</tr>
<tr>
<td align="center"><b>简明指南 (Shorthand Guide)</b><br/>设置、基础知识、哲学。<b>请先阅读此篇。</b></td>
<td align="center"><b>详细指南 (Longform Guide)</b><br/>令牌（Token）优化、内存持久化、评测（Evals）、并行化。</td>
</tr>
</table>

| 主题 | 你将学到什么 |
|-------|-------------------|
| 令牌（Token）优化 | 模型选择、系统提示词瘦身、后台进程 |
| 内存持久化 | 跨会话自动保存/加载上下文的钩子 (Hooks) |
| 持续学习 | 自动将会话模式提取为可重用的技能 (Skills) |
| 验证循环 | 检查点 vs 持续评测、评分器类型、pass@k 指标 |
| 并行化 | Git worktrees、级联方法、何时扩展实例 |
| 子智能体编排 | 上下文问题、迭代检索模式 |

---

## 更新内容 (What's New)

### v1.7.0 — 跨平台扩展与演示文稿生成器 (2026年2月)

- **Codex 应用 + CLI 支持** — 直接支持基于 `AGENTS.md` 的 Codex，安装器目标定位及 Codex 文档
- **`frontend-slides` 技能 (Skill)** — 无依赖的 HTML 演示文稿生成器，包含 PPTX 转换指南和严格的视口自适应规则
- **5 个新型通用业务/内容技能** — `article-writing`（文章写作）、`content-engine`（内容引擎）、`market-research`（市场研究）、`investor-ma

## Links

- Repository: https://github.com/xu-xiang/everything-claude-code-zh
- Homepage: https://oneskill.one
