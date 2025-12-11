#!/usr/bin/env python3
"""
HSP-Knowledge 記事投稿PR検証スクリプト

記事の形式検証、更新時の検証を行います。
スパム判定はGeminiが担当します。
"""

import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import yaml


class ArticleValidator:
    """記事の検証を行うクラス"""

    def __init__(self, file_path: str, content: str, original_content: Optional[str] = None):
        self.file_path = Path(file_path)
        self.content = content
        self.original_content = original_content
        self.issues: List[str] = []
        self.suggestions: List[Dict] = []

    def validate(self) -> Dict:
        """記事の形式検証を実施（スパム判定はGeminiが担当）"""
        result = {
            "is_valid_format": True,
            "auto_approve": False,
            "issues": [],
            "summary": ""
        }

        # ファイル名検証
        if not self._validate_filename():
            result["is_valid_format"] = False

        # 内容の解析
        front_matter, body = self._parse_markdown()

        if front_matter is None:
            self.issues.append("Front Matterが見つかりません")
            result["is_valid_format"] = False
        else:
            # Front Matter検証
            if not self._validate_front_matter(front_matter):
                result["is_valid_format"] = False

            # 更新時の検証
            if self.original_content:
                if not self._validate_update(front_matter):
                    result["is_valid_format"] = False

        # 本文検証
        if not self._validate_body(body):
            result["is_valid_format"] = False

        # 結果の集約
        result["issues"] = self.issues
        result["suggestions"] = self.suggestions
        # 形式が正しければ自動承認可能（スパム判定はGeminiが担当）
        result["auto_approve"] = result["is_valid_format"]

        # サマリー生成
        result["summary"] = self._generate_summary(result)

        return result

    def _validate_filename(self) -> bool:
        """ファイル名の検証"""
        filename = self.file_path.name

        # テンプレート名チェック
        invalid_names = ['template.md', 'new-article.md', '-new-article.md']
        if filename in invalid_names or filename.endswith('-new-article.md'):
            self.issues.append(f"ファイル名がテンプレートのままです: {filename}")
            return False

        # 日付形式チェック (YYYY-MM-DD-*.md)
        pattern = r'^\d{4}-\d{2}-\d{2}-.+\.md$'
        if not re.match(pattern, filename):
            self.issues.append(f"ファイル名が 'YYYY-MM-DD-title.md' 形式ではありません: {filename}")
            return False

        return True

    def _parse_markdown(self) -> Tuple[Optional[Dict], str]:
        """Markdownファイルを解析してFront Matterと本文に分離"""
        # Front Matterの抽出
        front_matter_pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
        match = re.match(front_matter_pattern, self.content, re.DOTALL)

        if not match:
            return None, self.content

        try:
            front_matter = yaml.safe_load(match.group(1))
            body = match.group(2).strip()
            return front_matter, body
        except yaml.YAMLError as e:
            self.issues.append(f"Front MatterのYAML解析エラー: {str(e)}")
            return None, match.group(2).strip()

    def _validate_front_matter(self, front_matter: Dict) -> bool:
        """Front Matterの検証"""
        required_fields = ['title', 'date', 'author', 'tags', 'summary']
        is_valid = True

        for field in required_fields:
            if field not in front_matter:
                self.issues.append(f"Front Matterに必須フィールド '{field}' がありません")
                is_valid = False

        # author が テンプレートのままでないかチェック
        if 'author' in front_matter:
            invalid_authors = ['あなたの名前', 'Your Name', 'Author Name', '']
            if front_matter['author'] in invalid_authors:
                self.issues.append("投稿者名がテンプレートのままです")
                is_valid = False

        # title が テンプレートのままでないかチェック
        if 'title' in front_matter:
            if '記事タイトル' in front_matter['title'] or 'ここを変更' in front_matter['title']:
                self.issues.append("タイトルがテンプレートのままです")
                is_valid = False

        return is_valid

    def _validate_update(self, front_matter: Dict) -> bool:
        """記事更新時の検証（投稿者名・日付の不変性）"""
        if not self.original_content:
            return True

        original_fm, _ = self._parse_markdown_content(self.original_content)
        if not original_fm:
            return True

        is_valid = True

        # 投稿者名が変更されていないかチェック
        if 'author' in original_fm and 'author' in front_matter:
            if original_fm['author'] != front_matter['author']:
                self.issues.append(
                    f"投稿者名が変更されています: '{original_fm['author']}' → '{front_matter['author']}'"
                )
                is_valid = False

        # 日付が変更されていないかチェック（URL維持のため）
        if 'date' in original_fm and 'date' in front_matter:
            original_date = str(original_fm['date'])
            new_date = str(front_matter['date'])
            if original_date != new_date:
                self.issues.append(
                    f"⚠️ dateフィールドの変更を検出: '{original_date}' → '{new_date}' (URLが変わります)"
                )

                # lastupdate フィールドが更新されているかチェック
                original_lastupdate = original_fm.get('lastupdate')
                new_lastupdate = front_matter.get('lastupdate')

                # dateを元に戻し、lastupdateを追加するsuggestionを生成
                from datetime import datetime
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S +09:00')

                suggestion_text = self._generate_date_fix_suggestion(
                    front_matter,
                    original_date,
                    current_time
                )

                self.suggestions.append({
                    "type": "date_changed",
                    "message": "dateフィールドを元に戻し、代わりにlastupdateを使用してください",
                    "suggestion": suggestion_text,
                    "original_date": original_date,
                    "new_date": new_date
                })

                # dateの変更はマージをブロック
                is_valid = False

        return is_valid

    def _generate_date_fix_suggestion(self, front_matter: Dict, original_date: str, current_time: str) -> str:
        """dateを元に戻し、lastupdateを追加するsuggestionを生成"""
        # Front Matterを再構築（dateを元に戻し、lastupdateを追加）
        updated_fm = front_matter.copy()
        updated_fm['date'] = original_date
        updated_fm['lastupdate'] = current_time

        # YAMLとして出力
        fm_lines = []
        fm_lines.append("---")

        # 元の順序を保持しつつlastupdateを追加
        # 推奨順序: layout, title, date, lastupdate, author, tags, summary
        field_order = ['layout', 'title', 'date', 'lastupdate', 'author', 'tags', 'summary']

        # 順序に従ってフィールドを出力
        for field in field_order:
            if field in updated_fm:
                value = updated_fm[field]
                if isinstance(value, list):
                    fm_lines.append(f"{field}: {yaml.dump(value, allow_unicode=True, default_flow_style=True).strip()}")
                elif isinstance(value, str):
                    fm_lines.append(f"{field}: {value}")
                else:
                    fm_lines.append(f"{field}: {value}")

        # 残りのフィールド（field_orderにないもの）も出力
        for field, value in updated_fm.items():
            if field not in field_order:
                if isinstance(value, list):
                    fm_lines.append(f"{field}: {yaml.dump(value, allow_unicode=True, default_flow_style=True).strip()}")
                elif isinstance(value, str):
                    fm_lines.append(f"{field}: {value}")
                else:
                    fm_lines.append(f"{field}: {value}")

        fm_lines.append("---")

        return "\n".join(fm_lines)

    def _parse_markdown_content(self, content: str) -> Tuple[Optional[Dict], str]:
        """Markdown内容を解析（ヘルパーメソッド）"""
        front_matter_pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
        match = re.match(front_matter_pattern, content, re.DOTALL)

        if not match:
            return None, content

        try:
            front_matter = yaml.safe_load(match.group(1))
            body = match.group(2).strip()
            return front_matter, body
        except yaml.YAMLError:
            return None, match.group(2).strip()

    def _validate_body(self, body: str) -> bool:
        """本文の検証"""
        if not body or len(body.strip()) < 50:
            self.issues.append("本文が短すぎるか、存在しません")
            return False

        # テンプレートのままでないかチェック
        # 本文の最初の3行を取得（コードブロック内などを誤判定しないよう、冒頭のみチェック）
        body_lines = body.strip().split('\n')
        first_lines = body_lines[:3]

        # テンプレートに含まれる文言（完全一致または行の主要部分）
        template_patterns = [
            r'^\s*ここに本文を書きます[。\.]*\s*$',  # 「ここに本文を書きます」または「ここに本文を書きます。」
            r'^\s*ここに記事の本文を書いてください[。\.]*\s*$',  # 別バージョンのテンプレート
        ]

        for line in first_lines:
            for pattern in template_patterns:
                if re.match(pattern, line):
                    self.issues.append(f"本文がテンプレートのままです（冒頭に「{line.strip()}」が残っています）")
                    return False

        return True

    def _generate_summary(self, result: Dict) -> str:
        """判定結果のサマリーを生成（形式チェックのみ）"""
        if not result["is_valid_format"]:
            return f"形式に問題があります: {', '.join(self.issues)}"

        if result["auto_approve"]:
            if len(self.issues) == 0:
                return "記事の形式は適切です。"
            else:
                return f"記事の形式は承認可能です。軽微な改善提案: {', '.join(self.issues)}"

        return f"要確認: {', '.join(self.issues)}"


def main():
    """メイン処理"""
    if len(sys.argv) < 2:
        print("Usage: python check_pr.py <file_path> [original_file_path]")
        sys.exit(1)

    file_path = sys.argv[1]
    original_file_path = sys.argv[2] if len(sys.argv) > 2 else None

    # ファイル読み込み
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(json.dumps({
            "error": f"ファイルの読み込みに失敗: {str(e)}",
            "is_valid_format": False,
            "auto_approve": False,
        }))
        sys.exit(1)

    # 元ファイルの読み込み（更新の場合）
    original_content = None
    if original_file_path and os.path.exists(original_file_path):
        try:
            with open(original_file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
        except Exception:
            pass

    # 検証実行
    validator = ArticleValidator(file_path, content, original_content)
    result = validator.validate()

    # 結果を JSON で出力
    print(json.dumps(result, ensure_ascii=False, indent=2))

    # 終了コード
    sys.exit(0 if result["auto_approve"] else 1)


if __name__ == "__main__":
    main()