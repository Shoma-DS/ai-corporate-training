# GitHub Project分類スキーマ

## 対象

- Owner: `Shoma-DS`
- Repository: `Shoma-DS/ai-corporate-training`
- Project number: `1`
- Project title: `AI法人研修｜講座アイデア管理`
- Visibility: private

Project URLや内部アイデア本文は公開ファイルへ記載しない。

## フィールド

| フィールド | 種類 | 値 |
| --- | --- | --- |
| Status | Single select | Todo / In Progress / Done |
| 制度区分 | Single select | 事業展開等リスキリング / 従来の助成金講座 / 制度共通 / 未判定 |
| アイデア種別 | Single select | 新規講座 / 既存講座改善 / 教材ネタ / 制度対応 / 調査 |
| 職務直結度 | Single select | 直接 / 要具体化 / 対象外候補 |
| 優先度 | Single select | 高 / 中 / 低 |
| 対象職務 | Text | 例: 法人営業担当者 |
| 根拠確認日 | Date | YYYY-MM-DD |

## 公開Issue用ラベル

- `制度:事業展開等リスキリング`
- `制度:従来助成金講座`
- `制度:共通`
- `種別:講座案`
- `種別:教材ネタ`
- `種別:制度対応`
- `判定:要制度確認`
- `職務直結:要具体化`

ラベルは公開Issueの粗い分類、Projectフィールドは実務管理の詳細分類として使い分ける。未公開のネタはIssue化せずDraft itemにする。

## 本文テンプレート

```markdown
## アイデア
一文要約

## 分類
- 制度区分:
- アイデア種別:
- 職務直結度:
- 優先度:

## 職務への接続
- 対象職務:
- 直接業務:
- 業務成果物:

## 根拠
- URL:
- 確認日:

## 次の判断
- 未確定事項または次の作業
```
