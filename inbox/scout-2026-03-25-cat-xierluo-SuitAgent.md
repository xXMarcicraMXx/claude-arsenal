---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code agent subagent"
  quality_score: 65
  scoring_breakdown:
    stars: 18
    recency: 15
    docs: 20
    community: 12
github_data:
  full_name: "cat-xierluo/SuitAgent"
  url: "https://github.com/cat-xierluo/SuitAgent"
  description: "基于 Claude Code 的诉讼法律服务智能分析系统，采用10个 SubAgents 协作的模式，将复杂的诉讼案件分析分解为多个可独立执行的工作流，实现法律文书的工程化生成。"
  stars: 128
  forks: 44
  open_issues: 0
  language: "Python"
  license: "AGPL-3.0"
  last_push: "2026-01-01"
  created: "2025-11-03"
  topics: []
---

# cat-xierluo/SuitAgent

> Discovered by arsenal scout — awaiting manual triage

## Description

基于 Claude Code 的诉讼法律服务智能分析系统，采用10个 SubAgents 协作的模式，将复杂的诉讼案件分析分解为多个可独立执行的工作流，实现法律文书的工程化生成。

## README Excerpt

# SuitAgent - 诉讼法律服务智能分析系统

---

## 📖 项目介绍文章

想了解SuitAgent的完整设计思路和使用场景？查看详细文章：

**👉 [SuitAgent：基于Claude Code的AI代理诉讼法律服务系统](https://mp.weixin.qq.com/s/Atm48_tpp7bcQhT12P7Btg)**

---

## 👨‍💼 关于作者

我是一名律师，擅长技术类（知识产权、数据与 AI）纠纷，如想进一步交流，欢迎添加我的微信：

<div align="center">
  <img src="微信二维码.jpg" width="200" alt="微信二维码"/>
  <p><strong></strong></p>
</div>

---

## 项目概述

SuitAgent 是一个基于 **Claude Code 架构** 的诉讼法律服务智能分析系统，采用10个专业AI代理协作的模式，将复杂的诉讼案件分析分解为多个可独立执行的工作流，实现法律文书的工程化生成。

## ✨ 核心特性

- 🎯 **多阶段覆盖**：从诉前分析到判决执行，全流程支持
- 🚀 **一键启动**：上传文档即可自动分析，无需复杂配置
- 🔄 **灵活组合**：10个专业AI代理可自由组合使用
- 📊 **标准化输出**：统一的文档管理结构和命名规范
- 📱 **终端操作**：基于命令行界面，（并不）简单易用

## 📋 目录

- [项目概述](#项目概述)
- [核心特性](#-核心特性)
- [系统架构](#-系统架构)
  - [四层架构设计](#-agent分层架构)
  - [架构优势](#-架构优势)
  - [典型工作流](#-典型工作流)
- [10个AI代理介绍](#-10个ai代理介绍)
  - [📥 输入层](#-输入层-input-layer)
    - [1. DocAnalyzer - 文档分析](#1-docanalyzer文档分析)
    - [2. EvidenceAnalyzer - 证据分析](#2-evidenceanalyzer证据分析)
  - [🔍 分析层](#-分析层-analysis-layer)
    - [3. IssueIdentifier - 争议识别](#3-issueidentifier争议识别)
    - [4. Researcher - 法律研究](#4-researcher法律研究)
    - [5. Strategist - 诉讼策略](#5-strategist诉讼策略)
  - [📝 输出层](#-输出层-output-layer)
    - [6. Writer - 法律文书](#6-writer法律文书)
    - [7. Summarizer - 摘要生成](#7-summarizer摘要生成)
    - [8. Reporter - 案件报告](#8-reporter案件报告)
  - [⚙️ 支持层](#-支持层-support-layer)
    - [9. Scheduler - 日程规划](#9-scheduler日程规划)
    - [10. Reviewer - 智能审查](#10-reviewer智能审查)
- [安装指南](#-安装指南)
  - [安装Claude Code CLI](#安装claude-code-cli推荐方式)
  - [下载并安装Zed编辑器](#下载并安装zed编辑器-推荐新手)
  - [配置AI模型](#第三步配置ai模型-)
  - [使用cc-switch配置](#使用cc-switch配置)
  - [验证安装](#验证安装)
- [快速开始](#-快速开始)
- [常见使用场景](#-常见使用场景)
- [文档管理](#-文档管理)
- [常见问题](#-常见问题)
- [实用工具链接](#-实用工具链接)

## 🏗️ 系统架构

SuitAgent 采用**四层架构设计**，将10个Agent按职能分为4个层级：

### 📊 Agent分层架构

```
┌─────────────────────────────────────────┐
│              输入层 (Input Layer)        │  文档数据采集与解析
│  ┌─────────────────┐ ┌─────────────────┐ │
│  │  DocAnalyzer    │ │ EvidenceAnalyzer│ │
│  │   文档分析      │ │   证据分析      │ │
│  └─────────────────┘ └─────────────────┘ │
└─────────────────┬───────────────────────┘
                  ▼
┌─────────────────────────────────────────┐
│              分析层 (Analysis Layer)     │  智能分析与研究
│  ┌─────────────┐ ┌─────────────────────┐ │
│  │IssueIdentifier│ │   Researcher       │ │
│  │  争议识别    │ │   法律研究         │ │
│  └─────────────┘ └─────────────────────┘ │
│  ┌─────────────────────────────────────┐ │
│  │        Strategist                   │ │
│  │        诉讼策略                     │ │
│  └─────────────────────────────────────┘ │
└─────────────────┬───────────────────────┘
                  ▼
┌─────────────────────────────────────────┐
│              输出层 (Output Layer)      │  文书生成与报告
│  ┌─────────────┐ ┌─────────────────────┐ │
│  │   Writer    │ │     Reporter        │ │
│  │  法律文书    │ │   报告整合         │ │
│  └─────────────┘ └─────────────────────┘ │
│  ┌─────────────────────────────────────┐ │
│  │        Summarizer                   │ │
│  │        摘要生成                     │ │
│  └────

## Links

- Repository: https://github.com/cat-xierluo/SuitAgent
