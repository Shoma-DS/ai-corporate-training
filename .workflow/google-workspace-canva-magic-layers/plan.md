# Google Workspace Canva Image-first Presentation

## Goal

Google Drive同期フォルダとCanva内に「AI法人研修 > Google Workspace・GASで進めるAI業務効率化-DX実践講座 > 回別」のプロジェクトフォルダを作り、同講座のスライド画像を回ごとに1本の画像ベースCanvaプレゼンテーションへ取り込む。

標準では全242枚をCanva MCPでMagic Layers化しない。まず画像または回別PPTXをアップロードして複数ページプレゼンを作成し、編集頻度が高いページだけCanva上で手動Magic Layers化する。

## Success Criteria

- Google Drive for desktop同期配下に、AI法人研修ルート、講座フォルダ、6回分の回別フォルダが存在する。
- Canva側にも、AI法人研修ルート、講座フォルダ、6回分の回別フォルダが存在する。
- 対象講座の各回について、1本ずつ画像ベースCanvaプレゼンテーションが存在する。
- 各回のCanvaプレゼンページ数がローカルの `スライド画像/S*.png` 枚数と一致する。
- 手動Magic Layers化するページ候補を `非公開/Canva/` に記録する。
- URL一覧は公開リポジトリ外の `非公開/Canva/` とGoogle Drive同期フォルダ側に出力する。
- 公開リポジトリにはCanva URL、認証情報、design ID、社内固有情報を追加しない。

## Current Context

- リポジトリ: `/Users/deguchishouma/Desktop/AI法人研修`
- 対象講座: `講座/Google Workspace・GASで進めるAI業務効率化-DX実践講座`
- 対象枚数: 242枚
- 回別枚数:
  - 01: 42枚
  - 02: 40枚
  - 03: 44枚
  - 04: 40枚
  - 05: 40枚
  - 06: 36枚
- Google Drive同期ルート: ローカルのGoogle Drive for desktop同期配下の `AI法人研修` フォルダ

## Constraints

- `AGENTS.md`に従い、会社資料、URL一覧、実リンクは`非公開/`またはGoogle Drive同期側に置く。
- 今回の対象はGoogle Workspace・GAS講座のみ。他講座の処理は行わない。
- 既存の公開資料本文やスライド画像は変換元として読み、必要がなければ編集しない。
- Canva MCPの `_image_to_design` による全ページMagic Layers化は標準フローでは使わない。
- Canva MCPはフォルダ作成、フォルダ移動、必要時の補助に限定する。

## Magic Layers Selection Policy

手動Magic Layers対象:

- 表紙、章扉、クロージング
- 企業名、実施日、講師名、部署名の差し替えページ
- カリキュラム表、受講対象、成果物一覧
- 提案時に文言変更が起きやすいページ
- 受講企業ごとに差し替えるケース紹介ページ

画像のまま残すページ:

- 固定の業務フロー図、概念図、Before/After図
- 画面共有への遷移スライド
- 公式画面やスクリーンショット中心の説明
- 演習手順、確認観点、まとめ

## Risks

- 外部サービス(Canva)へのアップロードやインポートのため、途中失敗、レート制限、タイムアウトが起き得る。
- Google Drive MCPが利用できない場合、Drive for desktop同期フォルダへのローカル作成で代替する。同期状態そのものはローカルから完全検証できない。
- CanvaのPPTX/画像インポート後、ページサイズや余白が変わる場合があるため、ページ数と代表ページの見た目確認が必要。
- 公開リポジトリへ実URLを誤って入れないよう、URL一覧は非公開/Drive側のみへ出力する。

## Approval Required

- ユーザー依頼に「スキルもフローも改善」が明示されているため、文書・テンプレートの更新は承認済みとして扱う。
- 外部サービスへの新規作成、削除、上書き、Git pushは今回行わない。

## Work Packets

- P1: 対象画像インベントリ作成とDriveフォルダ準備
- P2: Canvaフォルダ階層作成
- P3: 回別PPTXまたは画像アップロード用バンドル作成
- P4: 回別Canva画像ベースプレゼン作成と移動
- P5: 手動Magic Layers対象ページリスト作成
- P6: URL一覧出力、カウント検証、公開リポジトリ安全確認

## Integration Policy

- 回別プレゼンのURL、design ID、フォルダIDは非公開ログで管理する。
- Magic Layers対象ページはページ番号、理由、編集項目、優先度を記録する。
- CanvaフォルダID、Google Driveパス、実URLは `非公開/Canva/` 側のstateまたはメモに記録する。

## Verification

- 対象画像数242とCanva側ページ総数242が一致すること。
- 回別のページ数が42/40/44/40/40/36に一致すること。
- Google Drive同期フォルダに回別フォルダとURL一覧ファイルが存在すること。
- Canvaの回別フォルダIDと回別プレゼンURLがすべて非公開ログに記録されていること。
- 手動Magic Layers対象ページリストが存在し、全ページ一括変換前提になっていないこと。
- `python3 scripts/validate_local_skills.py`と`git diff --check`を実行する。
- `git status --short`で`非公開/`やDrive同期フォルダ内ファイルがステージ対象に出ていないことを確認する。

## Reusable Artifacts

- `.workflow/canva-presentation-per-session/plan.md`を、今後の講座別Canva画像アップロード先行ワークフローのひな形として使う。
- `.workflow/google-workspace-canva-magic-layers/`は旧一括Magic Layers実行の履歴を含むため、再利用時はこの新方針を優先する。
