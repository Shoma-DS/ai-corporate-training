# Claude引き継ぎプロンプト: 全講座の目次・章見出し・高密度図解ルール反映

あなたは `/Users/deguchishouma/Desktop/AI法人研修` のローカルリポジトリで作業するClaude Codeです。以下の目的で、未修正の講座資料を直してください。

## 目的

GAS講座だけでなく、今後の全講座を同じ品質基準で作る。

- 各回の冒頭に「目次/全体像」スライドを入れる。
- 各章の開始位置に「章見出し/現在位置」スライドを入れる。
- 通常スライドでも、講座名、回、S番号、現在セクションが分かるテンプレート項目を保つ。
- 図解画像は文字なし・短ラベルだけにせず、S04「DXは大きなシステム導入だけではない」くらいの情報量を持つ資料画像にする。
- HTML/編集可能Google Slidesテンプレートへ添付する図解画像は、横幅を広く保ち、縦はやや短めにして、テンプレート側のタイトル、S番号、セクション名、現在位置表示を圧迫しない。

## 最初に必ず読むファイル

1. `AGENTS.md`
2. `クライアント指示コンテキスト.md`
3. `skills/corporate-training-course-builder/SKILL.md`
4. `skills/corporate-training-course-builder/references/editable-google-slides-workflow.md`
5. `skills/corporate-training-course-builder/references/session-production-workflow.md`
6. 対象講座の `スライド案.md`、`Googleスライド編集用アウトライン.md`、`図解パーツ生成プロンプト.md`

## 2026-06-29時点で反映済みのルール変更

Codex側で以下は更新済みです。内容を読み、必要なら整合性だけ確認してください。

- `AGENTS.md`
- `クライアント指示コンテキスト.md`
- `skills/corporate-training-course-builder/SKILL.md`
- `skills/corporate-training-course-builder/references/editable-google-slides-workflow.md`
- `skills/corporate-training-course-builder/references/session-production-workflow.md`
- `skills/gws-ai-training-slide-exporter/SKILL.md`
- `scripts/build_editable_google_slides_sources.py`

検証済み:

```bash
python3 -m py_compile scripts/build_editable_google_slides_sources.py skills/gws-ai-training-slide-exporter/scripts/export_editable_ai_training_slides_to_gws.py
python3 scripts/validate_local_skills.py
```

`validate_local_skills.py` は `local skills ok` でした。

## 全講座へ適用する新しいスライド案ルール

各回のスライド案は、最低でも次を満たしてください。

- S01: 表紙。講座名、回、今回のテーマ、成果物予告がある。
- S02: 今日の成果物。受講者が持ち帰る成果物と使い道が分かる。
- S03付近: 目次/全体像。3〜6個の章、時間配分、成果物、デモ/演習位置が分かる。
- 各章開始位置: 章見出し/現在位置スライド。現在章を大きく見せ、前後の章、これから扱う判断軸、作る成果物、次の演習や画面共有への接続を書く。
- 通常解説スライド: 結論型ヘッドライン、3〜6個の具体ブロック、表/BeforeAfter/プロセス/チェックリスト/業種別例/演習手順/レビュー観点のいずれかを持つ。
- まとめ: 本日の成果物、次回接続、自己チェック、情報管理/運用リスク確認がある。

章見出しスライドは、単なる「第2章」や雰囲気画像では不合格です。目次のどの項目に入るかが、見た瞬間に分かる必要があります。

## 図解画像ルール

`図解パーツ/Sxx.png` は、Codex App Server / GPT image 2 / `imagegen` 相当で生成された完成ラスター画像だけを完成物としてください。

- SVG、HTML/CSS、canvas、ブラウザスクリーンショット、PIL/Pillow、ImageMagick、PDF/PPTX書き出し、ローカル合成、テキスト後載せで作ったPNGは禁止。
- 文字なし、短ラベルだけ、抽象アイコンだけの図解は禁止。
- S04サンプルのように、Before/After表、階層図、業種別例、判断軸、リスク/確認観点、成果物名などを読める密度で入れる。
- ただし講座名、回、S番号、セクション名、フルタイトルはテンプレート側で編集可能に残す。図解画像には焼き込みすぎない。
- 画像は横長で、縦はやや短めにする。タイトルや現在位置表示を置く上部領域を奪わない。

## 現在未修正の主要タスク

### GAS講座

対象:

`講座/生成AI・GASで実践する業務変革・DX推進講座/`

未完了:

- スライド案そのものには、まだ新ルールの「章見出し/現在位置」スライドが全章に挿入されていない。
- `scripts/build_editable_google_slides_sources.py` は新基準へ更新済みだが、スライド案側の章見出し追加・S番号再整理が必要。
- `図解パーツ` は欠番・重複が残っており、Google Slidesへ完成版として再書き出しできる状態ではない。

直近の `python3 scripts/check_diagram_integrity.py` 結果:

