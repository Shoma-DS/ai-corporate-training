# Google Workspace / Apps Script / スプレッドシート・フォーム自動化 出典メモ

## Source

- Title: Google Apps Script overview
- Publisher: Google for Developers
- URL: https://developers.google.com/apps-script/overview
- Retrieved: 2026-05-20

- Title: Built-in Google Services
- Publisher: Google for Developers
- URL: https://developers.google.com/apps-script/guides/services
- Retrieved: 2026-05-20

- Title: Spreadsheet Service
- Publisher: Google for Developers
- URL: https://developers.google.com/apps-script/reference/spreadsheet
- Retrieved: 2026-05-20

- Title: Forms Service
- Publisher: Google for Developers
- URL: https://developers.google.com/apps-script/reference/forms
- Retrieved: 2026-05-20

- Title: Installable Triggers
- Publisher: Google for Developers
- URL: https://developers.google.com/apps-script/guides/triggers/installable
- Retrieved: 2026-05-20

- Title: Custom Menus in Google Workspace
- Publisher: Google for Developers
- URL: https://developers.google.com/apps-script/guides/menus
- Retrieved: 2026-05-20

- Title: Quotas for Google Services
- Publisher: Google for Developers
- URL: https://developers.google.com/apps-script/guides/services/quotas
- Retrieved: 2026-05-20

- Title: Choose where to save form responses
- Publisher: Google Docs Editors Help
- URL: https://support.google.com/docs/answer/2917686
- Retrieved: 2026-05-20

- Title: Use Gems in Gemini Apps
- Publisher: Gemini Apps Help
- URL: https://support.google.com/gemini/answer/15146780
- Retrieved: 2026-05-20

- Title: Use apps in Gemini
- Publisher: Gemini Apps Help
- URL: https://support.google.com/gemini/answer/13695044
- Retrieved: 2026-05-21

- Title: Use Google Workspace apps in Gemini
- Publisher: Gemini Apps Help
- URL: https://support.google.com/gemini/answer/14959807
- Retrieved: 2026-05-21

- Title: Transcribe Google Meet meetings
- Publisher: Google Workspace Individual Help
- URL: https://support.google.com/google-workspace-individual/answer/12849897
- Retrieved: 2026-05-21

- Title: Turn meeting transcription on or off
- Publisher: Google Workspace Admin Help
- URL: https://support.google.com/a/answer/12076932
- Retrieved: 2026-05-21

- Title: Automatic meeting artifact settings
- Publisher: Google Workspace Admin Help
- URL: https://support.google.com/a/answer/15496523
- Retrieved: 2026-05-21

- Title: Work with artifacts
- Publisher: Google for Developers
- URL: https://developers.google.com/workspace/meet/api/guides/artifacts
- Retrieved: 2026-05-21

- Title: Meet API transcripts
- Publisher: Google for Developers
- URL: https://developers.google.com/workspace/meet/api/reference/rest/v2/conferenceRecords.transcripts
- Retrieved: 2026-05-21

- Title: Meet API transcript entries
- Publisher: Google for Developers
- URL: https://developers.google.com/workspace/meet/api/reference/rest/v2/conferenceRecords.transcripts.entries/list
- Retrieved: 2026-05-21

- Title: Drive Service
- Publisher: Google for Developers
- URL: https://developers.google.com/apps-script/reference/drive
- Retrieved: 2026-05-21

- Title: Advanced Google services
- Publisher: Google for Developers
- URL: https://developers.google.com/apps-script/guides/services/advanced
- Retrieved: 2026-05-21

- Title: Udemy講座ベンチマーク: Google Workspace・GAS・スプレッドシート・フォーム
- Publisher: Internal research note
- URL: 調査/Udemy-Google-Workspace-GAS-スプレッドシート-フォーム講座ベンチマーク-2026-05-20.md
- Retrieved: 2026-05-20

- Title: Google Apps Script Complete Course New IDE 100+ Examples
- Publisher: Udemy
- URL: https://www.udemy.com/course/course-apps-script/
- Retrieved: 2026-05-20

- Title: Google Apps Script Complete Course Beginner to Advanced
- Publisher: Udemy
- URL: https://www.udemy.com/course/apps-script-course/
- Retrieved: 2026-05-20

- Title: GASでスプレッドシートを自由自在に操るためのスキル習得講座
- Publisher: Udemy
- URL: https://www.udemy.com/course/automate-spreadsheet-by-gas/
- Retrieved: 2026-05-20

- Title: GASで超実用的なシステムを神速開発するためのスキル習得講座
- Publisher: Udemy
- URL: https://www.udemy.com/course/mastering-google-apps-script/
- Retrieved: 2026-05-20

