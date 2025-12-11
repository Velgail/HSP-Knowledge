---
layout: post
title: HSPスクリプトエディタのUTF-8版「hsed3u8.exe」を作りました！
date: 2025-12-11 22:50:11 +09:00
author: Velgail
tags: [HSP3, 作品紹介, 中級, UTF-8]
summary: HSPのファイルはShift-JISでの作成となり、現代的な言語としてはとてもレガシーな状態に陥っている。このエディタを利用することで、UTF-8でのファイル編集となり、元々のHSP3と最大限互換したShift-JISコンパイルと、hsp3utf適合コンパイルをエディタレベルで実現する。
---

<img width="100%" alt="HSP3UTFランタイムとHSP3ランタイム、hsed3とhsed3u8の比較画像" src="https://github.com/user-attachments/assets/026bf5b9-f670-4a90-a2f2-74fbe4a0f6f8" />
上がHSP3UTFランタイム、下がHSP3ランタイム
左がhsed3（今迄のエディタ）、右がhsed3u8（今回のエディタ）

## 概要

**hsed3u8.exe** は、HSP（Hot Soup Processor）標準のスクリプトエディタ（hsed3.exe）をベースに、**UTF-8（原則BOMなし）** での保存・読み込みに対応させた派生エディタです。

従来のShift-JIS環境では困難だった **GitHubでのソースコード管理（日本語コメントの文字化け回避、正確な差分表示）** を、HSPの使い勝手はそのままに実現します。

## 解決する課題

HSP標準の `hsed3.exe` はShift-JISでファイルを保存するため、現代の開発フローにおいて以下の問題がありました。

  * **GitHubでの文字化け**: ブラウザ上で日本語コメントが正しく表示されない。
  * **差分確認の困難さ**: Pull Request等のレビュー時に、日本語を含む行の差分が正確に表示されない。
  * **CI/CD連携**: UTF-8を前提としたツールチェーンとの連携が難しい。

**hsed3u8.exe** は、ファイルをUTF-8（原則BOMなし）で扱うことでこれらの問題を解決します。

-----

## 主な機能

### 1\. UTF-8（BOMなし）での読み込み・保存

エディタの挙動を以下のように変更しています。

  * **読み込み**: ファイルの文字コード（UTF-8 / Shift-JIS）を自動判定して開きます。
  * **保存**: 新規・既存問わず、常に **UTF-8（原則BOMなし）** で保存します。(元ファイルがUTF-8-BOMの場合のみBOMありでの保存)

### 2\. UTF-8モードでのコンパイル

コンパイル時、HSPコンパイラに対して明示的に「UTF-8入力モード」を指定します。

| ランタイム | 挙動 |
| :--- | :--- |
| **hsp3.exe** | Shift-JISとしてコンパイル（従来の挙動） |
| **hsp3utf.exe** | **UTF-8としてコンパイル（Unicode文字表示可能）** |
| **HSP3Dish** | Shift-JISとしてコンパイル（Windows上ではUnicode表示不可） |

### 3\. 既存プロジェクトの一括変換

メニューの **「ツール」→「参照ファイルをUTF-8に変換」** から、プロジェクトフォルダ内の全ソースコード（`.hsp`, `.as`）をUTF-8へ一括変換できます。

> **安心設計**
>
>   * **再帰的処理**: サブフォルダ内のファイルも全て検出します。
>   * **自動バックアップ**: 変換対象ファイルは必ず `.bak` ファイルを作成してから書き換えます。
>   * **重複防止**: 既にUTF-8のファイルはスキップされます。

### 4\. 標準ヘッダのUTF-8化（u8common）

初回の変換実行時、HSPインストールフォルダ内の `common` フォルダを複製し、UTF-8変換済みの `u8common` フォルダを自動生成します。
これにより、`#include` で読み込む標準モジュールもUTF-8として正しくコンパイルされます。

-----

## 導入と使い方

### インストール

1.  ビルド済みの `hsed3u8.exe` をHSPのインストールフォルダ（`hsed3.exe` がある場所）に配置します。

### 新規プロジェクトの場合

1.  `hsed3u8.exe` を起動してスクリプトを記述・保存します。自動的にUTF-8となります。

### 既存プロジェクト（Shift-JIS）の移行手順

1.  `hsed3u8.exe` で既存の `.hsp` ファイルを開きます。
2.  メニューバーから **「ツール」→「参照ファイルをUTF-8に変換」** を選択します。
<img width="100%" alt="image" src="https://github.com/user-attachments/assets/ddc4a24d-c653-47d9-beed-b308907a1a5e" />
3.  確認ダイアログで「はい」を押すと、関連ファイルが一括変換されます。
<img width="100%" alt="image" src="https://github.com/user-attachments/assets/f2981ce3-c7ba-4507-8850-b6b608fff1c7" />
<img width="100%" alt="image" src="https://github.com/user-attachments/assets/6a7f4f64-759d-44f1-9ad5-58fe36c4735c" />


-----

## 技術的詳細（Implementation Details）

本エディタは OpenHSP をフォークし、以下の実装変更を行っています。

### エンコーディング検出ロジック

ファイル読み込み時、以下の優先順位でエンコーディングを判定します。

1.  **BOMチェック**: UTF-8 BOM または UTF-16 LE/BE の確認。
2.  **UTF-8妥当性検証**: バイト列が正当なUTF-8シーケンスかチェック。
3.  **Shift-JIS**: 上記以外はShift-JIS（CP932）として扱う。

<!-- end list -->

```cpp
// convert_utf8.cpp より抜粋
static EncodingType DetectEncoding(const unsigned char* data, DWORD size) {
    if (size >= 3 && data[0] == 0xEF && data[1] == 0xBB && data[2] == 0xBF) {
        return ENC_UTF8_BOM;
    }
    if (IsValidUTF8(data, size)) {
        return ENC_UTF8;
    }
    return ENC_SHIFT_JIS; // Fallback
}
```

### コンパイラへの指示

`hsc_comp` 関数呼び出し時、第2引数にフラグ `32` を追加することで、コンパイラにUTF-8入力を指示しています。

```cpp
// 32 = UTF-8 Input Mode
a = hsc_comp(1, 32, hsp_debug, 0);
```

### 一括変換プロセス

変換処理はデータの損失を防ぐため、以下のフローで実装されています。

1.  ファイルをメモリへ読み込み
2.  エンコーディング検出（既にUTF-8なら終了）
3.  `.bak` バックアップファイルの作成（`CopyFileA`）
4.  内部で WideChar (UTF-16) を経由して UTF-8 へ変換
5.  ファイルへの書き込み

## リポジトリ情報

ソースコードはGitHubにて公開しています。

  * **Repository**: [Velgail/OpenHSP (branch: feature/hsed3u8)](https://github.com/Velgail/OpenHSP/tree/feature/hsed3u8)
  * **License**: OpenHSP ライセンスに準拠

-----

ご質問やバグ報告は、このページの Discussions までお願いします。
HSPでのモダンな開発フロー構築にお役立てください。
