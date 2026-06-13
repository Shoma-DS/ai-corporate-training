# Udemy講座ベンチマーク: Google Workspace・GAS・AI業務効率化

調査日: 2026-05-20

## 目的

対象講座の内容を厚くするため、Udemy上で公開されている近いテーマの講座から、項目設計、演習の切り口、最新トピックの扱い方を抽象化して整理する。

今回の講座では、Googleスプレッドシート、Googleフォーム、Google Apps Scriptを主軸にしつつ、無料範囲で使えるGemini/GemをAI活用要素として入れる。ユーザー環境で有料Gemini for Google Workspaceを使わない前提のため、課金や管理者設定がないと説明しづらい高度機能は必須演習から除外する。

## 参照したUdemy講座

公開ページ確認日: 2026-05-20

| 講座 | URL | 更新日 | 今回の扱い |
| --- | --- | --- | --- |
| Google Apps Script Complete Course New IDE 100+ Examples | https://www.udemy.com/course/course-apps-script/ | 2025-12 | DriveApp、GmailApp、CalendarApp、SlidesApp、FormAppなど、Apps Scriptをサービス別に深掘りする構成を参考にする。 |
| Google Apps Script Complete Course Beginner to Advanced | https://www.udemy.com/course/apps-script-course/ | 2025-12 | Apps Scriptの導入、Google Workspace連携、実例、演習、ソースコード付き段階学習の作り方を参考にする。 |
| GASでスプレッドシートを自由自在に操るためのスキル習得講座 | https://www.udemy.com/course/automate-spreadsheet-by-gas/ | 2026-01 | スプレッドシート自動化、売上情報の集計、コード読解、生成AI活用の切り口を参考にする。 |
| GASで超実用的なシステムを神速開発するためのスキル習得講座 | https://www.udemy.com/course/mastering-google-apps-script/ | 2026-01 | Gmail、Docs、Drive、Forms、Calendarなどを連携した実務システム化の演習設計を参考にする。 |
| Google Forms : Basic to Advanced - Complete Automation | https://www.udemy.com/course/google-forms-basic-to-advanced-complete-automation/ | 2025-12 | フォーム回答をスプレッドシートへ集約し、受付管理、通知、申請に展開する切り口を参考にする。 |
| Crie Agentes de IA com ChatGPT (GPTs) e Google Gemini (Gems) | https://www.udemy.com/course/gpts-e-gems/ | 2026-03 | Gem作成、役割設定、ルール化、再利用可能なAIエージェント設計の考え方を参考にする。 |
| GeminiでわかるAI入門 | https://www.udemy.com/course/gemini-google/ | 2025-06 | Gemini初心者向けの導入説明、業務プロンプト、AI活用の入口設計を参考にする。 |

## ベンチマークから見えた拡張ポイント

### 1. Apps Scriptはサービス別の小課題に分解する

Sheets、Gmail、Drive、Calendar、Forms、Docs/Slidesのようにサービス別に細かく分ける。補助教材として「サービス別ミニレシピ」を追加する。

### 2. スプレッドシートはExcel的処理の置き換えとして厚くする

CSV整形、未対応抽出、期限超過抽出、別シート転記、重複チェック、COUNTIF/SUMIF/FILTER/QUERY/ピボット、GASでの一括更新とログ追記を厚く扱う。

### 3. フォーム連携は受付業務として一連で扱う

Googleフォームの設問設計、回答先スプレッドシート、回答シートと管理台帳の分離、受付番号、確認メール、担当者通知、ステータス管理、Drive保存、Docs帳票、期限リマインドまで扱う。

### 4. Gem/GeminiによるAI活用を業務フローに入れる

Gemini/Gemは、単独のチャット体験ではなく、フォーム回答や台帳データをもとにした分類、要約、返信案、GASコード読解に使う。特にGemは、目的、役割、入力、出力形式、禁止事項、確認観点を固定し、社内で再利用しやすい形にする。

### 5. 運用設計を独立した回として扱う

要件定義、例外条件、個人情報と権限、AI入力禁止情報、GASの実行制限、ログ設計、エラー通知、AI出力レビュー、手動復旧、テスト観点、引き継ぎを扱う。

### 6. 提案書までの実務成果物を厚くする

法人研修として、最終成果物を「Gem設計書」「AI活用プロンプト」「GASミニプロトタイプ」「運用設計書」「導入提案書」に統合する。KPI、リスク、権限、ログ、手動復旧、現場定着まで含める。

## 本講座へ反映する方針

- 6回、各120分、合計約12時間の基本枠は維持する。
- 各回に「本編」「デモ」「演習」「発展課題」「提出物」を追加する。
- 公式ロゴとスクリーンショットの利用方針を入れる。サービス紹介では、画像生成AIに実在ロゴを描かせず、公式ロゴと公式公開画像またはダミー環境のスクリーンショットを使う。
- Gemini/Gemは無料範囲で説明できる業務AI活用として本編に入れる。Deep Research、AI Studio、Workspace Studioなど契約や管理者設定に依存する機能は必須演習に入れない。
- Udemy講座の章立てや説明文は転載せず、公開ページで確認できるテーマを抽象化して、法人研修向けの実務課題、演習、成果物に変換する。
