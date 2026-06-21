#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


COURSE_DIR = Path("講座/生成AI・GASで実践する業務変革・DX推進講座")
COURSE_NAME = "生成AI・GASで実践する業務変革・DX推進講座"


@dataclass
class SessionInfo:
    no: int
    folder: str
    title: str
    output: str
    example: str


@dataclass
class Slide:
    no: str
    title: str
    headline: str
    layout: str
    items: list[tuple[str, str]]


SESSIONS: dict[str, SessionInfo] = {
    "01-業務DXの基礎とGoogle Workspace活用設計": SessionInfo(
        1,
        "01-業務DXの基礎とGoogle Workspace活用設計",
        "業務DXの基礎とGoogle Workspace活用設計",
        "業務棚卸しシート、As-Is/To-Beメモ、改善候補選定表",
        "営業事務の見積依頼、製造現場の日報、小売店舗の棚卸しなど、転記・集計・確認・通知が毎週発生する業務",
    ),
    "02-業務データ基盤の設計": SessionInfo(
        2,
        "02-業務データ基盤の設計",
        "業務データ基盤の設計",
        "フォーム設計、台帳設計、マスタ・権限・運用ルールの設計メモ",
        "申請フォーム、問い合わせ受付、作業日報、請求管理のように、入力欄と台帳列のずれが品質低下につながる業務",
    ),
    "03-GASによる業務プロセス自動化": SessionInfo(
        3,
        "03-GASによる業務プロセス自動化",
        "GASによる業務プロセス自動化",
        "自動処理スクリプト、抽出結果シート、処理ログシート、コード読み替えメモ",
        "未請求行の抽出、問い合わせステータス更新、期限超過タスクのリマインドなど、表の同じ操作を繰り返す業務",
    ),
    "04-Gem-Geminiを使った文書作成-分類-要約": SessionInfo(
        4,
        "04-Gem-Geminiを使った文書作成-分類-要約",
        "Gem/Geminiを使った文書作成・分類・要約",
        "文書生成プロンプト、分類ルール、要約レビュー表、人による確認観点",
        "問い合わせ本文、議事録、報告メモをAIで下書き・分類・要約し、最終判断は担当者が行う業務",
    ),
    "05-AI-GAS自動化の要件定義-運用設計": SessionInfo(
        5,
        "05-AI-GAS自動化の要件定義-運用設計",
        "AI/GAS自動化の要件定義・運用設計",
        "要件定義メモ、権限・ログ・例外対応、テストケース、運用設計",
        "自動返信、期限通知、分類補助、レポート作成を、止め方・直し方まで含めて業務に組み込む場面",
    ),
    "06-AI業務効率化プロジェクト提案書の作成": SessionInfo(
        6,
        "06-AI業務効率化プロジェクト提案書の作成",
        "AI業務効率化プロジェクト提案書の作成",
        "AI/GAS導入提案書、KPI仮説、リスク対策、導入ロードマップ",
        "部門長や上司に、なぜその自動化を先に行うのか、効果・リスク・運用体制を説明する場面",
    ),
}


