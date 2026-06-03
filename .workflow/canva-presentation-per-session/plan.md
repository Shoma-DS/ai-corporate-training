# Canva 画像アップロード先行プレゼンワークフロー（テンプレート）

## Goal

対象講座のスライド画像を、回ごとに1本のCanvaプレゼンテーションとして作成する。標準では全ページをMagic Layers化せず、画像ベースの完成見た目を保ったまま取り込み、編集頻度が高いページだけCanva上で手動Magic Layers化する。

## 期待する成果物

- 回ごとに1本のCanvaプレゼンテーション（`edit_url` が1つ）
- 各ページは `スライド画像/Sxx.png` を全面配置した画像ページ
- 手動Magic Layers化するページの候補リスト
- Canvaフォルダ階層: `AI法人研修 > 講座名 > 01-xxx, 02-xxx, ...`
- URL一覧: `非公開/Canva/<講座スラッグ>_Canva_URL一覧.csv`
- 手動編集メモ: `非公開/Canva/<講座スラッグ>_Magic_Layers対象ページ.md`

## Default Policy

- Canva MCPで全ページをMagic Layers化しない。
- まず画像または回別PPTXをCanvaへアップロードして、複数ページプレゼンを作る。
- Magic LayersはCanva上で手動適用する。対象は編集頻度が高いページだけに絞る。
- 図解、スクリーンショット、操作説明、演習手順、まとめは画像ページのまま残す。
- Canva URL、design ID、認証情報、顧客固有情報はpublicリポジトリに書かない。

## Phases

### P1: インベントリとPPTX作成

- `スライド画像/S*.png` の存在、連番、枚数、空ファイル有無を確認する。
- 標準では `skills/gws-ai-training-slide-exporter/scripts/export_ai_training_slides_to_gws.py --canva-course-pptx-only --canva-pptx-dir` で講座単位PPTXを書き出す。
- 出力先は `<canva-pptx-dir>/<講座名>/<講座名>.pptx` とする。
- 回別運用が必要な場合だけ `--canva-pptx-only --all-sessions` を使い、`<canva-pptx-dir>/<講座名>/<回フォルダ名>.pptx` を作る。
- PPTXはCanva取り込み用の中間成果物として扱う。

### P2: Canvaフォルダ作成

- Canva側に `AI法人研修 > 講座名 > 回別` のフォルダを作る。
- 既存フォルダがある場合はIDを再利用し、重複作成しない。
- フォルダID、design ID、実URLは `非公開/Canva/` 側のstateまたはメモに記録する。

### P3: 回ごとの画像ベースプレゼン作成

- 各セッションについて、画像または回別PPTXをCanvaへアップロードする。
- 1セッションにつき1本の複数ページプレゼンテーションを作る。
- 作成したプレゼンを対応するCanvaフォルダへ移動する。
- `presentation_design_id`, `edit_url`, `view_url`, `page_count` を非公開ログに記録する。

### P4: 手動Magic Layers対象ページの選定

Magic Layers対象にするページ:

- 表紙、章扉、クロージング
- 企業名、実施日、講師名、部署名などを差し替えるページ
- カリキュラム表、受講対象、成果物一覧
- 提案書・営業資料化するときに文言調整が起きるページ
- 受講企業別に差し替えるケース紹介ページ

画像のまま残すページ:

- 固定の業務フロー図、概念図、Before/After図
- 画面共有への遷移スライド
- 公式画面やスクリーンショット中心の説明
- 演習手順、確認観点、まとめ

### P5: 集計・検証

- 回ごとの `page_count` とローカル画像枚数が一致することを確認する。
- `非公開/Canva/<講座スラッグ>_Canva_URL一覧.csv` を作る。
- `非公開/Canva/<講座スラッグ>_Magic_Layers対象ページ.md` を作る。
- Drive同期側に公開してよい範囲の `Canva_URL一覧.csv` だけを置く。
- publicリポジトリへのCanva URL、design ID、認証情報の混入がないことを確認する。

## Legacy: 全ページMagic Layers化が必要な場合

ユーザーが明示的に「全ページをMagic Layers化したい」と指定した場合だけ、旧ルートを使う。

- S01から昇順に `_image_to_design(image_file=<絶対パス>)` を呼ぶ。
- 1画像につき1つの独立したMagic Layersデザインを作る。
- 作成した1ページデザインをCanva Connect API `/v1/merges` で回ごとに結合する。
- 変換ログ、結合結果、URL一覧はすべて `非公開/Canva/` に置く。
- レート制限、変換品質低下、トークン消費が大きいため、標準フローにはしない。

## state.json 構造

```json
{
  "title": "<講座名> Canva Image-first Presentation",
  "slug": "<講座スラッグ>-canva-image-first",
  "status": "in_progress",
  "scope": {
    "course": "講座/COURSE",
    "sessions": { "01-xxx": N, "02-xxx": N }
  },
  "canva": {
    "root_folder_id": "",
    "course_folder_id": "",
    "session_presentations": {
      "01-xxx": {
        "design_id": "",
        "edit_url": "",
        "view_url": "",
        "folder_id": "",
        "page_count": 0,
        "magic_layers_pages": []
      }
    }
  },
  "logs": {
    "url_csv": "非公開/Canva/<スラッグ>_Canva_URL一覧.csv",
    "magic_layers_plan": "非公開/Canva/<スラッグ>_Magic_Layers対象ページ.md"
  }
}
```

## Safety

- `非公開/`, credentials, 顧客情報をCanvaにアップロードしない。
- Canva URL、design ID、認証情報をpublicリポジトリに書かない。
- 既存プレゼンテーションがある場合は非公開stateのIDを再利用し、重複作成しない。
- ページ数不一致、アップロード失敗、フォルダ移動失敗があれば、非公開ログに残してユーザーに報告する。
