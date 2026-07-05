# GAS図解パーツ生成キュー

- 対象講座: `講座/生成AI・GASで実践する業務変革・DX推進講座`
- 総タスク数: 283
- 方針: 全S番号を新しい `図解パーツ生成プロンプト.md` から再生成する。既存PNGはS番号ずれの可能性があるため完成扱いにしない。
- 共有キュー: `shared_queue.py` と `shared-queue-state.json` で `pending/claimed/complete/failed` をファイルロック付き管理する。追加ワーカーは固定シャードではなく `claim` で1件ずつ取得する。
- 実行経路: Codex App Server / GPT image 2 / `imagegen` のみ。ローカル描画、HTML/SVG/canvas、PIL、ImageMagick、スクリーンショット代替は禁止。
- コピー元: 各ワーカー自身の `generated_images/<session-id>/` のみ。他ワーカーの画像を拾わない。

## 2026-07-01 再開方針

遅延原因:

- Agentsブラウザ/対話UIでワーカーを動かすと、ページ表示・スクリーンショット・手動確認の待ち時間が画像生成ごとに乗る。
- 旧実行ではターミナル上の `codex exec` ワーカーが共有キューを消費していたため、ブラウザ表示を待たずに複数サブエージェントが継続実行できていた。
- `TooManyRequests` 後に一部タスクが `claimed` のまま残り、再開時に実ファイルと共有キューの状態がずれた。

修正:

- `shared_queue.py reset-stale` で古いclaimだけを戻す。
- `launch_fast_screen_workers.sh` で1つのscreenセッションから複数の `codex exec` ワーカーを起動する。
- 外側の `fast_codex_worker.py` がclaimとプロンプト抽出を行い、内側の `codex exec` へ1タスクずつ短いプロンプトを渡す。これにより各サブエージェントが毎回リポジトリ全体を読み直す時間を削る。
- `nohup` 直下のバックグラウンド `codex exec` は、この環境ではHeadroom/Codex CLIがassistant処理に入らず終了することがあったため標準経路にしない。疑似TTYを持つ `screen` 経路を使う。
- ワーカー数はまず6並列を標準にする。429が増える場合は4並列へ落とし、安定していれば8並列まで増やす。

再開コマンド:

```bash
python3 .workflow/gas-diagram-generation/shared_queue.py reset-stale --stale-minutes 90
python3 .workflow/gas-diagram-generation/shared_queue.py sync-existing --mark-existing-newer-than '2026-06-29 00:00:00'
bash .workflow/gas-diagram-generation/launch_fast_screen_workers.sh 6 71
```

状況確認:

```bash
python3 .workflow/gas-diagram-generation/shared_queue.py status --sample 20
python3 scripts/check_diagram_integrity.py
```

## シャード

固定シャードは初期投入時の参照用。共有キュー方式へ切り替えた後は、各ワーカーが `python3 .workflow/gas-diagram-generation/shared_queue.py claim --worker worker-XX --stale-minutes 90` で次のタスクを取得する。

| ワーカー | セッション | 枚数 | キューファイル |
|---|---|---:|---|
| worker-01 | 01-業務DXの基礎とGoogle Workspace活用設計 | 49 | `shards/worker-01.jsonl` |
| worker-02 | 02-業務データ基盤の設計 | 45 | `shards/worker-02.jsonl` |
| worker-03 | 03-GASによる業務プロセス自動化 | 50 | `shards/worker-03.jsonl` |
| worker-04 | 04-Gem-Geminiを使った文書作成-分類-要約 | 46 | `shards/worker-04.jsonl` |
| worker-05 | 05-AI-GAS自動化の要件定義-運用設計 | 46 | `shards/worker-05.jsonl` |
| worker-06 | 06-AI業務効率化プロジェクト提案書の作成 | 47 | `shards/worker-06.jsonl` |
