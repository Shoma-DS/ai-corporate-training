#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


COURSE_DIR = Path("講座/AIエージェント実装・連携設計アカデミー")
COURSE_NAME = "AIエージェント実装・連携設計アカデミー"


@dataclass
class Slide:
    no: str
    title: str
    headline: str
    pattern: str
    layout: str
    items: list[tuple[str, str]]
    main: str
    material: str


TERM_RULES: list[tuple[str, tuple[str, ...], str, str]] = [
    (
        "As-Is/To-Be",
        ("As-Is", "To-Be", "現状", "目指す姿", "Gap"),
        "As-Isは今の仕事の流れ、To-Beは改善後の流れです。部屋の模様替えでいえば、家具を買う前に今の動線と新しい動線を比べる作業です。",
        "応用では、To-Beを完全自動化の絵にせず、AIが候補を出す工程、人が承認する工程、止める工程を分けて設計します。",
    ),
    (
        "Codex",
        ("Codex",),
        "Codexは、業務改善リポジトリ内のファイルを読み、修正案、スクリプト、テスト、確認結果まで支援するAIエージェントです。",
        "応用では、対象ファイル、禁止事項、期待出力、検証コマンド、差分確認を依頼前にそろえることで、作業を任せても戻せる状態にします。",
    ),
    (
        "MCP",
        ("MCP", "Resources", "Prompts", "Tools", "STDIO", "HTTP", "JSON-RPC"),
        "MCPはAIエージェントと外部ツールをつなぐ共通の接続口です。家電でいうコンセントや変換アダプターのように、つなぎ方の型をそろえるものです。",
        "応用では、つなげるかどうかだけでなく、読み取り専用か、書き込みまで許すか、承認をどこに置くか、ログをどこに残すかまで決めます。",
    ),
    (
        "リポジトリ",
        ("リポジトリ", "フォルダ構成", "docs/", "data/sample/", "scripts/", "tests/", "runbooks/"),
        "リポジトリはコード置き場だけではありません。設計書、サンプルデータ、作業手順、テスト結果をまとめる業務改善の作業箱です。",
        "応用では、誰が見ても再現できるように、仕様、入力データ、出力例、検証方法、変更履歴を同じ場所に残します。",
    ),
    (
        "AGENTS.md",
        ("AGENTS.md", "AGENTS"),
        "AGENTS.mdは、AIエージェント向けの作業手順書です。新人に渡す業務ルールの紙を、AIにも読める形で置くイメージです。",
        "応用では、許可する作業、承認が必要な作業、禁止する操作、テスト方法、公開不可情報の扱いを明文化します。",
    ),
    (
        "ダミーデータ",
        ("ダミーデータ", "匿名化", "架空化", "公開不可", "実データ", "秘密情報"),
        "ダミーデータは、本物に似せた架空データです。料理練習で本番の高級食材ではなく練習用の材料を使うのに近いです。",
        "応用では、件数、列名、例外、空欄、重複は実務に近づけつつ、顧客名、社員名、契約情報、認証情報は入れません。",
    ),
    (
        "Git",
        ("Git", "差分", "コミット", "変更履歴", "戻し方"),
        "Gitは変更履歴の台帳です。差分は変更前後の赤入れ、コミットはその時点の作業記録だと考えるとわかりやすいです。",
        "応用では、AIが何を変えたかを差分で確認し、問題があれば戻せる単位で記録してから次の作業へ進めます。",
    ),
    (
        "サンドボックス",
        ("サンドボックス", "workspace-write", "承認", "危険なコマンド", "外部接続"),
        "サンドボックスは、安全に試すための作業スペースです。工場で本番ラインを止めずに試験ラインで検証する考え方に近いです。",
        "応用では、ファイル削除、外部送信、認証情報の利用、費用が発生する操作を承認対象に分けます。",
    ),
    (
        "プロトタイプ",
        ("プロトタイプ", "試作", "実装", "デバッグ", "テスト", "期待出力"),
        "プロトタイプは本番システムではなく、業務改善の仮説を小さく試す試作品です。",
        "応用では、動くことだけでなく、空欄、重複、異常値、文字化け、出力形式までテストして、次の連携設計へ渡せるかを確認します。",
    ),
    (
        "API/OAuth",
        ("API", "OAuth", "Bearer", "認証", "認証情報"),
        "APIはシステム同士の窓口、OAuthやBearerトークンは入館証のようなものです。持っている人が何をできるかを必ず制限します。",
        "応用では、読み取りだけの権限、書き込み権限、期限、保管場所、漏えい時の停止手順まで決めます。",
    ),
    (
        "プロンプトインジェクション",
        ("プロンプトインジェクション", "ツール誤実行", "権限過多"),
        "プロンプトインジェクションは、資料や入力文の中に紛れ込んだ悪い指示でAIの行動を変えようとする攻撃です。",
        "応用では、外部資料の指示をそのまま信じず、実行前承認、読み取り専用、ログ確認、停止手順を組み合わせて防ぎます。",
    ),
    (
        "KPI",
        ("KPI", "効果試算", "削減時間", "ミス削減", "対応速度"),
        "KPIは効果を見る物差しです。何となく便利ではなく、時間、件数、ミス、対応速度などで変化を確認します。",
        "応用では、数字を成果保証として見せず、仮説、前提、測定方法、見直し時期をセットで説明します。",
    ),
    (
        "ロードマップ",
        ("ロードマップ", "展開計画", "90日", "横展開", "本番化"),
        "ロードマップは導入の工程表です。いつ、誰が、何を確認し、どこまで広げるかを順番に並べます。",
        "応用では、試行、本番化、教育、運用、改善、横展開を分け、途中で止める判断基準も入れます。",
    ),
]


