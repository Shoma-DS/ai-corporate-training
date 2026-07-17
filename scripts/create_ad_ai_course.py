#!/usr/bin/env python3
"""Create the AI advertising-operations efficiency course source materials.

This writes public-safe course documents, session slide plans, provisional
scripts, image prompt sources, worksheets, handouts, and sample CSV data. It
does not draw final slide images; final `スライド画像/Sxx.png` files must be
generated through the repository imagegen path.
"""

from __future__ import annotations

import csv
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE_NAME = "生成AIで実践する広告運用効率化・改善提案講座"
COURSE_DIR = ROOT / "講座" / COURSE_NAME
TEMPLATE_ID = "isometric-corporate-clean"
ACCESS_DATE = "2026-07-13"
LMS_TEXT = (
    "eラーニング。本研修は、LMS(学習管理システム:Learning Management System)を利用し、"
    "各自の受講状況や受講時間を全て記録することで、受講者の学習状況の把握を行い、"
    "適切なスキルアップをサポートいたします。"
)


SOURCES = [
    (
        "Google Ads Help: Performance Max campaigns",
        "https://support.google.com/google-ads/answer/10724817",
        "P-MAXを、目標・コンバージョン・素材・オーディエンス信号を渡してGoogle AIが配信面横断で最適化する章に反映。",
    ),
    (
        "Google Ads Help: Smart Bidding",
        "https://support.google.com/google-ads/answer/7065882",
        "自動入札はコンバージョン/価値を最適化する仕組みとして扱い、目標CPA/ROASの読み替えと十分な計測データの重要性を入れる。",
    ),
    (
        "Google Ads Help: AI Max for Search",
        "https://support.google.com/google-ads/answer/15910187",
        "検索広告のAI拡張は、検索語句拡張、テキスト生成、URL拡張、透明性/除外コントロールとセットで扱う。",
    ),
    (
        "Google Ads Help: Demand Gen campaigns",
        "https://support.google.com/google-ads/answer/13695777",
        "YouTube/Discover/Gmail等の需要創出面で、AIがクリエイティブと配信を組み合わせる例として扱う。",
    ),
    (
        "Google Analytics Help: Connect Google Ads to Analytics",
        "https://support.google.com/analytics/answer/9379420",
        "広告AIに任せる前提として、GA4キーイベント/Google Adsコンバージョン/リマーケティング連携を計測基盤章に反映。",
    ),
    (
        "Google Ads Help: Enhanced conversions",
        "https://support.google.com/google-ads/answer/9888656",
        "ハッシュ化されたファーストパーティデータの扱い、同意、プライバシー確認を計測章とガバナンス章に反映。",
    ),
    (
        "Looker Studio: Google Ads connector",
        "https://docs.cloud.google.com/data-studio/connect-to-google-ads",
        "広告レポート自動化と月次報告テンプレートのデモ/演習へ反映。",
    ),
    (
        "Google Ads Help: Optimization score",
        "https://support.google.com/google-ads/answer/9061546",
        "最適化スコア/提案は丸呑みせず、事業目標・ブランド・予算・検証設計で採否判断する演習にする。",
    ),
    (
        "Meta Business Help: About Meta Advantage+",
        "https://www.facebook.com/business/help/733979527611858",
        "MetaのAI最適化は、配信・オーディエンス・クリエイティブの自動化と人のコントロールの両方を扱う。",
    ),
    (
        "Meta Business Help: Advantage+ Creative",
        "https://www.facebook.com/business/help/297506218282224",
        "画像/動画のバリエーション最適化は、ブランド/審査/表示崩れ確認とセットで扱う。",
    ),
    (
        "LINEヤフー広告ヘルプ: スマートターゲティング",
        "https://ads-help.yahoo-net.jp/s/article/H000047178",
        "日本国内媒体のターゲティング自動化例として、配信実績・予算・入札状況に応じた調整を扱う。",
    ),
    (
        "LINEヤフー広告ヘルプ: 最適化提案",
        "https://ads-help.yahoo-net.jp/s/article/H000044358",
        "媒体からの最適化提案を、人が採否判断する業務フローとして扱う。",
    ),
    (
        "Microsoft Advertising: Generative AI tools",
        "https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_generativeaitools",
        "診断、アセット生成、パフォーマンススナップショット、推奨を広告運用補助の例として扱う。",
    ),
    (
        "Microsoft Advertising: Performance Max",
        "https://about.ads.microsoft.com/en/solutions/ad-products-formats/performance-max",
        "Microsoft広告側のP-MAX/AI最適化を、Google Adsだけに偏らない媒体比較として扱う。",
    ),
    (
        "Google Ads Policies: Misrepresentation",
        "https://support.google.com/adspolicy/answer/6020955",
        "広告文・LP・生成コピーの誤認表示/重要情報欠落のチェックへ反映。",
    ),
    (
        "Meta Transparency Center: Advertising Standards",
        "https://transparency.meta.com/policies/ad-standards/",
        "個人属性の示唆、差別、誤認を避ける広告レビュー観点へ反映。",
    ),
    (
        "個人情報保護委員会: 生成AIサービスの利用に関する注意喚起",
        "https://www.ppc.go.jp/news/careful_information/230602_AI_utilize_alert/",
        "個人情報・顧客リスト・広告計測データを生成AIへ入力する前の確認観点へ反映。",
    ),
    (
        "消費者庁: 景品表示法",
        "https://www.caa.go.jp/policies/policy/representation/fair_labeling",
        "広告表示の優良誤認・有利誤認・根拠確認を、クリエイティブレビュー章へ反映。",
    ),
    (
        "Public course outline: AI-powered digital advertising",
        "https://www.classcentral.com/course/udemy-digital-advertising-for-beginners-404878",
        "公開講座ではGoogle Ads/Meta/GA4/クリエイティブが多い一方、法人向けの承認・計測・運用提案を厚くする差別化に反映。",
    ),
]


