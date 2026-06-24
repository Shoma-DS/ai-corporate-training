# GAS講座 編集可能Google Slides用 図解パーツ生成ハンドオフ

## 目的

`講座/生成AI・GASで実践する業務変革・DX推進講座/` の編集可能Google Slides用に、各回 `図解パーツ/Sxx.png` を Codex App Server / GPT image 2 / `imagegen` 経由で生成し、最終的に `--embed-diagram-parts` でGoogle Slidesへ埋め込める状態にする。

## 現在の方針

- 図解パーツはスライド本文を置き換えない補助ビジュアル。
- 文字なし固定にしない。短い日本語ラベルが理解に必要なら画像内に入れてよい。
- 入れてよい文字は短い語句だけ。講座名、回名、S番号、スライドタイトル全文、ヘッドライン全文、表本文、長文はGoogle Slides側の編集可能テキストに残す。
- 実在ロゴ、実在UI、偽Google画面、個人情報、古い講座名は入れない。
- 生成画像は現在の imagegen session directory `/Users/deguchishouma/.codex/generated_images/019ef80a-45d3-7d02-b095-47dc4014cacb/` から、marker 以後のPNGだけをコピーする。

## 進捗

- 第1回: `43/43 ok`
- 第2回: `40/40 ok`
- 第3回: `16/44` まで生成済み。次は `S17` から。
- 第4回: `3/40` まで生成済み。次は `S04` から。
- 第5回: `9/40` まで生成済み。次は `S10` から。
- 第6回: `7/40` まで生成済み。次は `S08` から。

注意: `python3 scripts/check_diagram_parts.py` の通常表示は欠番の先頭8件だけを出す。全欠番は `--json` で確認する。

## 直近で完了した作業

- `クライアント指示コンテキスト.md` と講座作成スキル側には「図解パーツは文字なし固定にしない」ルールが反映済み。
- `python3 scripts/validate_local_skills.py` は `local skills ok`。
- 第2回 `S34`〜`S40` を生成・保存済み。
- 第3回 `S09`〜`S16` を生成・保存済み。

## 検証コマンド

```bash
python3 scripts/check_diagram_parts.py
python3 scripts/check_diagram_parts.py --json
python3 scripts/check_diagram_integrity.py
python3 scripts/validate_local_skills.py
```

## コピー手順

各画像生成前に marker を作る。

```bash
touch /private/tmp/gws_s03_s17.marker
```

生成後、次の形式でコピーする。

```bash
python3 scripts/copy_latest_generated_image.py \
  --marker /private/tmp/gws_s03_s17.marker \
  --target '講座/生成AI・GASで実践する業務変革・DX推進講座/03-GASによる業務プロセス自動化/図解パーツ/S17.png' \
  --session-id 019ef80a-45d3-7d02-b095-47dc4014cacb \
  --expect-mime image/png
```

## 次の作業

1. 第3回 `S17`〜`S44` を順に生成する。
2. 第4回 `S04`〜`S40`、第5回 `S10`〜`S40`、第6回 `S08`〜`S40` を生成する。
3. `python3 scripts/check_diagram_integrity.py` で重複ハッシュを確認し、過去に誤コピーされた重複画像を再生成する。
4. すべて通ったら、編集可能Google Slides書き出しをまず `--dry-run` で確認する。
