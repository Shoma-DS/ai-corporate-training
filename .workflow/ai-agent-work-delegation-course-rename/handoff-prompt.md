# Handoff Prompt

Objective: Continue the in-progress rename/update of the Claude Cowork course to the public-facing name `AIエージェントに仕事を任せる業務改善・DX推進講座`, preserving public-repo safety rules and repository-local course workflow rules.

Course path: `講座/AIエージェントに仕事を任せる業務改善・DX推進講座/`

Legacy path/name: `講座/AI業務委任・実行管理DX推進講座/` / `AI業務委任・実行管理DX推進講座`

New subtitle: `Claude Coworkで学ぶ業務整理・作業指示・確認ルール・導入提案`

Current artifacts:
- New course folder exists and contains `全体/`, sessions `01` through `06`, slide plans, scripts, prompts, worksheets, handouts, exercise data, and session 1 slide PNGs.
- `全体/AIエージェントに仕事を任せる業務改善・DX推進講座_パンフレット.html` exists.
- `全体/AIエージェントに仕事を任せる業務改善・DX推進講座_パンフレット.pdf` exists.
- `全体/スライド画像再生成キュー.md` records the session 1 and session 2 slide-image generation/QA status.
- `書き出し/canva-pptx/AIエージェントに仕事を任せる業務改善・DX推進講座/01-業務課題整理とCowork委任設計.pptx` exists as a Canva-import-ready, image-based local PPTX for session 1.
- `書き出し/canva-pptx/AIエージェントに仕事を任せる業務改善・DX推進講座/02-デスクトップ業務環境と情報管理設計.pptx` exists as a Canva-import-ready, image-based local PPTX for session 2.
- `書き出し/canva-pptx/AIエージェントに仕事を任せる業務改善・DX推進講座/03-Coworkによる資料-表計算-ファイル整理実践.pptx` exists as a Canva-import-ready, image-based local PPTX for session 3.

Status table:

| Area | Status | Notes |
| --- | --- | --- |
| Client context | Read | `クライアント指示コンテキスト.md` includes the 2026-06-16 rename instruction. |
| Local course workflow | Read | `skills/corporate-training-course-builder/SKILL.md` is the entrypoint. |
| Pamphlet helper | Read | `skills/course-pamphlet-html-pdf/SKILL.md` governs HTML/PDF conversion and verification. |
| Text rename | Mostly complete | Search the new course folder for old name/subtitle before final delivery. |
| PDF refresh | Complete | Regenerated from the HTML via `skills/course-pamphlet-html-pdf/scripts/html_to_pdf.py`; local PDF text extraction tools were unavailable. |
| Slide images | Session 1 assembled | S01-S40 exist. S05/S10/S30/S31/S35/S39/S40 were regenerated or newly generated with GPT image 2 / built-in image generation and checked by contact sheet. |
| Slide images S10/S30 | Complete | Regenerated on 2026-06-17 with built-in image generation, copied into `スライド画像/S10.png` and `S30.png`, and visually checked for new course name, no old course name, and no real-logo imitation. |
| Session 1 PPTX | Complete | Created with `gws-ai-training-slide-exporter --canva-pptx-only`; verified 40 slides, 40 embedded images, and slide1->image1 through slide40->image40 order. |
| Session 2 slide images | Complete | Generated S01-S40 with built-in image generation, saved under `02-デスクトップ業務環境と情報管理設計/スライド画像/`, and created `.workflow/ai-agent-work-delegation-course-rename/qa/session02-slide-contact-sheet.png`. |
| Session 2 PPTX | Complete | Created with `gws-ai-training-slide-exporter --canva-pptx-only`; verified 40 slides, 40 embedded images, and slide1->image1 through slide40->image40 order. |
| Session 3 slide images | Complete | Generated S01-S40 with built-in image generation, saved under `03-Coworkによる資料-表計算-ファイル整理実践/スライド画像/`, and created `.workflow/ai-agent-work-delegation-course-rename/qa/session03-slide-contact-sheet.png`. |
| Session 3 PPTX | Complete | Created with `gws-ai-training-slide-exporter --canva-pptx-only`; verified 40 slides, 40 embedded images, and slide1->image1 through slide40->image40 order. |
| Public URL memo cleanup | Complete | Removed the public `Canva版スライドURL一覧: 非公開/Canva/Canva_URL一覧.md` memo block from all six `講師台本.md` files. |
| Git finalization | Ignored by current instruction | User instructed to ignore git-related work and continue without stopping for confirmation. |

