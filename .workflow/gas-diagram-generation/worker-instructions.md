# GAS図解パーツ生成ワーカー手順

あなたは `/Users/deguchishouma/Desktop/AI法人研修` のサブエージェントです。GAS講座の編集可能Google Slides用 `図解パーツ/Sxx.png` を、共有キューからclaimして生成してください。

## 絶対ルール

- 対象は、`.workflow/gas-diagram-generation/shared_queue.py claim --worker worker-XX` で取得した1件だけ。固定シャードは旧方式の参照用であり、coordinatorから共有キュー指示がある場合は使わない。
- 書き込み先はclaim結果の `task.target` だけ。`スライド案.md`、`Googleスライド編集用アウトライン.md`、`図解パーツ生成プロンプト.md`、スキル、スクリプトは編集しない。
- 画像生成は Codex App Server / GPT image 2 / `imagegen` のみ。OpenAI APIキー、CLI fallback、独自SDK、SVG/HTML/CSS/canvas/PIL/ImageMagick/ブラウザスクリーンショット/ローカル合成は禁止。
- 既存PNGはS番号ずれの可能性があるため、対象S番号はすべて1枚まるごと再生成する。
- 画像は横長・やや短めの高密度ラスター資料画像にする。文字なし、短ラベルだけ、抽象アイコンだけは禁止。
- 画像内に講座名、セッション名、S番号、セクションヘッダー、フルスライドタイトルは焼き込まない。テンプレート側の編集可能テキストとして残す。
- 図解内には、見ただけで内容が理解できる見出し、表セル、カード説明、成果物、判断軸、リスク/確認観点、具体例を入れる。
- 生成後は、あなた自身の Codex セッションに表示された `generated_images/<session-id>/` だけをコピー元にする。他ワーカーやグローバル最新画像を拾わない。

## 基本手順

1. `AGENTS.md`、`クライアント指示コンテキスト.md`、`skills/corporate-training-course-builder/SKILL.md` の画像生成・図解ルールを確認する。
2. 次のコマンドで1件claimする。`status` が `empty` なら完了報告へ進む。

   ```bash
   python3 .workflow/gas-diagram-generation/shared_queue.py claim --worker worker-XX --stale-minutes 90
   ```

3. claim結果の `task.prompt_file` から対象 `## Sxx ...` ブロックを読み、プロンプト内容を反映して `imagegen` で生成する。
4. 各生成前にマーカーを作る。例:

   ```bash
   mkdir -p /tmp/gas-diagram-markers
   touch /tmp/gas-diagram-markers/worker-XX-<task_id>.marker
   ```

5. `imagegen` 生成後、生成画像の保存先として表示された自分の `generated_images/<session-id>/` をコピー元にし、次のようにコピーする。

   ```bash
   python3 scripts/copy_latest_generated_image.py \
     --marker /tmp/gas-diagram-markers/worker-XX-<task_id>.marker \
     --target '<target>' \
     --search-root '<あなた自身の generated_images/<session-id> ディレクトリ>' \
     --expect-mime image/png
   ```

   `--search-root` を指定できない場合は、作業を止めて coordinator に相談する。グローバル `generated_images` から最新ファイルを拾ってはいけない。

6. 生成画像を低負荷で検品する。最低限、`file '<target>'`、必要に応じて `view_image detail:low` を使う。
7. 重要語の誤字、文字化け、極小文字、空欄、偽ロゴ/偽UI、薄すぎる情報量があれば、そのS番号を丸ごと再生成する。ローカルで文字を後載せしない。
8. 合格したら共有キューをcompleteにする。

   ```bash
   python3 .workflow/gas-diagram-generation/shared_queue.py complete \
     --worker worker-XX \
     --task-id '<task_id>' \
     --claim-token '<claim_token>' \
     --target '<target>' \
     --note 'PNG生成・コピー・file確認済み'
   ```

9. 失敗して再試行を他ワーカーへ渡す場合は `fail --requeue`、自分で再生成する場合はcompleteせずに同じclaim内で再生成する。
10. 完了/未完了を `.workflow/gas-diagram-generation/reports/worker-XX.md` に書く。レポートは自分のワーカー番号だけ編集する。
11. 2に戻り、キューがemptyになるまで繰り返す。

## 完了報告

割り当て分が完了、またはブロックされたら、Orca orchestration の `worker_done` で coordinator に報告してください。本文には以下を含めてください。

- 完了したtask_id/S番号
- 再生成した枚数
- 失敗/再試行/未完了のS番号
- 使った自分の generated_images session id
- レポートファイルのパス