SESSION_MEMOS = {
    "01": "第1回は実装に入らず、Codexへ安全に依頼できる業務テーマを選ぶ回です。説明が抽象化したら、業務名、頻度、所要時間、入力、出力、確認者、禁止事項へ戻してください。",
    "02": "第2回は、Codexに作業させる前の安全な作業場づくりが主題です。Gitやターミナルの操作説明に寄りすぎず、リポジトリ、AGENTS.md、ダミーデータ、承認境界へ戻してください。",
    "03": "第3回は、小さなプロトタイプを作り、テストと差分確認まで行う回です。完成品を作る話ではなく、検証可能な試作品を安全に作る話として進めてください。",
    "04": "第4回は、MCPで何でも接続する回ではなく、接続してよいもの、接続しないもの、承認が必要なものを設計する回です。Resources、Prompts、Toolsを業務の役割と結びつけて説明してください。",
    "05": "第5回は、作ったものを安全に使い続けるための評価、権限、運用設計が主題です。リスクを怖がらせるだけでなく、確認、ログ、停止、復旧、教育の手順へ落とし込んでください。",
    "06": "第6回は、これまでの成果物を導入判断に使える提案書へまとめる回です。効果だけを強調せず、前提、リスク、運用、ロードマップ、次アクションまでそろえてください。",
}


WORK_MINUTES = {
    "ワーク1": 10,
    "ワーク2": 12,
    "ワーク3": 12,
    "ワーク4": 8,
    "自己レビュー": 5,
    "受講後": 5,
}


