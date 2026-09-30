# Repository rules

- `students/` is the only home for student submissions, exam copies, named feedback, grades, and local grading records. It is Git ignored. Never stage, commit, or push any student work or identifiable student record, including by force-adding an ignored file.
- Keep downloaded raw datasets and any identifiable records in `data/raw/` or `data/private/`, which are also Git ignored. Commit only documented, reviewed teaching extracts that are permitted for redistribution.
- Keep teaching guides, quizzes, answer keys, and instructor-only grading notes in the ignored `instructor/` directory. Quizzes are printed and completed offline; never put these instructor materials in tracked files.
- Review `git diff --cached --name-only` before every commit. Do not use `git add .` in this repository.
- Keep API keys and other credentials out of all tracked files. Use environment variables.
- Student-facing materials belong on `main`. The `2025-26` branch archives the previous course. Do not copy student work or private grading records to either branch.