Public/private constraints:
- Do not copy private Drive originals, client chats, contact details, pricing, credentials, or private URLs into public files.
- Do not stage `非公開/`, source PDFs, `.DS_Store`, credentials, or private links.
- Final `スライド画像/Sxx.png` must be generated bitmap images or approved official screenshots/assets, not local screenshots, PIL/ImageMagick, HTML/CSS, SVG, canvas, or text overlays.

Next verification commands:

```powershell
rg -n "AI業務委任・実行管理DX推進講座|Claude Coworkで学ぶ作業委任設計・権限承認・継続運用" "講座/AIエージェントに仕事を任せる業務改善・DX推進講座"
rg -n "オンラインワークショップ|ハイブリッド|レベル3相当の評価観点|140分|AI業務委任・実行管理DX推進講座|Claude Coworkで学ぶ作業委任設計・権限承認・継続運用" "講座/AIエージェントに仕事を任せる業務改善・DX推進講座/全体/AIエージェントに仕事を任せる業務改善・DX推進講座_パンフレット.html"
```

Latest checks:

- `rg` found old course names only inside `全体/スライド画像再生成キュー.md` explanatory QA notes.
- `rg` found no `オンラインワークショップ`, `ハイブリッド`, `共有指示:`, `チャットでも構いません`, `口頭で共有`, `発表してください`, `今から.*分取ります`, `残り1分`, or `声がけ` in live-instruction contexts. Remaining hits are checklist/meta guidance.
- `rg` found no Canva URL list memo after cleanup. Official source URLs remain only in `全体/調査/出典メモ-Claude-Cowork-AIX-DX-2026-05-31.md`.
- Session 1 Canva-ready PPTX was written to `書き出し/canva-pptx/AIエージェントに仕事を任せる業務改善・DX推進講座/01-業務課題整理とCowork委任設計.pptx`.
- PPTX zip inspection found 40 slide XML files, 40 embedded PNGs, and correct page-to-image order through S40.
- Session 2 slide images S01-S40 were generated and written to `講座/AIエージェントに仕事を任せる業務改善・DX推進講座/02-デスクトップ業務環境と情報管理設計/スライド画像/`.
- Session 2 contact sheet was written to `.workflow/ai-agent-work-delegation-course-rename/qa/session02-slide-contact-sheet.png`.
- Session 2 Canva-ready PPTX was written to `書き出し/canva-pptx/AIエージェントに仕事を任せる業務改善・DX推進講座/02-デスクトップ業務環境と情報管理設計.pptx`, with 40 slide XML files, 40 embedded PNGs, and correct page-to-image order.
- Session 3 slide images S01-S40 were generated and written to `講座/AIエージェントに仕事を任せる業務改善・DX推進講座/03-Coworkによる資料-表計算-ファイル整理実践/スライド画像/`.
- Session 3 contact sheet was written to `.workflow/ai-agent-work-delegation-course-rename/qa/session03-slide-contact-sheet.png`.
- Session 3 Canva-ready PPTX was written to `書き出し/canva-pptx/AIエージェントに仕事を任せる業務改善・DX推進講座/03-Coworkによる資料-表計算-ファイル整理実践.pptx`, with 40 slide XML files, 40 embedded PNGs, and correct page-to-image order.