- Title: Google Forms : Basic to Advanced - Complete Automation
- Publisher: Udemy
- URL: https://www.udemy.com/course/google-forms-basic-to-advanced-complete-automation/
- Retrieved: 2026-05-20

- Title: Crie Agentes de IA com ChatGPT (GPTs) e Google Gemini (Gems)
- Publisher: Udemy
- URL: https://www.udemy.com/course/gpts-e-gems/
- Retrieved: 2026-05-20

- Title: GeminiでわかるAI入門
- Publisher: Udemy
- URL: https://www.udemy.com/course/gemini-google/
- Retrieved: 2026-05-20

## Research Use

中小企業向けに、Google Workspace、Google Apps Script、Googleスプレッドシート、Googleフォーム、Gemini/Gemを使ったAI業務効率化研修を設計するために使う。

## Public Notes

- Apps Scriptは、Google Workspaceと連携する業務アプリケーションをすばやく作るためのJavaScriptベースの開発プラットフォーム。
- Apps Scriptは、Gmail、Calendar、DriveなどのGoogle Workspaceアプリ向け組み込みサービスを利用できる。
- Google Meetの文字起こしは、利用できるWorkspaceエディションと管理者設定に依存する。講座では、使える場合は会議後にDriveへ保存される文字起こしDocsを扱い、使えない場合は配布済み文字起こしサンプルで代替する。
- Meet文字起こしの自動生成・保存・開始権限は組織設定や会議設定に左右されるため、講座内のGAS演習では「Meet終了を直接トリガーにする」前提にせず、Drive上のDocs、手動配置したDocs、または配布テキストを入力元にする。
- Meet REST APIには会議アーティファクトや文字起こしエントリを扱う機能があるが、OAuthスコープ、管理者設定、取得期限を考慮する必要があるため、標準演習では発展扱いにする。
- Spreadsheet Serviceは、スプレッドシート、シート、範囲、セル、データ検証、フィルタ、チャートなどを扱える。
- Forms Serviceは、Googleフォームの作成、編集、回答取得などに使える。
- 自動実行は、時間主導、フォーム送信、スプレッドシート編集などのインストール型トリガーで設計できる。
- Apps Scriptには実行時間、送信、呼び出し回数などの割り当てや制限があるため、法人研修では「小さく始める」「ログを残す」「例外時に止まる/通知する」設計を扱う。
- Googleフォームの回答はスプレッドシートに保存できるため、受付、申請、日報、アンケートの台帳化に使いやすい。
- Apps Scriptはカスタムメニュー、ダイアログ、サイドバーなどのUI拡張を使えるため、現場担当者が実行しやすい手動ボタンや確認画面の設計も扱える。
- 課金や管理者設定が必要な高度機能は必須演習にしない。無料範囲で使えるGeminiアプリやGemは、分類、要約、返信案、GASコード読解、業務プロンプトの共有に使う。
- GeminiのGoogle Workspace連携は、Gmail、Drive、Docs、Calendar、Meet文字起こしなどの検索、要約、予定確認、議事録整理に使える場合がある。ただし、アカウント種別、管理者設定、提供状況で利用可否が変わるため、必須演習はSheets、Forms、GAS、Gem、貼り付けデータ、配布文字起こしサンプルで成立させる。

## Course Design Implication

- 中小企業向けでは、Sheets中心のデータ整理、Forms受付、Gem/Geminiによる分類・要約、GeminiのGoogle Workspace連携によるGmail/Drive/Docs/Calendar/Meet文字起こしの情報整理、Gmail通知、Drive保存、Docs帳票、Calendar期限管理を題材にすると実務転用しやすい。
- レベル3相当にする場合は、単なるコード写経ではなく、業務フローのAs-Is/To-Be、対象データ、権限、例外処理、運用担当、効果指標まで設計させる。
- Excel的な表処理は、関数で済む処理、スプレッドシート機能で済む処理、GASで自動化する処理、Gem/Geminiで下書きする処理、人が確認する処理に分けると学習しやすい。
- フォーム連携は、回答シートを原本、管理台帳を業務処理用として分けると、データ破損や上書きリスクを下げられる。
- サービス紹介では、公式ロゴと公式スクリーンショットまたはダミー環境の画面を使う。画像生成AIに実在ロゴや実在画面を描かせない。
- 録画やデモでは、検証用アカウントと `各回フォルダの演習データ/` のダミーデータを使い、個人アカウント、実メール、実顧客情報、社内未公開資料を映さない。
