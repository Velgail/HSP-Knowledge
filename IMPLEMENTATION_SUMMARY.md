# 実装完了: 記事投稿の自動検証・承認システム

## ✅ 実装した機能

### 1. Gemini Code Assistによるスパム判定 (`.gemini/prompts.yaml`)

記事のスパム判定と形式検証を行うためのプロンプトエンジニアリングを実装しました。

**検証項目:**
- HSP関連の内容かどうか
- スパム判定（広告、乱文、不適切な内容）
- Front Matterの形式チェック
- ファイル名の検証
- テンプレートのまま残っている箇所の検出

### 2. PR検証スクリプト (`scripts/check_pr.py`)

記事の総合的な検証を行うPythonスクリプトを実装しました。

**機能:**
- ファイル名検証（`YYYY-MM-DD-title.md` 形式、テンプレート名でない）
- Front Matter検証（必須フィールド、テンプレートのまま残っていない）
- 本文検証（テンプレートのまま残っていない、最低限の長さ）
- スパム判定（HSPキーワード、外部リンク数、スパムワード）
- **更新時の検証**（投稿者名が変更されていない）
- JSON形式での結果出力

### 3. GitHub Actionsワークフロー (`.github/workflows/pr-auto-review.yml`)

記事投稿PRの自動検証と自動承認・マージを行うワークフローを実装しました。

**ワークフロー:**

#### Job 1: `validate-article` (PR作成時)
- PRで変更された記事ファイルを検証
- `check_pr.py` を実行して検証結果を取得
- 検証結果をPRにコメントとして投稿

#### Job 2: `auto-merge` (@publish コマンド検知時)
- コメントに `@publish` が含まれているか確認
- コメント投稿者がPR作成者本人か確認
- 記事を再検証
- 検証に合格した場合、自動的にApproveとMergeを実行

### 4. ドキュメント

- `docs/AUTO_REVIEW_SYSTEM.md`: システムの詳細な説明
- `README.md`: クイックスタートガイドを追加

## 🎯 使い方

### 記事投稿者向け

1. `_posts/` フォルダに記事を作成
2. PRを開く
3. 自動検証の結果を確認
4. ✅ 承認可能な場合、`@publish` とコメント
5. 自動的にマージ完了！

### @publish コマンド

- **構文**: PRのコメント欄に `@publish` と入力
- **使用条件**: PRの作成者のみ
- **動作**: 検証に合格している場合、自動的にApproveとMergeを実行

## 🧪 テスト結果

### ✅ 正常な記事（自動承認可能）
```json
{
  "is_spam": false,
  "is_valid_format": true,
  "auto_approve": true,
  "issues": [],
  "summary": "記事は適切です。形式も正しく、HSPに関連する有益な内容です。"
}
```

### ⚠️ テンプレートのまま
```json
{
  "is_spam": false,
  "is_valid_format": false,
  "auto_approve": false,
  "issues": [
    "本文がテンプレートのままです: 'ここに本文を書きます'"
  ],
  "summary": "形式に問題があります: 本文がテンプレートのままです: 'ここに本文を書きます'"
}
```

### ❌ スパム判定
```json
{
  "is_spam": true,
  "is_valid_format": true,
  "auto_approve": false,
  "issues": [],
  "summary": "スパムと判定されました。記事内容が不適切です。"
}
```

## 📁 ファイル構成

```
.gemini/
  prompts.yaml              # Gemini Code Assistのプロンプト設定
.github/
  workflows/
    pr-auto-review.yml      # 自動検証・承認ワークフロー
scripts/
  check_pr.py               # PR検証スクリプト
docs/
  AUTO_REVIEW_SYSTEM.md     # システムの詳細ドキュメント
README.md                   # クイックスタートガイドを追加
.gitignore                  # Pythonキャッシュを追加
```

## 🔒 セキュリティ

- `@publish` コマンドはPRの作成者のみが使用可能
- 投稿者名（author）の変更は検出され、自動承認されない
- スパム判定により不適切な内容は自動的に却下
- 検証に合格した記事のみが自動マージされる

## 🚀 今後の拡張案

- Gemini APIを直接呼び出してスパム判定を強化
- 記事の品質スコアリング
- 自動的なタグの提案
- 類似記事の検出
- コードブロックの構文チェック

## 📝 コミット履歴

```
feat: 記事投稿の自動検証・承認システムを実装
chore: Pythonキャッシュファイルを.gitignoreに追加
```

## ✨ 完了

すべての要件を実装しました：

1. ✅ Gemini Code Assistによるスパム判定プロンプト
2. ✅ 記事更新時の投稿者名とファイル名の検証
3. ✅ 形式が適合している記事の自動認定
4. ✅ @publish コマンドによる自動承認・マージ
5. ✅ GitHub Actionsによる完全自動化

システムは即座に利用可能です！
