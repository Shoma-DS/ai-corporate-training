# 引き継ぎプロンプト

あなたは `/Users/deguchishouma/Desktop/AI法人研修` で作業する Codex です。次の目的を継続してください。

## 目的

講座のスライドの `画像生成プロンプト.md` を改善してから、まだ未生成のスライドだけを GPT image 2 / built-in `image_gen` で1枚ずつ完成ラスター画像として生成し、`スライド画像/Sxx.png` に保存する。

## 最優先で読むファイル

1. `AGENTS.md`
2. `クライアント指示コンテキスト.md`
3. `skills/corporate-training-course-builder/SKILL.md`
4. `スライド/テンプレート/カタログ.yml`
5. `スライド/テンプレート/アイソメトリック法人向けクリーン.md`

必ず `corporate-training-course-builder` のルールに従う。未生成画像は SVG / HTML / CSS / canvas / PIL / ImageMagick / ブラウザスクショ / ローカル合成 / テキスト後載せで作らない。`スライド画像/Sxx.png` は GPT image 2 / built-in `image_gen` の完成ビットマップ、または規約確認済み公式素材だけを完成物とする。

`view_image` は原則 `detail:"low"` で1枚ずつ使う。文字検品は OCR、コピー確認は `shasum`、欠番確認はファイル一覧で行い、`detail:"high"` は最終判断に必要な1枚だけに限定する。`{"detail":"Bad Request"}`、WebSocket切断、response未完了後の再送エラーが出ても、画像生成失敗と決めつけず、生成済みPNGと保存先の状態を確認して低負荷な確認方法で続行する。同じ高解像度 `view_image` をそのまま再試行して止まらない。

## 現在の作業対象

優先中の対象セッション:

`講座/AIエージェント実装・連携設計アカデミー/01-DX業務課題整理とCodex活用設計/`

正しい講座名:

`AIエージェント実装・連携設計アカデミー`

サブタイトル:

`CodexとMCPで学ぶプロトタイプ検証・運用設計・DX導入提案`

旧講座名 `CodexとMCPで進めるDX業務効率化講座` は可視テキストとして使わない。

## 現在の進捗

- `画像生成プロンプト.md` の S01 と S02 は改善済み。
- `S01.png` は生成・目視確認・保存済み。
  - 保存先: `講座/AIエージェント実装・連携設計アカデミー/01-DX業務課題整理とCodex活用設計/スライド画像/S01.png`
  - 元生成ファイル: `/Users/deguchishouma/.codex/generated_images/019eb7c1-fd8f-7ea1-964a-e45bf4ce92e8/ig_00357bf68303358e016a2e121768988191b577a73711757418.png`
  - 目視: 新講座名、サブタイトル、成果物、ダミーデータ注意が入っている。旧講座名なし。
  - OCR: `AIエージェント実装・連携設計アカデミー` は拾えている。
- `S02` は生成・目視確認済みだが、まだ対象フォルダへコピーしていない。
  - 生成ファイル: `/Users/deguchishouma/.codex/generated_images/019eb7c1-fd8f-7ea1-964a-e45bf4ce92e8/ig_00357bf68303358e016a2e134d03e48191a655113a9ef9635d.png`
  - 目視: 成果物3枚、後続回での使い道、小フロー、下部安全帯があり、旧講座名は見当たらない。
  - 次の最初の具体作業: この S02 生成PNGをピクセル変更なしで `講座/AIエージェント実装・連携設計アカデミー/01-DX業務課題整理とCodex活用設計/スライド画像/S02.png` にコピーし、低解像度 `view_image` と OCR で確認する。

## 未生成判定

機械スキャンでは、未生成が多い。まず現在対象セッションの S02 以降を順番に進める。

優先セッション:

`講座/AIエージェント実装・連携設計アカデミー/01-DX業務課題整理とCodex活用設計`

- prompt slides: S01-S40
- 現在保存済み: S01のみ
- 次: S02をコピー・検品、その後 S03 から順次プロンプト改善 -> 画像生成 -> 検品 -> 保存

注意: GAS講座第3回は README 上に「S02-S44未生成」とあるが、現状では `S02.png` 以降も実ファイルが存在し、S02を目視した限り完成画像として使える。READMEだけで未生成扱いにせず、プロンプト番号と実ファイル欠番を照合して判断する。

## サブエージェント分担ルール化の要望

ユーザーが「サブエージェントを使って分担して並列処理をするようにルール化して」と依頼している。次のどちらかで対応する。

1. まず `AGENTS.md` と `skills/corporate-training-course-builder/SKILL.md` の既存「Parallel Subagents」節を確認する。
2. 不足していれば、リポジトリルールとして以下を追記する。

- 画像生成はスライド番号の排他バッチで分担する。
- 例: S03-S10、S11-S20、S21-S30、S31-S40。
- 各担当は自分の割当範囲の `画像生成プロンプト.md` と `スライド画像/Sxx.png` だけを扱う。
- メイン担当は講座名、公開可否、最終検品、ステージング、コミット範囲を確認する。
- 生成前に必ずプロンプトを Dense Slide Image Standard に合わせて改善する。
- 画像生成の最終成果物にはローカル合成や HTML/SVG 等を使わない。

