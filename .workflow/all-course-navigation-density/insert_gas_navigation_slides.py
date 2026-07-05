#!/usr/bin/env python3
"""Insert agenda/current-position slides into the GAS course slide plans."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


COURSE_DIR = Path("講座/生成AI・GASで実践する業務変革・DX推進講座")


@dataclass
class Section:
    name: str
    minutes: str
    start: int
    end: int
    goal: str


@dataclass
class Slide:
    number: int
    title: str
    body: str


SECTION_META: dict[str, dict[str, dict[str, object]]] = {
    "01": {
        "オープニングと本日の目的": {
            "axis": "今日の成果物・ツール役割・自動化と人の確認の線引きをそろえる",
            "output": "業務棚卸しへ入る前の受講準備と判断軸",
            "points": ["3成果物を確認する", "6つのツールの役割を見る", "人が確認する範囲を決める", "作業環境を開く"],
        },
        "中小企業の業務DX動向": {
            "axis": "DXを大規模投資ではなく、身近な転記・集計・確認・通知の改善として捉える",
            "output": "改善候補を選ぶための根拠メモ",
            "points": ["中小企業のDX現状", "経営とIT基盤の両輪", "Workspace/Gemini事例", "小さく始める理由"],
        },
        "業務課題の可視化": {
            "axis": "手作業の頻度・時間・ミス影響を数値で見える化する",
            "output": "業務棚卸しシート",
            "points": ["Excel的手作業を観察", "累積負担を数値化", "業務を6分類", "Forms→Sheetsの流れ"],
        },
        "As-Is/To-Be設計": {
            "axis": "現状フローと改善後フローを分け、人・ツール・AI/GASの役割を決める",
            "output": "As-Is/To-Beメモ",
            "points": ["現状を5〜8ステップで書く", "全自動にしないTo-Be", "手段の使い分け", "人が確認する場面"],
        },
        "自動化候補の選定": {
            "axis": "頻度・効果・リスク・実現性で候補をA/B/Cに分ける",
            "output": "改善候補選定表とKPI仮置き",
            "points": ["向く業務の5条件", "慎重に扱う3パターン", "優先順位マトリクス", "KPIを仮置き"],
        },
        "演習とまとめ": {
            "axis": "3つの成果物を見直し、第2回のフォーム・台帳設計へ接続する",
            "output": "業務棚卸し・As-Is/To-Be・候補選定の完成版",
            "points": ["記入例と比較", "AI入力禁止情報を確認", "次回準備", "第1回の自己チェック"],
        },
    },
    "02": {
        "導入とケース選定": {
            "axis": "第1回のA候補から、フォーム化する業務ケースを1つ選ぶ",
            "output": "フォーム化対象ケース",
            "points": ["前回成果物との接続", "入力元を分ける判断軸", "フォーム化に向く業務", "ケースを選ぶ"],
        },
        "Googleフォーム設計": {
            "axis": "1設問1情報・必須・選択肢・回答先を設計する",
            "output": "フォーム設計表",
            "points": ["入力形式の使い分け", "自由記述を減らす", "必須と入力ルール", "回答先Sheetsを作る"],
        },
        "回答シートと管理台帳": {
            "axis": "回答原本と管理台帳を分け、列・ID・ステータス・ログを設計する",
            "output": "管理台帳列定義",
            "points": ["2層構造", "基本7列", "受付番号", "人/AI/GAS列の分担"],
        },
        "台帳の品質管理": {
            "axis": "1行1件・1列1項目を守り、入力規則・集計列で台帳崩壊を防ぐ",
            "output": "台帳品質チェック",
            "points": ["崩れる表設計を直す", "マスタシート", "プルダウン", "未対応を集計する"],
        },
        "権限・保存設計と演習レビュー": {
            "axis": "Drive権限・保存場所・命名規則を決め、第3回のGAS準備を終える",
            "output": "権限・保存設計メモ",
            "points": ["閲覧/コメント/編集/オーナー", "共同編集の注意", "保存場所と命名", "GASで扱いやすい台帳レビュー"],
        },
    },
    "03": {
        "導入とGASの位置づけ": {
            "axis": "GASで減らす作業と、人が判断する作業を切り分ける",
            "output": "自動処理の対象範囲メモ",
            "points": ["GASの役割", "やること/やらないこと", "エディタ画面", "権限と情報管理"],
        },
        "JavaScript最小限": {
            "axis": "コード読解に必要な変数・配列・条件分岐・ループだけを押さえる",
            "output": "コード読み替えメモの基礎",
            "points": ["読む順番", "変数と定数", "2次元配列", "条件分岐とループ"],
        },
        "SpreadsheetApp基礎": {
            "axis": "シート・範囲・値・ヘッダーを扱い、台帳を壊さず読み書きする",
            "output": "SpreadsheetApp操作メモ",
            "points": ["4つの階層", "シート取得", "範囲取得", "getValues/setValues"],
        },
        "Excel的処理の自動化": {
            "axis": "抽出・転記・集計・重複チェック・更新・ログを業務処理に落とし込む",
            "output": "自動処理スクリプトとログシート",
            "points": ["対象行抽出", "別シート転記", "Map/Set活用", "ステータス更新とログ"],
        },
        "カスタムメニューとエラー処理": {
            "axis": "現場担当者が押せる実行方法と、止まった時の見方を設計する",
            "output": "カスタムメニュー・テスト観点",
            "points": ["メニュー化", "手動/自動実行", "try/catch", "制限と通知"],
        },
        "演習とレビュー": {
            "axis": "サンプルコードを自分の台帳条件へ読み替え、動かす前にテスト観点を確認する",
            "output": "業務適用版の読み替えメモ",
            "points": ["未対応抽出の演習", "サンプルコード全体構造", "読み替える5項目", "テスト観点"],
        },
    },
    "04": {
        "導入と役割分担": {
            "axis": "GAS・Sheets・Gem/Gemini・人の確認を切り分ける",
            "output": "AIを入れる位置の判断メモ",
            "points": ["第1〜4回の接続", "AIの役割", "自動化しすぎない判断", "情報管理"],
        },
        "Gemini/Gemの使いどころ": {
            "axis": "Workspace連携と貼り付け代替手順を分け、必須演習にしない範囲を確認する",
            "output": "利用可否と代替手順メモ",
            "points": ["GeminiとGem", "有償/管理者設定", "Workspace連携", "貼り付け運用"],
        },
        "Gem設計の型": {
            "axis": "役割・入力・出力形式・禁止事項・判断基準を業務用指示書として固める",
            "output": "Gem設計書",
            "points": ["7項目の型", "役割/文脈/出力形式", "入力データ整備", "判断基準"],
        },
        "業務別ユースケース": {
            "axis": "問い合わせ分類・日報要約・文書要約・コード読解を、台帳反映まで含めて扱う",
            "output": "AI活用プロンプトと出力例",
            "points": ["分類Gem", "返信案と要約", "Meet文字起こし", "コード読解と台帳戻し"],
        },
        "AI出力レビューと運用": {
            "axis": "事実・推測・要確認・利用不可に分け、台帳へ戻す前に人が確認する",
            "output": "出力レビュー表",
            "points": ["4分類レビュー", "参照元確認", "台帳反映前チェック", "改善サイクル"],
        },
        "演習とまとめ": {
            "axis": "自社業務用Gem設計書を仕上げ、第5回の要件定義へつなぐ",
            "output": "Gem設計書・プロンプト・レビュー表",
            "points": ["業務用Gemを選ぶ", "設計書を書く", "出力をレビュー", "次回へ橋渡し"],
        },
    },
    "05": {
        "導入と危機感": {
            "axis": "作った自動化が止まる原因を先に知り、今回の設計範囲を明確にする",
            "output": "運用設計の範囲メモ",
            "points": ["作って終わりのリスク", "設計6層", "典型失敗", "最悪ケース"],
        },
        "要件定義の分解": {
            "axis": "対象業務・利用者・入力元・出力先・AI/GAS/人の役割を6項目で決める",
            "output": "要件定義メモ",
            "points": ["6項目の全体像", "現場の約束事", "対象業務を絞る", "利用者/確認者/入力元"],
        },
        "自動化方式の選定": {
            "axis": "手動・時間トリガー・フォーム送信・Gem/Geminiをリスクで選ぶ",
            "output": "方式選定メモ",
            "points": ["4択と選び方", "手動実行", "時間/フォームトリガー", "Gem/Gemini連携"],
        },
        "権限・制限・情報管理": {
            "axis": "AI入力禁止・匿名化・共有範囲・GAS制限を先に決める",
            "output": "リスクチェックリスト",
            "points": ["入力禁止情報", "匿名化", "権限分離", "GAS制限とスコープ"],
        },
        "ログ・テスト・復旧": {
            "axis": "ログ・エラー分類・テスト観点・復旧手順を、止まった時のために設計する",
            "output": "テストケースと復旧手順",
            "points": ["ログは守るため", "エラー3種類", "テスト6観点", "手動復旧"],
        },
        "演習と次回接続": {
            "axis": "運用設計書とリスクチェックを仕上げ、第6回の提案書に転用する",
            "output": "運用設計書・リスクチェックリスト",
            "points": ["演習で作るもの", "第6回への橋渡し", "提案書セクションへの対応", "自己チェック"],
        },
    },
    "06": {
        "導入と提案書の考え方": {
            "axis": "提案書を作ったものの紹介ではなく、導入判断の材料として設計する",
            "output": "提案書骨子の前提整理",
            "points": ["最終回の位置づけ", "導入判断の材料", "8セクション", "安全確認"],
        },
        "課題整理とユースケース選定": {
            "axis": "誰のどの業務を改善するか、課題・As-Is/To-Be・非対象範囲を絞る",
            "output": "課題/As-Is/To-Be/Gapメモ",
            "points": ["ユースケースを1文で言う", "課題は3つ以内", "As-Is/To-Be", "非対象範囲"],
        },
        "プロトタイプと技術構成": {
            "axis": "第2〜5回の成果物を、技術構成と判断材料として提案書に組み込む",
            "output": "プロトタイプ構成メモ",
            "points": ["判断材料として見せる", "スクリーンショット安全確認", "入力/処理/出力", "Gemini連携と代替運用"],
        },
        "KPIと効果試算": {
            "axis": "控えめで説明可能なKPI・仮試算・測定方法を作る",
            "output": "KPI表と効果試算",
            "points": ["導入後に測るKPI", "控えめな試算", "AI効果の測り方", "GASログで見る"],
        },
        "リスク・運用・ロードマップ": {
            "axis": "リスク、情報管理、役割、段階導入を先に書き、承認しやすい提案にする",
            "output": "リスク対策・運用体制・ロードマップ",
            "points": ["5カテゴリのリスク", "情報管理対策", "役割分担", "段階ロードマップ"],
        },
        "提案書骨子の作成と自己レビュー": {
            "axis": "8セクションの骨子へ自分の業務ケースを当てはめ、講師例と比較する",
            "output": "提案書骨子・自己レビュー",
            "points": ["骨子を組み立てる", "演習で完成", "講師例と比較", "8観点レビュー"],
        },
        "講座後の実践計画": {
            "axis": "全6回の成果物を現場へ持ち帰る順番を決める",
            "output": "次アクションメモ",
            "points": ["講座後の動き", "全成果物をつなぐ", "良い提案書チェック", "振り返り"],
        },
    },
}


def clean_cell(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def parse_sections(text: str) -> list[Section]:
    lines = text.splitlines()
    start_index = next((i for i, line in enumerate(lines) if "120分の時間配分" in line), -1)
    if start_index < 0:
        return []
    sections: list[Section] = []
    for line in lines[start_index + 1 :]:
        if not line.strip().startswith("|"):
            if sections and line.strip():
                break
            continue
        cells = [clean_cell(cell) for cell in line.strip().strip("|").split("|")]
        if len(cells) < 4 or cells[0] in {"ブロック", "大項目", "---"}:
            continue
        range_match = re.search(r"S(\d{2})\s*[–-]\s*S(\d{2})", line)
        if not range_match:
            continue
        sections.append(
            Section(
                name=cells[0],
                minutes=cells[1],
                start=int(range_match.group(1)),
                end=int(range_match.group(2)),
                goal=cells[-1],
            )
        )
    return sections


def parse_slides(text: str) -> tuple[str, list[Slide], str]:
    match = re.search(r"^## スライド詳細\s*$", text, re.MULTILINE)
    if not match:
        raise ValueError("Missing slide detail section")
    preamble = text[: match.end()].rstrip()
    detail = text[match.end() :]
    matches = list(re.finditer(r"^### S(\d{2})\s+(.+)$", detail, re.MULTILINE))
    slides: list[Slide] = []
    postlude_start = len(text)
    for idx, slide_match in enumerate(matches):
        body_start = slide_match.end()
        if idx + 1 < len(matches):
            body_end = matches[idx + 1].start()
        else:
            next_top_heading = re.search(r"^##\s+", detail[body_start:], re.MULTILINE)
            body_end = body_start + next_top_heading.start() if next_top_heading else len(detail)
            postlude_start = match.end() + body_end
        body = detail[body_start:body_end].strip()
        body = re.sub(r"(?:\n\s*---\s*)+\Z", "", body).strip()
        body = re.sub(r"\A(?:\s*---\s*\n)+", "", body).strip()
        slides.append(
            Slide(
                number=int(slide_match.group(1)),
                title=clean_cell(slide_match.group(2)),
                body=body,
            )
        )
    return preamble, slides, text[postlude_start:].strip()


def insertion_positions(sections: list[Section]) -> dict[int, Section]:
    positions: dict[int, Section] = {}
    for section in sections:
        pos = 4 if section.start <= 3 else section.start
        positions[pos] = section
    return positions


def new_number_for_old(old_no: int, positions: list[int]) -> int:
    return old_no + sum(1 for pos in positions if pos <= old_no)


def signpost_number_for_section(section: Section, positions: list[int]) -> int:
    pos = 4 if section.start <= 3 else section.start
    return pos + sum(1 for other in positions if other < pos)


def update_s_refs(text: str, number_map: dict[int, int]) -> str:
    def repl(match: re.Match[str]) -> str:
        no = int(match.group(1))
        return f"S{number_map.get(no, no):02d}"

    return re.sub(r"S(\d{2})", repl, text)


def update_preamble(preamble: str, sections: list[Section], positions: list[int], new_count: int) -> str:
    out = re.sub(r"スライド枚数:\s*\d+枚\s*/\s*120分", f"スライド枚数: {new_count}枚 / 120分", preamble)
    out = re.sub(r"120分・\d+枚構成", f"120分・{new_count}枚構成", out)

    if "スライド枚数:" not in out:
        out = re.sub(
            r"(対象講座:[^\n]+(?:\n|。(?:\n|$)))",
            lambda m: m.group(1).rstrip("。\n") + f"\nスライド枚数: {new_count}枚 / 120分\n",
            out,
            count=1,
        )

    new_ranges = {
        section.name: f"S{(1 if section.start <= 3 else signpost_number_for_section(section, positions)):02d}–S{new_number_for_old(section.end, positions):02d}"
        for section in sections
    }
    lines: list[str] = []
    for line in out.splitlines():
        if line.strip().startswith("|"):
            for section in sections:
                if f"| {section.name} " in line or line.strip().startswith(f"| {section.name} |"):
                    line = re.sub(r"S\d{2}\s*[–-]\s*S\d{2}", new_ranges[section.name], line)
                    break
        lines.append(line)
    return "\n".join(lines)


def agenda_slide(session_no: str, sections: list[Section], slides: list[Slide], positions: list[int]) -> tuple[str, str]:
    meta = SECTION_META[session_no]
    rows = []
    for idx, section in enumerate(sections, 1):
        start = 1 if section.start <= 3 else signpost_number_for_section(section, positions)
        end = new_number_for_old(section.end, positions)
        output = str(meta.get(section.name, {}).get("output", section.goal))
        rows.append(f"| {idx} | {section.name} | {section.minutes} | S{start:02d}–S{end:02d} | {output} |")

    events = []
    event_pattern = re.compile(r"画面共有|実演|演習|ワーク")
    for slide in slides:
        if event_pattern.search(slide.title):
            events.append(f"| S{new_number_for_old(slide.number, positions):02d} | {slide.title} |")
    if not events:
        events.append("| 該当なし | この回はスライド内ワーク中心 |")

    title = f"第{int(session_no)}回の目次/全体像"
    body = "\n".join(
        [
            f"**ヘッドライン:** 今日は{len(sections)}つの章を順番に進み、成果物を作りながら次の回へ接続する",
            "",
            "**内容ブロック①：目次と成果物の全体像**",
            "| No. | 目次項目 | 時間 | スライド範囲 | この章で支える成果物 |",
            "|---:|---|---:|---|---|",
            *rows,
            "",
            "**内容ブロック②：デモ/演習の位置**",
            "| スライド | ここで行うこと |",
            "|---|---|",
            *events[:10],
            "",
            "**内容ブロック③：見方のルール**",
            "- 各章の開始では「章見出し/現在位置」スライドで、今どこを学ぶかを確認する",
            "- 通常スライドでは右上のセクション名とS番号で現在位置を追う",
            "- 章ごとの成果物が、最終的に第6回の提案書へつながる",
            "",
            "- **図解パターン:** roadmap-timeline（目次/全体像）",
            "- **テンプレートID:** isometric-corporate-clean",
            "- **スクリーンショット:** なし",
        ]
    )
    return title, body


def signpost_slide(session_no: str, sections: list[Section], section: Section, positions: list[int]) -> Slide:
    meta = SECTION_META[session_no][section.name]
    idx = sections.index(section) + 1
    total = len(sections)
    prev_name = sections[idx - 2].name if idx > 1 else "表紙・成果物・目次"
    next_name = sections[idx].name if idx < total else "まとめ・次回接続"
    section_start = 1 if section.start <= 3 else signpost_number_for_section(section, positions)
    section_end = new_number_for_old(section.end, positions)
    points = [str(point) for point in meta["points"]]
    body = "\n".join(
        [
            f"**ヘッドライン:** {section.name}では、{meta['axis']}ことで、{meta['output']}につなげる",
            "",
            "**内容ブロック①：目次の中の現在地**",
            "| 位置 | 目次項目 | 時間 | 状態 |",
            "|---|---|---:|---|",
            f"| 前 | {prev_name} | - | ここまで確認済み |",
            f"| 今 | {section.name} | {section.minutes} | S{section_start:02d}–S{section_end:02d}を扱う |",
            f"| 次 | {next_name} | - | 次に接続 |",
            "",
            "**内容ブロック②：これから見る判断軸**",
            *(f"- {point}" for point in points),
            "",
            "**内容ブロック③：成果物・レビューへの接続**",
            f"- この章で支える成果物: {meta['output']}",
            f"- ねらい: {section.goal}",
            "- 見るポイント: 何をAI/GAS/人に任せ、どこを人が確認するかを毎回言語化する",
            "- 次の作業: 章末のデモ・ワーク・自己レビューで、ワークシートへ反映する",
            "",
            "- **図解パターン:** roadmap-timeline（章見出し/現在位置）",
            "- **テンプレートID:** isometric-corporate-clean",
            "- **スクリーンショット:** なし",
        ]
    )
    return Slide(
        number=signpost_number_for_section(section, positions),
        title=f"章見出し/現在位置 {idx}/{total}: {section.name}",
        body=body,
    )


def update_slide_plan(path: Path) -> None:
    session_no = path.parent.name.split("-", 1)[0]
    text = path.read_text(encoding="utf-8")
    sections = parse_sections(text)
    if not sections:
        raise ValueError(f"No sections found: {path}")
    preamble, slides, postlude = parse_slides(text)
    insertions = insertion_positions(sections)
    positions = sorted(insertions)
    number_map = {slide.number: new_number_for_old(slide.number, positions) for slide in slides}
    new_count = len(slides) + len(sections)
    preamble = update_preamble(preamble, sections, positions, new_count)
    agenda_title, agenda_body = agenda_slide(session_no, sections, slides, positions)

    rendered: list[Slide] = []
    for slide in slides:
        if slide.number in insertions:
            rendered.append(signpost_slide(session_no, sections, insertions[slide.number], positions))
        title = agenda_title if slide.number == 3 else update_s_refs(slide.title, number_map)
        body = agenda_body if slide.number == 3 else update_s_refs(slide.body, number_map)
        rendered.append(Slide(number=number_map[slide.number], title=title, body=body))

    parts = [preamble, ""]
    for slide in rendered:
        parts.extend(["---", "", f"### S{slide.number:02d} {slide.title}", slide.body.strip(), ""])
    if postlude:
        parts.extend(["---", "", postlude.strip(), ""])
    path.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")


def main() -> None:
    for slide_plan in sorted(COURSE_DIR.glob("[0-9][0-9]-*/スライド案.md")):
        update_slide_plan(slide_plan)
        print(f"updated {slide_plan}")


if __name__ == "__main__":
    main()
