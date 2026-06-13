# 出典メモ: Codex / MCP / DX業務効率化

作成日: 2026-05-28

## 目的

`AIエージェント実装・連携設計アカデミー` の公開可能な講座設計に使う公式情報を整理する。価格、利用可否、助成率、契約条件は変わるため固定しない。社内資料、顧客情報、接続先の認証情報、実業務データは教材内に保存しない。

## 参照元

| 区分 | 参照元 | 確認内容 | 講座への反映 |
| --- | --- | --- | --- |
| OpenAI Codex | OpenAI Developers `Codex CLI` https://developers.openai.com/codex/cli | Codex CLI はローカル端末で動くコーディングエージェントで、選択ディレクトリ内のコードを読み、変更し、コマンド実行できる。 | 第1回から、Codexを「業務改善の実装・検証を補助する作業者」として扱う。実演はダミーリポジトリで行う。 |
| OpenAI Codex | OpenAI Help `Using Codex with your ChatGPT plan` https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan | Codexはコード作成、レビュー、出荷を支援するAIエージェント。利用プラン、利用上限、データコントロール、ワークスペース管理の説明がある。 | 受講環境によって使える範囲が変わるため、プラン名・上限・料金は固定しない。管理者設定とデータ利用設定を確認事項に入れる。 |
| OpenAI Codex | OpenAI Developers `Model Context Protocol` https://developers.openai.com/codex/mcp | CodexはMCPサーバーをCLIとIDE拡張で利用できる。STDIO、Streamable HTTP、Bearer形式の認証情報、OAuth、`config.toml`、`codex mcp` による設定、ツール承認モードが説明されている。 | 第4回でMCP連携設計を扱う。MCP接続は「権限、認証、承認、ログ、用途」を設計してから使うものとして教える。 |
| OpenAI Codex | OpenAI Developers `Sandboxing` https://developers.openai.com/codex/concepts/sandboxing | Codexのサンドボックスは、Codexが起動するコマンドにも適用される。`workspace-write` と `on-request` のような低摩擦な既定設定、`read-only`、`danger-full-access` の違いが示されている。 | 第2回と第5回で、作業範囲、承認、危険なコマンド、ネットワーク、秘密情報の扱いを教材化する。 |
| MCP公式 | MCP `What is the Model Context Protocol?` https://modelcontextprotocol.io/docs/getting-started/intro | MCPはAIアプリケーションを外部システム、データソース、ツール、ワークフローへ接続するオープン標準。 | MCPを「AIに社内ツールを安全につなぐ標準化された接続口」として説明する。 |
| MCP公式 | MCP Draft Specification `Base Protocol Overview` https://modelcontextprotocol.io/specification/draft/basic | MCPはJSON-RPC、ライフサイクル管理、認可、サーバー機能、クライアント機能、ロギングなどで構成される。サーバー機能にはResources、Prompts、Toolsがある。 | 第4回で、ToolsだけでなくResourcesとPromptsも業務設計に入れる。 |
| MCP公式 | MCP Draft Specification `Resources` https://modelcontextprotocol.io/specification/draft/server/resources | Resourcesはファイル、DBスキーマ、アプリ固有情報などをURIで識別し、クライアントへ文脈として提供する。 | 社内資料や業務データは、誰が選び、どの範囲を読み込むかを明示する設計演習にする。 |
| MCP公式 | MCP Draft Specification `Tools` https://modelcontextprotocol.io/specification/draft/server/tools | Toolsはモデル制御で発見・呼び出される。人が承認できるUI、ツール一覧、ツール結果、機密パラメータをHTTPヘッダーに載せない注意がある。 | 第5回で、ツール呼び出しの承認、監査ログ、危険操作の抑止、PII/認証キーの扱いをチェックリスト化する。 |
| OpenAIブランド | OpenAI `Brand` https://openai.com/brand/ | OpenAIロゴ・商標の利用ガイドラインとロゴダウンロード導線がある。 | スライド画像生成ではOpenAIロゴを想像生成しない。公式ロゴを使う場合は `素材/ロゴ/` に取得元メモ付きで保存してから参照する。 |

## 講座設計上の判断

- 講座区分は `人への投資促進コース 高度デジタル人材` 寄りに設計する。
- 目的は「CodexやMCPの操作を覚える」ではなく、「業務課題を整理し、要件定義し、Codexで改善プロトタイプを作り、MCP連携を安全に運用できる提案へ落とし込む」ことにする。
- 録画eラーニング前提のため、ワークは「動画を一時停止して取り組む」形式にする。発表、チャット共有、相互レビューは入れない。
- 実演はすべてダミーの業務データ、サンプルリポジトリ、架空部署名で行う。
- MCP接続先は、研修内では原則としてダミーまたはローカルサンプルにする。実在SaaS、社内DB、Google Drive、Notion、GitHub等の接続は、管理者承認、権限、ログ、利用規約、秘密情報管理を確認してから発展例として扱う。
- 公式ロゴ、UIスクリーンショットを使う場合は、公式ページまたはダミー環境から取得し、画像生成AIに実在ロゴや実在UIを描かせない。
