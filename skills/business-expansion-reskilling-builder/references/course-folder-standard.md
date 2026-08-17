# 専用講座フォルダ基準

## ルート

対象講座は、既存の審査向け `講座/` と分けて次に置く。

```text
事業展開等リスキリング講座/
├── AGENTS.md
├── 講座テンプレート/
└── <公開講座名>/
    ├── 全体/
    │   ├── 講座設計.yml
    │   ├── <公開講座名>_講座カリキュラムパンフレット.html
    │   ├── <公開講座名>_講座カリキュラムパンフレット.pdf
    │   └── 調査/
    │       └── 制度出典メモ.md
    ├── 01-<回名>/
    │   ├── slides.json
    │   ├── 講義スライド.html
    │   ├── 講義スライド.pdf
    │   ├── 講師進行メモ.md
    │   ├── 配布資料/
    │   └── 演習データ/
    └── 02-.../
```

## `講座設計.yml` 必須項目

```yaml
course_title: 公開講座名
scheme_route: dx_current_job
target_role: 営業担当者
direct_tasks:
  - 顧客ヒアリングメモから提案書の構成案を作る
business_outputs:
  - 商品提案書
delivery: e_learning
standard_learning_minutes: 720
lms_evidence:
  - completion_date
  - start_end_datetime
  - learning_minutes
  - progress_rate
official_sources_checked: 2026-08-17
```

`scheme_route` は `business_expansion`、`dx_current_job`、`planned_future_job` のいずれか一つを使う。

## 命名

- 講座名には対象職務と業務成果を入れる。
- `生成AI基礎講座`、`DX入門`、`プロンプト研修` のような汎用名だけにしない。
- 回名も操作名ではなく、業務成果へつながる動作で書く。

## 完了条件

- パンフレットHTML/PDFが存在する。
- 各回の `slides.json`、HTML、PDF、講師進行メモが存在する。
- 合計標準学習時間が10時間以上で、各回と全体の合計が一致する。
- 受講者、対象職務、直接業務、成果物、確認者、LMS証跡が特定されている。
- 公的資料の確認日とURLが記録されている。
- 受給保証や顧客固有情報が公開物にない。
