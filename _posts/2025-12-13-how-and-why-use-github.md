---
layout: post
title: 初心者でもわかる！GitHubって何？～ケンタとミサキの優しいGit入門～
date: 2025-12-13 03:43:20 +09:00
author: Velgail & Claude 4.5 Opus & Nano Banana Pro
tags: [HSP3, ゲーム制作, Tips, 入門, GitHub, Git, バージョン管理]
summary: 事件です！　昨日まで動いていたコードが動かなくなりました。しかも上書きしてしまって直しかたがわからない?!　そんなときでもGitとGitHubを使うと便利にタイムトラベルできるんです！
---

# 初心者でもわかる！GitHubって何？～ケンタとミサキの優しいGit入門～

{% include toc.html %}

(挿絵は全てGemini製のため、一部文字列に誤りがあります)

**「もう失敗を恐れなくていい。」**

<img width="80%" alt="image" src="https://github.com/user-attachments/assets/ec2f448d-ba32-42e3-8e03-545668da97dd" />

**昨日まで動いてたのに、今日なぜか動かない？**

**しかも修正前に戻れない?!　その絶望、GitHubで終わりにしよう。**

**登場人物**
- **ケンタ**: HSP中級者だけど、Gitはほぼ知らない若手プログラマー
- **ミサキ**: 優しい先輩エンジニア。GitHubは日常的に使っている

---

## プロローグ：ファイル管理の地獄

ある日の開発室。ケンタのPCの前で......

{% include chat.html face="https://github.com/user-attachments/assets/b2eef45a-ef34-416b-8eba-a9bdac251cff" name="ケンタ" color="blue" text='うわあああ...絶望...（頭を抱える）' %}
{% include chat.html face="https://github.com/user-attachments/assets/19055df0-5052-4e10-b61a-4569e5d49775" name="ミサキ" color="red" text='あら？どうしたのケンタくん。顔色悪いわよ？' %}
{% include chat.html face="https://github.com/user-attachments/assets/f1a20f91-5738-4e89-b847-4f651f4c5c9b" name="ケンタ" color="blue" text='あのですね...機能を追加するたびにファイルが混乱してきて...もう何が最新版かわからなくなっちゃったんです...' %}
{% include chat.html face="https://github.com/user-attachments/assets/6f6a4fb4-9ffa-44df-8dfd-b134831e4d76" name="ミサキ" color="red" text='あー、あるある。`shooting.hsp`、`shooting_tama.hsp`、`shooting_tama_atari.hsp`、`shooting_tama_atari_sound.hsp`、`shooting_ugoku_yatsu.hsp`...って感じでファイルが増えていくやつね（笑）' %}
{% include chat.html face="https://github.com/user-attachments/assets/f1a20f91-5738-4e89-b847-4f651f4c5c9b" name="ケンタ" color="blue" text='まさに！どれが最新かわからなくて、バックアップもぐちゃぐちゃで...先輩、どうしたらいいんですか...！？' %}

ファイル名で管理していると、こういう問題は誰もが一度は経験するもの。でも、実はこれを解決する素晴らしいツールがあるんです。

---

## 第1章：GitHubって何？

### Gitとは？

{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='それなら、GitHubを使ってみたらどう？' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='ギッ、ギットハブ...？（聞いたことはあるけど）' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='そう。Gitっていうのは、簡単に言うとファイルの履歴を管理してくれるツールなの。GitHubは、そのGitをネット上で使えるようにしたサービスよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='えっと...つまり、どういうことですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='例えば、ゲームのセーブデータって、「セーブ1」「セーブ2」「セーブ3」って複数保存できるでしょ？Gitはそれをプログラムでやってくれるの。「この時点のコード」「あの時点のコード」って、全部記録しておけるのよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='おお...！それなら、間違えて大事なコードを消しちゃっても戻せるってことですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='その通り！しかも、「いつ」「誰が」「何を」「なぜ」変更したかも全部記録できるの。メモも残せるから、後で見返したときに「あれ、なんでこうしたんだっけ？」ってならないのよ' %}

<img width="100%" alt="image" src="https://github.com/user-attachments/assets/c7672f5f-032c-47fa-85cf-c3131540932c" />

Gitとは「バージョン管理システム」のこと。プログラムの変更履歴を記録して、過去の状態に戻したり、変更内容を確認したりできる優れものです。

---

### 公開されちゃうの？

