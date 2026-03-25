---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code agent subagent"
  quality_score: 75
  scoring_breakdown:
    stars: 18
    recency: 25
    docs: 20
    community: 12
github_data:
  full_name: "dongbeixiaohuo/writing-agent"
  url: "https://github.com/dongbeixiaohuo/writing-agent"
  description: "🚀 一个基于 Claude Code (Skills + Subagents) 的“去AI味”全栈写作系统。不仅防套路，更通过专属规则强制注入人类观点与细节，搭配读者测试评估与自动图文排版。全面支持 DeepSeek / 智谱GLM / MiniMax 等国产低成本大模型，提供从选题、风格建模到审稿发布的高维全自动写作工作流。"
  stars: 128
  forks: 33
  open_issues: 0
  language: "JavaScript"
  license: "MIT"
  last_push: "2026-03-22"
  created: "2025-12-21"
  topics: ["ai-writing", "claude-code", "content-generation", "deepseek", "style-modeling", "writing-agent", "writing-assistant", "writing-workflow"]
---

# dongbeixiaohuo/writing-agent

> Discovered by arsenal scout — awaiting manual triage

## Description

🚀 一个基于 Claude Code (Skills + Subagents) 的“去AI味”全栈写作系统。不仅防套路，更通过专属规则强制注入人类观点与细节，搭配读者测试评估与自动图文排版。全面支持 DeepSeek / 智谱GLM / MiniMax 等国产低成本大模型，提供从选题、风格建模到审稿发布的高维全自动写作工作流。

## README Excerpt

# 写稿Agent v0.7.0