TERM_RULES: list[tuple[str, tuple[str, ...], str, str]] = [
    (
        "Googleフォーム",
        ("Google Forms", "Googleフォーム", "フォーム"),
        "Googleフォームは、入力の入口です。ファミレスのタッチパネル注文機のように、入力する人が直接項目を選ぶため、あとから転記する手間と入力ミスを減らせます。",
        "応用では、必須項目、選択肢、入力制限を先に設計し、集計やGAS処理で迷わないデータにしておきます。",
    ),
    (
        "Googleスプレッドシート",
        ("Google Sheets", "Googleスプレッドシート", "Sheets", "スプレッドシート"),
        "Googleスプレッドシートは、全員が同じ場所を見られる掲示板兼ホワイトボードです。Excelファイルが誰かのパソコンに閉じている状態から、共有された業務台帳へ変わります。",
        "応用では、入力シート、マスタ、出力シート、ログシートを分け、権限と更新ルールを設計します。",
    ),
    (
        "Google Apps Script",
        ("Google Apps Script", "Apps Script", "GAS"),
        "GASは、決まった仕事を自動でこなす事務担当ロボットです。土日も動きますが、例外判断や責任判断は人の仕事として残します。",
        "応用では、トリガー、ログ、例外処理、権限をセットで設計し、動いた後に確認できる状態を作ります。",
    ),
    (
        "Gemini/Gem",
        ("Gemini", "Gem", "Gem/Gemini"),
        "GeminiやGemは、文章の下書き、分類、要約を手伝う補助担当です。新人スタッフのたたき台作成に近く、最終確認は必ず人が行います。",
        "応用では、入力してよい情報、判断させない範囲、根拠確認、NG例をプロンプトに含めます。",
    ),
    (
        "As-Is/To-Be",
        ("As-Is", "To-Be", "現状フロー", "改善後フロー"),
        "As-Isは今の業務の流れ、To-Beは改善後の流れです。部屋の模様替えで、今の動線と新しい動線を比べる作業に近いです。",
        "応用では、AIやGASで置き換える工程だけでなく、人が確認する工程、止める工程、記録する工程も描きます。",
    ),
    (
        "CSV",
        ("CSV",),
        "CSVは、表をカンマ区切りのテキストとして保存したファイルです。見た目は地味ですが、システム間で荷物を受け渡す段ボール箱のような役割をします。",
        "応用では、列名、文字コード、日付形式、空欄、重複を確認し、取り込み後の台帳で壊れない形に整えます。",
    ),
    (
        "マスタ",
        ("マスタ", "master"),
        "マスタは、商品名、担当者、部門名などの正しい一覧表です。住所録や品番表のように、他の表が参照する基準になります。",
        "応用では、誰が更新してよいか、いつ棚卸しするか、古い値をどう扱うかまで決めます。",
    ),
    (
        "API",
        ("API",),
        "APIは、別のシステムと決まった窓口で情報をやり取りする仕組みです。電話の代表番号ではなく、用途ごとに決まった受付窓口だと考えてください。",
        "応用では、認証、利用制限、エラー時の再実行、ログ保存を含めて設計します。",
    ),
    (
        "OAuth/権限",
        ("OAuth", "権限", "スコープ", "アクセス権"),
        "権限は、誰がどの棚を開けてよいかを決める鍵です。便利だからと全員に合鍵を渡すと、情報漏洩や誤操作の原因になります。",
        "応用では、最小権限、共有範囲、承認者、ログ確認をセットで運用します。",
    ),
    (
        "トリガー",
        ("トリガー", "trigger", "Trigger", "onOpen", "installableTrigger"),
        "トリガーは、自動処理を始める合図です。目覚まし時計や玄関チャイムのように、時刻や操作をきっかけにGASを動かします。",
        "応用では、実行タイミング、失敗時の通知、二重実行の防止、手動実行の逃げ道を設計します。",
    ),
    (
        "ログ",
        ("ログ", "Logger", "Logger.log", "処理ログ"),
        "ログは、処理の足あとです。配送伝票の追跡番号のように、いつ何件処理し、どこで止まったかを後から確認できます。",
        "応用では、実行日時、処理件数、エラー内容、担当者が見る場所を決め、属人化を防ぎます。",
    ),
    (
        "JavaScript",
        ("JavaScript", "変数", "配列", "2次元配列", "条件分岐", "ループ", "for...of"),
        "JavaScriptはGASの土台になる言葉です。最初は文法を全部覚えるより、表の行を1行ずつ読み、条件に合う行だけ処理する流れを理解すれば十分です。",
        "応用では、変数、配列、条件分岐、ループを、シート名・列名・抽出条件・出力先へ読み替えて使います。",
    ),
    (
        "SpreadsheetApp",
        ("SpreadsheetApp", "getValues", "setValues", "appendRow", "headerMap"),
        "SpreadsheetAppは、GASからスプレッドシートを操作するための道具箱です。getValuesは表を読む、setValuesはまとめて書く、appendRowは一番下へ追記すると考えてください。",
        "応用では、1行ずつ書くよりまとめて読み書きし、ヘッダー名で列を探すことで、列の並び替えに強いコードにします。",
    ),
    (
        "try/catch",
        ("try/catch", "エラー処理", "例外処理"),
        "try/catchは、処理が転んだときに受け止める安全ネットです。エラーを無視するのではなく、どこで止まったかを記録するために使います。",
        "応用では、利用者向けメッセージ、ログ、再実行手順、管理者への連絡を分けます。",
    ),
    (
        "KPI",
        ("KPI", "効果試算", "ROI"),
        "KPIは、改善が進んでいるかを見るものさしです。体重計の数字のように、感覚ではなく同じ基準で変化を見ます。",
        "応用では、削減時間、エラー件数、処理リードタイム、差し戻し件数など、業務に近い指標へ落とします。",
    ),
    (
        "要件定義",
        ("要件定義", "非対象範囲", "運用設計", "テストケース"),
        "要件定義は、何を作るか、何を作らないか、誰がどう使うかを決める設計図です。工事の前に間取りを決める作業に近いです。",
        "応用では、例外、権限、ログ、テスト、運用担当まで決め、作って終わりにしない状態へ持っていきます。",
    ),
]


