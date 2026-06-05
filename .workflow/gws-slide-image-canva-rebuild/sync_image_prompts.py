#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path("講座/Google Workspace・GASで進めるAI業務効率化-DX実践講座")


COMMON_RULES = """## 共通ルール

- 画角は16:9、1920x1080想定。
- 日本語テキストは大きく、読みやすいゴシック体風にする。
- 画像内テキストは各スライドで指定した短い文言だけにする。本文全文、表の全文、謎文字、ダミー文字列は入れない。
- 実在Googleロゴ、Google Workspaceロゴ、Forms/Sheets/Drive/Gmail/Calendar/Gemini/Apps Scriptの実在UIは、画像生成AIに記憶で描かせない。
- 公式ロゴが必要な場合は `素材/ロゴ/` の取得済み公式素材を参照素材として使う。プロンプトだけで実在ロゴを再現させない。
- 画面説明が必要な場合は、各回フォルダの `スクリーンショット/` に置く公式公開画像またはダミー環境スクショを参照素材として使う。生成画像側で実在UIを想像再現しない。
- 会社名、顧客名、社員名、メールアドレス、価格、連絡先、契約情報、APIキー、社内固有情報は入れない。
- `素材配置枠`、`公式ロゴ`、空の破線枠、透かし、QRコード、架空UI、架空ロゴを入れない。
"""


BASE_PROMPTS = {
    "isometric-corporate-clean": """```text
16:9、1920x1080の法人研修用スライド画像を作成。isometric-corporate-clean の白背景、ネイビー見出し、ブルー/ティール/ミントのアクセント、薄いグレー罫線、角丸カード、控えめな影、清潔なアイソメトリック業務図解で統一する。Google Workspace/GAS講座として、入力、台帳、権限、通知、AI確認、運用改善を抽象アイコンとカードで表現する。日本語テキストは指定文言だけを大きく正確に配置。実在ロゴ、実在UI、個人情報、価格、連絡先、QRコード、透かしは入れない。
```""",
    "soft-isometric-corporate-warm": """```text
16:9、1920x1080の法人研修用スライド画像を作成。soft-isometric-corporate-warm の白背景、柔らかい人物イラスト、淡い角丸カード、薄いグレー罫線、控えめな影、ネイビー見出し、ブルーとグリーンのアクセント、必要最小限の赤い注意表示で統一する。権限、共同編集、情報管理、演習レビューをやさしく実務的に表現する。日本語テキストは指定文言だけを大きく正確に配置。実在ロゴ、実在UI、個人情報、価格、連絡先、QRコード、透かしは入れない。
```""",
}


NEGATIVE = """```text
文字化け、誤字、余計な文字、小さすぎる文字、読めない日本語、長文の詰め込み、参照画像なしでのGoogleロゴ再現、参照画像なしでの実在UI再現、架空のGoogle画面、架空のGoogleロゴ、実在企業名、人物名、メールアドレス、価格、連絡先、QRコード、透かし、素材配置枠、公式ロゴという文字、空の破線枠、暗い背景、派手なグラデーション、装飾過多、漫画風、手書き風、過度な3D、雑然としたレイアウトを避ける。
```"""


PATTERN_HINTS = [
    ("cover", "表紙として、中央の大見出しと3つの小さな成果物カードで構成する。"),
    ("roadmap", "横長のロードマップで現在位置を強調し、前後の回とのつながりを示す。"),
    ("comparison", "左右比較または3列比較のカードで、違いと判断軸を一目で分かるようにする。"),
    ("before-after", "Before/Afterカードで、現状課題から改善後の業務状態への変化を示す。"),
    ("check", "チェックリストと確認者アイコンで、実務で確認する観点を整理する。"),
    ("workshop", "演習導入として、手順、成果物、確認ポイントの3カードを大きく配置する。"),
    ("flow", "左から右への業務フローで、入力、処理、確認、出力の順序を示す。"),
    ("matrix", "2軸または表形式のマトリクスで、役割、権限、判断基準を整理する。"),
    ("table", "表をそのまま細かく描かず、列見出しと代表カードでデータ設計の要点を見せる。"),
    ("risk", "注意バナーと確認カードで、情報管理・権限・誤送信リスクを落ち着いた表現で示す。"),
]


def pick_hint(pattern: str) -> str:
    p = pattern.lower()
    for key, hint in PATTERN_HINTS:
        if key in p:
            return hint
    return "3〜5個の角丸カードまたは短いフローで、業務上の判断、具体例、成果物、確認ポイントを整理する。"