{% include chat.html face="https://github.com/user-attachments/assets/f1a20f91-5738-4e89-b847-4f651f4c5c9b" name="ケンタ" color="blue" text='でも、待ってください！GitHubって、世界中に公開されちゃうんですよね...？僕の恥ずかしいコードが全世界に晒されるのは...（青ざめる）' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='あはは、安心して。それは「パブリック（公開）リポジトリ」の場合ね。GitHubには「プライベート（非公開）リポジトリ」っていう機能があるの' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='プライベート...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='うん。プライベートにしておけば、自分だけ、もしくは許可した人だけが見られるようになるの。だから、個人の勉強用とか、会社の秘密のプロジェクトとかも安心して使えるのよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/6436d587-a398-4d60-b3cc-9a12fb429f8c" name="ケンタ" color="blue" text='そうなんですか！じゃあ、僕のぐちゃぐちゃなコードも安全に管理できるんですね...' %}
{% include chat.html face="https://github.com/user-attachments/assets/29b59426-e842-4399-a21d-592b354c534d" name="ミサキ" color="red" text='そうそう。むしろ、ぐちゃぐちゃなコードだからこそ、Gitで整理していくのがおすすめよ。後で「あの時はこんなコード書いてたんだ」って成長が実感できるから' %}

GitHubは無料でプライベートリポジトリを作成できます（無制限！）。初心者のうちは、まずプライベートで練習するのがおすすめです。

---

### GitHubでできること

{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='じゃあ、GitHubで具体的に何ができるか説明するわね' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='お願いします！' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='まず一番大事なのが「タイムマシン機能」。さっき言ったように、過去のどの時点にも戻れるの' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='それ、すごく便利そうです！「やっぱりさっきの方が良かった」ってなった時とか...' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='そうそう。例えば、「昨日の夜までは動いてたのに、今日いじったら動かなくなった」って時、昨日の状態に簡単に戻せるのよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='便利すぎる...！' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='それから、「ブランチ」っていう機能もあるの。これは、元のコードはそのままにして、別の場所で新機能を試せるの' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='別の場所...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='うん。例えば、「今動いてるゲーム」はそのままにして、「新しい敵キャラを追加してみる実験」を別のブランチでやるの。うまくいったら元に合流させて、失敗したら捨てればいい' %}
{% include chat.html face="https://github.com/user-attachments/assets/d75d2bde-5e93-4095-8591-f6ba676960d2" name="ケンタ" color="blue" text='なるほど...！「完成版」と「実験版」を分けて管理できるってことですね' %}

<!-- 画像案：ブランチの概念図（mainから分岐して戻ってくる矢印） -->

ブランチは、同じプロジェクトの中で「平行世界」を作れる機能。メインの開発を止めずに、新しいアイデアを試せます。

---

{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='あと、すごく便利なのが「複数のパソコンで同じプロジェクトを扱える」ってことね' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='複数のパソコン...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='そう。例えば、家のデスクトップPCと、持ち運び用のノートPCでプログラミングするとするでしょ？' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='はい...僕、まさにそうなんです。家と学校でプログラミングしたくて...' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='だったら、GitHubは最高よ！家でコミット＆プッシュしておけば、学校のPCでプルするだけで、続きから作業できるの' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='えっ、そんなに簡単なんですか！？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='簡単よ。USBメモリでファイルを持ち運ぶ必要もないし、「あれ、最新版どっちだっけ？」って悩むこともないの' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='それ、めっちゃ便利じゃないですか...！今までUSBメモリで持ち運んでて、時々古いバージョン上書きしちゃってたんです...' %}
{% include chat.html face="https://github.com/user-attachments/assets/6f6a4fb4-9ffa-44df-8dfd-b134831e4d76" name="ミサキ" color="red" text='あるある（笑）。GitHubを使えば、そういう悲劇とはおさらばよ' %}

GitHubは「クラウドストレージ」としても機能します。ただのファイル保存ではなく、バージョン管理もできる高機能なストレージです。

---

## 第2章：始める前の準備

### 難しくないの？

{% include chat.html face="https://github.com/user-attachments/assets/f1a20f91-5738-4e89-b847-4f651f4c5c9b" name="ケンタ" color="blue" text='でも、そういうツールって、使い方が難しそうで...コマンドとか覚えないといけないんですよね？' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='確かに、Gitのコマンドは最初はちょっと戸惑うかもね。でも大丈夫！' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='大丈夫なんですか...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='うん。実は、GitHubには「GitHub Desktop」っていうアプリがあるの。これを使えば、マウスでポチポチするだけでGitが使えるのよ<br/><img width="100%" alt="image" src="https://github.com/user-attachments/assets/bc7a82af-4673-439c-acb9-af1b977736d9" />' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='えっ、コマンド打たなくていいんですか！？' %}
{% include chat.html face="https://github.com/user-attachments/assets/ae3eb7e8-10da-411f-884f-c5e06f315528" name="ミサキ" color="red" text='打たなくていいの（笑）。ボタンを押すだけで保存できるし、履歴も見やすいし、初心者にはすごくおすすめよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/6436d587-a398-4d60-b3cc-9a12fb429f8c" name="ケンタ" color="blue" text='それなら僕でもできそう...！' %}
{% include chat.html face="https://github.com/user-attachments/assets/29b59426-e842-4399-a21d-592b354c534d" name="ミサキ" color="red" text='それに、慣れてきたらコマンドも覚えていけばいいから。最初はアプリで感覚をつかむのが一番よ' %}

GitHub Desktopは無料でダウンロードできます。Windows版もMac版もあり、直感的な操作でGitを使えます。

[GitHub Desktop](https://github.com/apps/desktop?ref_product=desktop&ref_type=engagement&ref_style=button&locale=ja)

---

### ⚠️ 重要：UTF-8エディタを使おう

{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='あ、そうだ。GitHubを使う前に、一つ大事な準備があるの' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='大事な準備...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='HSPのエディタ、普段は「hsed3.exe」を使ってるでしょ？' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='はい、標準のやつですよね' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='GitHubで使うなら、「hsed3u8.exe」に変えた方がいいわ。これはUTF-8版のエディタなの' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='ユーティーエフエイト...？何が違うんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='文字コードの違いね。標準版はShift-JISっていう古い形式なんだけど、GitHubはUTF-8が標準なの' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='それって、使わないとどうなるんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/20c02915-cf54-45c3-a170-eadbc77d279d" name="ミサキ" color="red" text='GitHubで「どこを変更したか」を見る画面があるんだけど、文字コードが違うと文字化けして、まともに比較できなくなっちゃうのよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/f1a20f91-5738-4e89-b847-4f651f4c5c9b" name="ケンタ" color="blue" text='えっ、それは困る...！' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='だから、最初からUTF-8版を使っておけば安心ってこと。使い方は標準版とほとんど同じだから、心配いらないわ' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='わかりました！hsed3u8.exeを使います！' %}

**hsed3u8.exe（UTF-8版エディタ）について**

この記事を書いているときにUTF-8版じゃないと駄目じゃん！　と気付いてしまったので急遽作ったやつです。詳しい使い方は[こちらの記事](https://hsp-knowledge.github.io/2025/12/11/introduce-hsed3u8.html)を参照してください。

GitHubでコードの差分（Diff）を正しく表示するために、UTF-8でファイルを保存することが重要です。

---

### アカウントを作ろう

{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='じゃあ、実際の使い方を簡単に説明するわね' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='はい！' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='まず、GitHubのサイトでアカウントを作るの。メールアドレスがあれば無料で作れるわ<br/><img width="100%" alt="image" src="https://github.com/user-attachments/assets/1495e0f9-79ea-4df7-b07d-89972ddd6af9" />' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='アカウント登録って、面倒じゃないですか...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='全然！メールアドレスとパスワード、ユーザー名を決めるだけで、1分もかからないわよ<br/><img width="100%" alt="image" src="https://github.com/user-attachments/assets/b46fff54-a0b2-466d-b8e9-5b451e598532" />' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='そんなに簡単なんですか！' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='それに、実はGitHubは2018年にMicrosoftに買収されて、今はMicrosoft傘下なの' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='えっ、マイクロソフト！？Windowsの！？' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='そう！だから、すごく安心して使えるのよ。世界最大のソフトウェア企業がバックにいるから、サービスが突然終了する心配もないしね' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='なるほど...！Windowsの会社なら信頼できますね！' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='大手企業も、中小企業もお金を払ってPrivateリポジトリで自社サービスを開発しているわよ。あ、でも個人向けはPrivateが無料だから安心して使ってね！' %}


GitHubは2018年にMicrosoftが75億ドルで買収。世界最大のソフトウェア企業の傘下にあるため、安定性と信頼性は抜群です。

Privateリポジトリは5人までの共有が無料で、それ以上が有料なのです。会社だと5人を超えることは普通なので、結果として有料になっているのです。HSP開発者として使う分には無料です！

---

{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='次に、「リポジトリ」っていうのを作るの。これは、プロジェクト専用の保存場所みたいなものね' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='リポジトリ...ゲームごとに一つ作る感じですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='そうそう、その理解で大丈夫！「シューティングゲーム用」「RPG用」って分けて作るイメージね' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='わかりました！' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='そしたら、GitHub Desktopでそのリポジトリを「クローン」するの。これは、ネット上のリポジトリを自分のPCにコピーすることよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/d75d2bde-5e93-4095-8591-f6ba676960d2" name="ケンタ" color="blue" text='ダウンロードみたいなものですね' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='その通り！で、普段通りプログラムを書いて、キリのいいところで「コミット」するの' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='コミット...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='セーブのことよ。「ここまでの変更を記録する」って操作ね。その時に「敵キャラのスピードを調整」とかメモを残すの' %}
{% include chat.html face="https://github.com/user-attachments/assets/d75d2bde-5e93-4095-8591-f6ba676960d2" name="ケンタ" color="blue" text='なるほど...セーブデータに名前をつける感じですね' %}
{% include chat.html face="https://github.com/user-attachments/assets/ae3eb7e8-10da-411f-884f-c5e06f315528" name="ミサキ" color="red" text='いい例え！最後に「プッシュ」して、変更をネット上のGitHubに送れば完了よ' %}

基本的な流れは「クローン（コピー）→ 編集 → コミット（保存）→ プッシュ（アップロード)」です。

---

## 第3章：実際にやってみよう！

### リポジトリを作成する

{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='じゃあ、実際にケンタくんのシューティングゲームをGitHubで管理してみましょうか' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='はい！お願いします！' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='まず、GitHubにログインして、右上の「+」ボタンから「New repository」を選ぶの' %}
{% include chat.html face="https://github.com/user-attachments/assets/f142bf03-36b0-481e-b729-1a9689b91d74" name="ケンタ" color="blue" text='（操作しながら）えっと...あった！「New repository」... <br/><img width="100%" alt="image" src="https://github.com/user-attachments/assets/cd9eca07-5ec4-45c9-aaa4-14a8380e0bc1" />' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='リポジトリの名前は「shooting-game」とかでいいわね。下の方に「Private」ってチェックボックスがあるから、それにチェックを入れて<br/><img width="100%" alt="Screen Shot 2025-12-10 at 01 12 37" src="https://github.com/user-attachments/assets/9e89743e-6983-4eba-8277-a4abf514ae43" />' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='プライベート...これで自分だけになるんですね。チェックしました！' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='「Create repository」ボタンを押したら、リポジトリの完成よ' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='できた！なんか、自分専用の保管庫ができた気分です...！<br/><img width="100%" alt="Screen Shot 2025-12-10 at 01 13 55" src="https://github.com/user-attachments/assets/2f8c31a1-c01c-4520-9208-3ff5aecd9f0e" />' %}

<!-- 画像案：New repository作成画面（Private選択状態） -->

---

{% include chat.html face="https://github.com/user-attachments/assets/29b59426-e842-4399-a21d-592b354c534d" name="ミサキ" color="red" text='いい感覚ね（笑）。次に、GitHub Desktopを開いて、「Clone a repository」を選んで、今作ったリポジトリを選ぶの' %}
{% include chat.html face="https://github.com/user-attachments/assets/f142bf03-36b0-481e-b729-1a9689b91d74" name="ケンタ" color="blue" text='えっと...「shooting-game」...あった！どこに保存しますか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='ドキュメントフォルダとか、わかりやすい場所でいいわよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/f142bf03-36b0-481e-b729-1a9689b91d74" name="ケンタ" color="blue" text='（操作中）...できました！' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='じゃあ、そのフォルダに、今まで作ってたHSPファイルをコピーしてみて' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='はい...（コピー中）...入れました' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='GitHub Desktopを見てみて。左側に変更されたファイルが表示されてるはずよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='ホントだ！「shooting.hsp」って表示されてる...！' %}

<!-- 画像案：GitHub Desktopで変更ファイルが表示されている画面 -->

---

### .gitignoreを設定する

{% include chat.html face="https://github.com/user-attachments/assets/f142bf03-36b0-481e-b729-1a9689b91d74" name="ケンタ" color="blue" text='（ファイルをコピーして）...あれ、先輩、変なファイルも表示されてます...' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='変なファイル？どんなの？' %}
{% include chat.html face="https://github.com/user-attachments/assets/f142bf03-36b0-481e-b729-1a9689b91d74" name="ケンタ" color="blue" text='えっと...「hsptmp」とか「obj」とか「packfile」とか...' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='あー！それはHSPが自動で作る一時ファイルね。実行したりコンパイルすると勝手にできるやつ' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='これ、コミットしちゃダメなんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='ダメダメ！これをコミットすると、実行するたびに『ファイルが変更された』って表示されて、めちゃくちゃ混乱するわよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/f1a20f91-5738-4e89-b847-4f651f4c5c9b" name="ケンタ" color="blue" text='えっ、それは困る...！' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='こういう『管理しなくていいファイル』を指定するために、「.gitignore（ギットイグノア）」っていうファイルを作るの' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='ギットイグノア...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='うん。『ignore（無視する）』って意味ね。このファイルに書いたものは、Gitが無視してくれるのよ' %}

HSPは実行時に一時ファイルを自動生成します。これらはプログラムの本体ではないので、Gitで管理する必要はありません。

---

### HSP用の.gitignoreファイル

プロジェクトフォルダに`.gitignore`という名前のファイルを作成し、以下の内容を記述します。これはHSP向けの最低限のオススメ設定です。

```gitignore
# HSPの一時ファイル
hsptmp
obj/
packfile
*.ax

# 実行ファイル（必要に応じて）
*.exe

# Windowsのゴミファイル
Thumbs.db
desktop.ini
```

{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='あの、「#」から始まる行は何ですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='それは「コメント」ね。メモみたいなもので、Gitは無視するわ。自分が後で見返すときのために書いておくの。HSPで言うなれば、 `;` コメント、あるいは `//` コメントよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/d75d2bde-5e93-4095-8591-f6ba676960d2" name="ケンタ" color="blue" text='なるほど...親切ですね' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='あと、「`*.exe`」は『すべてのexeファイル』って意味。「`*`」はワイルドカードって言って、『何でもいい』って意味なの' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='へぇ...便利ですね！' %}

<!-- 画像案：.gitignore設定後、不要ファイルが消えた画面 -->

.gitignoreファイルは、プロジェクトの「門番」のようなもの。一度作っておけば、あとは自動で不要ファイルを弾いてくれます。

---

### 初めてのコミット

{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='じゃあ、初めてのコミットをしてみましょう。左下の「Summary」っていう欄に、メモを書くの' %}
{% include chat.html face="https://github.com/user-attachments/assets/b748d508-55d0-4d62-9de1-f839a2d3e600" name="ケンタ" color="blue" text='えっと...何て書けばいいんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='最初だから「初回コミット」とか「プロジェクト開始」とかでいいわよ。英語で「Initial commit」って書く人も多いわね' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='じゃあ「シューティングゲーム、プロジェクト開始！」って書きます' %}
{% include chat.html face="https://github.com/user-attachments/assets/29b59426-e842-4399-a21d-592b354c534d" name="ミサキ" color="red" text='いいわね！気持ちがこもってる（笑）。じゃあ、青い「Commit to main」ボタンを押してみて' %}
{% include chat.html face="https://github.com/user-attachments/assets/f142bf03-36b0-481e-b729-1a9689b91d74" name="ケンタ" color="blue" text='（ポチッ）...あれ、ファイルの表示が消えた？' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='正解！コミット（保存）されたから、変更済みファイルのリストから消えたのよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='おお...！' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='最後に、上の「Push origin」ボタンを押して、GitHubに送るの' %}
{% include chat.html face="https://github.com/user-attachments/assets/f142bf03-36b0-481e-b729-1a9689b91d74" name="ケンタ" color="blue" text='（ポチッ）...これで完了ですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='そう！GitHubのサイトに戻って、リポジトリを見てみて' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='（ブラウザを見る）わあ...！ファイルがアップロードされてる...！すごい...！' %}

<!-- 画像案：GitHubでファイルがアップロードされた画面 -->

おめでとうございます！これで、あなたのコードは安全にGitHubで管理されるようになりました。

---

### 日常的な使い方

{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='これからは、プログラムを書いたら、こまめにコミットする習慣をつけるといいわよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='こまめに...どのくらいですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='そうね、「敵キャラを追加した」「弾の速度を調整した」「BGMを追加した」みたいに、一つの機能ができたらコミットする感じかな' %}
{% include chat.html face="https://github.com/user-attachments/assets/d75d2bde-5e93-4095-8591-f6ba676960d2" name="ケンタ" color="blue" text='一つの機能ごと、ですね！' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='そう。あんまり細かすぎても大変だけど、「今日やったこと全部まとめて」だと、後で探しにくくなるからね' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='なるほど...バランスが大事なんですね' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='それと、コミットメッセージ（さっきのメモ）は、後で自分が見てわかるように書くのがコツよ。「修正」だけじゃなくて、「敵の当たり判定を修正」って書いた方が、後で探しやすいわ' %}
{% include chat.html face="https://github.com/user-attachments/assets/d75d2bde-5e93-4095-8591-f6ba676960d2" name="ケンタ" color="blue" text='確かに...！未来の自分のために書くんですね' %}

コミットメッセージは、未来の自分へのメモ。丁寧に書いておくと、数ヶ月後に「神...！」ってなります。

---

## 第4章：複数のパソコンで開発する

{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='先輩、さっき言ってた「複数のPCで作業する」のを、実際にやってみたいんですけど...' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='いいわね！流れは簡単よ' %}

### 基本の流れ

**家で作業する時も、学校で作業する時も、やることは同じ：**

1. **プル**（最新版を取得）
2. **作業**（プログラミング）
3. **コミット**（保存）
4. **プッシュ**（アップロード）

{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='あれ...場所が違っても同じなんですね？' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='そう、まったく同じ（笑）。重要なのは「作業前に必ずプル」ってこと。これを忘れると、古いバージョンで作業しちゃうから' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='気をつけます！' %}

<!-- 画像案：プル→作業→コミット→プッシュのサイクル図 -->

マルチデバイス開発の極意は「プルを忘れない」。これさえ守れば、トラブルはほぼ起きません。

---

{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='もし両方のPCで同時に作業しちゃったらどうなるんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='そしたら、Gitが「コンフリクトしてるよ」って教えてくれるの' %}
{% include chat.html face="https://github.com/user-attachments/assets/f1a20f91-5738-4e89-b847-4f651f4c5c9b" name="ケンタ" color="blue" text='コンフリクト...！怖い...！' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='大丈夫、落ち着いて。GitHub Desktopなら、「自分の変更を優先」か「相手（クラウド）の変更を優先」かをボタンで選べるから、パニックにならなくても大丈夫よ' %}
{% include chat.html face="https://github.com/user-attachments/assets/6436d587-a398-4d60-b3cc-9a12fb429f8c" name="ケンタ" color="blue" text='そうなんですね...でも、できればコンフリクトは避けたいです...' %}
{% include chat.html face="https://github.com/user-attachments/assets/ae3eb7e8-10da-411f-884f-c5e06f315528" name="ミサキ" color="red" text='その気持ち、大事よ。だから、「プッシュ忘れない」「プルを習慣にする」を徹底すれば大丈夫！' %}

コンフリクトは怖くありません。GitHub Desktopなら、GUIで簡単に解決できます。

---

{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='あ、でも一つ心配なんですけど...学校のPCって、再起動したらファイル消えちゃうんです...' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='逆にGitHubが超便利なのよ！作業が終わったらプッシュしておけば、PCのデータが消えても、GitHubには残ってるから' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='あっ、そうか！クラウドに保存されてるから大丈夫なんですね！' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='その通り！むしろ、そういう環境でこそGitHubの真価が発揮されるわ' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='すごい...もうUSBメモリ持ち歩かなくていいんですね...！' %}

GitHubは、データが消える環境でも安心。クラウドに保存されているので、いつでもどこでも作業を再開できます。

---

## 第5章：もしもの時の「戻る」機能

{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='先輩、さっき「タイムマシン機能」って言ってましたけど、具体的にどうやって戻るんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='いい質問ね！「戻る」には2つのパターンがあるのよ' %}

### パターン1：まだコミットしてない変更を取り消す（超重要！）

{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='例えば、新しい敵キャラを追加してみたけど、全然うまくいかなくて、コードがぐちゃぐちゃになっちゃった、みたいな状況' %}
{% include chat.html face="https://github.com/user-attachments/assets/f1a20f91-5738-4e89-b847-4f651f4c5c9b" name="ケンタ" color="blue" text='あるある...！そういう時、Ctrl+Zで戻そうとするんですけど、どこまで戻せばいいかわからなくなって...' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='そういう時こそ、Gitの出番！変更したファイルを右クリックして、「Discard changes...（変更を破棄）」を選ぶの' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='これを選ぶと...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='前回コミットした時の状態に、一瞬で戻るの！まさにセーブポイントに戻るゲームみたいでしょ？' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='すごい...！じゃあ、何時間かけて失敗したコードも、一瞬で消せるんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='そう！だから、思い切って実験できるのよ。失敗しても「Discard changes」で戻せばいいだけだから' %}

<!-- 画像案：Discard changesの右クリックメニュー -->

「Discard changes（変更を破棄）」は、Gitで最もよく使う機能の一つです。

---

### パターン2：コミットした後で取り消す（たまに使う）

{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='次は、コミットした後で「やっぱりダメだった」ってパターンね' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='コミットした後でも戻せるんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='戻せるわよ。GitHub Desktopの「History」タブで、戻りたいコミットを右クリックして、「Revert changes in commit」を選ぶの' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='「Revert（リバート）」...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='「打ち消す」って意味ね。例えば、「敵キャラを追加」ってコミットをRevertすると、「敵キャラを削除」っていう新しいコミットが作られるの。履歴は残るけど、内容は元に戻るわ' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='へぇ...！便利ですね' %}

<!-- 画像案：Historyタブとrevertメニュー -->

Revertは「やり直し」ではなく「打ち消し」。履歴は消さずに、効果だけを元に戻します。

---

### どっちを使えばいい？

| 状況 | 使う機能 | 頻度 |
|------|---------|------|
| まだコミットしてない変更を取り消したい | **Discard changes** | ⭐⭐⭐（超頻繁） |
| コミットした変更を取り消したい | **Revert** | ⭐（たまに） |

{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='9割は「Discard changes」を使うことになるわ。だから、まずはこっちを覚えておけば大丈夫！' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='わかりました！これで、安心して実験できます！' %}

失敗を恐れずチャレンジできる環境。それが、Gitの最大の魅力です。

---

## 第6章：応用編 〜ブランチとPull Request〜

### ブランチを使ってみよう

{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='慣れてきたら、「ブランチ」も使ってみるといいわよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='ブランチ...さっき言ってた、平行世界を作るやつですよね' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='そう！例えば、「ボスキャラを追加したいけど、うまくいくかわからない」って時、新しいブランチを作るの' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='どうやって作るんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='GitHub Desktopの上の方に「Current branch」ってあるでしょ？そこをクリックして「New branch」を選ぶの。名前は「boss-character」とかでいいわね' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='はい...（作成中）...できました！' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='これで、今から書くコードは「boss-character」ブランチに記録されるの。元の「main」ブランチには影響しないわ' %}
{% include chat.html face="https://github.com/user-attachments/assets/6436d587-a398-4d60-b3cc-9a12fb429f8c" name="ケンタ" color="blue" text='じゃあ、失敗しても大丈夫なんですね！' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='そう。うまくいったら「main」に合流（マージ）させて、失敗したらブランチを削除すればいいの' %}

<!-- 画像案：ブランチ作成画面 -->

ブランチを使えば、「安全な実験場」が手に入ります。

---

### ブランチVS Revert～なぜブランチが便利なのか

{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='あ、先輩、質問があるんですけど...さっき習った「Revert」じゃダメなんですか？失敗したコミットを打ち消すっていう方法は...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='いい質問ね！確かに、Revertでも「やり直す」ことはできるのよ。でも、ブランチとRevertでは考え方が全然違うの' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='考え方...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='Revertはね、「あの変更は間違いだった」ってことにして、逆の変更を記録するの。つまり、「敵キャラを追加した」を「敵キャラを削除した」に打ち消すのよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/b748d508-55d0-4d62-9de1-f839a2d3e600" name="ケンタ" color="blue" text='そしたら、敵キャラの追加も削除も両方、履歴に残るんですね' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='そう！でも、もし「敵キャラ追加」が1日かけた大きな実験だったら、どう？' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='え...どうするんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='ブランチなら、最初から「敵キャラ実験用ブランチ」を作って、そこで1日かけて試行錯誤するわけよ。途中の細かいコミットも全部残る' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='あ...！途中の過程も残るんですか' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='そう。「敵キャラの色を変えてみた」「当たり判定を調整した」「ボス敵にしてみた」...こういう全部のコミットが記録されるの。そのブランチ内では履歴が完全に保存されるわ' %}
{% include chat.html face="https://github.com/user-attachments/assets/d75d2bde-5e93-4095-8591-f6ba676960d2" name="ケンタ" color="blue" text='なるほど...！' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='で、「やっぱりうまくいかないな」ってなったら、そのブランチ全体を削除しちゃう。mainブランチは触られない。きれいなままよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='あっ、そっか！mainの履歴がぐちゃぐちゃにならないんですね' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='その通り！それにね、「敵キャラ実験」と「BGM追加実験」を同時にやりたくなったら、ブランチなら簡単よ。別々のブランチで同時進行できるのよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='Revertだと...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='Revertだと、「敵キャラ追加」を打ち消した後に「BGM追加」をやるから、実験が直列になっちゃう。遅いのよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='あ～！ブランチなら並列で何個も実験できるんですね！' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='その通り！だからね、「大きな実験」「新機能の追加」「いろんなことを試したい」って時は、ブランチを使う。それに対して、Revertは「あ、もう遠くになった1個のコミットで小さなミスがあった」みたいな時に使うイメージね' %}
{% include chat.html face="https://github.com/user-attachments/assets/d75d2bde-5e93-4095-8591-f6ba676960d2" name="ケンタ" color="blue" text='なるほど...ブランチは「実験区域」で、Revertは「過去の誤りを打ち消す」って感じですね' %}
{% include chat.html face="https://github.com/user-attachments/assets/29b59426-e842-4399-a21d-592b354c534d" name="ミサキ" color="red" text='いい理解よ！使い分けをまとめるとこんな感じね' %}

**ブランチとRevertの使い分け**

| やりたいこと | 使う機能 |
|-------------|---------|
| 失敗して全部捨てたい | **ブランチ削除** |
| 途中のステップも全部残したい | **ブランチで管理** |
| 複数の実験を同時にやりたい | **ブランチ複数作成** |
| 遠い過去の1つのコミットだけ打ち消したい | **Revert** |

{% include chat.html face="https://github.com/user-attachments/assets/b343fba6-67e5-4b6b-afb3-a0002d7eb85d" name="ケンタ" color="blue" text='わかりました！今後はブランチを積極的に使います！' %}

ブランチは「実験を安全に管理する仕組み」。Revertは「古い変更を打ち消す仕組み」。用途が違うのです。

---

### Pull Requestで自分をレビュー

{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='ブランチで作業したコードを、mainに合流させる時って、いきなりマージしちゃっていいんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='いい質問ね！実はもっといい方法があるの。「Pull Request」っていう機能を使うのよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='プル...リクエスト？' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='「この変更をmainブランチに取り込んでください」っていうお願いを出す機能なの' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='でも、僕一人でやってるんですけど...自分に自分でお願いするんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='そう見えるけど（笑）、実はこれ、一人プロジェクトでもすごく便利なのよ！' %}

---

{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='Pull Requestを使うと、変更内容を「レビュー画面」で見られるの。何を追加して、何を削除したか、一目でわかるのよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='へぇ...！' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='「Files changed」っていうタブをクリックすると、変更内容が色分けで表示されるの。赤が削除、緑が追加ね' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='わかりやすい...！' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='ここで、自分のコードをじっくり見直すの。「このコメント、わかりにくいな」とか「この変数名、もっといい名前にしよう」とか気づくことが多いのよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/d75d2bde-5e93-4095-8591-f6ba676960d2" name="ケンタ" color="blue" text='客観的に見られるってことですね！' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='まさに！問題なければ、「Merge pull request」ボタンを押せば、mainブランチに合流できるわ' %}

<!-- 画像案：Pull RequestのFiles changed画面（diff表示） -->

Pull Requestは「マージ前の検査場」。ここで最終チェックをすることで、品質の高いコードをmainブランチに保てます。

---

### AIがコードを見てくれる？

{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='あっ、先輩！Pull Requestに何かコメントがついてるんですけど...僕、誰にも共有してないのに...' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='あー、それはGemini Code Assistね' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='ジェミニ...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='GoogleのAIがコードを自動でレビューしてくれる機能よ。Pull Requestを作ると、勝手にコードを見て「ここ、こうした方がいいんじゃない？」って提案してくれるの' %}
{% include chat.html face="https://github.com/user-attachments/assets/c6204e7f-312d-4157-a759-09d7ae6ceaae" name="ケンタ" color="blue" text='えっ、AIが先生みたいにレビューしてくれるんですか！？' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='そう！例えば、「この数字、マジックナンバーだから定数にした方がいいよ」とか、具体的にアドバイスしてくれるのよ' %}

<!-- 画像：Gemini Code AssistのSummary of Changes画面 -->

{% include chat.html face="https://github.com/user-attachments/assets/d75d2bde-5e93-4095-8591-f6ba676960d2" name="ケンタ" color="blue" text='すごい...一人で開発してると、誰にも見てもらえないから不安だったんですけど...' %}
{% include chat.html face="https://github.com/user-attachments/assets/d5d8bdb5-08d2-4334-aec9-b9bcd8ca4c7b" name="ミサキ" color="red" text='でしょ？一人プロジェクトでも、AIがペアプログラミングの相手になってくれる感じね' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='どうやって使うんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='GitHubのMarketplaceから「Gemini Code Assist」をインストールするだけよ。無料で使えるわ' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='それ、すぐ入れます！　……って先輩いつの間に入れていたの？！' %}

<!-- 画像：Gemini Code Assistの具体的なコードレビュー（マジックナンバーの指摘） -->

{% include chat.html face="https://github.com/user-attachments/assets/29b59426-e842-4399-a21d-592b354c534d" name="ミサキ" color="red" text='必要だったからね。ただし、AIの提案が常に正しいとは限らないから、「なるほど、こういう考え方もあるんだ」くらいの気持ちで参考にするのがいいわね' %}
{% include chat.html face="https://github.com/user-attachments/assets/41730ebd-75a2-40d5-9a8e-bcdd80e66700" name="ケンタ" color="blue" text='わかりました！鵜呑みにしないで、自分でも考えるようにします' %}

Gemini Code Assistは、Pull Requestに自動でレビューコメントをつけてくれるAIツールです。一人開発でも「第三者の目」が得られるので、コードの品質向上に役立ちます。

**Gemini Code Assistの主な機能**
- **変更サマリー**: PRの変更内容を日本語で要約
- **コードレビュー**: マジックナンバーや改善点を指摘
- **優先度表示**: High / Medium / Low で重要度がわかる

---

{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='ちなみに、Pull Requestをマージしたら、そのブランチは削除していいわよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='えっ、削除しちゃっていいんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='大丈夫。マージ済みのブランチは、もう役目を終えたから。GitHubが「Delete branch」ボタンも用意してくれてるわ' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='なるほど...整理整頓も大事なんですね！' %}

マージ済みのブランチは削除してOK。Pull Requestの記録は残るので、履歴は失われません。

---

## 第7章：困ったときは？

{% include chat.html face="https://github.com/user-attachments/assets/f1a20f91-5738-4e89-b847-4f651f4c5c9b" name="ケンタ" color="blue" text='使ってるうちに、わからないことが出てきたらどうしよう...？' %}
{% include chat.html face="https://github.com/user-attachments/assets/29b59426-e842-4399-a21d-592b354c534d" name="ミサキ" color="red" text='大丈夫、GitHubは利用者が多いから、ネットに情報がたくさんあるわよ' %}
{% include chat.html face="https://github.com/user-attachments/assets/7027ab79-dae1-4cc0-ba13-b26e5a205f63" name="ケンタ" color="blue" text='そうなんですか？' %}
{% include chat.html face="https://github.com/user-attachments/assets/da42644e-501b-45a9-8cab-3ef08e926733" name="ミサキ" color="red" text='うん。「GitHub 使い方」とか「Git 初心者」とか検索すれば、優しい記事がいっぱい出てくるわ。GitHub公式のドキュメントも日本語対応してるし' %}
{% include chat.html face="https://github.com/user-attachments/assets/6436d587-a398-4d60-b3cc-9a12fb429f8c" name="ケンタ" color="blue" text='安心しました...！' %}
{% include chat.html face="https://github.com/user-attachments/assets/29b59426-e842-4399-a21d-592b354c534d" name="ミサキ" color="red" text='最初は戸惑うこともあるかもしれないけど、使ってるうちに絶対慣れるから。焦らずゆっくりいきましょ' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='はい！頑張ります！' %}

コミュニティも活発なので、困ったことがあっても大丈夫。みんな最初は初心者でした。

---

### 💡 HSPとGitHubの補足

**複数人開発について**

HSPは基本的に一つの大きなファイルで開発することが多いため、複数人で同時にコードを編集すると「コンフリクト」が起きやすいです。もし友達と一緒に開発したい場合は、「役割分担」（Aさんは画像担当、Bさんは音楽担当、自分はプログラム担当など）をはっきりさせるか、`#module`を使ってファイルを分割することをおすすめします。

**Issue（課題管理）について**

GitHubには「Issue」という課題管理機能もありますが、小規模な一人プロジェクトでは、コミットメッセージで十分管理できることが多いです。「将来実装したい機能」のメモとして使うのはアリですが、無理に使う必要はありません。

---

## エピローグ：一週間後...

{% include chat.html face="https://github.com/user-attachments/assets/82139cab-21c9-4e3d-9af2-24fa1fa9df44" name="ミサキ" color="red" text='ケンタくん、その後GitHubは使ってる？' %}
{% include chat.html face="https://github.com/user-attachments/assets/b343fba6-67e5-4b6b-afb3-a0002d7eb85d" name="ケンタ" color="blue" text='はい！もう手放せないです...！' %}
{% include chat.html face="https://github.com/user-attachments/assets/6f0d39c1-acbe-44a1-b4f9-a867a9123a9e" name="ミサキ" color="red" text='おお、いい感じじゃない（笑）' %}
{% include chat.html face="https://github.com/user-attachments/assets/0ab8afeb-dba9-464c-adf4-91ec49a5d579" name="ケンタ" color="blue" text='こないだ、大胆にコード変更して、やっぱりダメだったから戻した時は感動しました...！本当にタイムマシンみたいで...！' %}
{% include chat.html face="https://github.com/user-attachments/assets/bcb05627-febb-450f-915d-dc92b92539f5" name="ミサキ" color="red" text='でしょ？それがGitの醍醐味よ' %}
{% include chat.html face="https://github.com/user-attachments/assets/d75d2bde-5e93-4095-8591-f6ba676960d2" name="ケンタ" color="blue" text='それに、コミットメッセージを見返すと、自分の成長が見えて楽しいんです。「この時はこんなこと考えてたんだな」って' %}
{% include chat.html face="https://github.com/user-attachments/assets/29b59426-e842-4399-a21d-592b354c534d" name="ミサキ" color="red" text='すごくいい使い方してるわね！' %}
{% include chat.html face="https://github.com/user-attachments/assets/2c603f79-89d2-44c5-b556-8a4207adb4b3" name="ケンタ" color="blue" text='先輩のおかげです。教えてくれてありがとうございました！' %}
{% include chat.html face="https://github.com/user-attachments/assets/d3ed2abc-1a5e-40a9-82f3-38696847ff0a" name="ミサキ" color="red" text='どういたしまして。これからも、どんどん新しいことに挑戦していってね' %}
{% include chat.html face="https://github.com/user-attachments/assets/b343fba6-67e5-4b6b-afb3-a0002d7eb85d" name="ケンタ" color="blue" text='はい！次はブランチを使いこなせるように頑張ります！' %}

こうして、ケンタのプログラミングライフは、GitHubによって大きく変わりました。安心して挑戦できる環境があれば、成長のスピードも加速します。あなたも、今日からGitHubを始めてみませんか？

---

## まとめ：GitHubを始めるための3ステップ

**1. 準備する**
- hsed3u8.exe（UTF-8版エディタ）を使う
- GitHubアカウントを作成
- GitHub Desktopをインストール

**2. 基本を覚える**
- リポジトリを作る（Privateで）
- コミット → プッシュ の流れを習慣にする
- .gitignoreを設定する

**3. 便利機能を使う**
- Discard changesで失敗を恐れず実験
- ブランチ＆Pull Requestで安全に新機能追加
- Gemini Code AssistでAIレビュー

---

### 🎯 覚えるべき用語（最小限）

| 用語 | 意味 |
|------|------|
| **リポジトリ** | プロジェクトの保存場所 |
| **コミット** | 変更を記録すること（セーブ） |
| **プッシュ** | ローカルの変更をGitHubに送ること |
| **プル** | GitHubの変更をローカルに持ってくること |
| **ブランチ** | 並行世界を作る機能 |
| **Pull Request** | 変更を確認してから合流させる機能 |

---

**最後に...**

GitHubは最初は難しく感じるかもしれませんが、使えば使うほど「これなしでどうやってプログラミングしてたんだろう？」と思えるほど便利なツールです。

一歩ずつ、焦らずに。あなたのペースで始めてみてください。

きっと、プログラミングがもっと楽しくなりますよ！ 🚀

（完全な余談ですが、私はこの記事を書くためだけにGitHub Desktopを入れました。いつもはどうしてるかって？　Visual Studio CodeはGit管理便利なんです）
