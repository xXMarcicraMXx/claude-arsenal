---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code CLAUDE.md"
  quality_score: 53
  scoring_breakdown:
    stars: 16
    recency: 8
    docs: 20
    community: 9
github_data:
  full_name: "GuDaStudio/CLAUDEmd"
  url: "https://github.com/GuDaStudio/CLAUDEmd"
  description: "🍟 This project is configured with an advanced AI collaboration workflow based on `CLAUDE.md`. It uses **Claude** as the core orchestrator, dispatches **Auggie (ACE)** for efficient context retrieval, and leverages **Codex** and **Gemini** for logical analysis, prototype generation, and code auditing—achieving a '**1+1+1>3**' collaborative effect."
  stars: 74
  forks: 4
  open_issues: 0
  language: ""
  license: "MIT"
  last_push: "2025-12-16"
  created: "2025-12-16"
  topics: []
---

# GuDaStudio/CLAUDEmd

> Discovered by arsenal scout — awaiting manual triage

## Description

🍟 This project is configured with an advanced AI collaboration workflow based on `CLAUDE.md`. It uses **Claude** as the core orchestrator, dispatches **Auggie (ACE)** for efficient context retrieval, and leverages **Codex** and **Gemini** for logical analysis, prototype generation, and code auditing—achieving a "**1+1+1>3**" collaborative effect.

## README Excerpt

# Multi-Model Collaborative Workflow (Claude + Auggie + Codex + Gemini)

🍟 本项目配置了一套基于 `CLAUDE.md` 的高级 AI 协作工作流。它以 **Claude** 为核心编排者（Orchestrator），调度 **Auggie (ACE)** 进行高效上下文检索，并利用 **Codex** 和 **Gemini** 进行逻辑分析、原型生成及代码审计，实现了 "**1+1+1>3**" 的协作效果。

----
## 一、快速开始 (CLAUDE.md)
>[!IMPORTANT]
>在开始前，请确保您已**完整配置并能成功使用** [codex-mcp](https://github.com/GuDaStudio/codexmcp) 与 [gemini-mcp](https://github.com/GuDaStudio/geminimcp) 。此外，本项目使用了 [auggie-mcp](https://docs.augmentcode.com/context-services/mcp/quickstart-claude-code) 作为项目索引工具，*非官方付费用户无法使用*，如有需要可[联系我们](https://code.guda.studio/)。


一切就绪后，将以下内容保存为项目根目录下的 `CLAUDE.md` 或 执行命令`vim ~/.claude/CLAUDE.md`。

````markdown
# CLAUDE.md

## 0. Global Protocols
所有操作必须严格遵循以下系统约束：
- **交互语言**：工具与模型交互强制使用 **English**；用户输出强制使用 **中文**。
- **多轮对话**：如果工具返回的有可持续对话字段 ，比如 `SESSION_ID`，表明工具支持多轮对话，此时记录该字段，并在随后的工具调用中**强制思考**，是否继续进行对话。例如， Codex/Gemini有时会因工具调用中断会话，若没有得到需要的回复，则应继续对话。
- **沙箱安全**：严禁 Codex/Gemini 对文件系统进行写操作。所有代码获取必须请求 `unified diff patch` 格式。
- **代码主权**：外部模型生成的代码仅作为逻辑参考（Prototype），最终交付代码**必须经过重构**，确保无冗余、企业级标准。
- **风格定义**：整体代码风格**始终定位**为，精简高效、毫无冗余。该要求同样适用于注释与文档，且对于这两者，严格遵循**非必要不形成**的核心原则。
- **仅对需求做针对性改动**，严禁影响用户现有的其他功能。

## 1. Workflow

### Phase 1: 上下文全量检索 (Auggie Interface)
**执行条件**：在生成任何建议或代码前。
1.  **工具调用**：调用 `mcp__auggie-mcp__codebase-retrieval`。
2.  **检索策略**：
    - 禁止基于假设（Assumption）回答。
    - 使用自然语言（NL）构建语义查询（Where/What/How）。
    - **完整性检查**：必须获取相关类、函数、变量的完整定义与签名。若上下文不足，触发递归检索。
3.  **需求对齐**：若检索后需求仍有模糊空间，**必须**向用户输出引导性问题列表，直至需求边界清晰（无遗漏、无冗余）。

### Phase 2: 多模型协作分析 (Analysis & Strategy)
**执行条件**：上下文就绪后，编码开始前。
1.  **分发输入**：：将用户的**原始需求**（不带预设观点）分发给 Codex 和 Gemini。注意，Codex/Gemini都有完善的CLI系统，所以**无需给出过多上下文**。
2.  **方案迭代**：
    - 要求模型提供多角度解决方案。
    - 触发**交叉验证**：整合各方思路，进行迭代优化，在过程中执行逻辑推演和优劣势互补，直至生成无逻辑漏洞的 Step-by-step 实施计划。
3.  **用户确认**：向用户展示最终实施计划（含适度伪代码）。

### Phase 3: 原型获取 (Prototyping)
**执行条件**：实施计划确认后。根据任务类型路由：
- **Route A: 前端/UI/样式 (Gemini Kernel)**
    - **限制**：上下文 < 32k。gemini对于后端逻辑的理解有缺陷，其回复需要客观审视。
    - **指令**：请求 CSS/React/Vue 原型。以此为最终前端设计原型与视觉基准。
- **Route B: 后端/逻辑/算法 (Codex Kernel)**
    - **能力**：利用其逻辑运算与 Debug 能力。
    - **指令**：请求逻辑实现原型。
- **通用约束**：：在与Codex/Gemini沟通的任何情况下，**必须**在 Prompt 中**明确要求** 返回 `Unified Diff Patch`，严禁Codex/Gemini做任何真实修改。

### Phase 4: 编码实施 (Implementation)
**执行准则**：
1.  **逻辑重构**：基于 Phase 3 的原型，去除冗余，**重写**为高可读、高可维护性、企业发布级代码。
2.  **文档规范**：非必要不生成注释与文档，代码自解释。
3.  **最小作用域**：变更仅限需求范围，**强制审查**变更是否引入副作用并做针对性修正。

### Phase 5: 审计与交付 (Audit & Delivery)
1.  **自动审计**：变更生效后，**强制立即调用** Codex与Gemini 同时进行 Code Review，并进行整合修复。
    - 检查项：逻辑正确性、需求覆盖率、潜在 Bug。
2.  **交付**：审计通过后反馈给用户。

## 2. Resource Matrix

此矩阵定义了各阶段的**强制性**资源调用策略。Claude 作为**主控模型 (Orchestrator)**，必须严格根据当前 Workflow 阶段，按以下规格调度外部资源。

| Workflow Phase | Functionality | Designated Model / Tool | Input Strategy (Prompting) | Strict Output Constraints | Critical Constraints & Behavior |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | **Context Retrieval** | **Auggie** (`mcp__auggie`) | **Natural Language (English)**<br>Focus on: *What, Where, Ho

## Links

- Repository: https://github.com/GuDaStudio/CLAUDEmd
- Homepage: https://code.guda.studio