def clean_text(value: str) -> str:
    value = re.sub(r"`+", "", value)
    value = re.sub(r"\*\*", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip(" -:：|")


def short_title(title: str) -> str:
    title = re.sub(r"^S\d{2}\s*", "", title).strip()
    return title[:28]


def extract_field(block: str, label: str, default: str = "なし") -> str:
    m = re.search(rf"^\s*-?\s*\*\*{re.escape(label)}:\*\*\s*(.+)$", block, re.M)
    if not m:
        return default
    return clean_text(m.group(1))


def extract_keywords(block: str) -> list[str]:
    values: list[str] = []
    for m in re.finditer(r"^\*\*内容ブロック[^:：]*[:：]\s*(.+)$", block, re.M):
        values.append(clean_text(m.group(1)))
    if len(values) < 3:
        for m in re.finditer(r"^\|\s*([^|\n]{2,18})\s*\|", block, re.M):
            text = clean_text(m.group(1))
            if text and text not in {"---", "項目", "回", "業種"}:
                values.append(text)
    if len(values) < 3:
        for m in re.finditer(r"^-\s+\*\*([^*]+)\*\*", block, re.M):
            values.append(clean_text(m.group(1)))
    banned = {
        "図解パターン",
        "テンプレートID",
        "スクリーンショット",
        "スライドタイプ",
        "素材",
    }
    unique: list[str] = []
    for value in values:
        if value and value not in banned and value not in unique:
            unique.append(value[:24])
    return unique[:5]


def parse_slides(text: str) -> list[dict[str, str | list[str]]]:
    matches = list(re.finditer(r"^###\s+(S\d{2})\s+(.+)$", text, re.M))
    slides: list[dict[str, str | list[str]]] = []
    for i, match in enumerate(matches):
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]
        slide_no = match.group(1)
        title = clean_text(match.group(2))
        headline = extract_field(block, "ヘッドライン", title)
        pattern = extract_field(block, "図解パターン", "module-block")
        template = extract_field(block, "テンプレートID", "isometric-corporate-clean")
        screenshot = extract_field(block, "スクリーンショット", "なし")
        keywords = extract_keywords(block)
        slides.append(
            {
                "no": slide_no,
                "title": title,
                "headline": headline,
                "pattern": pattern,
                "template": template,
                "screenshot": screenshot,
                "keywords": keywords,
            }
        )
    return slides


def in_image_text(slide: dict[str, str | list[str]]) -> list[str]:
    title = short_title(str(slide["title"]))
    headline = str(slide["headline"])
    words = [title]
    if headline and headline != title:
        headline = re.split(r"[。．、,，とでがをにへは]", headline)[0]
        words.append(headline[:24])
    for keyword in slide["keywords"]:  # type: ignore[assignment]
        words.append(str(keyword)[:18])
    unique: list[str] = []
    for word in words:
        word = clean_text(word)
        if word and word not in unique:
            unique.append(word)
    return unique[:6]


def write_prompt(session_dir: Path, slides: list[dict[str, str | list[str]]]) -> None:
    session_title = session_dir.name
    templates = [str(s["template"]) for s in slides]
    template = max(set(templates), key=templates.count) if templates else "isometric-corporate-clean"
    parts = [
        f"# {session_title} 画像生成プロンプト",
        "",
        "対象講座: Google Workspace・GASで進めるAI業務効率化/DX実践講座。",
        f"対象スライド: S01-S{len(slides):02d}",
        f"採用テンプレート: `{template}`",
        "",
        "このファイルは新しい `スライド案.md` に同期した正本。各スライドはGPT image 2 / built-in image generationで1枚まるごとの完成画像として生成する。SVG、HTML/CSS、canvas、ブラウザスクリーンショット、ローカル変換、後載せテキスト合成は使わない。",
        "",
        COMMON_RULES,
        "",
        "## 共通ベースプロンプト",
        "",
        BASE_PROMPTS.get(template, BASE_PROMPTS["isometric-corporate-clean"]),
        "",
        "## 共通ネガティブプロンプト",
        "",
        NEGATIVE,
        "",
    ]
    for slide in slides:
        text_items = in_image_text(slide)
        quoted = "、".join(f"`{item}`" for item in text_items)
        pattern = str(slide["pattern"])
        screenshot = str(slide["screenshot"])
        has_screenshot = screenshot and not screenshot.startswith("なし")
        prompt_text = (
            f"共通ベースプロンプトに従う。上部に大きく「{text_items[0]}」。"
            f"{pick_hint(pattern)} "
            f"画像内テキストは {', '.join(text_items)} の短い文言だけに抑える。"
            "長い本文や表の全文は入れず、3〜5個の見出しカードで具体度を出す。"
        )
        if has_screenshot:
            prompt_text += f" スクリーンショット/公式素材は「{screenshot}」を参照し、実在UIを記憶で描かない。"
        parts.extend(
            [
                f"## Slide {slide['no']}. {slide['title']}",
                "",
                f"- 使用テンプレート: `{slide['template']}`",
                f"- 図解パターン: `{pattern}`",
                f"- 画像内テキスト: {quoted}",
                f"- スクショ/公式ロゴ要否: {screenshot}",
                "- プロンプト:",
                "",
                "```text",
                prompt_text,
                "```",
                "",
                "- ネガティブプロンプト: 共通ネガティブプロンプトに従う。実在ロゴ、実在UI、細かい文字、素材配置枠を避ける。",
                "",
            ]
        )
    (session_dir / "画像生成プロンプト.md").write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    for session_dir in sorted(ROOT.glob("[0-9][0-9]-*")):
        slide_plan = session_dir / "スライド案.md"
        if not slide_plan.exists():
            continue
        slides = parse_slides(slide_plan.read_text(encoding="utf-8"))
        if not slides:
            raise SystemExit(f"No slides found: {slide_plan}")
        write_prompt(session_dir, slides)
        print(f"{session_dir.name}: {len(slides)} prompts")


if __name__ == "__main__":
    main()
