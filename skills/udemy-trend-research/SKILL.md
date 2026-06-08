---
name: udemy-trend-research
description: UdemyのAI・DX関連講座を定期リサーチし、法人AI研修のネタ帳（非公開/udemy-ai-research-netatyou-YYYY-MM.md）を生成・更新するスキル。Kimi WebBridgeでブラウザ操作し、最新順・高評価順の2軸で複数キーワードを調査してトレンドと研修テーマ案を整理する。
---

# Udemy トレンドリサーチ スキル

## 目的

Udemyの日本語AI・DX講座を定期調査し、**法人AI研修に転用できるテーマのネタ帳**をファイルで蓄積する。

## トリガー

以下のいずれかの発言でこのスキルを使う：
- 「Udemyをリサーチして」「UdemyでAI講座を調べて」
- 「研修ネタを探して」「最新のAIトレンドを調べて」
- 「ネタ帳を更新して」

## 前提条件

- Kimi WebBridge が動作していること（`~/.kimi-webbridge/bin/kimi-webbridge status` で `running: true` かつ `extension_connected: true`）
- 動作していない場合は `~/.kimi-webbridge/bin/kimi-webbridge start` で起動

---

## 実行手順

### Step 0: ヘルスチェック

```bash
~/.kimi-webbridge/bin/kimi-webbridge status
```

`running: false` の場合：
```bash
~/.kimi-webbridge/bin/kimi-webbridge start
```

---

### Step 1: 検索セッションの開始

セッション名 `udemy-trend-YYYYMM`（例：`udemy-trend-202606`）を使う。

**検索クエリ一覧**（最低3つを実施）

| 優先度 | URL | 目的 |
|--------|-----|------|
| 必須 | `https://www.udemy.com/courses/search/?q=ChatGPT+AI%E6%B4%BB%E7%94%A8&sort=newest&lang=ja` | 最新トレンドの把握 |
| 必須 | `https://www.udemy.com/courses/search/?q=%E7%94%9F%E6%88%90AI+%E6%A5%AD%E5%8B%99%E5%8A%B9%E7%8E%87%E5%8C%96&sort=highest-rated&lang=ja&ratings=4.0` | 高評価・安定人気テーマ |
| 必須 | `https://www.udemy.com/courses/search/?q=MCP+Claude+Cursor+%E6%A5%AD%E5%8B%99&sort=newest&lang=ja` | 最新AIツール動向 |
| 任意 | `https://www.udemy.com/courses/search/?q=Microsoft+Copilot&sort=newest&lang=ja` | Microsoft環境向け |
| 任意 | `https://www.udemy.com/courses/search/?q=AI%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88+DX&sort=newest&lang=ja` | DX・AIエージェント系 |

---

### Step 2: ページからテキストを取得する方法

各ページで以下の手順を踏む：

**2-1. ページ読み込み後3秒待機**
```bash
sleep 3
```

**2-2. クッキーダイアログが出たら閉じる**
```bash
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"evaluate","args":{"code":"(() => { const btns = Array.from(document.querySelectorAll(\"button\")); const accept = btns.find(b => b.textContent.includes(\"すべてのフィルター\") === false && (b.textContent.includes(\"許可\") || b.textContent.includes(\"同意\") || b.textContent.includes(\"承認\"))); if(accept){accept.click(); return \"clicked:\"+accept.textContent.trim();} return \"no cookie btn\"; })()"},"session":"SESSION_NAME"}'
```

**2-3. フィルターモーダルが開いていたらEscで閉じる**
```bash
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"evaluate","args":{"code":"document.dispatchEvent(new KeyboardEvent(\"keydown\",{key:\"Escape\",bubbles:true})); \"esc sent\""},"session":"SESSION_NAME"}'
```

**2-4. ページ本文テキストを分割取得（3000文字ずつ）**
```bash
# 前半
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"evaluate","args":{"code":"document.body.innerText.slice(2500, 6000)"},"session":"SESSION_NAME"}'

# 後半
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"evaluate","args":{"code":"document.body.innerText.slice(6000, 10000)"},"session":"SESSION_NAME"}'
```

---

### Step 3: 収集する情報の抽出ポイント

各検索結果から以下を記録する：

```
講座タイトル
講師名
評価（x.x / 5段階中）
評価件数
合計時間
レクチャー数
レベル（初級/中級/すべてのレベル）
説明文（1〜2行）
```

また、ページ左カラムの **「トピック」件数**も記録する（需要の大きさの指標になる）。

---

### Step 4: ネタ帳ファイルに保存

保存先：`非公開/udemy-ai-research-netatyou-YYYY-MM.md`

ファイルの構成テンプレート：

```markdown
# Udemy AI・DX関連講座リサーチ ネタ帳
調査日: YYYY-MM-DD
調査方法: Udemy 日本語講座を「最新順」「高評価順」で複数キーワード検索

---

## 注目トレンドまとめ（法人研修テーマ候補）

### ★★★ 最旬・今すぐ使えるテーマ
（テーマ名 | 根拠となる講座・件数）

### ★★ 定番・需要の厚いテーマ

### ★ 特定職種・業種向けの切り口

---

## Udemyで見えた急上昇キーワード（YYYY年MM月時点）

---

## 法人研修への転用アイデア（優先度順）

### 優先度A：すぐ企画できるもの
（テーマ・ターゲット・内容・根拠）

### 優先度B：差別化できるもの

---

## 参考：Udemy 日本語AI講座の件数

（キーワード | 件数）

---

## 今後ウォッチすべきテーマ
```

---

### Step 5: セッションを閉じる

```bash
curl -s -X POST http://127.0.0.1:10086/command \
  -H 'Content-Type: application/json' \
  -d '{"action":"close_session","args":{},"session":"SESSION_NAME"}'
```

---

## 注意事項・既知の問題

- **クッキーモーダル**: Udemyはページ遷移のたびにクッキーダイアログが表示される場合がある。Step 2-2 で毎回対処する
- **フィルターモーダル**: 検索URLに `&lang=ja` が入っている場合、自動的にフィルターモーダルが開くことがある。Escで閉じる
- **スケルトン表示**: ページ読み込み直後は講座カードがスケルトン状態（class名に "skeleton" を含む）。`sleep 3` 後に取得する
- **ページネーション**: 1ページあたり20件表示。`&p=2` `&p=3` でページ送りできる
- **サンドボックス制限**: `curl` コマンドは `dangerouslyDisableSandbox: true` が必要な場合がある

---

## 保存先とファイル命名規則

```
非公開/udemy-ai-research-netatyou-YYYY-MM.md
```

- 同月に追加調査した場合は同ファイルに追記する（新規作成しない）
- 翌月の調査は新しいファイルを作成する
- 非公開フォルダに保存するため、public repo には含まれない
