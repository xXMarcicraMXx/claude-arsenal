---
scout_metadata:
  discovered_at: "2026-03-25T12:31:20Z"
  source: github_search
  query_matched: "claude code starter kit"
  quality_score: 71
  scoring_breakdown:
    stars: 17
    recency: 25
    docs: 20
    community: 9
github_data:
  full_name: "cloudnative-co/claude-code-starter-kit"
  url: "https://github.com/cloudnative-co/claude-code-starter-kit"
  description: "One-command setup of a complete Claude Code development environment with interactive wizard"
  stars: 102
  forks: 5
  open_issues: 0
  language: "Shell"
  license: "MIT"
  last_push: "2026-03-24"
  created: "2026-02-10"
  topics: []
---

# cloudnative-co/claude-code-starter-kit

> Discovered by arsenal scout — awaiting manual triage

## Description

One-command setup of a complete Claude Code development environment with interactive wizard

## README Excerpt

[English README](README.en.md) | [更新履歴 (CHANGELOG)](CHANGELOG.md)

# Claude Code Starter Kit

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform: macOS/Windows](https://img.shields.io/badge/Platform-macOS%20%7C%20Windows-blue.svg)](#-インストール)

Claude Code を初めて使う人でも、**ワンコマンドで開発環境を整えられる** セットアップキットです。
プログラミングやターミナルが初めての方にもわかるように、やさしく説明しています。

> **このキットは、株式会社クラウドネイティブ代表取締役社長・文部科学省最高情報セキュリティアドバイザーの齊藤愼仁が普段使っている Claude Code 環境をそのまま再現できる内容になっています。**

## Quick Start

**Mac:**

```bash
curl -fsSL https://raw.githubusercontent.com/cloudnative-co/claude-code-starter-kit/main/install.sh | bash
```

**Windows（PowerShell を管理者で実行）:**

```powershell
irm https://raw.githubusercontent.com/cloudnative-co/claude-code-starter-kit/main/install.ps1 | iex
```

> インストール後はターミナルを再起動して `claude` を実行。詳しくは [インストール](#-インストール) を参照。

---

## 目次

- [はじめに](#-はじめに)
- [必要なもの](#-必要なもの)
- [このキットでできること](#-このキットでできること)
- [インストール](#-インストール)
- [ウィザードの流れ](#-ウィザードの流れ)
- [ウィザード設定と反映先の対応表](docs/wizard-config-mapping.md)
- [プロファイルの選び方](#-プロファイルの選び方)
- [主な機能](#-主な機能)
- [セットアップ後にできること](#-セットアップ後にできること)
- [非対話モード](#-非対話モード自動セットアップ)
- [カスタマイズ](#-カスタマイズ)
- [アンインストール](#-アンインストール)
- [FAQ](#-faq)
- [トラブルシューティング](#-トラブルシューティング)
- [ディレクトリ構成](#-ディレクトリ構成)
- [更新履歴](#-更新履歴)
- [ライセンス](#-ライセンス)

---

## 🌟 はじめに

### Claude Code とは？

**Claude Code** は、Anthropic が提供する **CLI（コマンドラインインターフェース）ツール** です。
ターミナル（後述）から Claude AI に指示を出して、以下のようなことを手伝ってもらえます：

- コードの作成・修正
- 設計の相談・計画づくり
- コードのレビュー（間違いがないかチェック）
- テストの作成・実行
- バグ（不具合）の調査・修正

つまり、**AI がプログラミングのパートナーになってくれるツール** です。

### ターミナルとは？

**ターミナル** は、パソコンを **文字の命令（コマンド）で操作するアプリ** です。
普段はマウスでクリックして操作しますが、ターミナルでは「ファイルを開く」「ソフトをインストールする」といった操作を **短い命令文をキーボードで入力して実行** します。

| OS | ターミナルの開き方 |
|---|---|
| **macOS** | Spotlight（`Cmd + Space`）で「ターミナル」と入力して起動 |
| **Windows** | セットアップ時は「PowerShell」、セットアップ後は「**Windows Terminal + WSL**」を使います（[使い方はこちら](#windows-での使い方)） |

### エディタ（コードエディタ）とは？

**エディタ** は、プログラムのコード（テキスト）を書いたり編集したりするための **専用アプリ** です。
メモ帳（テキストエディット）のプログラミング向け高機能版と考えてください。コードの色分け表示、入力補完、エラー検出など、コーディングを助ける機能が備わっています。

> **Claude Code 自体はターミナルで動くため、エディタがなくても使えます。**
> ただし、このキットの一部機能（git push 前のコードレビュー）でエディタと連携できるため、ウィザードでエディタの質問が表示されます。
> **エディタを持っていない場合や、よくわからない場合は「なし」を選べば問題ありません。**

#### おすすめエディタ：VS Code

**[VS Code（Visual Studio Code）](https://code.visualstudio.com/)** は、Microsoft が提供する **無料** のコードエディタで、世界で最も多くの開発者に使われています。初心者からプロまで幅広く対応しており、日本語にも対応しています。

| OS | インストール方法 |
|---|---|
| **macOS** | [公式サイト](https://code.visualstudio.com/) からダウンロード → `.app` をアプリケーションフォルダにドラッグ |
| **Windows** | [公式サイト](https://code.visualstudio.com/) からダウンロード → インストーラーを実行 |

> **ヒント**: macOS でインストール後、VS Code を開いて `Cmd + Shift + P` →「shell command」と入力 →「**Shell Command: Install 'code' command in PATH**」を実行すると、ターミナルから `code` コマンドで VS Code を起動できるようになります。これを済ませておくと、ウィザードで「VS Code」を選んだときにスムーズに連携できます。

#### その他の選択肢

| エディタ | 特徴 | 公式サイト |
|---|---|---|
| **Cursor** | VS Code ベースの AI 特化エディタ | [cursor.com](https://www.cursor.com/) |
| **Zed** | 超高速・軽量な次世代エディタ | 

## Links

- Repository: https://github.com/cloudnative-co/claude-code-starter-kit
