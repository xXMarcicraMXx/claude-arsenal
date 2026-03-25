---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code agent subagent"
  quality_score: 76
  scoring_breakdown:
    stars: 19
    recency: 25
    docs: 20
    community: 12
github_data:
  full_name: "JDArmy/Evasion-SubAgents"
  url: "https://github.com/JDArmy/Evasion-SubAgents"
  description: "Claude Code 免杀 SubAgents"
  stars: 172
  forks: 28
  open_issues: 0
  language: "Python"
  license: "MIT"
  last_push: "2026-03-25"
  created: "2026-03-06"
  topics: []
---

# JDArmy/Evasion-SubAgents

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Code 免杀 SubAgents

## README Excerpt

# Evasion SubAgents

基于 Claude Code 的免杀技术研究与 Shellcode Loader 生成框架。

## 项目概述

本项目是一个 Claude Code 插件，通过 SubAgents 和 Skills 实现：

| Agent | 功能 | Skill |
|-------|------|-------|
| **research-agent** | 搜索 GitHub 技术，分析代码模式，更新知识库 | `research` |
| **loadergen-agent** | 从 loader 知识库组合组件，生成 loader | `loader_generate` |
| **evasion-agent** | 将 evasion 技术集成到现有 loader | `evasion_integrate` |
| **c2-evasion-agent** | 分析 C2 框架源码，查找检测规则，修改源码免杀 | `c2_evasion` |


## 环境要求

| 依赖 | 版本要求 | 用途 |
|------|----------|------|
| Python | 3.8+ | 知识库管理脚本 |
| MinGW-w64 | 最新版 | 编译 Windows 可执行文件 |
| GitHub CLI (gh) | 2.0+ | 搜索 GitHub 仓库和代码 |
| Claude Code | 最新版 | 主框架 |

### Windows 安装指南

#### 1. 安装 Python

```powershell
# 使用 winget 安装
winget install Python.Python.3.12

# 或从官网下载
# https://www.python.org/downloads/
```

#### 2. 安装 MinGW-w64 (交叉编译器)

```powershell
# 使用 winget 安装
winget install MSYS2.MSYS2

# 安装后，在 MSYS2 终端中运行：
pacman -S mingw-w64-x86_64-gcc

# 添加到 PATH (PowerShell 管理员)
$env:PATH += ";C:\msys64\mingw64\bin"
# 永久添加
[Environment]::SetEnvironmentVariable("PATH", $env:PATH + ";C:\msys64\mingw64\bin", "User")

# 验证安装
x86_64-w64-mingw32-gcc --version
```

#### 3. 安装 GitHub CLI

```powershell
# 使用 winget 安装
winget install GitHub.cli

# 登录 GitHub
gh auth login

# 验证安装
gh --version
gh auth status
```

#### 4. 安装 Claude Code

```powershell
# 使用 npm 安装 (需要 Node.js)
npm install -g @anthropic-ai/claude-code

# 或使用官方安装器
# https://github.com/anthropics/claude-code

# 验证安装
claude --version
```

### Linux/macOS 安装指南

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip mingw-w64 gh

# macOS (Homebrew)
brew install python mingw-w64 gh

# 安装 Claude Code
npm install -g @anthropic-ai/claude-code

# 登录 GitHub
gh auth login
```


## 加载插件到 Claude Code

### 方法一：项目目录方式（推荐）

将项目作为 Claude Code 的工作目录：

```bash
# 进入项目目录
cd "D:\Dev\Agent\LoaderSubAgents\LoaderSub Agents"

# 启动 Claude Code
claude

# Claude Code 会自动加载 .claude/ 目录下的配置
```

Claude Code 会自动识别：
- `.claude/agents/` - SubAgent 定义
- `.claude/skills/` - Skill 定义
- `.claude/commands/` - 自定义命令

### 方法二：CLAUDE.md 全局配置

在用户主目录创建全局配置：

```bash
# Windows
notepad %USERPROFILE%\.claude\CLAUDE.md

# Linux/macOS
nano ~/.claude/CLAUDE.md
```

添加项目路径：

```markdown
# 项目路径
- D:\Dev\Agent\LoaderSubAgents\LoaderSub Agents
```


### 验证加载成功

启动 Claude Code 后，使用以下命令验证：

```bash
# 查看可用命令
> /help

# 应看到：
# /research - Search GitHub for shellcode loader and evasion techniques
# /loader_generate - Generate shellcode loaders
# /evasion_integrate - Integrate evasion techniques
# /c2_evasion - C2 framework evasion analysis and modification
```

## 架构

```
evasion-agent-teams/
├── .claude-plugin/
│   └── plugin.json
├── agents/
│   ├── research-agent.md        # 研究技术
│   ├── loadergen-agent.md       # 生成 loader
│   └── evasion-agent.md         # 集成 evasion
│   └── c2-evasion-agent.md      # C2 免杀
├── skills/
│   ├── research/
│   │   └── SKILL.md             # 搜索分析技能
│   ├── loader_generate/
│   │   └── SKILL.md             # loader 生成技能
│ 

## Links

- Repository: https://github.com/JDArmy/Evasion-SubAgents
