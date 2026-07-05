# 引き継ぎプロンプト（第2回 画像生成プロンプト再検証）

## 2026-06-27 現在の進捗

- `scripts/build_editable_google_slides_sources.py` を更新し、図解パーツ生成プロンプトが元スライド案の本文ブロック・表・成果物・確認観点を `Source slide information preserve diagram meaning` として含むようにした。
- 図解パーツ用の短い表示ラベル候補は、内容ブロック名・表の行見出しを優先し、`図解パターン` などのメタ項目、ダミー人名・会社名風語を除外する。
- コードブロック由来の入れ子Markdownフェンスは、プロンプト生成時に `コード例:` へ変換する。
- 第2回 `02-業務データ基盤の設計` は、`S04.png`、`S06.png`、`S08.png` をGPT image 2 / `imagegen` 経由でまるごと再生成済み。`scripts/check_diagram_parts.py` と `scripts/check_diagram_integrity.py` で第2回は `40/40 ok`。
- 第2回の編集可能Google Slidesは `export_editable_ai_training_slides_to_gws.py --session-dir ... --replace-existing-decks --embed-diagram-parts --make-diagram-images-readable-by-link` で置換更新済み。非公開レポート: `非公開/gws-exports/生成AI・GASで実践する業務変革・DX推進講座/session02-editable-diagrams-report.json`。レポート上は `embedded 40/40`、`editableSlideCount 40`、`speakerNoteBlockCount 40`、`warnings []`。
- 第3回 `03-GASによる業務プロセス自動化` は `S17.png`〜`S24.png` を再生成済み。現在 `24/44`。次は `S25` から。
- 現在の整合性チェック残り:
  - 第3回: `S25`〜`S32` 以降が未生成（まず `S25`〜`S32`）。
  - 第4回: `S04`〜`S11` 以降が未生成。
  - 第5回: `S10`〜`S17` 以降が未生成。
  - 第6回: `S08`〜`S15` 以降が未生成。
  - 重複ハッシュ残り: 第5回`S09`/第6回`S07`、第4回`S03`/第3回`S08`、第1回`S03`/第5回`S03`。

## 生成時の注意

- 画像内にコード関数名を無理に入れると誤字が出やすい。コード名は編集可能本文に任せ、図解パーツでは日本語ラベル中心にする。
- 実在Googleロゴ・Google Sheets風アイコン・Apps Script UIを想像生成しない。汎用の表/歯車/カード/ログパネルで表現する。
- 生成後は `scripts/copy_latest_generated_image.py --marker ... --target ... --search-root "$CODEX_HOME/generated_images" --expect-mime image/png` でコピーする。
- コピー後は `file`/`sips`/`scripts/check_diagram_parts.py`/`scripts/check_diagram_integrity.py` を使い、必要な代表画像だけ `view_image` で確認する。

目的
- 第2回（業務データ基盤の設計）の図解/画像生成を、モデル変更後に再検証し、必要ならプロンプト再改善する。
- 目標は「スライド単体で見るだけで、学習行動・成果物・確認観点が読み取れる密度」を維持・回復すること。

前提
- 対象セッション: 講座/生成AI・GASで実践する業務変革・DX推進講座/02-業務データ基盤の設計
- 対象ファイル
  - `講座/生成AI・GASで実践する業務変革・DX推進講座/02-業務データ基盤の設計/画像生成プロンプト.md`
  - `講座/生成AI・GASで実践する業務変革・DX推進講座/02-業務データ基盤の設計/図解パーツ生成プロンプト.md`
- 画像生成はAGENTS方針に従い、`isometric-corporate-clean` を維持。SVG/HTML/CSS/ローカル描画後合成は不可。

現状（今回の編集）
- 画像プロンプト側は、40枚分の共通文言を強化済み。
  - 「source of truth」文に、3〜6構造要素＋学習行動＋成果物＋レビュー観点の可視化を明示。
  - `Make the slide understandable ...` を「次回接続」「具体的な出力」「確認ポイント」を要求する文言へ変更。
- 共通ルールに「各スライドで学習行動／成果物／確認観点を最低1つずつ可視化」を追加。
- 図解パーツ側も、短いラベルの意味情報（役割名・プロセス名・成果物名・確認観点）を許可/要求方向へ変更。
- `Visible text inside the image` を40枚分更新し、2〜5ラベル+演習/レビュー系の最低1観点表示ルールを追加。

未実施タスク
1. 指定モデルに切り替え。
2. S01-S40を再生成。
3. スライド画像を再検証（密度/誤字/情報欠損/可読性）。
4. 必要なら、問題スライドのみ対象プロンプトを再微調整。

再検証チェック項目（最優先）
- スライド1枚ごとに「何を学ぶか」「何を作るか」「どこを確認するか」が画像上で推定可能か。
- `画像生成プロンプト.md`の更新対象文言が未崩壊で反映されているか。
- 誤字・文字化け・抽象化しすぎ・過密/空白帯の偏りがないか。
- 3〜6情報要素（表/カード/フロー/チェックリスト）が存在しているか。
- 実在ロゴ・実在UIの無断生成なし。

便利コマンド
- 更新確認:
  - `rg -n "Build a high-density slide reading layer|Keep text density and contrast|学習行動|成果物|確認観点" \
  "講座/生成AI・GASで実践する業務変革・DX推進講座/02-業務データ基盤の設計/画像生成プロンプト.md"`
  - `rg -n "Visible text inside the image" \
  "講座/生成AI・GASで実践する業務変革・DX推進講座/02-業務データ基盤の設計/図解パーツ生成プロンプト.md"`
- 差分確認: `git diff -- '講座/.../画像生成プロンプト.md' '講座/.../図解パーツ生成プロンプト.md'`

制約
- 未許諾の既存差分（例: prompt-timeline関連）は、今回のタスク外。
- 公開リポジトリに内部情報/顧客情報/連絡先等を入れない。
- 再生成は`imagegen`経由で完走、ローカル後編集や文字後載せはしない。
