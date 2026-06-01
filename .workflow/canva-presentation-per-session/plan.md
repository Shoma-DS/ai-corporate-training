# Canva プレゼンテーション単位 Magic Layers ワークフロー（テンプレート）

## Goal

対象講座の全スライドを、回ごとに1本のCanvaプレゼンテーションとしてMagic Layers化する。

## 期待する成果物

- 回ごとに1本のCanvaプレゼンテーション（`edit_url` が1つ）
- 各スライドがそのプレゼンテーション内のページとしてMagic Layers化されている
- Canvaフォルダ階層: `AI法人研修 > 講座名 > 01-xxx, 02-xxx, ...`
- 処理ログ: `非公開/Canva/<講座スラッグ>.jsonl`
- URL一覧: `非公開/Canva/<講座スラッグ>_Canva_URL一覧.csv`

## Phases

### P1: インベントリとCanvaフォルダ作成

- `スライド画像/S*.png` の存在と枚数を確認
- `_create_folder` でCanvaフォルダ階層を作成（既存フォルダはIDを再利用）

### P2: 回ごとのCanvaプレゼンテーション作成

- 各セッションに対して `_create_design(design_type: "presentation", title: セッション名)` を呼ぶ
- `presentation_design_id`, `edit_url`, `view_url` を `state.json` に記録
- `_move_item_to_folder` で対応するCanvaフォルダに移動

### P3〜P(N-1): セッションごとのMagic Layersページ追加

- S01から昇順に `_image_to_design(image_file=<絶対パス>, design_id=<プレゼンテーションID>)` を呼ぶ
- 成功: `page_position`, `status: success` をJSONLに記録
- 失敗: 1回リトライ。2回失敗→ `status: failed` で記録して次へ
- セッション単位でワーカーを分割できる（並列実行可）

### P(N): 集計・検証

- JSONLから回ごとのページ数を集計
- `page_count == expected_count` を確認
- CSV出力: `非公開/Canva/<講座スラッグ>_Canva_URL一覧.csv`
- Drive同期側: `Canva_URL一覧.csv`
- publicリポジトリへのCanva URL混入がないことを確認

## state.json 構造

```json
{
  "title": "<講座名> Canva Presentation",
  "slug": "<講座スラッグ>-canva-presentation",
  "status": "in_progress",
  "scope": {
    "course": "講座/COURSE",
    "sessions": { "01-xxx": N, "02-xxx": N }
  },
  "canva": {
    "root_folder_id": "",
    "course_folder_id": "",
    "session_presentations": {
      "01-xxx": { "design_id": "", "edit_url": "", "view_url": "", "folder_id": "" }
    }
  },
  "logs": {
    "jsonl": "非公開/Canva/<スラッグ>.jsonl"
  }
}
```

## Safety

- `非公開/`, credentials, 顧客情報をCanvaにアップロードしない
- Canva URLをpublicリポジトリに書かない
- 既存プレゼンテーションがある場合は `state.json` のIDを再利用し、重複作成しない
- 失敗が全スライドの20%を超えたら処理を停止しユーザーに報告する
