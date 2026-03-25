---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code agent subagent"
  quality_score: 51
  scoring_breakdown:
    stars: 14
    recency: 8
    docs: 20
    community: 9
github_data:
  full_name: "CoderMageFox/claudecode-codex-subagents"
  url: "https://github.com/CoderMageFox/claudecode-codex-subagents"
  description: "A Claude Code plugin for orchestrating complex tasks by delegating to multiple parallel Codex agents, then merging and reviewing results."
  stars: 41
  forks: 3
  open_issues: 0
  language: "Shell"
  license: "MIT"
  last_push: "2025-11-07"
  created: "2025-11-06"
  topics: []
---

# CoderMageFox/claudecode-codex-subagents

> Discovered by arsenal scout — awaiting manual triage

## Description

A Claude Code plugin for orchestrating complex tasks by delegating to multiple parallel Codex agents, then merging and reviewing results.

## README Excerpt

# Codex Subagents - Claude Code Plugin

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/CoderMageFox/claudecode-codex-subagents?style=social)](https://github.com/CoderMageFox/claudecode-codex-subagents)
[![GitHub Issues](https://img.shields.io/github/issues/CoderMageFox/claudecode-codex-subagents)](https://github.com/CoderMageFox/claudecode-codex-subagents/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/CoderMageFox/claudecode-codex-subagents/pulls)

[中文](./README-zh.md) | [English](./README-en.md)

通过并行委托多个 Codex 代理来编排复杂任务，然后合并和审查结果的 Claude Code 插件。

## 功能特点

- 🚀 **并行处理**: 将复杂任务分解为可并行执行的单元（每批最多3个代理）
- 🔗 **链式处理**: 超过3个任务时自动进行链式批量处理
- 📊 **实时进度**: 使用 TodoWrite 实时显示任务执行进度
- 📝 **详细日志**: 所有子代理活动记录到 `.codex-temp/[时间戳]/` 目录
- 🤖 **智能委托**: 通过 MCP 服务器自动委托给多个 Codex 子代理
- 🔄 **智能合并**: 自动检测冲突并应用最佳合并策略
- ✅ **质量验证**: 包含编译、测试、代码质量等多重验证关卡

## 快速安装

### 方式 1：一键安装脚本（推荐）

**适合：首次使用，希望全自动安装**

```bash
git clone https://github.com/CoderMageFox/claudecode-codex-subagents.git
cd claudecode-codex-subagents
./install.sh
```

**安装脚本会自动完成：**
- ✅ 检测并自动安装缺失的依赖（Python 3, uv, Codex CLI）
- ✅ 安装 Plugin 到 `~/.claude/plugins/`
- ✅ **复制命令到 `~/.claude/commands/` 以确保直接可用**
- ✅ 配置 MCP 服务器（无需手动安装）
- ✅ 自动安装中英文双版本命令
- ✅ 验证安装完整性

### 方式 2：通过 Claude Code Plugin 系统安装

**适合：熟悉 Claude Code plugin 系统，希望使用 plugin 管理**

#### 步骤 1：添加 Plugin Marketplace

在 Claude Code 中运行：

```bash
# 方式 A: 通过 GitHub URL 添加
/plugin marketplace add CoderMageFox/claudecode-codex-subagents

# 方式 B: 或者在 settings.json 中添加
```

在 `~/.claude/settings.json` 中添加：

```json
{
  "extraKnownMarketplaces": [
    {
      "name": "codex-subagents",
      "url": "https://github.com/CoderMageFox/claudecode-codex-subagents"
    }
  ]
}
```

#### 步骤 2：安装 Plugin

```bash
# 从 marketplace 安装
/plugin install codex-subagents@CoderMageFox

# 或者直接通过 GitHub 路径安装
/plugin install CoderMageFox/claudecode-codex-subagents
```

#### 步骤 3：配置 MCP 服务器

手动在 `~/.claude/mcp_settings.json` 中添加：

```json
{
  "mcpServers": {
    "codex-subagent": {
      "command": "uvx",
      "args": ["codex-as-mcp@latest"],
      "transport": "stdio"
    }
  }
}
```

#### 步骤 4：重启 Claude Code

```bash
# 退出当前会话
exit

# 重新启动 Claude Code
claude
```

#### 步骤 5：验证安装

```bash
# 验证 plugin 结构
/plugin validate

# 检查 MCP 服务器状态
/mcp

# 测试命令
/codex-subagents 测试任务
```

### 方式对比

| 特性 | 一键安装脚本 | Plugin 系统安装 |
|------|------------|----------------|
| 安装难度 | ⭐ 简单 | ⭐⭐⭐ 中等 |
| 自动配置 | ✅ 全自动 | ❌ 需手动配置 MCP |
| 依赖安装 | ✅ 自动检测安装 | ❌ 需手动安装 |
| 命令可用性 | ✅ 立即可用 | ✅ 重启后可用 |
| Plugin 管理 | ⚠️ 手动更新 | ✅ 支持 `/plugin update` |
| 适用场景 | 快速开始 | 企业团队管理 |

**前置要求：**
- Python 3 (macOS 通常自带，脚本会自动检测)
- uv (脚本会提示并自动安装)
- Codex CLI >= 0.46.0 (脚本会提示并自动安装)
- Claude Code CLI

> 💡 **提示**: 如果缺少依赖，安装脚本会自动检测并询问是否安装，无需手动准备！

安装完成后，重启 Claude Code 即可使用。

## 使用方法

### 基本用法

```bash
/codex-subagents <任务描述>
```

### 示例

**示例 1: 创建 React 组件**
```bash
/codex-subagent

## Links

- Repository: https://github.com/CoderMageFox/claudecode-codex-subagents