ただし、同じファイルを複数エージェントで同時編集させない。サブエージェントには「読み取り・下書き・番号別生成作業」など排他的な担当を割り当てる。

## 生成時の共通品質基準

- テンプレートは `isometric-corporate-clean` のみ。
- 白背景、ネイビー/ティール、カード型整理、アイソメトリック法人研修調。
- 1枚に以下を入れる。
  - 講座名/回/スライド番号の小ヘッダー
  - So What型ヘッドライン
  - 3〜6個の具体カード、表、フロー、チェックリスト等
  - 成果物、演習、確認観点、リスク/情報管理のいずれか
  - Codex/MCP/サービス名は目的とセットで書く
- 実在ロゴや実在UIを画像生成に想像させない。ロゴは参照素材がある場合だけ。
- public repo に非公開情報、Drive/Canvaリンク、価格、個人名、ID/Password、顧客情報を入れない。

## 推奨ワークフロー

1. `git status --short` で作業範囲を確認。既存の `.agent/` と `prompt-timeline/` の未コミット変更は今回対象外なので触らない。
2. S02生成済みPNGを対象 `S02.png` へコピー。
3. 低解像度 `view_image` で S02 を確認。高解像度表示は必要な1枚だけに限定する。
4. `tesseract ... -l jpn+eng --psm 6` で旧講座名がないか確認。
5. S03以降は、各スライドごとに:
   - `画像生成プロンプト.md` の該当 Sxx ブロックを読む。
   - 講座名、ヘッダー、成果物、後続回との接続、具体事例、リスク/確認帯が弱ければ改善する。
   - `image_gen` で1枚まるごと生成。
   - 生成先 `/Users/deguchishouma/.codex/generated_images/019eb7c1-fd8f-7ea1-964a-e45bf4ce92e8/` の最新PNGを目視。
   - 合格なら `cp` で `スライド画像/Sxx.png` へコピー。
   - OCRと目視で旧講座名、文字化け、プレースホルダー、情報量不足を確認。
6. ある程度まとまったら README または進捗メモを更新する。古い「未生成」README と実態が矛盾する場合は直す。
7. 検証後、対象ファイルだけをステージし、公開不可情報混入を確認して日本語コミット、push。

## 現在のgit状態の注意

現時点の対象作業による未コミット:

- `講座/AIエージェント実装・連携設計アカデミー/01-DX業務課題整理とCodex活用設計/画像生成プロンプト.md` が変更済み。
- `講座/AIエージェント実装・連携設計アカデミー/01-DX業務課題整理とCodex活用設計/スライド画像/S01.png` が未追跡で追加済み。

対象外の既存未コミット変更:

- `.agent/skills/agent-prompt-timeline/...`
- `prompt-timeline/...`

これらはユーザーまたは別作業由来として扱い、今回の講座画像生成では触らない・ステージしない。

## 便利な確認コマンド

```bash
git status --short

python3 - <<'PY'
from pathlib import Path
import re
root = Path('講座')
for prompt in sorted(root.glob('**/画像生成プロンプト.md')):
    text = prompt.read_text(errors='ignore')
    nums = sorted({int(m.group(1)) for m in re.finditer(r'(?:^|\n)#{2,4}\s*(?:Slide\s*)?S(\d{2})\b', text)})
    if not nums:
        nums = sorted({int(m.group(1)) for m in re.finditer(r'\bSlide\s+S(\d{2})\b', text)})
    if not nums:
        continue
    imgdir = prompt.parent / 'スライド画像'
    missing = [n for n in nums if not (imgdir / f'S{n:02d}.png').exists()]
    if missing:
        print(prompt.parent)
        print('  missing:', ' '.join(f'S{n:02d}' for n in missing[:60]))
PY

tesseract '講座/AIエージェント実装・連携設計アカデミー/01-DX業務課題整理とCodex活用設計/スライド画像/S02.png' stdout -l jpn+eng --psm 6 | rg 'CodexとMCPで進めるDX業務効率化講座|AIエージェント実装・連携設計アカデミー|ダミー|安全|検証'

rg -n 'CodexとMCPで進めるDX業務効率化講座|Claude Coworkで始める|NotebookLMで進める|事例で学ぶ中小企業' 講座 --glob '!**/*.png' --glob '!**/*.pdf' --glob '!非公開/**'

git diff --check -- '講座/AIエージェント実装・連携設計アカデミー/01-DX業務課題整理とCodex活用設計'
```

## 完了条件

このゴール全体の完了は、対象となる未生成スライドすべてについて以下が成立してから。

- プロンプトが改善済みで、Dense Slide Image Standard を満たす。
- `スライド画像/Sxx.png` が存在する。
- 画像は GPT image 2 / built-in `image_gen` の完成ラスター画像で、ローカル合成ではない。
- 旧講座名、文字化け、プレースホルダー、情報量不足、公開不可情報がない。
- `画像生成プロンプト.md`、スライド画像、進捗 README/メモの状態が一致している。
- 対象変更だけをコミット・pushしている。

この目的はまだ完了していない。S02保存と S03 以降の生成を続けること。
