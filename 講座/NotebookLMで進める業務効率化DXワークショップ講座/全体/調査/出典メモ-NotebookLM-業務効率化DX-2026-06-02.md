# 出典メモ: NotebookLM 業務効率化DXワークショップ

作成日: 2026-06-02

## 公式情報

### NotebookLM Help: Learn about NotebookLM

- URL: https://support.google.com/notebooklm/answer/16164461?hl=en
- 確認日: 2026-06-02
- 反映内容:
  - NotebookLMはAI搭載のリサーチアシスタントとして、PDF、Webサイト、YouTube動画、音声ファイル、Google Docs、Google Slidesなどの取り込みを案内している。
  - ノートブック内の資料に基づく回答、インライン引用、学習ガイド、ブリーフィング、Audio Overview、Mind Mapなどの生成を扱う。
  - 80以上の言語、年齢や国・地域、アカウント種別による利用可否に注意が必要。

### NotebookLM Help: NotebookLM Help top-level topics

- URL: https://support.google.com/notebooklm/?hl=en
- 確認日: 2026-06-02
- 反映内容:
  - チャット、ノート作成、Mind Map、Audio Overview、Video Overview、Flashcards/Quizzes、Infographic、Slide Deck、公開ノートブック、モバイルアプリ、仕事・学校アカウント利用などのヘルプ項目を確認した。
  - 講座では、機能名を固定的な到達保証として扱わず、利用環境により使える機能が変わる前提で説明する。

### Generative AI in Google Workspace Privacy Hub

- URL: https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub?hl=en
- 確認日: 2026-06-02
- 反映内容:
  - Workspace利用時、NotebookLMはGoogle Workspaceのコアサービスとして扱われ、Workspace契約やCloud Data Processing Addendumの対象になる旨を確認した。
  - NotebookLMへのアップロード、クエリ、モデル応答は、人間によるレビューや生成AIモデル訓練に使われない旨を確認した。
  - Driveからソースを取り込む場合、NotebookLMは各ファイルの新しいコピーを作成し、そのコピーはDriveではなくNotebookLMデータとして保存される点を講座の注意事項に反映した。
  - Workspace DLPは現時点でNotebookLMに直接統合されていないため、情報管理ワークで入力禁止情報、共有範囲、IRM、管理者設定の確認を扱う。
  - 管理者によるON/OFF、Context Aware Access、Takeout/Data Exportにも触れる。

### Google Blog: NotebookLM adds audio and YouTube support

- URL: https://blog.google/innovation-and-ai/products/notebooklm-audio-video-sources/
- 確認日: 2026-06-02
- 反映内容:
  - YouTube URLと音声ファイルをソースにできること、YouTubeではトランスクリプトに基づく引用や動画埋め込みを使う説明がある。
  - 音声会話、会議録、研修素材を検索・要約する演習設計に反映した。
  - WorkspaceユーザーはAudio Overviewの公開リンク共有に制限がある旨があり、講座では共有機能を環境依存として扱う。

### Google Blog: NotebookLM updates and Google I/O 2026 notebook

- URL: https://blog.google/innovation-and-ai/products/notebooklm/notebooklm-google-io-2026/
- 確認日: 2026-06-02
- 反映内容:
  - Google自身がNotebookLMを使い、YouTube動画、ブログ記事などを含むノートブックからAudio Overview、Slide Deck、Infographic、Video Overview、質問応答を案内している。
  - NotebookLMは根拠付き回答を支援するが、AIは不正確な出力をする可能性があるという注意を講座の出力確認ルールに反映した。

## 講座設計への反映

- NotebookLMを「資料を入れて要約するツール」ではなく、情報源設計、根拠確認、業務アウトプット化、共有・更新ルールまで含むDXワークショップとして構成した。
- 実務資料をそのまま公開リポジトリに置かず、架空企業のダミーデータだけで演習を成立させる。
- 変わり得る機能、上限、プラン、共有可否は固定しない。受講前に最新の公式情報と自社の管理者設定を確認する前提にする。