SESSIONS = [
    {
        "no": "01",
        "dir": "01-広告運用課題整理とAI活用設計",
        "title": "広告運用課題整理とAI活用設計",
        "short": "課題整理",
        "promise": "広告運用を媒体操作ではなく、目的、計測、制作、配信、改善、承認の業務フローとして設計する",
        "output": "広告運用棚卸し表、KPIツリー、AI活用候補選定表",
        "case": "つばめ商店・EC小売・従業員8名・演習用の月間広告予算60万円・Google/Meta/LINEヤフーを想定",
        "main_tools": "ChatGPT, Claude, Google Ads, Meta Ads, LINEヤフー広告, GA4, Looker Studio",
        "chapter2": "広告運用の業務分解",
        "chapter3": "AI活用候補の選定",
        "chapter4": "運用体制と改善サイクル",
        "deep1_title": "広告運用を入力・処理・出力・確認に分ける",
        "deep1_rows": [
            ["入力", "目的、予算、LP、商品情報、ターゲット", "不足情報の抽出、質問案"],
            ["処理", "キーワード、媒体、入札、クリエイティブ", "候補生成、比較表"],
            ["出力", "広告文、画像、キャンペーン構成、レポート", "下書き、要約"],
            ["確認", "審査、景表法、ブランド、個人情報", "チェックリスト化"],
            ["運用", "予算配分、改善履歴、月次報告", "異常検知、改善案"],
        ],
        "deep2_title": "AIに任せる前に広告目的を1枚で定義する",
        "deep2_rows": [
            ["認知", "表示回数、動画視聴", "過度な成果保証を避ける"],
            ["集客", "クリック、LP到達、検索語句", "無駄クリックを見直す"],
            ["獲得", "CV、CPA、ROAS", "計測が正しいか確認する"],
            ["継続", "LTV、リピート、CRM", "顧客データの扱いを確認する"],
        ],
        "platform_rows": [
            ["Google Ads", "検索、P-MAX、Demand Gen", "目標とコンバージョン、素材、除外設定"],
            ["Meta Ads", "Advantage+、クリエイティブ最適化", "ブランド、表示崩れ、個人属性表現"],
            ["LINEヤフー広告", "検索広告、ディスプレイ、スマートターゲティング", "国内媒体の審査・配信面"],
            ["GA4/Looker Studio", "計測とレポート", "CV定義、UTM、差分説明"],
        ],
    },
    {
        "no": "02",
        "dir": "02-計測データ基盤と広告レポート設計",
        "title": "計測データ基盤と広告レポート設計",
        "short": "計測設計",
        "promise": "広告AIが学習できるよう、CV定義、UTM、GA4、広告管理画面、月次レポートの見方をそろえる",
        "output": "計測設計シート、UTM命名ルール、広告レポート診断表",
        "case": "つばめ商店のLP、カート到達、購入、問い合わせを演習用イベントとして設計する",
        "main_tools": "GA4, Google Ads, Looker Studio, Google Tag Manager, ChatGPT, Claude",
        "chapter2": "CVとイベント設計",
        "chapter3": "レポート診断",
        "chapter4": "月次報告の自動化",
        "deep1_title": "広告AIの良し悪しは計測データの質に左右される",
        "deep1_rows": [
            ["CV定義", "購入、問い合わせ、資料DL", "事業成果と一致するか"],
            ["中間イベント", "LP到達、カート到達、滞在", "学習補助に使えるか"],
            ["UTM", "source、medium、campaign", "媒体横断で比較できるか"],
            ["除外", "社内クリック、重複CV", "誤学習を防げるか"],
            ["同意/個人情報", "Cookie、顧客リスト", "規約と社内承認を確認"],
        ],
        "deep2_title": "月次レポートは数字の羅列ではなく意思決定表にする",
        "deep2_rows": [
            ["何が起きたか", "費用、CV、CPA、ROAS", "前月差を示す"],
            ["なぜ起きたか", "媒体、検索語句、素材、LP", "仮説として書く"],
            ["何を変えるか", "予算、入札、広告文、LP", "次の打ち手を1つ選ぶ"],
            ["何を止めるか", "低品質流入、誇大表現、未承認素材", "リスクも判断する"],
        ],
        "platform_rows": [
            ["GA4", "キーイベントと広告連携", "Google Ads CVへの利用条件"],
            ["Google Ads", "コンバージョン、拡張コンバージョン", "同意とハッシュ化データ"],
            ["Looker Studio", "Google Adsコネクタ", "月次テンプレート化"],
            ["ChatGPT/Claude", "レポート要約", "個人情報や非公開顧客情報を入れない"],
        ],
    },
    {
        "no": "03",
        "dir": "03-媒体AI機能とキャンペーン設計",
        "title": "媒体AI機能とキャンペーン設計",
        "short": "媒体AI",
        "promise": "Performance Max、AI Max、Advantage+、スマートターゲティングを、目的・制約・人のコントロールとセットで使う",
        "output": "媒体別AI機能比較表、キャンペーン設計メモ、採否判断チェックリスト",
        "case": "つばめ商店の春キャンペーンを検索、P-MAX、Meta、LINEヤフーへどう分けるか検討する",
        "main_tools": "Google Ads Performance Max, AI Max for Search, Meta Advantage+, LINEヤフー広告, Microsoft Advertising",
        "chapter2": "媒体AI機能の比較",
        "chapter3": "キャンペーン構造",
        "chapter4": "採否判断と例外管理",
        "deep1_title": "媒体AIは万能ではなく入力信号と制約で動かす",
        "deep1_rows": [
            ["目標", "購入、問い合わせ、来店", "媒体に渡すゴールを固定"],
            ["素材", "広告文、画像、動画、LP", "品質と権利を確認"],
            ["信号", "オーディエンス、検索テーマ、CV", "学習の方向を与える"],
            ["制約", "除外、ブランド、地域、予算", "暴走を防ぐ"],
            ["透明性", "検索語句、アセット、配信面", "結果を読む"],
        ],
        "deep2_title": "自動化するほど、何を人が決めるかを明確にする",
        "deep2_rows": [
            ["任せる", "入札調整、組み合わせ、配信面探索", "媒体AIの得意領域"],
            ["決める", "事業目標、予算上限、ブランド、除外", "人の責任領域"],
            ["見る", "CPA、CV品質、検索語句、素材疲労", "週次レビュー"],
            ["止める", "誤認表示、低品質流入、未承認素材", "即時停止条件"],
        ],
        "platform_rows": [
            ["Google P-MAX", "配信面横断の最適化", "素材・CV・オーディエンス信号"],
            ["AI Max for Search", "検索語句拡張と広告文/URL最適化", "ブランド/URL/除外コントロール"],
            ["Meta Advantage+", "配信・オーディエンス・クリエイティブ支援", "個人属性表現とブランド確認"],
            ["LINEヤフー", "スマートターゲティング・最適化提案", "国内媒体の審査と運用履歴"],
        ],
    },
    {
        "no": "04",
        "dir": "04-広告コピー-クリエイティブ制作と審査対応",
        "title": "広告コピー・クリエイティブ制作と審査対応",
        "short": "制作審査",
        "promise": "生成AIで広告案を増やし、誇大表現、個人属性、ブランド、権利、媒体審査の観点で採否判断する",
        "output": "広告コピー案比較表、クリエイティブレビュー表、審査リスク修正メモ",
        "case": "つばめ商店の新商品広告を、検索広告、Meta画像広告、LINE配信用に3案ずつ比較する",
        "main_tools": "ChatGPT, Claude, Canva, Adobe Express, Google Ads, Meta Ads, LINEヤフー広告",
        "chapter2": "広告コピー生成",
        "chapter3": "クリエイティブレビュー",
        "chapter4": "媒体審査と修正",
        "deep1_title": "広告コピーは売れる言葉より先に根拠と禁止表現を見る",
        "deep1_rows": [
            ["訴求", "誰に何を伝えるか", "一訴求に絞る"],
            ["根拠", "比較、No.1、効果、実績", "裏付け資料を確認"],
            ["個人属性", "あなたは太っている等の示唆", "Meta等で禁止リスク"],
            ["景表法", "優良誤認・有利誤認", "断定/過度な割引表現を確認"],
            ["LP整合", "広告文とLP内容", "媒体審査とユーザー信頼"],
        ],
        "deep2_title": "AI生成クリエイティブは3案比較で採用する",
        "deep2_rows": [
            ["A案", "問題提起型", "刺さるが個人属性表現に注意"],
            ["B案", "ベネフィット型", "無難だが差別化が弱い"],
            ["C案", "限定/期限型", "有利誤認と条件表示に注意"],
            ["採否", "採用/修正/不採用/法務確認", "履歴を残す"],
        ],
        "platform_rows": [
            ["検索広告", "見出し/説明文", "LPと検索意図の一致"],
            ["Meta広告", "画像/動画/本文", "個人属性とビフォーアフター表現"],
            ["LINEヤフー広告", "タイトル/説明文/画像", "審査落ち時の修正履歴"],
            ["Canva/Adobe Express", "量産とリサイズ", "素材権利とブランド基準"],
        ],
    },
    {
        "no": "05",
        "dir": "05-運用改善ループ-自動化-ガバナンス設計",
        "title": "運用改善ループ・自動化・ガバナンス設計",
        "short": "運用改善",
        "promise": "週次の改善会議、予算ペーシング、異常検知、AI提案の採否、承認ログを運用ルールにする",
        "output": "週次運用チェックリスト、AI改善提案採否表、広告運用ガバナンスルール",
        "case": "つばめ商店のCPA悪化、CV品質低下、素材疲労、審査落ちを週次で処理する",
        "main_tools": "Google Ads recommendations, Meta Ads reporting, Looker Studio, ChatGPT, Claude, Microsoft Advertising Copilot",
        "chapter2": "週次改善会議",
        "chapter3": "AI提案の採否",
        "chapter4": "権限と承認ログ",
        "deep1_title": "AI提案は採用する前に事業ルールでふるいにかける",
        "deep1_rows": [
            ["成果", "CPA、ROAS、CV品質", "数字だけで判断しない"],
            ["ブランド", "広告文・配信面・画像", "許容範囲を確認"],
            ["予算", "上限、日次消化、月末見込み", "急な増額を止める"],
            ["審査", "媒体ポリシー、景表法、個人情報", "公開前チェック"],
            ["履歴", "採用/保留/却下の理由", "翌月レビューに使う"],
        ],
        "deep2_title": "週次改善は異常検知、仮説、実験、承認の順に回す",
        "deep2_rows": [
            ["異常検知", "CPA急騰、CV急減、配信停止", "まず原因を分ける"],
            ["仮説", "検索語句、LP、素材、競合、季節性", "AIに候補を出させる"],
            ["実験", "広告文、入札、予算、LP", "1回に変える点を絞る"],
            ["承認", "予算/表現/個人情報", "担当と責任者を分ける"],
        ],
        "platform_rows": [
            ["Google最適化スコア", "改善提案の入口", "丸呑みせず採否理由を残す"],
            ["Metaレポート", "クリエイティブ疲労と配信傾向", "表示崩れと表現確認"],
            ["Looker Studio", "週次ダッシュボード", "数字の差異と更新日を記録"],
            ["AI補助", "異常要因の仮説出し", "顧客データは匿名化/最小化"],
        ],
    },
    {
        "no": "06",
        "dir": "06-広告運用改善提案書と90日展開計画",
        "title": "広告運用改善提案書と90日展開計画",
        "short": "提案計画",
        "promise": "6回分の成果物を束ね、予算、KPI、媒体AI活用、計測、制作、承認、90日計画を提案書にまとめる",
        "output": "広告運用改善提案書、90日展開ロードマップ、効果試算表",
        "case": "つばめ商店の広告運用を、手作業改善からAI活用型の継続運用へ移行する",
        "main_tools": "ChatGPT, Claude, Google Ads, Meta Ads, GA4, Looker Studio, Canva",
        "chapter2": "提案書構成",
        "chapter3": "効果試算",
        "chapter4": "90日展開",
        "deep1_title": "提案書はAI導入ではなく広告運用の改善計画として書く",
        "deep1_rows": [
            ["現状課題", "計測不足、制作手戻り、予算判断の属人化", "事実と仮説を分ける"],
            ["改善方針", "CV定義、媒体AI、広告制作、週次運用", "順番を示す"],
            ["体制", "担当、承認者、レビュー会議", "責任を曖昧にしない"],
            ["KPI", "CPA、ROAS、CV品質、工数", "演習上の試算と明示"],
            ["リスク", "個人情報、誤認表示、審査落ち", "対応策も書く"],
        ],
        "deep2_title": "90日計画は試行、展開、定着の3段階で作る",
        "deep2_rows": [
            ["1-30日", "計測診断と1媒体で試行", "小さく検証"],
            ["31-60日", "媒体AIと制作テンプレートを展開", "採否ルールを固定"],
            ["61-90日", "レポート自動化と週次会議", "運用として定着"],
            ["以降", "勝ちパターンの再利用", "KPIを見て改善"],
        ],
        "platform_rows": [
            ["提案資料", "Canva / Google Slides", "顧客情報や価格は入れない"],
            ["レポート", "GA4 / Looker Studio", "数値差異の注記を残す"],
            ["広告管理画面", "Google/Meta/LINEヤフー", "実アカウント画面は公開資料に入れない"],
            ["AI補助", "ChatGPT / Claude", "匿名化した要約と構成案に使う"],
        ],
    },
]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(text).strip() + "\n", encoding="utf-8")