> 🚀 一个基于 Claude Code Skills + Subagents 的全栈写作系统。
> 
> **不仅是写作，更是打磨进化：**
> *   🧠 **自进化架构**：首次引入采样编译闭环，能记住修改偏好并复用，越用越顺手。
> *   🤖 **反AI味写作**：从选题到初稿，源头遏制 AI 腔调。
> *   🧬 **深度 Humanizer**：注入人类观点、细节与灵魂，彻底去除机器味。
> *   🎨 **文章配图师**：自动设计视觉风格，生成并植入高质量配图。
> *   📺 **真实读者模拟**：模拟真实用户的"心理弹幕"与"朋友圈转发"，只为了检验传播力。
> 
> **支持 DeepSeek / 智谱GLM / MiniMax 等多种国产大模型**，兼容 OpenAI/Gemini 接口，成本极低（使用包月套餐几可忽略不计）。
> 
> 从选题生成、风格建模、写作执行到发布评审与配图，提供完整的 AI 写作工作流。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-v0.7.0-blue.svg)](https://github.com/dongbeixiaohuo/writing-agent/releases)
[![Claude Code](https://img.shields.io/badge/Claude-Code%20Skills-blue)](https://code.claude.com)
[![DeepSeek](https://img.shields.io/badge/DeepSeek-Compatible-green)](https://platform.deepseek.com)

## 🎯 项目简介

写稿Agent 是一个**协作式写作工作流系统**，通过强制性的模式选择、需求澄清、风格建模、素材调研和主编审稿，帮助你写出**不像AI生成**的高质量文章。

### v0.7.0 系统自进化双轴架构 ⭐ New
- 🔄 **自动复盘与经验装载**：引入 `edit-diff-learner` 和 `memory-loader`。系统会自动对撞定稿与初稿提炼写作经验（15维风格DSL），并在下次写作前编译记忆包 (`00_memory_packet.md`)，注入到大纲、标题、执行和去AI味 Agent 中，实现"长记性"。
- ⚙️ **自动化物理排版 Hook**：利用 Claude Code Hooks 机制跳出大模型约束，在工作流大结局通过 `auto_clean_hook.py` 静默生成排版纯净版 `_clean.txt`。

### v0.6.4 技能结构优化
- 🔧 **Progressive Disclosure 架构升级**：应用 Skill Creator 最佳实践，大幅提升技能加载效率。
- 📉 **Token 使用优化**：公众号文章获取技能从 1238 行精简至 ~200 行，Token 消耗减少 85%。
- 📚 **文档结构化**：核心流程保留在 SKILL.md，详细说明拆分到 references 目录，按需加载。
- 📖 **调用示例增强**：工作流导演新增完整的 Agent 工具调用示例，提升可执行性。

### v0.6.3 去AI味专家进阶升级
- ⚖️ **50分制质量自评**：加入严苛输出把控，强迫 AI 根据五大维度自评，低于 40 分内部打回重写。
- 🚫 **致命黑名单词库**：精准打击“此外”、“至关重要”、“织锦”、“格局”等典型机器生成的“塑料词汇”。
- ⚡ **快速排雷自检 (Quick Check)**：强制打断 AI 常见的“三段式强迫症”、“等长句式”和“无聊排比”。
- ❤️ **全新注入灵魂指令**：通过引入具体生活细节、强加第一人称时局感、甚至刻意的逻辑混乱，赋予文本真正的强人设观感。

### v0.6.0 去AI味与真实模拟
- 🤖 **Humanizer 去AI味专家**：基于 Wikipedia AI Cleanup 项目，识别并修复24种AI痕迹（内容/语言/风格），注入人类"灵魂"。
- 🎨 **Article Illustrator 文章配图师**：为文章自动设计视觉风格并生成高质量配图（封面/插图/概念图）。
- 📺 **读者模拟器 v3.0 直播版**：模拟真实读者的"直播现场"——心理弹幕、朋友圈截图预览。

### v0.5.1 审稿质量增强
**解决"打分就过"的问题**，所有评审环节必须给出可执行的修改方案并等待用户确认：
- 🎯 **标题设计师 v2.0**：15种爆款公式（分6大类）+ 5个候选 + 钩子说明
- ✅ **发布前评审 v2.0**：每个问题都有「原文→改为」的修改方案 + 用户确认
- ✅ **读者模拟 v2.1**：具体修改建议 + 可自动执行修改 + 修改后重新测试
- 🔒 **强制用户确认**：不会再出现"打分就直接过去"的情况

### v0.5.0 重大架构升级

**引入 Subagent 模式**，实现上下文隔离：
- 🔄 **12 个执行步骤改为独立 Subagent**，每个任务独立上下文
- 📁 **信息通过文件传递**，不依赖对话上下文，避免 Token 累积
- 🎯 **工作流导演 Skill 显式调用 Subagent**，保持用户交互能力
- 💾 **每阶段产物自动落盘**，支持断点续写

### 核心特点

- ✅ **自进化归因引擎**：系统自动追溯初稿与定稿差异，抽取经验打包成 `99_episode.md` 实现跨次记忆 ✨ v0.7.0 New
- ✅ **无痕排版 Hook**：自动拦截大模型生成结果，利用纯 Python 正则脚本清除底噪，实现公众号直接粘贴 ✨ v0.7.0 New
- ✅ **超大编制 Subagent 架构**：16 个独立 Subagent 实现上下文完美隔离，将漫长的写作长链路切碎，节省海量 Token
- ✅ **深度协作工作流**：全 14 阶段创作者模式，囊括盘前准备、记忆装载、素材分析到模拟直播的全链条闭环
- ✅ **强制去 AI 味道**：Humanizer与24条红线规则，自动去除小标题病、排比上瘾、过度升华等AI特有文风
- ✅ **风格建模 v3.1**：支持公众号 URL 自动抓取分析、批量多篇拆解、增量汇入语料库
- ✅ **共情点与标题设计**：提供15类标题公式套件和5个候选方案，强制规划读者情绪跳动周期
- ✅ **全景素材调研**：不仅梳理网络数据，还进行结构论证、爆款拆解与痛点验伪
- ✅ **读者实况沙盘**：上线前模拟发出后的心理弹幕、真话吐槽以及朋友圈转发文案 ✨ v0.6.0
- ✅ **Article Illus

## Links

- Repository: https://github.com/dongbeixiaohuo/writing-agent
