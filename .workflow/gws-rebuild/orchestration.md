# Orchestration: Google Workspace講座スライド案リビルド統合

## Goal

Google Workspace・GASで進めるAI業務効率化-DX実践講座の全6回 `スライド案.md` を、AX・DXワークショップ講座の情報量・構図・具体度を参考にした密度へ整え、最終統合検証まで完了する。

## Success Criteria

- 全6回が35〜45枚程度、120分構成として成立している。
- 全スライドにSo What型ヘッドラインがある。
- 各回に比較表、プロセス、チェックリスト、業種別具体例、数値感、演習成果物が入っている。
- Google Workspace/GAS/Gemini固有の内容であり、AX・DX講座のコピーではない。
- 公式素材・スクリーンショットの扱い、出典URL、公開不可情報の除外方針が明記されている。

## Work Packets

| Packet | Scope | Verification |
|---|---|---|
| P1 | 第1回・第2回 | 枚数、ヘッドライン、DX基礎→Forms/Sheets設計の接続、公式素材参照 |
| P2 | 第3回・第4回 | GASコード読解、自動化、Gem/Gemini設計、AI出力レビュー、リスク説明 |
| P3 | 第5回・第6回 | 運用設計、ログ、復旧、提案書、KPI、時間配分表の整合 |
| P4 | 公式素材・スクリーンショット | 公式URL確認、保存済み素材、未取得画面の取得条件、出典メモ |
| P5 | 統合検証 | 全回の枚数・ヘッドライン・時間・公開安全・ワークフロー成果物 |

## Integration Decisions

- 第5回・第6回は本文密度が十分だったため、主な補修は第6回の時間配分表と画面共有タイムラインの整合修正に限定した。
- 公式OG画像は第2回の参考素材として保存したが、操作画面の説明はダミー環境または演習データからの取得を前提にする。
- 公式ヘルプやプロダクトページの画面を画像生成AIで再現しない。

## Verification Commands

```bash
for f in 講座/Google\ Workspace・GASで進めるAI業務効率化-DX実践講座/*/スライド案.md; do
  printf '%s\n' "$f"
  rg -c '^### S[0-9][0-9]' "$f"
  rg -c '^\*\*ヘッドライン:\*\*' "$f"
done

python3 scripts/validate_local_skills.py
python3 skills/codex-dynamic-workflows/scripts/verify_workflow.py .workflow/gws-rebuild
```