def write_raw(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def write_csv(path: Path, rows: list[list[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f, lineterminator="\n").writerows(rows)


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(cell.replace("\n", "<br>") for cell in row) + " |")
    return "\n".join(lines)


def slide(no: int, title: str, headline: str, blocks: list[tuple[str, str]], pattern: str, screenshot: str = "なし") -> str:
    lines = [f"### S{no:02d} {title}", f"**ヘッドライン:** {headline}", ""]
    for i, (label, body) in enumerate(blocks, 1):
        lines.append(f"**内容ブロック{i}：{label}**")
        lines.append(body.strip())
        lines.append("")
    lines += [
        f"- **図解パターン:** {pattern}",
        f"- **テンプレートID:** {TEMPLATE_ID}",
        f"- **スクリーンショット:** {screenshot}",
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


def toc_rows() -> list[tuple[int, str]]:
    return [
        (1, "1 導入"),
        (2, "2 設計"),
        (3, "3 AI実践"),
        (4, "4 運用"),
        (5, "5 統制"),
        (6, "6 まとめ"),
    ]


def divider(no: int, idx: int, name: str, minutes: str, prev_name: str, next_name: str, exit_line: str) -> str:
    return slide(
        no,
        f"章見出し/現在位置 {idx}/6: {name}",
        f"ここから「{idx}. {name}」に入ります",
        [
            ("現在位置（特大表示）", f"- **{idx}. {name}**（{minutes}）"),
            ("前後のつながり", f"- 済: {prev_name or 'なし'} / 今: {idx}. {name} / 次: {next_name or 'まとめ'}"),
            ("この章の出口", f"- {exit_line}"),
        ],
        "chapter-divider-hero（章見出し/現在位置・特大表示）",
    )


def common_tool_note(session: dict[str, object]) -> str:
    return (
        f"- 使用候補: {session['main_tools']}\n"
        "- サービス名は目的とセットで扱い、提供状況、利用条件、料金、管理者設定は導入時に最新の公式情報を確認する\n"
        "- 実在ロゴや実在UIは、公式素材・規約確認済み素材またはダミー環境のスクリーンショットだけを使う"
    )


def session_time_allocation() -> list[tuple[str, str, str, str]]:
    return [
        ("導入と全体像", "15分", "S01-S07", "成果物、ケース、使う/使わない情報を確認する"),
        ("設計とデータ整理", "20分", "S08-S12", "広告目的、計測、媒体、制作入力を整理する"),
        ("AI実践とレビュー", "25分", "S13-S17", "AIの提案・生成・媒体機能を人が採否判断する"),
        ("運用・レポート・自動化", "30分", "S18-S23", "週次運用、レポート、予算/改善履歴へ広げる"),
        ("統制・審査・情報管理", "15分", "S24-S27", "広告審査、景表法、個人情報、承認を確認する"),
        ("演習レビューと次回接続", "15分", "S28-S30", "成果物を自己レビューし、次回または実務へ渡す"),
    ]


def session_data(session: dict[str, object]) -> list[tuple[str, list[list[str]]]]:
    no = str(session["no"])
    if no == "01":
        return [
            (
                "ad_operation_backlog.csv",
                [
                    ["task_id", "media", "task", "frequency", "current_minutes", "pain", "ai_candidate", "human_check"],
                    ["AD-001", "Google Ads", "検索語句確認", "週1回", "45", "除外判断が属人化", "検索語句を分類", "除外の妥当性"],
                    ["AD-002", "Meta Ads", "広告文案作成", "週2回", "60", "案出しに時間", "コピー3案生成", "個人属性表現"],
                    ["AD-003", "LINEヤフー", "予算消化確認", "週1回", "30", "月末に偏る", "ペーシング表作成", "増減額承認"],
                    ["AD-004", "GA4", "月次報告", "月1回", "180", "数字の転記が多い", "要約下書き", "差異と根拠"],
                ],
            ),
            (
                "kpi_tree_template.csv",
                [
                    ["level", "metric", "definition", "owner", "review_cycle"],
                    ["事業", "売上", "広告経由売上の演習上の試算", "責任者", "月次"],
                    ["広告", "CV", "購入または問い合わせ", "広告担当", "週次"],
                    ["効率", "CPA", "広告費/CV", "広告担当", "週次"],
                    ["品質", "CV品質", "キャンセル/低品質問い合わせを除く", "営業担当", "月次"],
                ],
            ),
        ]
    if no == "02":
        return [
            (
                "measurement_design.csv",
                [
                    ["event_name", "business_meaning", "tool", "use_for_bidding", "privacy_note"],
                    ["page_view_lp", "LP到達", "GA4", "いいえ", "個人情報なし"],
                    ["add_to_cart", "購入意向", "GA4", "補助指標", "Cookie同意を確認"],
                    ["purchase", "購入", "Google Ads/GA4", "はい", "拡張CVは社内承認後"],
                    ["lead_submit", "問い合わせ", "Google Ads/GA4", "はい", "顧客情報は最小化"],
                ],
            ),
            (
                "monthly_report_sample.csv",
                [
                    ["month", "media", "cost", "clicks", "conversions", "cpa", "note"],
                    ["2026-06", "Google Ads", "360000", "4200", "96", "3750", "演習用仮数値"],
                    ["2026-06", "Meta Ads", "180000", "5100", "42", "4286", "演習用仮数値"],
                    ["2026-06", "LINEヤフー", "60000", "1300", "12", "5000", "演習用仮数値"],
                ],
            ),
        ]
    if no == "03":
        return [
            (
                "media_ai_comparison.csv",
                [
                    ["feature", "media", "ai_role", "input_needed", "human_control"],
                    ["Performance Max", "Google Ads", "配信面/入札/素材組み合わせ", "CV、素材、オーディエンス信号", "除外、目標、予算"],
                    ["AI Max for Search", "Google Ads", "検索語句拡張、広告文/URL最適化", "LP、既存広告、キーワード", "ブランド/URL/生成素材の確認"],
                    ["Advantage+", "Meta Ads", "配信とクリエイティブ最適化", "広告素材、目的、イベント", "個人属性表現、ブランド"],
                    ["スマートターゲティング", "LINEヤフー広告", "ターゲティング範囲調整", "配信実績、予算、入札状況", "適用可否と除外"],
                ],
            ),
            (
                "campaign_design_memo.csv",
                [
                    ["campaign", "goal", "media", "budget_share", "control_point"],
                    ["春キャンペーン検索", "購入", "Google Search", "35%", "検索語句とLP整合"],
                    ["春キャンペーンP-MAX", "購入価値", "Google P-MAX", "35%", "素材と除外"],
                    ["Meta新規向け", "サイト流入", "Meta", "20%", "個人属性表現"],
                    ["LINE既存向け", "再訪", "LINEヤフー", "10%", "配信面と頻度"],
                ],
            ),
        ]
    if no == "04":
        return [
            (
                "ad_copy_variation_review.csv",
                [
                    ["variant_id", "channel", "appeal", "copy", "risk", "decision"],
                    ["A", "検索", "時短", "春の買い替えを手軽に準備", "低", "採用候補"],
                    ["B", "Meta", "悩み訴求", "忙しい毎日に役立つ新生活セット", "個人属性表現に注意", "修正"],
                    ["C", "LINE", "期限", "週末限定の案内を確認", "有利誤認に注意", "条件追記"],
                ],
            ),
            (
                "creative_policy_check.csv",
                [
                    ["check_id", "category", "question", "status"],
                    ["P-001", "景表法", "No.1、必ず、最安など根拠が必要な表現がないか", "未確認"],
                    ["P-002", "個人属性", "利用者の属性や悩みを断定していないか", "未確認"],
                    ["P-003", "LP整合", "広告文とLPの条件が一致しているか", "未確認"],
                    ["P-004", "権利", "画像に商標・人物・既存作品類似がないか", "未確認"],
                ],
            ),
        ]
    if no == "05":
        return [
            (
                "weekly_optimization_log.csv",
                [
                    ["week", "issue", "signal", "ai_suggestion", "human_decision", "reason"],
                    ["W1", "CPA急騰", "検索語句に広い流入", "除外候補を追加", "一部採用", "CV品質を確認後"],
                    ["W2", "Meta CTR低下", "同じ素材の表示増", "新素材3案を作成", "採用", "ブランド基準内"],
                    ["W3", "予算消化過多", "月末見込み超過", "日予算を抑制", "承認待ち", "責任者確認が必要"],
                ],
            ),
            (
                "ai_recommendation_decision.csv",
                [
                    ["recommendation_id", "source", "recommendation", "decision", "check"],
                    ["R-001", "Google", "予算増額", "保留", "CV品質と月間上限"],
                    ["R-002", "Meta", "Advantage+ creative適用", "テスト", "ブランドと表示崩れ"],
                    ["R-003", "AI要約", "検索語句を除外", "一部採用", "LPとの関連性"],
                ],
            ),
        ]
    return [
        (
            "proposal_kpi_estimate.csv",
            [
                ["kpi", "before", "after_example", "note"],
                ["月次報告作成時間", "180分", "75分", "演習上の試算"],
                ["週次改善会議準備", "90分", "40分", "演習上の試算"],
                ["CPA", "4,800円", "4,200円", "成果保証ではなく仮説"],
                ["審査差し戻し", "月4件", "月2件", "チェックリスト運用後の想定例"],
            ],
        ),
        (
            "ninety_day_roadmap.csv",
            [
                ["phase", "days", "action", "output"],
                ["試行", "1-30", "計測診断と1媒体でAI改善案を試す", "試行結果メモ"],
                ["展開", "31-60", "媒体AIと広告制作レビューを展開", "運用ルール"],
                ["定着", "61-90", "週次レポートと承認ログを定着", "改善提案書"],
            ],
        ),
    ]


def slides_for_session(session: dict[str, object]) -> list[str]:
    prev_next = [
        ("", "設計"),
        ("導入", "AI実践"),
        ("設計", "運用"),
        ("AI実践", "統制"),
        ("運用", "まとめ"),
        ("統制", ""),
    ]
    deep1_rows = session["deep1_rows"]
    deep2_rows = session["deep2_rows"]
    platform_rows = session["platform_rows"]
    return [
        slide(
            1,
            f"{session['title']} ─ 第{int(session['no'])}回",
            str(session["promise"]),
            [
                ("この回の到達点", f"- {session['promise']}\n- 成果物: {session['output']}"),
                ("扱う業務ケース", f"- {session['case']}\n- 実在企業ではなく、公開可能な架空ケースとして扱う"),
                ("今日の進め方", "- 講義 → 画面共有デモ → 動画一時停止ワーク → 講師記入例との自己レビューで進める"),
            ],
            "cover-title（表紙カード）",
        ),
        slide(
            2,
            "今日の2時間で作る成果物と受講準備",
            "成果物を先に決めると、媒体AIの操作が目的化せず広告改善に戻せる",
            [
                (
                    "成果物セット",
                    md_table(
                        ["成果物", "内容", "使い道"],
                        [[item, "演習用ケースで作成", "次回または最終提案の材料"] for item in str(session["output"]).split("、")],
                    ),
                ),
                ("受講前チェック", "- 配布ワークシートを開く\n- `演習データ/` のCSVとREADMEを確認する\n- 実アカウントではなくダミーデータで演習する"),
                ("安全な演習範囲", "- 顧客リスト、実広告アカウント、実売上、メールアドレス、電話番号、契約情報は使わない"),
            ],
            "card-trio-with-checklist",
        ),
        slide(
            3,
            f"第{int(session['no'])}回の目次/全体像",
            "6章を順番に進み、広告AIに任せる範囲と人が見る範囲を分けて運用できる形に整える",
            [
                (
                    "目次と成果物",
                    md_table(
                        ["No.", "目次項目", "時間", "スライド範囲", "支える成果物"],
                        [
                            ["1", "導入と全体像", "15分", "S01-S07", "今日の成果物と利用範囲"],
                            ["2", str(session["chapter2"]), "20分", "S08-S12", "入力情報・計測・媒体設計"],
                            ["3", str(session["chapter3"]), "25分", "S13-S17", "AI提案/生成とレビュー"],
                            ["4", str(session["chapter4"]), "30分", "S18-S23", "運用・レポート・改善履歴"],
                            ["5", "統制・審査・情報管理", "15分", "S24-S27", "公開前/運用前チェック"],
                            ["6", "演習レビューと次回接続", "15分", "S28-S30", "自己レビューと持ち帰り"],
                        ],
                    ),
                ),
                (
                    "デモ/ワーク位置",
                    md_table(
                        ["スライド", "行うこと"],
                        [
                            ["S11", "画面共有: サンプルデータとワークシート確認"],
                            ["S17", "ワーク1: AI活用/媒体機能の採否表を記入"],
                            ["S22", "画面共有: レポート/改善ログの見方を確認"],
                            ["S29", "ワーク2: 成果物を講師記入例と自己レビュー"],
                        ],
                    ),
                ),
            ],
            "roadmap-timeline（目次/全体像）",
        ),
        divider(4, 1, "導入と全体像", "15分", prev_next[0][0], prev_next[0][1], "今日の成果物・扱う媒体・使わない情報をそろえる"),
        slide(
            5,
            "AIは広告運用担当者の代替ではなく判断材料を増やす補助線",
            "AIで速くする対象を工程ごとに分けると、予算とブランドを守ったまま改善速度を上げられる",
            [
                (
                    "広告運用工程マップ",
                    md_table(
                        ["工程", "AIで短縮しやすいこと", "人が確認すること"],
                        [
                            ["課題整理", "数字の要約、論点抽出", "事業目標と優先度"],
                            ["計測", "不足イベントの洗い出し", "CV定義と同意"],
                            ["制作", "広告文/画像案の生成", "景表法、ブランド、LP整合"],
                            ["配信", "媒体AIの提案整理", "予算、除外、責任者承認"],
                            ["改善", "異常要因の仮説化", "採否理由と次アクション"],
                        ],
                    ),
                ),
                ("業務上の狙い", "- 広告成果だけでなく、レポート工数、判断の属人化、審査差し戻し、承認漏れを減らす"),
                ("注意", common_tool_note(session)),
            ],
            "process-flow",
        ),
        slide(
            6,
            "広告運用AIツールの役割分担",
            "ツール名ではなく、広告運用のどの詰まりを解消するかで使い分ける",
            [
                (
                    "目的別の使い分け",
                    md_table(
                        ["目的", "候補", "使いどころ"],
                        [
                            ["論点整理", "ChatGPT / Claude", "月次レポート、検索語句、審査理由の要約"],
                            ["媒体最適化", "Google Ads / Meta / LINEヤフー", "入札、配信面、ターゲティング、素材組み合わせ"],
                            ["計測", "GA4 / GTM / Looker Studio", "CV定義、UTM、ダッシュボード"],
                            ["制作", "Canva / Adobe Express", "広告画像、リサイズ、ブランドテンプレート"],
                            ["連携候補", "Google Ads API / Microsoft Advertising MCP等", "提供・権限・読み取り範囲を公式確認"],
                        ],
                    ),
                ),
                ("判断基準", "- 効率、精度、権限、ブランド、審査、説明責任の6点で選ぶ"),
                ("公式確認", "- AI機能、ベータ、料金、管理者設定、データ利用条件は変わるため導入時に確認する"),
            ],
            "matrix-classification",
        ),
        slide(
            7,
            "つばめ商店ケース: 広告運用を数値と業務で見える化する",
            "架空ケースに予算・CV・作業時間を置くと、AI活用が抽象論ではなく改善対象として議論できる",
            [
                (
                    "演習上の現状",
                    md_table(
                        ["項目", "仮数値", "困りごと"],
                        [
                            ["月間広告予算", "60万円", "媒体別の配分理由が残らない"],
                            ["月間CV", "150件", "CV品質の良し悪しが見えない"],
                            ["月次報告作成", "180分", "数字転記と要約に時間"],
                            ["広告文作成", "週2回60分", "案出しと審査対応が属人化"],
                            ["週次改善", "90分", "AI提案の採否理由が残らない"],
                        ],
                    ),
                ),
                ("演習上の前提", "- 実在顧客や実広告アカウントは使わない\n- 予算、CPA、削減時間は演習上の仮数値であり成果保証ではない"),
            ],
            "data-insight",
        ),
        divider(8, 2, str(session["chapter2"]), "20分", prev_next[1][0], prev_next[1][1], "AIに渡す前の目的・データ・媒体条件を整理する"),
        slide(
            9,
            str(session["deep1_title"]),
            "広告AIの前処理を構造化すると、任せる範囲と人が判断する範囲が分かれる",
            [
                ("業務分解", md_table(["区分", "広告運用での例", "AI活用/確認"], deep1_rows)),  # type: ignore[arg-type]
                ("成果物との接続", f"- この整理が `{session['output']}` の入力になる"),
            ],
            "structure-layer",
        ),
        slide(
            10,
            str(session["deep2_title"]),
            "数字・媒体・制作・承認を同じ表で見ると、改善判断が感覚論から業務判断へ変わる",
            [
                ("判断表", md_table(["観点", "広告運用で見るもの", "確認ポイント"], deep2_rows)),  # type: ignore[arg-type]
                ("AIに渡す情報", "- 数値はダミー化または集計化し、実顧客情報や未公開営業情報は入れない"),
                ("禁止", "- 顧客リスト、メールアドレス、電話番号、契約条件、実売上の原本は公開AIに入力しない"),
            ],
            "governance-risk",
        ),
        slide(
            11,
            "画面共有: サンプルデータとワークシートを確認する",
            "AIを動かす前に、どの情報を見せ、どの情報を見せないかを画面で確認する",
            [
                ("見せるもの", "- `演習データ/` のCSV\n- 配布資料の講師記入例\n- KPI/媒体/計測/レビューの入力欄"),
                ("見せないもの", "- 実広告アカウント\n- 実顧客リスト\n- 実売上の原本\n- APIキーや請求画面"),
                ("見せるポイント", "- AI活用の前処理は、媒体画面を開くことではなく、目的、計測、制約、人の承認点をそろえること"),
            ],
            "screen-share-transition",
        ),
        slide(
            12,
            "ワーク1: AIに渡す前の入力情報を整理する",
            "動画を止めて入力情報を整理すると、広告AIの提案を業務判断で扱いやすくなる",
            [
                ("動画一時停止ワーク", "- ここで動画を一時停止して、8分ほど取り組んでください。取り組めたら再生してください。"),
                (
                    "記入欄",
                    md_table(
                        ["欄", "記入すること"],
                        [
                            ["目的", "認知、集客、獲得、継続のどれか"],
                            ["KPI", "CV、CPA、ROAS、CV品質など"],
                            ["媒体", "Google、Meta、LINEヤフーなど"],
                            ["制約", "予算上限、除外、ブランド、審査"],
                            ["確認者", "広告担当、責任者、法務/広報など"],
                        ],
                    ),
                ),
                ("自己チェック", "- 目的、KPI、媒体、制約、確認者が1枚で分かるか"),
            ],
            "exercise-workflow",
        ),
        divider(13, 3, str(session["chapter3"]), "25分", prev_next[2][0], prev_next[2][1], "AI提案・広告文・媒体機能を比較し、採用判断まで行う"),
        slide(
            14,
            "良いAI依頼は広告ブリーフの圧縮版",
            "雰囲気ではなく目的・KPI・媒体・制約・確認基準を入れると、業務で使える下書きに近づく",
            [
                (
                    "AI依頼の要素",
                    md_table(
                        ["要素", "入れる内容", "例"],
                        [
                            ["目的", "達成したい成果", "購入CVを増やす"],
                            ["対象", "誰に届けるか", "新生活用品を検討する既存/新規層"],
                            ["媒体", "検索、P-MAX、Meta、LINE", "媒体別に表現を分ける"],
                            ["制約", "予算、禁止表現、除外、LP", "No.1表現禁止、ブランド名除外"],
                            ["出力", "案数、比較軸、採否欄", "3案、CPA/審査/ブランドで比較"],
                        ],
                    ),
                ),
                ("悪い依頼", "- 効果の出る広告文を作って\n- 予算を最適化して\n- いい感じに改善して"),
                ("良い依頼", "- 目的、媒体、KPI、素材、禁止事項、レビュー基準を入れる"),
            ],
            "checklist-confirmation",
        ),
        slide(
            15,
            "媒体AI機能は目的とコントロールで選ぶ",
            "同じ自動化でも、配信面探索、検索語句拡張、クリエイティブ最適化、レポート補助で人の見る点が違う",
            [("媒体別AI機能", md_table(["媒体/機能", "AIの役割", "人が見ること"], platform_rows)), ("導入時の注意", "- ベータ機能、利用条件、管理者設定、配信面、生成素材の扱いは公式情報で確認する")],  # type: ignore[arg-type]
            "matrix-classification",
        ),
        slide(
            16,
            "AI提案は採用/修正/保留/却下で履歴に残す",
            "1案だけで判断せず、成果・ブランド・審査・予算・データ品質で比較する",
            [
                (
                    "レビュー表",
                    md_table(
                        ["評価軸", "確認内容", "判定例"],
                        [
                            ["成果", "CPA、CV品質、ROAS", "CPAは改善、CV品質は要確認"],
                            ["ブランド", "広告文、画像、配信面", "ブランド語調から外れる"],
                            ["審査/法務", "景表法、個人属性、誤認表示", "根拠がないNo.1表現"],
                            ["予算", "月額上限、日次消化", "上限超過のため保留"],
                            ["データ", "CV定義、計測抜け", "学習前に計測修正"],
                        ],
                    ),
                ),
                ("採用判断", "- 採用、修正して採用、保留、却下、責任者確認の5区分で残す"),
            ],
            "comparison-contrast",
        ),
        slide(
            17,
            "ワーク2: AI提案の採否表を作る",
            "作る指示と見る基準を同じ表に置くと、媒体AIを感覚ではなく業務ルールで扱える",
            [
                ("動画一時停止ワーク", "- ここで動画を一時停止して、10分ほど取り組んでください。取り組めたら再生してください。"),
                (
                    "作成するもの",
                    md_table(
                        ["作る欄", "内容"],
                        [
                            ["AI/媒体提案", "何を変える提案か"],
                            ["期待効果", "どのKPIに効く想定か"],
                            ["リスク", "審査、ブランド、予算、個人情報"],
                            ["採否", "採用/修正/保留/却下/確認"],
                        ],
                    ),
                ),
                ("自己レビュー", "- AI提案を自動適用する前提になっていないか\n- 採否理由と確認者があるか"),
            ],
            "exercise-workflow",
        ),
        divider(18, 4, str(session["chapter4"]), "30分", prev_next[3][0], prev_next[3][1], "広告改善を一回の操作ではなく週次運用へ広げる"),
        slide(
            19,
            "週次運用は見る順番を固定すると速くなる",
            "毎回ゼロから考えるのではなく、異常、原因、打ち手、承認、結果の順に見る",
            [
                (
                    "週次チェック",
                    md_table(
                        ["順番", "見るもの", "判断"],
                        [
                            ["1 異常", "CPA急騰、CV急減、消化過多", "止める/深掘り"],
                            ["2 原因", "媒体、検索語句、素材、LP", "仮説を書く"],
                            ["3 打ち手", "除外、広告文、予算、LP", "1回に変える点を絞る"],
                            ["4 承認", "予算、表現、個人情報", "責任者確認"],
                            ["5 結果", "翌週のKPI", "履歴へ残す"],
                        ],
                    ),
                ),
                ("使う候補", "- Looker Studio、Google Ads recommendations、Metaレポート、ChatGPT/Claude要約"),
            ],
            "continuous-operation-loop",
        ),
        slide(
            20,
            "レポートは次の打ち手を決める形式にする",
            "数字、原因仮説、次アクション、確認者を同じ表にすると月次報告が改善会議に変わる",
            [
                (
                    "月次報告フォーマット",
                    md_table(
                        ["欄", "書くこと", "AI補助"],
                        [
                            ["数字", "費用、CV、CPA、ROAS", "差分要約"],
                            ["仮説", "検索語句、素材、LP、季節性", "原因候補"],
                            ["打ち手", "予算、広告文、媒体、LP", "選択肢整理"],
                            ["リスク", "審査、個人情報、誤認表示", "チェックリスト"],
                            ["承認", "担当、期限、次回確認", "議事メモ"],
                        ],
                    ),
                ),
                ("注意", "- AI要約へ実顧客名や実アカウントIDを貼らない。必要なら集計値と匿名化したメモにする"),
            ],
            "data-insight",
        ),
        slide(
            21,
            "自動化候補は読み取り、下書き、承認実行に分ける",
            "広告運用では、AIが読む、AIが下書きする、人が承認して実行する、の線引きが重要",
            [
                (
                    "自動化レベル",
                    md_table(
                        ["レベル", "内容", "例"],
                        [
                            ["読み取り", "レポートや検索語句を要約", "Looker Studioの月次要約"],
                            ["下書き", "広告文、改善案、会議メモ", "Claudeで改善案3つ"],
                            ["承認待ち", "予算変更や除外候補", "担当者が採否入力"],
                            ["実行", "媒体画面で設定変更", "権限とログが必要"],
                        ],
                    ),
                ),
                ("MCP/API候補", "- Google Ads API、Microsoft Advertising MCP、広告レポート連携などは提供状況、権限、読み取り範囲、ログを公式確認してから扱う"),
            ],
            "structure-layer",
        ),
        slide(
            22,
            "画面共有: レポートと改善ログの見方",
            "媒体画面の細かい操作ではなく、数字から判断と履歴へ落とす流れを確認する",
            [
                ("見せるもの", "- 月次レポートCSV\n- KPIツリー\n- 改善ログ\n- AI提案採否表"),
                ("見るポイント", "- どの数字が悪化したか\n- 原因仮説はデータで説明できるか\n- 誰が承認する変更か"),
                ("代替手順", "- 実媒体画面が使えない場合は、配布CSVとワークシートだけで運用設計を行う"),
            ],
            "screen-share-transition",
        ),
        slide(
            23,
            "ワーク3: 週次改善ログを作る",
            "改善案を履歴に残すと、翌月の説明と引き継ぎができる",
            [
                ("動画一時停止ワーク", "- ここで動画を一時停止して、10分ほど取り組んでください。取り組めたら再生してください。"),
                (
                    "記入する表",
                    md_table(
                        ["欄", "記入例"],
                        [
                            ["異常", "CPAが前週比20%悪化"],
                            ["仮説", "検索語句が広がりすぎた"],
                            ["打ち手", "除外候補を3件追加"],
                            ["リスク", "CV数が減る可能性"],
                            ["承認", "広告責任者確認後に実施"],
                        ],
                    ),
                ),
                ("自己レビュー", "- 数字、仮説、打ち手、承認者がそろっているか"),
            ],
            "exercise-workflow",
        ),
        divider(24, 5, "統制・審査・情報管理", "15分", prev_next[4][0], prev_next[4][1], "速く改善するほど増える広告表示とデータ利用のリスクを止める"),
        slide(
            25,
            "広告AIの公開前チェックは6つに分ける",
            "個人情報・誤認表示・個人属性・ブランド・LP整合・承認を分けると、審査と炎上リスクを下げられる",
            [
                (
                    "6つのチェック",
                    md_table(
                        ["観点", "確認すること", "止める例"],
                        [
                            ["個人情報", "顧客リスト、メール、電話、実購買履歴", "生成AIへ原本貼付"],
                            ["誤認表示", "効果、No.1、割引条件", "根拠のない断定"],
                            ["個人属性", "あなたは悩んでいる等の断定", "Meta等で審査リスク"],
                            ["ブランド", "語調、配信面、画像", "ブランドを損なう訴求"],
                            ["LP整合", "広告文とLP条件", "条件が違う"],
                            ["承認", "誰が確認したか", "ログなし公開"],
                        ],
                    ),
                ),
                ("公式情報", "- 媒体ポリシー、景品表示法、個人情報保護委員会の注意喚起は導入時に最新確認する"),
            ],
            "governance-risk",
        ),
        slide(
            26,
            "広告審査の差し戻しは学習資産にする",
            "審査落ちを単発対応で終わらせず、理由、修正、再発防止をテンプレートへ戻す",
            [
                (
                    "差し戻しログ",
                    md_table(
                        ["欄", "書くこと", "次に使う場所"],
                        [
                            ["媒体", "Google/Meta/LINEヤフー", "媒体別ルール"],
                            ["理由", "誤認表示、個人属性、LP不一致", "チェックリスト"],
                            ["修正", "文言削除、条件追記、画像差し替え", "プロンプト"],
                            ["承認", "確認者、日付、結果", "運用ログ"],
                        ],
                    ),
                ),
                ("運用", "- 審査落ちの理由をAIに要約させる場合も、アカウントIDや顧客情報を入れず抽象化する"),
            ],
            "checklist-confirmation",
        ),
        slide(
            27,
            "効果はCPAだけで測らない",
            "広告AIの効率化は、成果指標、作業時間、審査品質、説明責任を合わせて判断する",
            [
                (
                    "KPI例",
                    md_table(
                        ["KPI", "演習上の測り方", "注意"],
                        [
                            ["CPA/ROAS", "媒体別・全体で確認", "成果保証ではなく仮説検証"],
                            ["CV品質", "キャンセル/低品質問い合わせを除く", "営業側と定義"],
                            ["レポート工数", "180分→75分の想定例", "数字確認は残す"],
                            ["審査差し戻し", "月4件→月2件の想定例", "品質KPIとして扱う"],
                            ["採否履歴率", "AI提案に理由が残る割合", "説明責任に使う"],
                        ],
                    ),
                ),
                ("AI導入時の注意", "- 速さだけを追うと誤認表示、個人情報、ブランド確認が抜ける。KPIに品質確認を入れる"),
            ],
            "data-insight",
        ),
        divider(28, 6, "演習レビューと次回接続", "15分", prev_next[5][0], prev_next[5][1], "成果物を確認し、次回または実務に渡せる状態にする"),
        slide(
            29,
            "講師記入例と比べて自己レビューする",
            "自分の成果物を講師例と比べると、足りない計測、制約、確認者が見つかる",
            [
                ("動画一時停止ワーク", "- ここで動画を一時停止して、7分ほど取り組んでください。取り組めたら再生してください。"),
                (
                    "自己レビュー表",
                    md_table(
                        ["確認", "見るポイント"],
                        [
                            ["目的", "誰に何をしてほしい広告か明確か"],
                            ["計測", "CV定義、UTM、レポートがつながっているか"],
                            ["AI活用", "任せる範囲と人の確認が分かれているか"],
                            ["リスク", "誤認表示、個人属性、個人情報、ブランドを見たか"],
                            ["運用", "担当者、承認者、次アクションがあるか"],
                        ],
                    ),
                ),
            ],
            "checklist-confirmation",
        ),
        slide(
            30,
            f"第{int(session['no'])}回まとめと次回への受け渡し",
            f"{session['short']}の成果物を、次の広告改善工程または最終提案へつなげる",
            [
                (
                    "今日の成果物チェック",
                    md_table(
                        ["成果物", "確認"],
                        [[item, "未記入欄、実データ混入、確認者、採否理由をチェック"] for item in str(session["output"]).split("、")],
                    ),
                ),
                ("次回/実務への接続", "- 今日作った成果物は、次回の入力資料または第6回の広告運用改善提案書に入れる"),
                ("注意", "- 広告媒体のAI機能、広告ポリシー、計測仕様、利用条件は変わるため、実導入前に公式情報を確認する"),
            ],
            "summary-bridge",
        ),
    ]


def build_slide_plan_markdown(session: dict[str, object]) -> str:
    allocation = "\n".join(f"| {a} | {b} | {c} | {d} |" for a, b, c, d in session_time_allocation())
    toc = "\n".join(f"| {no} | {name} |" for no, name in toc_rows())
    slides = "\n".join(slides_for_session(session)).rstrip()
    return f"""# 第{int(session['no'])}回 スライド構成案: {session['title']}

対象講座: {COURSE_NAME}
スライド枚数: 30枚 / 120分
テンプレートID: {TEMPLATE_ID}（全スライド共通）
レイアウト標準: 1枚まるごとラスター画像＋固定レイアウトワイヤーフレーム参照（`skills/corporate-training-course-builder/references/assets/講座スライドレイアウトワイヤフレーム.png`）

---

## 設計方針

- 120分の録画eラーニングとして、講義、画面共有、個人ワーク、講師記入例との自己レビューを組み合わせる。
- 採用テンプレート: `{TEMPLATE_ID}`。
- この回の業務遂行力: {session['promise']}。
- 成果物: {session['output']}。
- 広告運用固有の目的設計、CV計測、媒体AI機能、広告コピー/クリエイティブ、審査・景表法・個人情報、予算/改善履歴を扱い、汎用DX講座の言い換えで終わらせない。
- 実在の社名、顧客名、個人情報、連絡先、社内未公開資料、広告アカウントID、請求情報、APIキーは使わない。
- 予算、CPA、削減時間は演習用の仮数値として扱い、成果保証として書かない。
- サービス名は目的とセットで扱い、提供状況、利用条件、料金、管理者設定は導入時に最新公式情報を確認する。
- 録画動画形式のため、集合研修の待ち時間表現は使わず「動画を一時停止して〜分ほど取り組んでください」を使う。
- 章見出し/現在位置スライドは現在章の番号・章名を特大で見せるヒーロー型にし、詳細な論点は次の通常スライドで扱う。

---

## 目次ストリップ表示名

| 章 | 表示名 |
|---:|---|
{toc}

---

## 120分の時間配分

| ブロック | 時間 | スライド範囲 | ねらい |
|---|---:|---|---|
{allocation}

---

## スライド詳細

---

{slides}
"""


def worksheet(session: dict[str, object]) -> str:
    return f"""# 第{int(session['no'])}回 ワークシート: {session['title']}

対象講座: {COURSE_NAME}

## この回で作る成果物

{session['output']}

## ワーク1: 広告運用の入力情報整理

| 項目 | 記入欄 |
| --- | --- |
| 広告目的 |  |
| 対象者 |  |
| 媒体 |  |
| KPI/CV定義 |  |
| 使うデータ |  |
| 使わないデータ |  |
| 予算・制約 |  |
| 確認者 |  |

## ワーク2: AI/媒体提案の採否判断

| 要素 | 記入欄 |
| --- | --- |
| 提案内容 |  |
| 期待するKPI変化 |  |
| 審査・景表法リスク |  |
| 個人情報・顧客データリスク |  |
| ブランド/LP整合 |  |
| 採否 |  |
| 採否理由 |  |

## ワーク3: 運用ログと次アクション

| 観点 | チェック | メモ |
| --- | --- | --- |
| 数字 | CV、CPA、ROAS、CV品質を見た |  |
| 仮説 | 悪化/改善の原因を分けた |  |
| 打ち手 | 1回で変える点を絞った |  |
| 承認 | 予算/表現/個人情報の確認者がいる |  |
| 履歴 | 採否理由と次回確認日を残した |  |

## 講師記入例と比べる自己レビュー

- 目的、KPI、媒体、制約が1文で説明できるか。
- AIに渡す情報と渡さない情報を分けられているか。
- 成果物が次回または第6回の広告運用改善提案書に使える形になっているか。
"""


def provisional_script(session: dict[str, object]) -> str:
    lines = [
        f"# 第{int(session['no'])}回 講師台本（暫定）: {session['title']}",
        "",
        "> 注意: この台本はスライド画像生成前の暫定版です。`スライド画像/Sxx.png` が揃った後、各スライドの実際の配置を見て、右側・左側・下部帯などの位置参照を確定してください。",
        "",
        "## 事前準備",
        "",
        "- 配布ワークシートを開く。",
        "- `演習データ/README.md` とCSVを開ける状態にする。",
        "- 実広告アカウント、顧客リスト、請求画面、APIキー、実売上の原本を画面に出さない。",
        "",
    ]
    demo_count = 0
    for block in slides_for_session(session):
        title_line = next(line for line in block.splitlines() if line.startswith("### S"))
        slide_id, title = title_line.split(" ", 2)[1:3]
        headline_line = next(line for line in block.splitlines() if line.startswith("**ヘッドライン:**"))
        headline = headline_line.replace("**ヘッドライン:**", "").strip()
        lines += [
            "スライド切替:",
            f'{slide_id}「{title}」',
            "",
            "読み上げ:",
            f"「このスライドでは、{headline}という考え方を確認します。広告AIを便利なボタンとして見るのではなく、目的、計測、媒体、制作、審査、承認がつながった業務として扱ってください。」",
            "",
        ]
        if "画面共有" in title:
            demo_count += 1
            lines += [
                f"画面共有 ── 実演{demo_count}「{title.replace('画面共有: ', '')}」",
                "⏱ 約4分",
                "",
                "【手順1 – 約1分】",
                "`演習データ/` のREADMEを開き、この回で使うダミーデータだけを確認します。実データを使わない理由も一言添えます。",
                "",
                "【手順2 – 約2分】",
                "ワークシートまたはCSVの列を見せ、AIへ渡す情報、渡さない情報、人が確認する情報を分けて説明します。",
                "",
                "【手順3 – 約1分】",
                "講師記入例を見せ、このあとのワークでどの粒度まで書けばよいかを示します。",
                "",
                "【見せるポイント】",
                "広告媒体の操作そのものよりも、目的、計測、制約、確認者が整っていることがAI活用の前提だと伝えます。",
                "",
            ]
        if "ワーク" in title:
            lines += [
                "ワーク指示:",
                "「ここで動画を一時停止して、画面の表に沿ってワークシートへ記入してください。取り組めたら再生してください。実在の顧客名、社員名、連絡先、実広告アカウント情報、未公開の売上情報は書かず、ダミーの言葉や集計値に置き換えてください。」",
                "",
            ]
        lines += [
            "講師メモ:",
            "（読み上げない。スライド画像生成後、実際の配置に合わせて位置参照と読み上げの長さを調整する。）",
            "",
        ]
    lines += [
        "## スライド切替タイムライン",
        "",
        "| 範囲 | 目安 | 内容 |",
        "| --- | ---: | --- |",
        "| S01-S07 | 15分 | 導入と全体像 |",
        "| S08-S12 | 20分 | 設計とデータ整理 |",
        "| S13-S17 | 25分 | AI実践とレビュー |",
        "| S18-S23 | 30分 | 運用・レポート・自動化 |",
        "| S24-S27 | 15分 | 統制・審査・情報管理 |",
        "| S28-S30 | 15分 | 演習レビューと次回接続 |",
        "",
        "## 作業風景タイムライン",
        "",
        "| 番号 | タイトル | ⏱ 時間 | 操作概要 |",
        "| ---: | --- | ---: | --- |",
        "| 1 | サンプルデータとワークシート確認 | 約4分 | README、CSV、ワークシート、講師記入例を確認 |",
        "| 2 | レポートと改善ログ確認 | 約4分 | 月次レポート、KPI、改善ログ、採否表を確認 |",
    ]
    return "\n".join(lines).rstrip() + "\n"


def readme_for_data(session: dict[str, object]) -> str:
    return f"""# 第{int(session['no'])}回 演習データ

このフォルダのCSVはすべて架空データです。実在の顧客名、社員名、メールアドレス、電話番号、住所、広告アカウントID、APIキー、請求情報、契約条件、未公開売上情報は含めていません。

## この回の成果物

{session['output']}

## データの使い方

- ワークシートの入力例として使います。
- 広告媒体、GA4、Looker Studio、生成AIサービスへ投入する場合は、導入時の利用規約、管理者設定、データ利用条件、個人情報の扱いを確認してください。
- 講座内では、実アカウント画面や実在顧客データを公開資料に保存しません。
"""


def course_overview() -> str:
    rows = [[str(int(s["no"])), str(s["title"]), "120分", str(s["promise"]), str(s["output"])] for s in SESSIONS]
    return f"""# 講座概要

## タイトルと一言訴求

{COURSE_NAME}。

広告運用を、媒体の自動化機能に任せるだけで終わらせず、目的設計、計測、広告制作、媒体AI機能、週次改善、審査・表示リスク、承認ログ、改善提案までを一連の広告運用DXとして扱う実践講座。

## 研修の目的

中小企業や事業部門で発生しやすい、Google広告、Meta広告、LINEヤフー広告、GA4、Looker Studioを題材に、生成AIと媒体AI機能を使って広告運用を効率化しつつ、計測品質、広告審査、景品表示法、個人情報、ブランド確認、承認ログまで運用できる人材を育成する。

本講座は「広告媒体の操作講座」ではない。広告目的の整理、KPI/CV定義、AI機能の採否、広告コピー/クリエイティブレビュー、週次改善ログ、月次レポート、90日展開計画までを扱う。

## 本講座の独自性

- 広告運用を、目的、計測、制作、配信、改善、承認の業務フローとして分解する。
- Google Ads、Meta Ads、LINEヤフー広告、Microsoft Advertising等のAI機能を、目的と人の確認点に紐づけて扱う。
- AI生成コピーや媒体最適化提案をそのまま採用せず、成果、審査、景表法、個人情報、ブランド、予算でレビューする。
- 月次レポートの自動化だけでなく、週次改善ログ、採否履歴、承認フローまで扱う。
- 最終成果物は、広告運用改善提案書と90日展開ロードマップにまとめ、部署導入へ接続する。

## よくある悩み、導入背景

- 広告媒体のAI推奨をどこまで採用してよいか分からない。
- CV定義やUTMが曖昧で、AI入札やレポートの判断材料が弱い。
- 広告文や画像の案出しに時間がかかる一方で、景表法、個人属性、ブランド確認が後回しになる。
- 月次レポートが数字の転記で終わり、次の改善判断や承認履歴に残らない。
- 広告アカウント、顧客リスト、売上データを生成AIへどう扱うべきか不安がある。

## この研修で解決すること

- 広告運用を入力、処理、出力、確認、運用に分け、AI活用候補を選定できる。
- CV定義、UTM、GA4、広告媒体レポートを見直し、AIが学習できる計測基盤を整理できる。
- Performance Max、AI Max、Advantage+、スマートターゲティング等を、目的と制約に合わせて採否判断できる。
- AI生成広告文・クリエイティブを、景表法、個人属性、LP整合、ブランド、権利でレビューできる。
- 週次改善ログ、月次報告、AI提案採否表、承認フローを運用へ組み込める。
- 広告運用改善提案書として、KPI、効果試算、90日ロードマップ、リスク対策をまとめられる。

## 対象者、推奨される知識・経験

- 広告運用、マーケティング、EC運用、広報、営業企画、事業推進を担当する方。
- 広告代理店任せにせず、自社側で広告運用の判断材料を理解したい方。
- Google Ads、Meta Ads、LINEヤフー広告、GA4、Looker Studio等を使う、またはレポートを読む立場の方。
- 前提知識として、一般的なPC操作、ブラウザ利用、表計算ソフトの基本操作ができること。高度な広告運用経験やプログラミング経験は必須ではない。

## 提供方式、学習時間、受講管理

- 提供方式: {LMS_TEXT}
- 標準学習時間: 6回、各120分、合計約12時間。
- 受講管理: LMSによる受講状況、受講時間、課題提出、修了確認の記録を前提にする。
- 演習環境: ダミー広告データ、架空の月次レポート、媒体AI機能比較表、ワークシートを使う。
- 実サービスの利用: 広告媒体やAIサービスの画面・機能は利用環境により異なるため、必須演習はワークシートとサンプルデータだけでも成立する設計にする。

## カリキュラム表

{md_table(["回", "テーマ", "時間", "主な内容", "成果物"], rows)}

## 演習、成果物、業務への持ち帰り

- 第1回で広告運用を棚卸しし、KPIツリーとAI活用候補を作る。
- 第2回でCV定義、UTM、月次レポートの診断表を作る。
- 第3回で媒体AI機能を比較し、キャンペーン設計と採否判断チェックリストを作る。
- 第4回で広告コピー/クリエイティブ案を比較し、審査リスク修正メモを作る。
- 第5回で週次改善ログ、AI改善提案採否表、ガバナンスルールを作る。
- 第6回でKPI、効果試算、90日ロードマップを含む広告運用改善提案書にまとめる。

## 注意事項

- 生成AI出力と媒体AI提案は下書き扱いとし、公開前に人が審査、景表法、個人情報、ブランド、LP整合、承認を確認する。
- 顧客リスト、実広告アカウントID、請求情報、APIキー、未公開売上、契約条件、社員/顧客情報は公開AIに入力しない。
- AIツールや広告媒体の提供状況、利用条件、料金、管理者設定、広告ポリシー、計測仕様は変わり得るため、導入時に最新の公式情報を確認する。
- 参照素材なしに実在ロゴや実在UIを画像生成AIへ描かせない。
"""


def detailed_syllabus() -> str:
    lines = [f"# 詳細シラバス\n\n対象講座: {COURSE_NAME}\n"]
    for session in SESSIONS:
        lines += [
            f"## 第{int(session['no'])}回: {session['title']}",
            "",
            f"- 到達点: {session['promise']}",
            f"- 成果物: {session['output']}",
            f"- テーマ固有演習: {session['case']}",
            "",
            md_table(
                ["大項目", "小項目", "時間"],
                [
                    ["導入と全体像", "成果物、演習データ、利用ツール、情報管理の前提", "15分"],
                    ["設計とデータ整理", f"{session['chapter2']}、入力情報、媒体条件", "20分"],
                    ["AI実践とレビュー", f"{session['chapter3']}、採否表、レビュー基準", "25分"],
                    ["運用・レポート・自動化", f"{session['chapter4']}、改善ログ、承認履歴", "30分"],
                    ["統制・審査・情報管理", "景表法、広告ポリシー、個人情報、ブランド、LP整合", "15分"],
                    ["演習レビューと次回接続", "講師記入例との自己レビュー、次回または提案書への受け渡し", "15分"],
                ],
            ),
            "",
        ]
    return "\n".join(lines)


def source_memo() -> str:
    return f"""# 差別化・公式情報メモ

確認日: {ACCESS_DATE}
対象講座: {COURSE_NAME}

## 差別化判断

この講座は、広告媒体の操作や生成AIで広告文を作るだけの講座にしない。公開講座では、Google Ads、Meta Ads、GA4、広告コピー、クリエイティブ制作を扱うものが多い。一方、法人研修では、CV定義、広告AI機能の採否、広告審査、景品表示法、個人情報、予算承認、週次改善ログ、月次報告、90日展開計画まで扱う必要がある。

そのため、本講座の署名演習は「つばめ商店の広告運用を、KPI/CV設計、媒体AI機能の採否、広告コピー審査、週次改善ログ、広告運用改善提案書へつなげる」ことにする。これは既存のGAS講座やデザイン講座の言い換えではなく、広告運用固有の計測、媒体AI、審査、予算、改善履歴を中心にした構成である。

## 公式・公開情報から講座へ反映した点

{md_table(["確認元", "URL", "講座への反映"], [[name, url, memo] for name, url, memo in SOURCES])}

## 公開資料への反映ルール

- サービス名は目的とセットで書く。
- 提供状況、利用条件、料金、管理者設定、広告ポリシー、ベータ機能、計測仕様は変わり得るため、講座中に固定的に断定しない。
- 広告予算、CPA、ROAS、削減時間は演習上の仮数値として扱い、成果保証として書かない。
- 実在ロゴや実在UIは、公式素材・ダミー環境・規約確認済み素材がある場合だけ使う。
- 実広告アカウント、顧客リスト、売上原本、請求情報、APIキー、契約条件、連絡先、営業情報は public repo に保存しない。
"""


def pamphlet_html() -> str:
    curriculum_rows = "\n".join(
        f"<tr><td>{int(s['no'])}</td><td>{s['title']}</td><td>120分</td><td>{s['promise']}</td><td>{s['output']}</td></tr>"
        for s in SESSIONS
    )
    return f"""<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>{COURSE_NAME}_パンフレット</title>
  <style>
    @page {{ size: A4; margin: 14mm; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Yu Gothic", sans-serif; color: #102033; line-height: 1.68; margin: 0; }}
    .hero {{ border: 2px solid #0f766e; padding: 22px; background: #f8fbfd; margin-bottom: 18px; }}
    .hero-image {{ width: 100%; display: block; margin: 0 0 14px; border: 1px solid #cbd5e1; }}
    h1 {{ font-size: 27px; line-height: 1.25; margin: 0 0 10px; color: #0f2a44; }}
    h2 {{ font-size: 18px; margin: 24px 0 8px; padding-bottom: 4px; border-bottom: 2px solid #0f766e; color: #0f2a44; }}
    p {{ margin: 0 0 8px; }}
    ul {{ margin: 6px 0 10px 1.2em; padding: 0; }}
    table {{ width: 100%; border-collapse: collapse; margin: 8px 0 14px; font-size: 10.5px; }}
    th, td {{ border: 1px solid #cbd5e1; padding: 6px 7px; vertical-align: top; }}
    th {{ background: #e6f4f3; color: #0f2a44; }}
    .cards {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; }}
    .card {{ border: 1px solid #cbd5e1; padding: 10px; background: #ffffff; }}
    .note {{ font-size: 11px; color: #475569; }}
  </style>
</head>
<body>
  <section class="hero">
    <img class="hero-image" src="./講座ビジュアル.png" alt="{COURSE_NAME} 講座ビジュアル">
    <h1>{COURSE_NAME}</h1>
    <p><strong>広告媒体のAI機能を使うだけで終わらせず、目的設計、計測、広告制作、媒体AIの採否、審査・表示リスク、週次改善、承認ログまでを業務フローとして設計する実践講座。</strong></p>
    <p class="note">標準構成: 6回、各120分、合計約12時間。提供方式: {LMS_TEXT}</p>
  </section>

  <h2>研修の目的</h2>
  <p>Google広告、Meta広告、LINEヤフー広告、GA4、Looker Studioを題材に、生成AIと媒体AI機能を使って広告運用を効率化しつつ、計測品質、広告審査、景品表示法、個人情報、ブランド確認、承認ログまで運用できる人材を育成します。</p>

  <h2>よくある悩み、導入背景</h2>
  <ul>
    <li>広告媒体のAI推奨をどこまで採用してよいか分からない。</li>
    <li>CV定義やUTMが曖昧で、AI入札やレポートの判断材料が弱い。</li>
    <li>広告コピーや画像案は作れるが、景表法、個人属性、ブランド確認が後回しになる。</li>
    <li>月次レポートが数字の転記で終わり、次の改善判断や承認履歴に残らない。</li>
  </ul>

  <h2>この研修で解決すること</h2>
  <div class="cards">
    <div class="card"><strong>広告運用の標準化</strong><br>目的、KPI、媒体、予算、確認者を整理し、AI活用候補を選定します。</div>
    <div class="card"><strong>計測とレポート</strong><br>CV定義、UTM、GA4、Looker Studioを整理し、AIが学習できる材料を整えます。</div>
    <div class="card"><strong>媒体AIの採否判断</strong><br>P-MAX、AI Max、Advantage+、スマートターゲティングを目的と制約で比較します。</div>
    <div class="card"><strong>審査・情報管理</strong><br>景表法、個人属性、個人情報、ブランド、LP整合、承認ログを公開前チェックに組み込みます。</div>
  </div>

  <h2>本講座受講後の到達点</h2>
  <ul>
    <li>広告運用のAs-Is/To-Beを整理し、AIで短縮する工程と人が確認する工程を切り分けられる。</li>
    <li>CV定義、UTM、広告レポートを診断し、媒体AIの学習に必要な計測基盤を整理できる。</li>
    <li>媒体AI機能や広告コピー案を、成果、予算、審査、ブランド、個人情報の観点で採否判断できる。</li>
    <li>週次改善ログ、AI改善提案採否表、承認フローを含む広告運用ルールを設計できる。</li>
    <li>広告運用改善提案書として、KPI、効果試算、90日ロードマップ、リスク対策をまとめられる。</li>
  </ul>

  <h2>研修の強み</h2>
  <ul>
    <li>媒体操作ではなく、目的設計、計測、制作、配信、改善、承認までの広告運用全体を扱う。</li>
    <li>架空ケースとダミーデータを使い、public repo に載せられない実アカウントや顧客データを使わず演習できる。</li>
    <li>Google Ads、Meta Ads、LINEヤフー広告、GA4、Looker Studio、ChatGPT/Claudeを、業務目的と確認観点に紐づけて扱う。</li>
    <li>最終的に、部署へ説明できる広告運用改善提案書と90日展開計画へ落とし込む。</li>
  </ul>

  <h2>対象者、推奨される知識・経験</h2>
  <p>広告運用、マーケティング、EC運用、広報、営業企画、事業推進担当者。広告代理店任せにせず、自社側で広告運用の判断材料を理解したい方を想定します。高度な広告運用経験やプログラミング経験は必須ではありません。</p>

  <h2>提供方式、学習時間、受講管理</h2>
  <p>{LMS_TEXT}</p>
  <p>標準学習時間は6回、各120分、合計約12時間です。受講状況、受講時間、課題提出、修了確認はLMSで記録する前提です。</p>

  <h2>カリキュラム表</h2>
  <table>
    <thead><tr><th>回</th><th>テーマ</th><th>時間</th><th>主な内容</th><th>成果物</th></tr></thead>
    <tbody>{curriculum_rows}</tbody>
  </table>

  <h2>演習、成果物、業務への持ち帰り</h2>
  <p>6回を通じて、広告運用棚卸し表、KPIツリー、計測設計シート、媒体別AI機能比較表、広告コピー案比較表、週次運用チェックリスト、広告運用改善提案書を作成します。成果物は自社・自部署の広告運用フローへ置き換えられる形にします。</p>

  <h2>注意事項、申込や運用に関する確認事項</h2>
  <ul>
    <li>生成AI出力と媒体AI提案は下書き扱いとし、公開前に人が審査、景表法、個人情報、ブランド、LP整合、承認を確認します。</li>
    <li>顧客リスト、実広告アカウントID、請求情報、APIキー、未公開売上、契約条件、社員/顧客情報は公開AIに入力しません。</li>
    <li>AIツールや広告媒体の提供状況、利用条件、料金、管理者設定、広告ポリシー、計測仕様は変わり得るため、導入時に最新の公式情報を確認します。</li>
    <li>実在ロゴや実在UIは、公式素材・ダミー環境・規約確認済み素材がある場合だけ使用します。</li>
  </ul>
</body>
</html>
"""


def course_wide_files() -> None:
    write(COURSE_DIR / "全体" / "講座概要.md", course_overview())
    write(COURSE_DIR / "全体" / "詳細シラバス.md", detailed_syllabus())
    write(COURSE_DIR / "全体" / "調査" / "差別化・公式情報メモ-2026-07-13.md", source_memo())
    write_raw(COURSE_DIR / "全体" / f"{COURSE_NAME}_パンフレット.html", pamphlet_html())
    write(
        COURSE_DIR / "全体" / "スライド構成案.md",
        f"""# 全体スライド構成案

対象講座: {COURSE_NAME}

{md_table(["回", "テーマ", "スライド枚数", "時間", "到達点", "成果物"], [[str(int(s["no"])), str(s["title"]), "30枚", "120分", str(s["promise"]), str(s["output"])] for s in SESSIONS])}

全回で `{TEMPLATE_ID}` を使い、各回30枚、合計180枚の高密度スライド案として設計する。各回に目次/全体像と章見出し/現在位置スライドを配置し、広告運用の課題整理、計測、媒体AI、制作審査、週次改善、提案書へ段階的に進める。
""",
    )
    write(
        COURSE_DIR / "全体" / "全回ワークシート.md",
        "# 全回ワークシート\n\n"
        + "\n\n".join(
            f"## 第{int(s['no'])}回 {s['title']}\n\n- 成果物: {s['output']}\n- 主要ケース: {s['case']}"
            for s in SESSIONS
        ),
    )
    write(
        COURSE_DIR / "全体" / "全回講師用メモ.md",
        f"""# 全回講師用メモ

対象講座: {COURSE_NAME}

- 録画eラーニング前提で話す。ライブ共有、チャット、口頭発表、相互レビューは使わない。
- ワーク時間は「ここで動画を一時停止して、○分ほど取り組んでください。取り組めたら再生してください。」と案内する。
- 実広告アカウント、顧客リスト、連絡先、契約条件、請求画面、APIキー、未公開売上、広告アカウントIDは画面に出さない。
- ツール画面は利用環境により変わるため、必須演習はワークシートとCSVだけで成立するように説明する。
- スライド画像生成後に、各回の `講師台本.md` はスライド上の実際の配置を見て位置参照を確定する。
""",
    )
    write(
        COURSE_DIR / "全体" / "演習データ回別一覧.md",
        "# 演習データ回別一覧\n\n"
        + md_table(
            ["回", "テーマ", "主なデータ", "用途"],
            [
                [str(int(s["no"])), str(s["title"]), ", ".join(name for name, _ in session_data(s)), str(s["output"])]
                for s in SESSIONS
            ],
        ),
    )
    write(
        COURSE_DIR / "全体" / "レベル3対応表.md",
        f"""# 本講座受講後の到達点対応表

対象講座: {COURSE_NAME}

| 到達点 | 対応する回 | 提出・演習成果物 |
| --- | --- | --- |
| 広告運用課題を整理し、As-Is/To-Beを設計できる | 第1回 | 広告運用棚卸し表、KPIツリー |
| AIが学習できる計測基盤とレポートを設計できる | 第2回 | 計測設計シート、UTM命名ルール、広告レポート診断表 |
| 媒体AI機能を目的、制約、確認点で採否判断できる | 第3回 | 媒体別AI機能比較表、キャンペーン設計メモ |
| 広告コピー/クリエイティブを審査・景表法・ブランド観点でレビューできる | 第4回 | 広告コピー案比較表、審査リスク修正メモ |
| 週次改善、AI提案採否、承認ログを運用化できる | 第5回 | 週次運用チェックリスト、広告運用ガバナンスルール |
| KPIと90日ロードマップを含む導入提案を作れる | 第6回 | 広告運用改善提案書、効果試算表、90日展開ロードマップ |
""",
    )
    write(
        COURSE_DIR / "全体" / "ユースケース・ダミーデータ設計.md",
        f"""# ユースケース・ダミーデータ設計

対象講座: {COURSE_NAME}

## 共通ケース

つばめ商店（架空のEC小売、従業員8名）が、Google Ads、Meta Ads、LINEヤフー広告を使い、演習用の月間広告予算60万円で新商品キャンペーンを運用している想定で演習する。

## データ設計方針

- 実在企業名、顧客名、個人名、メールアドレス、電話番号、住所、広告アカウントID、請求情報、APIキー、契約条件、未公開売上は使わない。
- 予算、CPA、CV、削減時間は演習上の仮数値として扱い、成果保証として書かない。
- 画像生成AIへ実在ロゴや実在UIの再現を依頼しない。
- 公式ツール画面を使う場合は、ダミー環境または公式公開素材を使い、取得元を `全体/調査/` に残す。
""",
    )
    write(
        COURSE_DIR / "全体" / "制作ステータス.md",
        f"""# 制作ステータス

対象講座: {COURSE_NAME}

## 現在の状態

- コース全体資料、パンフレットHTML、6回分のスライド案、ワークシート、暫定講師台本、演習データを作成済み。
- `画像生成プロンプト.md` は `scripts/rebuild_gws_high_density_image_prompts.py --course-dir '講座/{COURSE_NAME}'` で作成する。
- パンフレット冒頭用の完成ラスター画像 `全体/講座ビジュアル.png` は、Codex App Server / GPT image 2 / imagegenで生成して配置する。
- 各回の `スライド画像/Sxx.png` は未生成。仮画像やローカル描画画像で生成済み扱いにしない。
- 講師台本は暫定版。スライド画像生成後に、実際の配置を見て位置参照を確定する必要がある。

## 次の作業

1. `画像生成プロンプト.md` を生成する。
2. パンフレット用 `講座ビジュアル.png` を生成し、HTML/PDFへ反映する。
3. Codex App Server / GPT image 2 / imagegenスキルで各回の `スライド画像/Sxx.png` を生成する。
4. 軽量チェックを行い、欠番、形式、サイズ、重複、旧講座名、禁止語、OCR疑義を確認する。
5. 画像確認後、講師台本を最終化する。
6. 必要に応じてGoogle Slides/Canva/PPTXへ書き出す。
""",
    )


def session_files() -> None:
    for session in SESSIONS:
        session_dir = COURSE_DIR / str(session["dir"])
        for sub in ["スクリーンショット", "スライド画像", "配布資料", "演習データ"]:
            (session_dir / sub).mkdir(parents=True, exist_ok=True)
        write(session_dir / "スライド案.md", build_slide_plan_markdown(session))
        write(session_dir / "ワークシート.md", worksheet(session))
        write(session_dir / "講師台本.md", provisional_script(session))
        write(session_dir / "配布資料" / "演習ガイド.md", worksheet(session))
        write(session_dir / "演習データ" / "README.md", readme_for_data(session))
        write(
            session_dir / "スライド画像" / "README.md",
            f"""# スライド画像

第{int(session['no'])}回 `{session['title']}` の完成ラスター画像保存先です。

現在は未生成です。`スライド画像/Sxx.png` は、Codex App Server / GPT image 2 / `imagegen` スキルで1枚まるごと生成した完成ビットマップ、または規約確認済みの公式素材だけを保存します。SVG、HTML/CSS、canvas、ブラウザスクリーンショット、PIL/Pillow、ImageMagick、PDF/PPTX書き出し、ローカル合成、後載せテキストで作ったPNGは完成物として保存しません。
""",
        )
        for filename, rows in session_data(session):
            write_csv(session_dir / "演習データ" / filename, rows)


def main() -> None:
    course_wide_files()
    session_files()
    print(f"created course materials: {COURSE_DIR}")


if __name__ == "__main__":
    main()
