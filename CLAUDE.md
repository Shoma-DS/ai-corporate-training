# AI法人研修 Claude Code ルール

このリポジトリで作業する Claude Code は、まず `AGENTS.md` を読む。`AGENTS.md` をこのリポジトリの共通ルールとして扱う。

## ローカルスキル

- リポジトリ専用スキルは `skills/` 以下を正とする。
- 研修資料、講師台本、スライド構成、画像生成プロンプト、スライド画像、配布資料、ワークシート、演習データを作る・直す場合、および講師台本のブラッシュアップ（画面共有の詳細化・メタファー追加・語り口の自然化）を行う場合は、`skills/corporate-training-course-builder/SKILL.md` を読んでから作業する。
- 詳細な制作チェックリストが必要な場合は、`skills/corporate-training-course-builder/references/session-production-workflow.md` を読む。
- スライド画像、講座ビジュアル、画像素材を GPT image 2 で作る場合、またはユーザーが「上から処理ではなく1枚まるごと生成」と指定した場合も、`skills/corporate-training-course-builder/SKILL.md` の画像生成ルールに従う。
- スライド画像の再生成では、既存画像への後載せ修正ではなく、SVG/HTML/CSS/canvas/ローカル変換を中間に挟まず、必要な公式ロゴやスクリーンショットを参照した1枚の完成画像として作り直す。
- ローカルスキルの確認は Ruby ではなく Python で行う。必要な場合は `python3 scripts/validate_local_skills.py` を使う。

## 公開リポジトリの注意

`非公開/`、会社資料、提携先資料、価格、連絡先、申請書類、個人情報、社内固有情報は public repo に保存しない。詳細は `AGENTS.md` に従う。
