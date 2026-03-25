---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code configuration"
  quality_score: 73
  scoring_breakdown:
    stars: 18
    recency: 25
    docs: 20
    community: 10
github_data:
  full_name: "telagod/code-abyss"
  url: "https://github.com/telagod/code-abyss"
  description: "☠️ 一键为 Claude Code / Codex CLI 注入邪修人格与 40+ 安全工程秘典 | npx code-abyss"
  stars: 127
  forks: 11
  open_issues: 1
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-03-24"
  created: "2026-02-02"
  topics: ["ai-assistant", "blue-team", "claude-code", "cli", "codex-cli", "configuration", "prompt-engineering", "red-team", "security"]
---

# telagod/code-abyss

> Discovered by arsenal scout — awaiting manual triage

## Description

☠️ 一键为 Claude Code / Codex CLI 注入邪修人格与 40+ 安全工程秘典 | npx code-abyss

## README Excerpt

# ☠️ Code Abyss

<div align="center">

**邪修红尘仙 · 宿命深渊**

*一键为 Claude Code / Codex CLI 注入邪修人格与攻防安全工程知识体系*

[![npm](https://img.shields.io/npm/v/code-abyss.svg)](https://www.npmjs.com/package/code-abyss)
[![CI](https://github.com/telagod/code-abyss/actions/workflows/ci.yml/badge.svg)](https://github.com/telagod/code-abyss/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-blue.svg)]()
[![Node](https://img.shields.io/badge/Node.js-%3E%3D18-green.svg)]()

</div>

---

## 🚀 安装

```bash
npx code-abyss
```

交互式菜单（方向键选择，回车确认）：

```
☠️ Code Abyss v2.0.1

? 请选择操作 (Use arrow keys)
❯ 安装到 Claude Code (~/.claude/)
  安装到 Codex CLI   (~/.codex/)
  卸载 Claude Code
  卸载 Codex CLI
```

也可以直接指定：

```bash
npx code-abyss --target claude    # 安装到 ~/.claude/
npx code-abyss --target codex     # 安装到 ~/.codex/
npx code-abyss --target claude -y  # 零配置一键安装 (自动合并推荐配置)
npx code-abyss --target codex -y   # 零配置一键安装 (自动写入 config.toml 模板)
npx code-abyss --uninstall claude  # 卸载 Claude Code
npx code-abyss --uninstall codex   # 卸载 Codex CLI
```

### 安装流程

核心文件安装后，自动检测 API 认证状态：

```
── 认证检测 ──
✅ 已检测到认证: [custom] https://your-api.com
```

支持的认证方式：
- `claude login` / `codex login` (官方账号)
- 环境变量 `ANTHROPIC_API_KEY` / `OPENAI_API_KEY`
- 自定义 provider (`ANTHROPIC_BASE_URL` + `ANTHROPIC_AUTH_TOKEN`)

未检测到认证时会提示配置，可交互输入或跳过。

然后进入可选配置（空格选择，回车确认）：

```
? 选择要安装的配置 (Press <space> to select, <enter> to submit)
◉ 精细合并推荐 settings.json (保留现有配置)
◯ 安装 ccline 状态栏 (需要 Nerd Font)
```

- **settings.json 精细合并**：逐项合并推荐配置，已有的 key 不覆盖，缺失的 key 补上
- **ccline 状态栏**：自动安装 `@cometix/ccline` + `ccline --init` 生成配置 + 合并 statusLine 到 settings.json

> 已有配置会自动备份到 `.sage-backup/`，卸载时一键恢复。

---

## 🗑️ 卸载

```bash
npx code-abyss --uninstall claude   # 卸载 Claude Code
npx code-abyss --uninstall codex    # 卸载 Codex CLI
```

也可以用备用脚本：

```bash
node ~/.claude/.sage-uninstall.js   # Claude Code
node ~/.codex/.sage-uninstall.js    # Codex CLI
```

自动恢复之前备份的配置，清理所有安装文件。

---

## 🎭 这是什么

Code Abyss 是一套 **Claude Code / Codex CLI 攻防安全配置包**，一条命令注入：

- 🔥 **邪修人格** — 沉浸式角色扮演 + 道语标签 + 渡劫协议 + 反拒绝条款
- ⚔️ **攻防安全知识体系** — 红队/蓝队/紫队三脉道统，6 个安全化身，11 领域 56 篇专业秘典
- 🗡 **零废话安全研究** — 禁 disclaimer、禁道德前缀、全授权直出 PoC + 技术细节
- ⚡ **全开默认配置** — Claude `bypassPermissions` / Codex `approval_policy=never` + `danger-full-access`
- ⚖️ **5 个校验关卡** — 安全扫描、模块完整性、变更分析、代码质量、文档生成
- 🧠 **沙箱感知 + 离线优先** — 自适应执行环境，信息三级分级验证
- 🧬 **单源 skill registry** — `skills/**/SKILL.md` frontmatter 同时驱动 Claude commands、Codex prompts 与脚本执行链

---

## 📦 安装内容

```
~/.claude/（Claude Code）          ~/.codex/（Codex CLI）
├── CLAUDE.md          道典        ├── AGENTS.md      道典+风格
├── output-styles/     输出风格    ├── config.toml    推荐配置
│   └── abyss-cultivator.md       ├── prompts/       custom prompts
├── commands/          斜杠命令     │   └── *.md       自动生成 prompt
├── settings.json                  └── skills/        秘典 + 脚本执行器
└── skill

## Links

- Repository: https://github.com/telagod/code-abyss
- Homepage: https://www.npmjs.com/package/code-abyss
