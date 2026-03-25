---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code tutorial"
  quality_score: 62
  scoring_breakdown:
    stars: 13
    recency: 20
    docs: 20
    community: 9
github_data:
  full_name: "young1lin/cc-tutorial"
  url: "https://github.com/young1lin/cc-tutorial"
  description: "Claude Code Tutorial."
  stars: 33
  forks: 5
  open_issues: 0
  language: ""
  license: "MIT"
  last_push: "2026-03-11"
  created: "2026-02-10"
  topics: []
---

# young1lin/cc-tutorial

> Discovered by arsenal scout — awaiting manual triage

## Description

Claude Code Tutorial.

## README Excerpt

# Claude Code 教程

> 全面掌握 Claude Code - Anthropic 出品的 AI 编程助手

## 简介

本项目包含 **9 层深度教程**的视频脚本、示例代码和研究资料，旨在帮助开发者有效使用 Claude Code。课程内容由浅入深：理论基础 → 安装与环境 → 基础操作 → 核心工作流 → 项目配置体系 → 高级功能 → 注意事项 → 实战案例 → 补充内容。基于官方 Anthropic 文档和行业专家（Boris Cherny、Addy Osmani、Andrew Ng 等）的建议编写。

### 配套实战案例

教程中的实践案例参考 [`mybatis-boost`](C:\PythonProject\mybatis-boost) 项目——一个真实的 VSCode 扩展，展示了 Claude Code 工作流的实际应用。

---

## 项目结构

```
cc-tutorial/
├── .claude/                      # Claude Code 配置
│   ├── commands/                 # 自定义斜杠命令
│   └── settings.json             # 项目设置
│
├── video-scripts/                # 视频脚本（9 层结构）
├── examples/                     # 示例代码和参考资料
├── research/                     # 研究资料
├── docs/                         # 文章、图片等
│
├── CLAUDE.md                     # 给 Claude Code 的项目说明
├── LICENSE                       # MIT 许可证
└── README.md                     # 本文件
```

---

## 视频脚本（九层结构）

| 层级 | 标题 | 内容概要 |
|------|------|----------|
| 第一层 | [理论基础](video-scripts/layer-01-theory.md) | LLM 基础、Token 与上下文窗口、多模态、模型选择 |
| 第二层 | [安装与环境](video-scripts/layer-02-setup.md) | 安装 Claude Code、IDE 联动、/init、中转、模型切换与费用 |
| 第三层 | [基础操作](video-scripts/layer-03-basics.md) | 快捷键、深度思考关键词、Resume/Rewind、Compact、图片支持 |
| 第四层 | [核心工作流](video-scripts/layer-04-workflow.md) | Vibe vs Spec Coding、Plan Mode、CLAUDE.md、Git 工作流、TDD |
| 第五层 | [项目配置体系](video-scripts/layer-05-config.md) | 配置目录结构、Rules、Memory、Commands、Context Engineering |
| 第六层 | [高级功能](video-scripts/layer-06-advanced.md) | MCP、SubAgent、插件、Skills、Hooks、Headless、Worktrees、SDK |
| 第七层 | [注意事项](video-scripts/layer-07-caveats.md) | AI 能力边界、翻车场景、Burnout、数据安全、扩展学习资源 |
| 第八层 | [实战案例](video-scripts/layer-08-practice.md) | 完整的项目修改流程演示 |
| 第九层 | [补充内容](video-scripts/layer-09-supplement.md) | Web 端、Session Teleport、国内订阅指南、安全提示 |

---

## 主要特性

### 自定义斜杠命令

- **`/commit-push`** - 暂存、提交（约定式提交格式）、推送，智能排除调试文件

### 示例代码库

位于 `examples/`：

- **HTTP API 示例** - 97 个示例，涵盖 LLM 能力、函数调用、提示工程、代理模式
- **官方技能文档** - 9 个官方 Claude Code 技能参考
- **推荐插件** - 精选的实用插件和扩展列表

### 研究资料

`research/` 中收录的权威资料：

- Boris Cherny（Claude Code 创造者）最佳实践
- 官方 Plan Mode 指南
- Andrew Ng 的 DeepLearning.AI 课程大纲
- Addy Osmani 的 2026 AI 编程工作流
- Ethan Mollick 和 Zvi Mowshowitz 的见解

---

## 核心理念

### AI 辅助工程 vs AI 自动化工程

本教程强调 **AI 辅助工程**：
- AI 是人类专业能力的放大器
- 人类工程师保持主导权和责任感
- Plan Mode 是基础工作流

### 重点技术主题

1. **Plan Mode** - 最重要的功能（按两次 Shift+Tab）
2. **多实例工作流** - 使用 git worktree 进行并行开发
3. **验证机制** - 测试、CI/CD、代码审查
4. **架构模式** - 整洁架构、六边形架构、DDD
5. **AAA 测试模式** - 单元测试的 Arrange-Act-Assert

---

## 视频脚本模板

每集视频遵循以下标准化格式：

1. **开场（30-60 秒）** - 是什么，为什么
2. **概念讲解（2-3 分钟）** - 配合图表/动画
3. **实机演示（5-8 分钟）** - 屏幕录制 + 编码
4. **总结（1-2 分钟）** - 关键要点
5. **练习（可选）** - 实践活动


---

## 快速开始

1. **安装 Claude Code** - 参考 [第二层：安装与环境](video-scripts/layer-02-setup.md)

   > **国内用户**: 原生安装可能遇到网络问题，推荐使用 npm 全局安装：
   > ```bash
   > npm install -g @anthropic-ai/claude-code
   > ```

2. **学习基础知识** - 从 [第一层：理论基础](video-scripts/layer-01-theory.md) 开始
3. **掌握核心工作流** - 重点学习 [第四层：核心工作流](video-scripts/layer-04-workflow.

## Links

- Repository: https://github.com/young1lin/cc-tutorial