```text
01-業務DXの基礎とGoogle Workspace活用設計: 43/43 ok
02-業務データ基盤の設計: 40/40 ok
03-GASによる業務プロセス自動化: 24/44 needs_fix missing=S25,S26,S27,S28,S29,S30,S31,S32
04-Gem-Geminiを使った文書作成-分類-要約: 3/40 needs_fix missing=S04,S05,S06,S07,S08,S09,S10,S11
05-AI-GAS自動化の要件定義-運用設計: 9/40 needs_fix missing=S10,S11,S12,S13,S14,S15,S16,S17
06-AI業務効率化プロジェクト提案書の作成: 7/40 needs_fix missing=S08,S09,S10,S11,S12,S13,S14,S15
duplicate_hash_groups:
- 05/S09.png == 06/S07.png
- 03/S08.png == 04/S03.png
- 01/S03.png == 05/S03.png
```

既存PNGを完成扱いせず、必要なら `非公開/diagram-backups/` に退避してから再生成してください。退避や削除をする前に、対象がGAS講座配下だけであることを必ず確認してください。

### GAS講座以外

未監査です。以下を順番に確認してください。

1. `講座/` 配下の各講座フォルダを一覧化する。
2. 各回 `スライド案.md` に、S03相当の目次/全体像と章開始位置の章見出し/現在位置スライドがあるか確認する。
3. なければスライド案を修正する。必要に応じてS番号を振り直す。
4. `画像生成プロンプト.md` または `図解パーツ生成プロンプト.md` が短ラベル・文字なし・抽象図になっていないか確認する。
5. 図解画像やスライド画像が旧基準なら、未生成/再生成対象として記録する。ローカル合成で仮画像を作らない。

## 作業手順案

1. 現在のgit状態を確認する。

```bash
git status --short
```

既に未コミット変更があります。無関係な変更を戻さないでください。特に `prompt-timeline/`、`.workflow/`、`scripts/* 2.py`、既存の未追跡PNGは触る前に必要性を確認してください。

2. GAS講座のスライド案へ章見出し/現在位置スライドを追加する。

- 既存の時間配分表を基準に、各ブロック開始位置へ章見出しスライドを置く。
- S番号の増加に合わせてスライド範囲表、本文中の参照、台本、プロンプト、アウトラインを更新する。
- 40枚前後に収める必要よりも、審査者が構造を追えることを優先する。ただし120分構成は崩さない。

3. 編集用アウトラインと図解プロンプトを再生成する。

```bash
python3 scripts/build_editable_google_slides_sources.py
```

4. 図解画像の再生成は、Codex App Server / GPT image 2 / `imagegen` 相当のみで行う。生成できない場合は未生成として記録し、仮画像を置かない。

5. 検証する。

```bash
python3 scripts/validate_local_skills.py
python3 -m py_compile scripts/build_editable_google_slides_sources.py skills/gws-ai-training-slide-exporter/scripts/export_editable_ai_training_slides_to_gws.py
python3 scripts/check_diagram_integrity.py
rg -n "Visible text: none|TEXT-FREE|short-label-only|文字なし|短いラベルだけ" AGENTS.md クライアント指示コンテキスト.md skills 講座
```

6. Google Slidesへの再書き出しは、図解PNGの欠番・重複が解消してから行う。完成版では必ず次を使う。

```bash
python3 skills/gws-ai-training-slide-exporter/scripts/export_editable_ai_training_slides_to_gws.py \
  --course-dir '講座/生成AI・GASで実践する業務変革・DX推進講座' \
  --all-sessions \
  --replace-existing-decks \
  --embed-diagram-parts \
  --make-diagram-images-readable-by-link \
  --write-link-index \
  --report-json '非公開/gws-export/editable-slides-with-diagrams-report.json' \
  --dry-run
```

ライブ実行はdry-run確認後に行う。

## 触ってはいけない/注意すること

- `非公開/` の中身、Drive APIレスポンス、顧客情報、価格、個人情報をpublicファイルへ出さない。
- 旧講座名 `Google Workspace・GASで進めるAI業務効率化-DX実践講座` を新しい表示名として復活させない。
- 既存PNGの上に文字を重ねて修正しない。
- OpenAI APIキー、CLI fallback、独自SDKへ進まない。
- 他講座へGAS講座の文言、章立て、演習内容をコピーしない。参照するのは密度・構図・現在位置表示の作り方だけ。

## 完了条件

- 全体ルールとスキルの新基準に反している講座をリストアップしている。
- 修正対象の `スライド案.md` に、目次/全体像と章見出し/現在位置が入っている。
- `Googleスライド編集用アウトライン.md` と `図解パーツ生成プロンプト.md` が新しいスライド構成と一致している。
- 図解PNGは欠番・重複・薄い情報量・文字なし飾りがない。
- 検証コマンド結果をユーザーに簡潔に報告できる。
