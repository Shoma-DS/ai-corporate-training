# P6 Aggregate And Verify

Objective: Generate URL indexes and verify the image-first run.

Do:
- Convert private session presentation logs into Markdown and CSV.
- Copy/update indexes under `非公開/Canva/`.
- Copy/update the allowed Drive-side `Canva_URL一覧.csv`.
- Run local workflow and repository safety checks.

Do not:
- Commit or push.
- Add private Canva URLs, design IDs, or credentials to public repo files.

Verification:
- Presentation count equals six sessions.
- Total page count equals 242.
- Session page counts match 42/40/44/40/40/36.
- Manual Magic Layers target memo exists.
- Drive files exist when Drive sync is available.
- `validate_local_skills.py`, workflow verification, and `git diff --check` pass.