def clean(text: str) -> str:
    text = text.replace("`", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_slides(prompt_text: str) -> list[tuple[str, str, str]]:
    matches = list(re.finditer(r"^## Slide (S\d{2})\. (.+)$", prompt_text, re.M))
    slides: list[tuple[str, str, str]] = []
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(prompt_text)
        slides.append((match.group(1), clean(match.group(2)), prompt_text[start:end]))
    return slides


def parse_slide_plan(plan_text: str) -> dict[str, tuple[str, str, str]]:
    result: dict[str, tuple[str, str, str]] = {}
    for line in plan_text.splitlines():
        if not line.startswith("| S"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 6:
            result[cells[0]] = (clean(cells[2]), clean(cells[4]), clean(cells[5]))
    return result


def parse_key_value_block(block: str) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    for raw in block.splitlines():
        line = raw.strip().lstrip("- ").strip()
        if not line or ":" not in line:
            continue
        # Some prompt files put all SOURCE TEXT labels on one line:
        # "タイトル: ... ヘッドライン: ... カード1 判断: ..."
        # Split those labels without requiring one label per line.
        matches = list(re.finditer(r"(^|\s)([^:\n]{1,32}?):\s*", line))
        if not matches:
            continue
        for i, match in enumerate(matches):
            key = clean(match.group(2))
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(line)
            value = clean(line[start:end])
            value = re.sub(r"\s*--- SOURCE TEXT END ---.*$", "", value).strip()
            if key and value:
                items.append((key, value))
    return items


def parse_items(section: str) -> list[tuple[str, str]]:
    block_match = re.search(
        r"画像内に必ず入れる(?:短い日本語文言|内容):\s*```(?:markdown|text)?\n(.*?)\n```",
        section,
        re.S,
    )
    if block_match:
        return parse_key_value_block(block_match.group(1))
    source_match = re.search(r"--- SOURCE TEXT START ---\s*(.*?)\s*--- SOURCE TEXT END ---", section, re.S)
    if source_match:
        return parse_key_value_block(source_match.group(1))
    inline_match = re.search(r"SOURCE TEXT START\s+(.*?)(?:SOURCE TEXT END|$)", section, re.S)
    if inline_match:
        return parse_key_value_block(inline_match.group(1))
    return []


def parse_prompt(path: Path, plan: dict[str, tuple[str, str, str]]) -> list[Slide]:
    text = path.read_text(encoding="utf-8")
    slides: list[Slide] = []
    for no, title, section in split_slides(text):
        headline = clean(re.search(r"- ヘッドライン:\s*(.+)", section).group(1)) if re.search(r"- ヘッドライン:\s*(.+)", section) else ""
        pattern = clean(re.search(r"- 図解パターン:\s*(.+)", section).group(1)) if re.search(r"- 図解パターン:\s*(.+)", section) else plan.get(no, ("", "", ""))[1]
        layout = clean(re.search(r"- 推奨レイアウト:\s*(.+)", section).group(1)) if re.search(r"- 推奨レイアウト:\s*(.+)", section) else ""
        main, plan_pattern, material = plan.get(no, ("", "", ""))
        slides.append(Slide(no, title, headline, pattern or plan_pattern, layout, parse_items(section), main, material))
    return slides


def get_existing_prepare(script_path: Path) -> str:
    if not script_path.exists():
        return ""
    text = script_path.read_text(encoding="utf-8")
    match = re.search(r"## 準備物\n\n(.*?)(?:\n\n講師メモ:|\n\nスライド切替:)", text, re.S)
    return match.group(1).strip() if match else ""


def visible_items(slide: Slide) -> list[tuple[str, str]]:
    skip = {"ヘッダー", "タイトル", "ヘッドライン", "サブタイトル", "回タイトル"}
    return [(k, v) for k, v in slide.items if k not in skip and v]


def item_value(slide: Slide, *keys: str) -> str:
    for key, value in slide.items:
        if any(key.startswith(k) or k in key for k in keys):
            return value
    return ""


def position_sentence(slide: Slide) -> str:
    text = f"{slide.title} {slide.pattern} {slide.layout}"
    if "画面共有" in slide.title:
        return "中央の案内カードで、これから開くファイル名、確認する列、見落としてはいけない点を先に確認します。"
    if "ワーク" in slide.title or "自己レビュー" in slide.title:
        return "中央のチェック項目を上から順に見て、下部の成果物または確認帯に書かれている到達点へつなげます。"
    if "左右" in text or "比較" in text or "comparison" in text:
        return "画面中央の左右のカードを見比べて、左側を現在の課題、右側を改善後または良い例として読み分けます。"
    if "ロードマップ" in text or "timeline" in text or "横" in text or "フロー" in text or "process" in text:
        return "画面中央の流れを左から右へ追い、各ステップで入力、処理、確認、出力がどう変わるかを見ます。"
    if "3カラム" in text or "3つ" in text or "3枚" in text:
        return "画面中央の3つのカードを左から順に見て、役割、使い道、後続回とのつながりを確認します。"
    if "リスク" in text or "governance" in text or "権限" in text or "承認" in text:
        return "中央のリスクカードと下部の確認帯を見て、使ってよい情報、止める操作、人が判断する場所を分けます。"
    if "表" in text or "matrix" in text or "分類" in text:
        return "中央の表または分類カードを見て、評価軸ごとに判断が分かれる点を確認します。"
    return "画面中央のカード群を見ながら、上段で考え方、下段で成果物と確認観点を結びつけます。"


def detect_terms(slide: Slide) -> list[tuple[str, str, str]]:
    text = " ".join([slide.title, slide.headline, slide.main] + [f"{k} {v}" for k, v in slide.items])
    found: list[tuple[str, str, str]] = []
    for _, triggers, simple, advanced in TERM_RULES:
        if any(trigger in text for trigger in triggers):
            found.append((triggers[0], simple, advanced))
        if len(found) >= 2:
            break
    return found


def summarize_points(slide: Slide, limit: int = 4) -> str:
    points = []
    for key, value in visible_items(slide):
        if key.startswith(("下部", "注記", "注意", "小フロー", "色分け")):
            continue
        points.append(f"{key}では「{value.rstrip('。')}」")
        if len(points) >= limit:
            break
    if points:
        return "中央の本文では、" + "、".join(points) + "を確認します。"
    if slide.main:
        return f"中央の本文では、{slide.main}を扱います。"
    return "中央の本文では、このスライドの判断材料を確認します。"


def bottom_sentence(slide: Slide) -> str:
    for key, value in slide.items:
        if key.startswith(("下部", "注記", "注意", "色分け", "小フロー")):
            return f"最後に、{key}の「{value}」を確認してください。ここが次の作業へ進めてよいかの判断点です。"
    if slide.material and slide.material not in {"図解", ""}:
        return f"素材は{slide.material}です。画面共有やワークシートでは、同じ項目名を使って確認します。"
    return "下部の成果物または確認帯は、あとでワークシートを見直すときのチェックポイントとして使います。"


def practical_example(slide: Slide) -> str:
    text = " ".join([slide.title, slide.headline, slide.main] + [v for _, v in slide.items])
    if "みどり商事" in text:
        return "例として出てくるみどり商事は、卸売業の架空企業です。問い合わせ、月次報告、FAX台帳転記のような現場に近い作業として考えてください。"
    if "問い合わせ" in text:
        return "実務では、問い合わせメールを台帳へ転記し、担当者を決め、返信案を確認する流れに置き換えると理解しやすくなります。"
    if "週次" in text or "月次" in text or "報告" in text:
        return "実務では、毎週または毎月の報告作成で、集計、下書き、確認、提出先を分けて考えます。"
    if "提案" in text or "KPI" in text:
        return "実務では、現場に便利そうですと伝えるだけでなく、削減時間、確認方法、リスク対応、次の担当者まで説明できる状態を目指します。"
    return "自社に置き換えるときは、部署名や顧客名を直接入れず、業務の種類、件数、頻度、確認者だけを抽象化して書きます。"


def read_aloud(slide: Slide) -> str:
    parts: list[str] = []
    if slide.headline:
        parts.append(f"上部のヘッドラインを見てください。「{slide.headline}」とあります。")
    parts.append(position_sentence(slide))
    parts.append(summarize_points(slide))
    for _, simple, advanced in detect_terms(slide):
        parts.append(simple)
        parts.append(advanced)
    parts.append(practical_example(slide))
    parts.append(bottom_sentence(slide))
    return " ".join(parts)


def work_minutes(title: str) -> int:
    for key, minutes in WORK_MINUTES.items():
        if key in title:
            return minutes
    return 8


def work_text(slide: Slide) -> str:
    minutes = work_minutes(slide.title)
    action = item_value(slide, "ワーク", "作業", "これからやること", "確認")
    if not action:
        action = slide.main or "スライド中央のチェック項目に沿って、ワークシートを見直す"
    terms = detect_terms(slide)
    term_sentence = ""
    if terms:
        _, simple, advanced = terms[0]
        term_sentence = f"{simple} {advanced} "
    return (
        f"このスライドを表示したまま、中央のチェック項目と下部の成果物欄を見てください。{term_sentence}"
        f"ここで動画を一時停止して、{minutes}分ほど取り組んでください。"
        f"作業内容は、{action}です。"
        "実在の顧客名、社員名、メールアドレス、契約情報、認証情報は書かず、架空名または抽象化した表現にしてください。"
        "取り組めたら再生してください。"
    )


def demo_title(slide: Slide) -> str:
    title = slide.title.replace("画面共有:", "").strip()
    if title.endswith("を見る") or title.endswith("確認する"):
        return title
    return title


def demo_file(slide: Slide) -> str:
    candidates = []
    for key, value in slide.items:
        if any(token in key for token in ("これから見るもの", "使用ファイル", "素材", "ファイル")):
            candidates.append(value)
    text = " ".join(candidates + [slide.main, slide.title])
    md = re.search(r"`([^`]+)`", text)
    if md:
        return md.group(1)
    for filename in re.findall(r"[\w一-龥ぁ-んァ-ンー・-]+?\.(?:csv|md|toml|json|xlsx)", text):
        return filename
    if "ワークシート" in text:
        return "ワークシート.md"
    if "提案書" in text:
        return "提案書アウトライン.md"
    return "該当する演習データまたは講師記入例"


def demo_steps(slide: Slide, demo_no: int) -> tuple[int, list[str], str]:
    file_name = demo_file(slide)
    checks = [(k, v) for k, v in visible_items(slide) if k.startswith("確認")]
    if not checks:
        checks = visible_items(slide)[:3]
    duration = 5 if len(checks) >= 3 else 4
    steps = [
        f"{file_name} を開きます。スライド中央の案内カードに書かれたファイル名と一致していることを示し、これはダミーデータまたは講師記入例だけを使う実演だと説明します。",
    ]
    for key, value in checks[:3]:
        steps.append(f"{key}として、{value}を画面上で指します。ここでは項目名を読むだけでなく、どの列やどの記入欄が後続の成果物につながるかを声に出して説明します。")
    steps.append("最後に、画面をスライドへ戻す前に、いま確認した入力、処理、出力、人の確認、保存先、停止条件のどれが次のワークに関係するかを一文でまとめます。")
    point = slide.headline or slide.main or "画面共有の確認ポイント"
    return duration, steps, f"{point}。画面共有では、操作の速さではなく、どの情報を見て、どの判断に使うのかを見せる。"


def screen_share_block(slide: Slide, demo_no: int) -> tuple[str, dict[str, str]]:
    duration, steps, point = demo_steps(slide, demo_no)
    lines = [f"画面共有 ── 実演{demo_no}「{demo_title(slide)}」", f"⏱ 約{duration}分", ""]
    each = max(45, int(duration * 60 / max(len(steps), 1)))
    for i, step in enumerate(steps, start=1):
        label = f"約{each}秒" if each < 60 else f"約{round(each / 60)}分"
        lines.append(f"【手順{i} – {label}】")
        lines.append(step)
        lines.append("")
    lines.append("【見せるポイント】")
    lines.append(point)
    return "\n".join(lines).rstrip(), {"no": f"実演{demo_no}", "title": demo_title(slide), "time": f"約{duration}分", "overview": point}


def slide_plan_timeline(slides: list[Slide]) -> str:
    lines = [
        "## スライド切替タイムライン",
        "",
        "| No. | タイトル | 操作概要 |",
        "| --- | --- | --- |",
    ]
    for slide in slides:
        overview = slide.main or slide.headline or "スライド内容を確認"
        lines.append(f"| {slide.no} | {slide.title} | {overview} |")
    return "\n".join(lines)


def demo_timeline(demos: list[dict[str, str]]) -> str:
    lines = [
        "## 作業風景タイムライン",
        "",
        "| 実演 | タイトル | ⏱ 時間 | 操作概要 |",
        "| --- | --- | --- | --- |",
    ]
    for demo in demos:
        lines.append(f"| {demo['no']} | {demo['title']} | {demo['time']} | {demo['overview']} |")
    return "\n".join(lines)


def rebuild_session(session_dir: Path) -> None:
    session_no = session_dir.name[:2]
    session_title = session_dir.name[3:]
    plan_text = (session_dir / "スライド案.md").read_text(encoding="utf-8")
    slides = parse_prompt(session_dir / "画像生成プロンプト.md", parse_slide_plan(plan_text))
    if len(slides) != 40:
        raise RuntimeError(f"{session_dir}: expected 40 slides, got {len(slides)}")

    existing_script = session_dir / "講師台本.md"
    prepare = get_existing_prepare(existing_script)
    if not prepare:
        prepare = "\n".join(
            [
                f"- 第{int(session_no)}回スライド S01-S40",
                "- `ワークシート.md`",
                "- `配布資料/演習ガイド.md`",
                "- `演習データ/` 内の該当サンプルファイル",
            ]
        )

    out: list[str] = [
        f"# 第{int(session_no)}回 講師台本: {session_title}",
        "",
        "<!-- canva-url-list -->",
        "> Canva版スライドURL一覧: `非公開/Canva/Canva_URL一覧.md`",
        "> 実URLは公開リポジトリに貼らず、非公開ファイルで管理する。",
        "<!-- /canva-url-list -->",
        "",
        f"講座名: {COURSE_NAME}",
        "",
        "## この台本の使い方",
        "",
        "この台本は録画動画によるeラーニング用です。ライブ形式のやり取りは行いません。ワークは動画を一時停止して取り組み、再生後に講師の記入例や確認観点と比べる形で進めます。",
        "",
        "## 準備物",
        "",
        prepare,
        "",
        "講師メモ:",
        SESSION_MEMOS.get(session_no, "スライド上の成果物、確認観点、下部帯を指しながら、実務で使える判断基準として説明してください。"),
        "",
    ]

    demos: list[dict[str, str]] = []
    demo_no = 1
    for slide in slides:
        opening = ""
        if slide.no == "S01":
            opening = f"この講座は「{COURSE_NAME}」です。今回は第{int(session_no)}回「{session_title}」を進めます。 "
        out.append("スライド切替:")
        out.append(f"{slide.no}「{slide.title}」")
        out.append("")
        if "画面共有" in slide.title:
            out.append("読み上げ:")
            out.append(f"「{opening}{read_aloud(slide)} この説明のあと、同じファイルまたは記入例を画面共有で確認します。」")
            out.append("")
            block, demo_info = screen_share_block(slide, demo_no)
            out.append(block)
            out.append("")
            demos.append(demo_info)
            demo_no += 1
        elif "ワーク" in slide.title or "自己レビュー" in slide.title or "受講後" in slide.title:
            out.append("ワーク指示:")
            out.append(f"「{work_text(slide)}」")
            out.append("")
        else:
            out.append("読み上げ:")
            out.append(f"「{opening}{read_aloud(slide)}」")
            out.append("")

    out.append(slide_plan_timeline(slides))
    out.append("")
    out.append(demo_timeline(demos))
    out.append("")
    existing_script.write_text("\n".join(out), encoding="utf-8")


def main() -> None:
    sessions = sorted([p for p in COURSE_DIR.iterdir() if p.is_dir() and re.match(r"\d{2}-", p.name)])
    for session in sessions:
        rebuild_session(session)
        print(f"rebuilt: {session}")


if __name__ == "__main__":
    main()