def clean(text: str) -> str:
    text = text.replace("`", "")
    text = text.replace("　", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip(" -\n\t")


def short(text: str, limit: int = 110) -> str:
    text = clean(re.sub(r"\|[-:| ]+\|", " ", text))
    text = text.replace("|", " / ")
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "…"


def split_slides(prompt_text: str) -> list[tuple[str, str, str]]:
    matches = list(re.finditer(r"^## Slide (S\d{2})\. (.+)$", prompt_text, re.M))
    slides: list[tuple[str, str, str]] = []
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(prompt_text)
        slides.append((match.group(1), clean(match.group(2)), prompt_text[start:end]))
    return slides


def parse_key_value_block(block: str) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    current_key: str | None = None
    current_value: list[str] = []

    def flush() -> None:
        nonlocal current_key, current_value
        if current_key and current_value:
            value = clean(" ".join(current_value))
            if value:
                items.append((clean(current_key), value))
        current_key = None
        current_value = []

    for raw in block.splitlines():
        line = raw.strip().lstrip("- ").strip()
        if not line:
            continue
        matches = list(re.finditer(r"(^|\s)([^:\n]{1,36}?):\s*", line))
        if not matches:
            if current_key:
                current_value.append(line)
            continue
        for i, match in enumerate(matches):
            prefix = line[: match.start()].strip()
            if i == 0 and prefix and current_key:
                current_value.append(prefix)
            flush()
            current_key = match.group(2)
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(line)
            value = line[start:end].strip()
            current_value = [value] if value else []
    flush()
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

    return []


def parse_prompt(path: Path) -> list[Slide]:
    text = path.read_text(encoding="utf-8")
    slides: list[Slide] = []
    for no, title, section in split_slides(text):
        headline_match = re.search(r"- ヘッドライン:\s*(.+)", section)
        layout_match = re.search(r"- 推奨レイアウト:\s*(.+)", section)
        slides.append(
            Slide(
                no=no,
                title=title,
                headline=clean(headline_match.group(1)) if headline_match else "",
                layout=clean(layout_match.group(1)) if layout_match else "",
                items=parse_items(section),
            )
        )
    return slides


def visible_items(slide: Slide) -> list[tuple[str, str]]:
    skip = ("タイトル", "ヘッドライン", "サブタイトル", "回タイトル")
    return [(k, v) for k, v in slide.items if not k.startswith(skip)]


def speech_label(label: str, index: int) -> str:
    if label.startswith("内容ブロック"):
        return ["ひとつ目の枠", "ふたつ目の枠", "三つ目の枠", "四つ目の枠"][min(index, 3)]
    if label.startswith("|") or re.fullmatch(r"\d+|0|1|2|3|4|5|6", label):
        return ["ひとつ目の行", "次の行", "その次の行", "下の行"][min(index, 3)]
    return f"「{label}」のところ"


def natural_items(slide: Slide, limit: int = 3) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    for key, value in visible_items(slide):
        cleaned = short(value, 130)
        if not cleaned:
            continue
        items.append((speech_label(key, len(items)), cleaned))
        if len(items) >= limit:
            break
    return items


def find_item(slide: Slide, *keys: str) -> str:
    for key, value in slide.items:
        if any(token in key for token in keys):
            return value
    return ""


def detect_terms(slide: Slide) -> list[tuple[str, str, str, str]]:
    text = " ".join([slide.title, slide.headline, slide.layout] + [f"{k} {v}" for k, v in slide.items])
    found: list[tuple[str, str, str, str]] = []
    for rule in TERM_RULES:
        _, triggers, _, _ = rule
        if any(trigger in text for trigger in triggers):
            found.append(rule)
        if len(found) >= 2:
            break
    return found


def position_sentence(slide: Slide) -> str:
    first_items = natural_items(slide, 2)
    if "画面共有" in slide.title or "実演" in slide.title:
        return "画面上の手順に沿って、どの画面を開き、何を確認するのかを順番に見ていきます。下の確認ポイントは、画面共有中に見落としやすいところです。"
    if "比較" in slide.title or "Before" in slide.title or "After" in slide.title or "Before" in slide.headline:
        return "ここは、左側から右側へ順番に見ていきます。左が今のやり方、右が改善後のやり方です。最後に、下の欄で持ち帰る判断ポイントを確認します。"
    if "流れ" in slide.title or "プロセス" in slide.title or "ステップ" in slide.title or "フロー" in slide.headline:
        return "このスライドは、矢印の流れに沿って左から右へ見ていきます。入力、処理、確認、出力がどこで出てくるかを、ひとつずつ確認します。"
    if "リスク" in slide.title or "権限" in slide.title or "確認" in slide.title:
        return "ここは、便利さよりも先に確認しておきたい注意点です。各項目を順番に見ながら、実務に持ち込む前に止める条件、確認する条件を押さえます。"
    if first_items:
        first = first_items[0][0]
        second = first_items[1][0] if len(first_items) > 1 else "下の確認ポイント"
        return f"まず{first}から見ていきます。続いて、{second}に移ります。"
    return "このスライドは、上から順に読むだけではなく、実務で使う順番に確認していきます。"


def content_sentence(slide: Slide) -> str:
    points = natural_items(slide, 3)
    if points:
        if len(points) == 1:
            label, value = points[0]
            return f"{label}では、「{value}」という点を押さえます。"
        chunks = [f"{label}で「{value}」" for label, value in points]
        return "ここでは、" + "、".join(chunks) + "を順番に確認します。"
    if slide.headline:
        return f"このスライドで伝えたいことは、「{slide.headline}」です。"
    return "ここでは、次の作業へ進むために何を確認すればよいかを押さえます。"


def applied_sentence(info: SessionInfo, slide: Slide) -> str:
    text = " ".join([slide.title, slide.headline] + [v for _, v in visible_items(slide)])
    if "リスク" in text or "権限" in text or "情報" in text:
        return "実務では、便利さだけで進めず、個人情報、顧客情報、未公開資料を入れないこと、共有範囲を最小限にすること、出力を人が確認することまでセットで見ます。"
    if "KPI" in text or "効果" in text or "提案" in text:
        return "実務では、削減時間やミス低減だけでなく、誰が運用し、止まったとき誰が直すかまで書くと、導入判断の材料になります。"
    if "コード" in text or "GAS" in text or "SpreadsheetApp" in text:
        return "実務では、コードを丸暗記するより、シート名、列名、条件、出力先、ログの5点を自分の業務に置き換えることが重要です。"
    if "Gemini" in text or "Gem" in text or "プロンプト" in text:
        return "実務では、AIに判断を丸投げせず、下書き、分類候補、要約案を作らせ、人が根拠と表現を確認する流れにします。"
    return f"実務では、{info.example}に置き換えると、このスライドの判断軸をそのまま使えます。"


def term_sentence(slide: Slide) -> str:
    terms = detect_terms(slide)
    if not terms:
        return ""
    chunks: list[str] = []
    for _, _, simple, advanced in terms:
        chunks.append(simple + " " + advanced)
    return "ここで、言葉の確認をしておきます。" + " ".join(chunks)


def closing_sentence(info: SessionInfo, slide: Slide) -> str:
    number = int(slide.no[1:])
    variants = [
        "聞きながら、自分の業務ではどこが入力で、どこが処理で、どこを人が確認するのかを当てはめてみてください。",
        "あとで見返すときは、ツール名よりも、業務の流れのどこを変える話だったかを思い出すと整理しやすくなります。",
        f"この考え方は、{info.example}のような業務にも置き換えられます。自社で近い作業がないかを考えながら見てください。",
        "ここで確認したことは、このあとの画面共有やワークでそのまま使います。いったん全体像をつかむことを優先しましょう。",
    ]
    return variants[number % len(variants)]


def work_instruction(info: SessionInfo, slide: Slide) -> str:
    trigger_text = " ".join([slide.title, slide.headline] + [k for k, _ in visible_items(slide)])
    if not any(token in trigger_text for token in ("ワーク", "演習", "自己レビュー", "記入", "完成", "棚卸し", "提案書骨子")):
        return ""
    minutes = "5"
    if "棚卸し" in trigger_text or "As-Is" in trigger_text or "To-Be" in trigger_text or "提案書" in trigger_text:
        minutes = "10"
    if "自己レビュー" in trigger_text or "確認" in trigger_text:
        minutes = "5"
    return (
        "ワーク指示:\n"
        f"「ここで動画を一時停止して、ワークシートの該当欄に{minutes}分ほど取り組んでください。"
        f"完成度よりも、{info.output}に向けて、入力、処理、出力、確認のどこが曖昧かを見つけることを優先します。"
        "書けたら再生して、講師の記入例と比べてください。」"
    )


def demo_steps(info: SessionInfo, slide: Slide, demo_no: int) -> tuple[str, int, list[str], str]:
    title = re.sub(r"^画面共有\s*[──:：-]*\s*", "", slide.title).strip("「」 ")
    title = re.sub(r"^実演\d+\s*", "", title).strip("「」 ")
    if not title:
        title = f"{info.title}の実演{demo_no}"
    text = " ".join([slide.title, slide.headline] + [v for _, v in visible_items(slide)])
    if info.no == 1:
        steps = [
            "スライドを表示したまま、実演で使うダミーCSVとワークシートの位置を示す。実業務データは映さず、架空データだけを使うと説明する。",
            "画面をダミーCSVまたはサンプルシートへ切り替え、列整形、重複確認、未対応抽出のどこに時間がかかるかを声に出して確認する。",
            "再びスライドへ戻り、中央のカードにある業務棚卸し、As-Is/To-Be、改善候補選定のどこへ記録するかを示す。",
        ]
        point = "手作業を否定するのではなく、どの作業が定型化でき、どこに人の確認が残るかを分けて見る。"
    elif info.no == 2:
        steps = [
            "ダミーのGoogleフォーム、回答スプレッドシート、マスタ表を順に開き、入力項目と台帳列がどう対応するかを示す。",
            "必須項目、選択肢、入力制限、担当者マスタを確認し、自由入力を減らすほど後工程の集計とGAS処理が安定することを説明する。",
            "共有範囲と編集権限を確認し、誰が入力し、誰が修正し、誰が閲覧だけにするかを画面上で示す。",
        ]
        point = "フォームと台帳は別物ではなく、入力の入口と業務台帳を1本の流れとして設計する。"
    elif info.no == 3:
        steps = [
            "演習用スプレッドシートを開き、入力シート、出力シート、処理ログシートの3つを確認する。",
            "Apps Scriptエディタへ切り替え、シート名、ヘッダー名、抽出条件、出力先、ログ追記の位置をコード内で指し示す。",
            "実行ボタンまたはカスタムメニューを使い、抽出結果と処理ログが更新される様子を確認する。失敗時はログを見ると説明する。",
        ]
        point = "GASは魔法ではなく、表の読み取り、条件判定、書き込み、ログ記録を順番に行う事務ロボットだと理解する。"
    elif info.no == 4:
        steps = [
            "ダミーの問い合わせ文、報告メモ、議事録サンプルを開き、Gemini/Gemへ入力してよい範囲を確認する。",
            "プロンプト例を入力し、分類候補、要約案、返信下書きが出る流れを見せる。個人情報や社外秘は入れないと説明する。",
            "出力結果をそのまま採用せず、根拠、表現、漏れ、誤分類を人がレビューするチェック表へ戻す。",
        ]
        point = "AIの役割は最終判断ではなく、下書きと整理の補助。人が確認する前提で業務フローに入れる。"
    elif info.no == 5:
        steps = [
            "要件定義メモ、権限保存設計サンプル、テストケースサンプルを開き、入力、処理、出力、確認者を順に確認する。",
            "トリガー、権限、ログ、例外対応の欄を見せ、便利さだけでなく止め方と直し方を書く理由を説明する。",
            "テストケースを1件読み、正常系、例外系、権限不足、データ欠損をどう確認するかを画面上でたどる。",
        ]
        point = "自動化は作成後の運用で差が出る。要件、権限、ログ、テストを先に決めるほど、現場で止まりにくくなる。"
    else:
        steps = [
            "提案書材料、KPI効果試算、リスク対策サンプルを開き、提案書へ転記する情報と入れない情報を分ける。",
            "提案書骨子の記入例を見せ、課題、As-Is/To-Be、解決策、非対象範囲、KPI、リスク、導入順序のつながりを確認する。",
            "自己レビュー欄を開き、根拠が弱い箇所、運用担当が曖昧な箇所、情報管理上の注意が抜けている箇所を見直す。",
        ]
        point = "提案書は熱意を伝える資料ではなく、導入判断に必要な根拠、リスク、運用条件をそろえる資料として見る。"
    if "KPI" in text or "効果" in text:
        steps[1] = "KPI効果試算サンプルを開き、削減時間、処理件数、エラー件数、リードタイムのどれを根拠にするかを確認する。"
    duration = 4 if len(steps) >= 3 else 3
    return title, duration, steps, point


def screen_share_block(info: SessionInfo, slide: Slide, demo_no: int) -> str:
    title, duration, steps, point = demo_steps(info, slide, demo_no)
    per_step = max(45, int(duration * 60 / len(steps)))
    label = f"約{per_step}秒" if per_step < 60 else f"約{round(per_step / 60)}分"
    lines = [f"画面共有 ── 実演{demo_no}「{title}」", f"⏱ 約{duration}分", ""]
    for i, step in enumerate(steps, start=1):
        lines.append(f"【手順{i} – {label}】")
        lines.append(step)
        lines.append("")
    lines.append("【見せるポイント】")
    lines.append(point)
    return "\n".join(lines).rstrip()


def needs_screen_share(slide: Slide) -> bool:
    text = " ".join([slide.title, slide.headline] + [f"{k} {v}" for k, v in visible_items(slide)])
    return "画面共有" in text or "実演" in slide.title


def build_reading(info: SessionInfo, slide: Slide, is_first: bool) -> str:
    paragraphs: list[str] = []
    if is_first:
        paragraphs.append(
            f"この講座は「{COURSE_NAME}」です。今回は第{info.no}回「{info.title}」を進めます。"
            f"この回では、{info.output}を持ち帰れる状態を目指します。"
        )
    if slide.headline:
        paragraphs.append(f"このスライドでは、まず上の大きな一文をご覧ください。「{slide.headline}」というところです。")
    paragraphs.append(position_sentence(slide))
    paragraphs.append(content_sentence(slide))
    term = term_sentence(slide)
    if term:
        paragraphs.append(term)
    paragraphs.append(applied_sentence(info, slide))
    paragraphs.append(closing_sentence(info, slide))
    return " ".join(paragraphs)


def build_script(info: SessionInfo, slides: list[Slide], existing_prep: str = "") -> str:
    lines: list[str] = [
        f"# 第{info.no}回 講師台本: {info.title}",
        "",
        f"講座タイトル: {COURSE_NAME}",
        "",
        "## この台本の使い方",
        "",
        "この台本は画面録画による動画講座用です。ライブ配信ではありません。",
        "各スライドのスピーカーノートに入る本文は、`スライド切替:` 以降の `Sxx「タイトル」` ブロックです。",
        "画面共有は、ダミーデータまたは公式公開画面だけを使い、実在会社名、顧客名、個人名、メールアドレス、価格、連絡先、社内固有情報は映しません。",
        "",
        "## 準備物",
        "",
    ]
    if existing_prep:
        lines.extend(existing_prep.splitlines())
    else:
        lines.extend(
            [
                f"- 第{info.no}回スライド S01-S{len(slides):02d}",
                "- ワークシートまたはテキストメモ",
                "- 演習データフォルダ内の架空データ",
                "- ダミー環境のGoogleアカウント",
            ]
        )
    lines.extend(["", "講師メモ:", "（録画前に、ブラウザの履歴、アカウント名、通知、実データが画面に映らないことを確認する。）", ""])

    demo_no = 1
    for idx, slide in enumerate(slides):
        lines.extend(["スライド切替:", f"{slide.no}「{slide.title}」", ""])
        lines.extend(["読み上げ:", f"「{build_reading(info, slide, idx == 0)}」", ""])
        if needs_screen_share(slide):
            lines.extend([screen_share_block(info, slide, demo_no), ""])
            demo_no += 1
        work = work_instruction(info, slide)
        if work:
            lines.extend([work, ""])
        lines.extend(
            [
                "講師メモ:",
                "（読み上げない。専門用語を説明するときは、スライド中央のカード名を指してから、実務例に置き換える。）",
                "",
            ]
        )

    lines.extend(["## スライド切替タイムライン", "", "| No. | タイトル | 重点説明 |", "| --- | --- | --- |"])
    for slide in slides:
        lines.append(f"| {slide.no} | {slide.title} | {short(slide.headline or content_sentence(slide), 80)} |")
    return "\n".join(lines).rstrip() + "\n"


def existing_prepare(script_path: Path) -> str:
    if not script_path.exists():
        return ""
    text = script_path.read_text(encoding="utf-8")
    match = re.search(r"## 準備物\n\n(.*?)(?:\n\n講師メモ:|\n\nスライド切替:|\n\n##)", text, re.S)
    if not match:
        return ""
    lines: list[str] = []
    for line in match.group(1).strip().splitlines():
        if "発表レビュー観点.csv" in line:
            lines.append("- レビュー観点CSV（実演5で使用。第6回演習データ内の架空データ）")
        else:
            lines.append(line)
    return "\n".join(lines)


def rebuild_session(session_dir: Path) -> None:
    info = SESSIONS[session_dir.name]
    prompt_path = session_dir / "画像生成プロンプト.md"
    script_path = session_dir / "講師台本.md"
    slides = parse_prompt(prompt_path)
    if not slides:
        raise SystemExit(f"No slides parsed: {prompt_path}")
    script = build_script(info, slides, existing_prepare(script_path))
    script_path.write_text(script, encoding="utf-8")
    print(f"rebuilt {session_dir.name}: {len(slides)} slides")


def main() -> None:
    for folder in sorted(SESSIONS):
        rebuild_session(COURSE_DIR / folder)


if __name__ == "__main__":
    main()
