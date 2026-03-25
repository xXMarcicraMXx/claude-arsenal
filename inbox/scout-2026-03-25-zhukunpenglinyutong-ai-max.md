---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code hook"
  quality_score: 66
  scoring_breakdown:
    stars: 20
    recency: 15
    docs: 20
    community: 11
github_data:
  full_name: "zhukunpenglinyutong/ai-max"
  url: "https://github.com/zhukunpenglinyutong/ai-max"
  description: "一键给Claude Code 提高智商，包含生产级 agents、skills、hooks、commands、rules 和 MCP 配置"
  stars: 206
  forks: 23
  open_issues: 4
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-02-11"
  created: "2026-01-22"
  topics: []
---

# zhukunpenglinyutong/ai-max

> Discovered by arsenal scout — awaiting manual triage

## Description

一键给Claude Code 提高智商，包含生产级 agents、skills、hooks、commands、rules 和 MCP 配置

## README Excerpt

# AI MAX

> 这是基于 [everything-claude-code](https://github.com/affaan-m/everything-claude-code) 进行二次开发，提供npm一键安装方式，协议沿用MIT

**Claude Code 增强配置，开箱即用。**

本仓库包含生产级 agents（代理）、skills（技能）、hooks（钩子）、commands（命令）、rules（规则）和 MCP 配置，帮助你快速提升 Claude Code 的使用体验。

---

## 快速开始

```bash
# 全局安装
npm install -g aimax

# 执行aimax，增强claude code智商
aimax                    # 终端执行aimax，进行交互式安装

# Claude Code 使用
/aimax:auto 你的问题      # 自动选择最优的aimax指令
```


CLI 提供交互式界面，让你选择要安装的组件：
- **Agents** - 专用子代理（planner, architect, tdd-guide 等）
- **Rules** - 必须遵循的准则（security, testing, coding-style 等）
- **Commands** - 斜杠命令（/aimax:plan, /aimax:tdd, /aimax:code-review 等）
- **Skills** - 工作流定义和领域知识

---

## 斜杠指令使用指南

安装 AI MAX 后，你可以在 Claude Code 中使用以下斜杠指令。只需输入 `/aimax:指令名` 加上你的需求即可。

### 快速参考

| 指令 | 用途 | 示例 |
|------|------|------|
| `/aimax:auto` | 智能选择最合适的指令 | `/aimax:auto 帮我修复这个 bug` |
| `/aimax:plan` | 功能规划与实现方案 | `/aimax:plan 添加用户登录功能` |
| `/aimax:tdd` | 测试驱动开发 | `/aimax:tdd 实现购物车功能` |
| `/aimax:code-review` | 代码质量与安全审查 | `/aimax:code-review` |
| `/aimax:build-fix` | 修复构建/类型错误 | `/aimax:build-fix` |
| `/aimax:e2e` | 端到端测试生成 | `/aimax:e2e 测试用户注册流程` |
| `/aimax:test-coverage` | 测试覆盖率分析 | `/aimax:test-coverage` |
| `/aimax:refactor-clean` | 代码重构与清理 | `/aimax:refactor-clean 优化这个模块` |
| `/aimax:update-docs` | 更新项目文档 | `/aimax:update-docs` |
| `/aimax:update-codemaps` | 更新代码架构图 | `/aimax:update-codemaps` |

---

### 详细说明

#### `/aimax:auto` - 智能指令选择器

不确定用哪个指令？使用 `/aimax:auto`，它会根据你的描述自动选择最合适的指令。

```
/aimax:auto 我的构建失败了，有类型错误
→ 自动选择 /aimax:build-fix

/aimax:auto 帮我写个新功能
→ 自动选择 /aimax:plan

/aimax:auto 检查一下代码有没有安全问题
→ 自动选择 /aimax:code-review
```

#### `/aimax:plan` - 实现规划

在编写代码之前创建详细的实现计划。适用于：
- 新功能开发
- 重大架构变更
- 复杂重构工作

```
/aimax:plan 添加实时通知功能
```

AI 会分析需求、识别风险、创建分步计划，**并等待你确认后才开始编码**。

#### `/aimax:tdd` - 测试驱动开发

强制执行 TDD 工作流：先写测试，再写实现。适用于：
- 新功能实现
- Bug 修复
- 关键业务逻辑

```
/aimax:tdd 实现价格计算器
```

遵循 **红-绿-重构** 循环，确保 80% 以上测试覆盖率。

#### `/aimax:code-review` - 代码审查

对未提交的更改进行全面审查，检查：
- 🔴 安全问题（凭证泄露、SQL 注入、XSS）
- 🟠 代码质量（函数过长、嵌套过深）
- 🟡 最佳实践（可变模式、缺少测试）

```
/aimax:code-review
```

#### `/aimax:build-fix` - 构建错误修复

快速修复构建和类型错误。适用于：
- TypeScript 类型错误
- 编译失败
- 构建流程问题

```
/aimax:build-fix
```

#### `/aimax:e2e` - 端到端测试

使用 Playwright 生成和运行 E2E 测试。适用于：
- 用户流程测试
- 跨页面功能验证
- UI 自动化测试

```
/aimax:e2e 测试用户登录到下单的完整流程
```

#### `/aimax:test-coverage` - 覆盖率分析

分析测试覆盖率，识别未覆盖的代码。

```
/aimax:test-coverage
```

#### `/aimax:refactor-clean` - 重构清理

移除死代码、优化结构、消除重复。

```
/aimax:refactor-clean 清理这个模块中未使用的代码
```

#### `/aimax:update-docs` - 文档更新

更新项目文档、README、API 文档。

```
/aimax:update-docs
```

#### `/aimax:update-codemaps` - 架构图更新

生成或更新代码架构图和模块依赖图。

```
/aimax:update-codemaps
```

### 推荐工作流

```
1. /aimax:plan        → 规划功能
2. /aimax:tdd         → 测试驱动实现
3. /aimax:code-review → 审查代码
4. /aimax:build-fix   → 修复构建问题（如有）
5. git commit         → 提交代码
```

---

## 核心概念

### Agents（代理）

子代理以有限的范围处理委派的任务。示例：

```markdown
---
name: code-reviewer
description: 审查代码的质量、安全性和可维护性
tools: Read, Grep, Glob, Bash
model: opus

## Links

- Repository: https://github.com/zhukunpenglinyutong/ai-max
- Homepage: https://www.mossx.ai
