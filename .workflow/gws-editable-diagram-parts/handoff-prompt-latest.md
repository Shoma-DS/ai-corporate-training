# GAS講座 図解パーツ再生成・Google Slides更新 引き継ぎプロンプト

あなたは `/Users/deguchishouma/Desktop/AI法人研修` で作業する。目的は、`講座/生成AI・GASで実践する業務変革・DX推進講座/` の編集可能Google Slides用 `図解パーツ/Sxx.png` を、元の全面スライド画像/スライド案の情報量を落とさないプロンプトに直したうえでGPT image 2 / `imagegen` 経由で再生成し、再生成した図解パーツを埋め込んだGoogle Slidesへ置換更新すること。

## 最初に必ず読む

1. `AGENTS.md`
2. `クライアント指示コンテキスト.md`
3. `skills/corporate-training-course-builder/SKILL.md`
4. `skills/gws-ai-training-slide-exporter/SKILL.md`
5. `skills/corporate-training-course-builder/references/session-production-workflow.md`
6. `~/.codex/skills/.system/imagegen/SKILL.md`

この作業では `corporate-training-course-builder` を入口にし、画像生成は通常経路の Codex App Server / GPT image 2 / `imagegen` のみを使う。`OPENAI_API_KEY`、独自SDK、CLI fallback、SVG/HTML/CSS/canvas/PIL/ImageMagick/スクリーンショット生成で `図解パーツ/Sxx.png` を作らない。

## 重要ルール

- `図解パーツ/Sxx.png` は、Google Slides上の編集可能本文を補助する図解。講座名、回名、S番号、フルタイトル、長文本文、フル表は画像内に固定しない。
- ただし「文字なし固定」ではない。元スライドの判断軸、成果物、手順、リスク、確認観点を短い日本語ラベルで3〜6要素のミニ図解として残す。
- 実在Googleロゴ、Google Sheets風アイコン、Apps Scriptの実UIを想像生成しない。汎用の表・歯車・ログパネル・カードで表現する。
- コード関数名は誤字が出やすい。必要な関数名はGoogle Slides本文側に任せ、図解内は日本語ラベル中心にする。
- 生成後は必ず `file`/`sips`/`scripts/check_diagram_parts.py`/`scripts/check_diagram_integrity.py` と、必要な代表画像だけ `view_image` で検品する。
- 複数ワーカーを使う場合、各ワーカーは自分の `$CODEX_HOME/generated_images/<session-id>/` のみをコピー元にする。グローバル最新画像を拾わない。

## 現在の変更内容

`scripts/build_editable_google_slides_sources.py` を更新済み。

- `図解パーツ生成プロンプト.md` に、元スライド案の本文ブロック、表、成果物、確認観点を `Source slide information preserve diagram meaning` として含めるようにした。
- 短い表示ラベル候補は、内容ブロック名・表の行見出しを優先し、`図解パターン` などのメタ項目、ダミー人名・会社名風語を除外する。
- コードブロック由来の入れ子Markdownフェンスは `コード例:` へ変換する。
- `python3 -m py_compile scripts/build_editable_google_slides_sources.py` と `python3 scripts/validate_local_skills.py` は通過済み。

必要に応じて次を再実行する。

```bash
python3 scripts/build_editable_google_slides_sources.py
```

## 完了済み

第2回 `02-業務データ基盤の設計`

- `図解パーツ/S04.png`
- `図解パーツ/S06.png`
- `図解パーツ/S08.png`

上記をGPT image 2 / `imagegen` 経由でまるごと再生成済み。第2回は `scripts/check_diagram_parts.py` と `scripts/check_diagram_integrity.py` で `40/40 ok`。

第2回の編集可能Google Slidesも置換更新済み。

- レポート: `非公開/gws-exports/生成AI・GASで実践する業務変革・DX推進講座/session02-editable-diagrams-report.json`
- Slides URL: `https://docs.google.com/presentation/d/1dEb6_HZ-aPxX4YpwzLlNoV1YHp_xHEBKKUZgNCKtcmc/edit?usp=drivesdk`
- レポート上の結果: `embedded 40/40`, `editableSlideCount 40`, `speakerNoteBlockCount 40`, `warnings []`

第3回 `03-GASによる業務プロセス自動化`

- `図解パーツ/S17.png`〜`S24.png` をGPT image 2 / `imagegen` 経由で生成済み。
- 現在は `24/44`。

## 現在の整合性チェック結果

直近の `python3 scripts/check_diagram_parts.py`:

```text
01-業務DXの基礎とGoogle Workspace活用設計: 43/43 ok
02-業務データ基盤の設計: 40/40 ok
03-GASによる業務プロセス自動化: 24/44 missing missing=S25,S26,S27,S28,S29,S30,S31,S32
04-Gem-Geminiを使った文書作成-分類-要約: 3/40 missing missing=S04,S05,S06,S07,S08,S09,S10,S11
05-AI-GAS自動化の要件定義-運用設計: 9/40 missing missing=S10,S11,S12,S13,S14,S15,S16,S17
06-AI業務効率化プロジェクト提案書の作成: 7/40 missing missing=S08,S09,S10,S11,S12,S13,S14,S15
```

直近の `scripts/check_diagram_integrity.py` では、上記欠番に加えて重複ハッシュが残っている。

- 第5回 `S09` / 第6回 `S07`
- 第4回 `S03` / 第3回 `S08`
- 第1回 `S03` / 第5回 `S03`

## 次にやること

1. 第3回 `S25`〜`S32` を生成する。
2. `python3 scripts/check_diagram_parts.py` で第3回が `32/44` 以上に進むことを確認する。
3. 続けて第3回の残り `S33`〜`S44` を生成し、第3回を `44/44 ok` にする。
4. 第4回、第5回、第6回も同じように欠番を順番に埋める。
5. 重複ハッシュ3組を、各スライド内容に合わせた再生成で解消する。
6. 全回が `ok` になったら、編集可能Google Slidesを全回置換更新する。

## 画像生成の具体手順

各スライドごとに marker を作る。

```bash
touch /private/tmp/gws_s03_s25.marker
```

`図解パーツ生成プロンプト.md` の対象S番号から、元スライド情報を読み、画像内テキストを短い日本語ラベルに絞って `imagegen` で生成する。

生成後、必ず現在のCodex App Server保存先からコピーする。現在の保存先例:

```text
$CODEX_HOME/generated_images/019f057f-53cb-7b93-bb07-75cfe718cfa5/
```

コピー例:

```bash
python3 scripts/copy_latest_generated_image.py \
  --marker /private/tmp/gws_s03_s25.marker \
  --target '講座/生成AI・GASで実践する業務変革・DX推進講座/03-GASによる業務プロセス自動化/図解パーツ/S25.png' \
  --search-root "$CODEX_HOME/generated_images" \
  --expect-mime image/png
```

検品:

```bash
file '講座/生成AI・GASで実践する業務変革・DX推進講座/03-GASによる業務プロセス自動化/図解パーツ/S25.png'
sips -g pixelWidth -g pixelHeight '講座/生成AI・GASで実践する業務変革・DX推進講座/03-GASによる業務プロセス自動化/図解パーツ/S25.png'
python3 scripts/check_diagram_parts.py
python3 scripts/check_diagram_integrity.py
```

## Google Slides更新コマンド

全回の図解が揃ってから実行する。まずdry-run。

```bash
python3 skills/gws-ai-training-slide-exporter/scripts/export_editable_ai_training_slides_to_gws.py \
  --course-dir '講座/生成AI・GASで実践する業務変革・DX推進講座' \
  --all-sessions \
  --replace-existing-decks \
  --embed-diagram-parts \
  --make-diagram-images-readable-by-link \
  --write-link-index \
  --report-json '非公開/gws-exports/生成AI・GASで実践する業務変革・DX推進講座/editable-diagrams-dry-run.json' \
  --dry-run
```

live:

```bash
python3 skills/gws-ai-training-slide-exporter/scripts/export_editable_ai_training_slides_to_gws.py \
  --course-dir '講座/生成AI・GASで実践する業務変革・DX推進講座' \
  --all-sessions \
  --replace-existing-decks \
  --embed-diagram-parts \
  --make-diagram-images-readable-by-link \
  --write-link-index \
  --report-json '非公開/gws-exports/生成AI・GASで実践する業務変革・DX推進講座/editable-diagrams-report.json'
```

`gws` が `~/.config/gws` の権限やトークンキャッシュ更新で失敗した場合は、同じコマンドを `require_escalated` で再実行する。前回、第2回単体更新ではこの承認付き再実行で成功した。

## 注意すべき未コミット差分

- `prompt-timeline/assets/events.js`
- `prompt-timeline/data/events.jsonl`

上記は今回作業とは別系統の既存差分の可能性がある。不要に戻さない。

## 完了条件

- 全6回の `図解パーツ/Sxx.png` が欠番なし。
- `scripts/check_diagram_parts.py` が全回 `ok`。
- `scripts/check_diagram_integrity.py` で bad PNG、odd size、重複ハッシュがない。
- 代表画像を目視し、重要語の誤字、空欄プレースホルダー、情報量不足、実在ロゴ/偽UI生成がない。
- 全回の編集可能Google Slidesを `--replace-existing-decks --embed-diagram-parts` で置換更新済み。
- 非公開レポートJSONで各回の `embeddedCount == expectedCount`、`editableSlideCount` と `speakerNoteBlockCount` が各回スライド枚数に一致し、`warnings []` または説明可能な警告だけ。
