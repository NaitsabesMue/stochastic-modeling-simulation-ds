# Stochastic Modeling and Simulation for Data Science

## 2026/27 course

Some questions about a real system cannot be answered from its existing records. Would another agent shorten a call-center queue? Would a machine cope with twice the load? The records describe the system **as it was**, while these questions ask what would happen **after a change**. In this course we observe a process, build a stochastic model, simulate it, compare its output with observed data, revise assumptions that fail, and use the model to assess a decision.

Queueing systems are the worked setting. Students learn to describe random arrivals and service, fit model inputs to data, check simulation uncertainty, compare models, and explain which assumptions drive a recommendation. Coding is in Python without SimPy. LLMs may be used to suggest code or challenge a theoretical argument; their output must be checked against a derivation, a reproducible computation, or an independent source. Never upload raw customer records or student work to an LLM.

The course has seven three-hour hands-on sessions and ends in a project. Basic Python is required; some probability and statistics help. **Only week 1 has teaching materials on `main` so far.** Weeks 2–7 have the outline below, but their materials still need to be developed. Previous slides, notebooks, case data, and evaluation files are preserved on the `2025-26` branch.

## Course route

| Week | Question | Main activity |
| --- | --- | --- |
| 1 | What do the records show, and what can they not answer? | Diagnose starting level; inspect real arrivals; test a first Poisson model. |
| 2 | How do arrivals and limited servers create a queue? | Build a queue simulation in plain Python. |
| 3 | Is a simulated difference larger than simulation noise? | Quantify uncertainty. |
| 4 | Which input distributions are supported by the records? | Estimate and check model inputs. |
| 5 | Where does the model fail, and which alternative helps? | Validate and select a model. |
| 6 | Would a proposed change improve the system? | Run and interpret policy experiments. |
| 7 | What decision can the evidence support? | Present and critique projects. |

Each session begins with a lecture and discussion with **screens closed, phones off, and no side conversations**. Students then work on notebooks and exercises on their own computers. They may discuss the work with their group, but must not copy code or answers. In sessions 1–6, the **last ten minutes** are a printed multiple-choice quiz, completed individually without devices or LLMs. Session 7 ends with the project instead of a continuous-control quiz. Quiz sheets and keys are kept outside Git. Week 1 begins with an **ungraded paper diagnostic** so teaching pace can respond to the class.

## Assessment

There is one graded multiple-choice quiz at the end of each of the first **six** sessions. An absence gives a score of **0** for that quiz. Each student has one “free card”: the **single lowest** quiz score is removed, whether it came from an absence or a completed quiz. Continuous control (`CC`) is the average of the other **five** scores. All quiz and exam scores are out of 20.

`CC = (q₁ + q₂ + q₃ + q₄ + q₅ + q₆ − lowest quiz score) / 5`

`Final mark = (Exam + CC) / 2`

For example, quiz scores of `0, 12, 13, 14, 15, 16` give `CC = 14` after dropping the zero. With `Exam = 12`, the final mark is `13`. If a student misses two quizzes, only one zero is removed. The Week 1 entrance diagnostic does not count toward `CC`.

## Week 1 materials

- [Lecture slides](slides/lecture1_motivation.pdf) and [source](slides/lecture1_motivation.tex)
- [Python lab](notebooks/lecture1_poisson_warmup.ipynb)
- [AnonymousBank dataset guide](data/anonymousbank_data_guide.md)
- [Data provenance and rebuild instructions](data/README.md)

The lab uses a non-identifying 15-minute arrival-count extract from the [Technion SEE Lab AnonymousBank data](https://seelab.net.technion.ac.il/data/). It contains November 1999 VRU-entry counts and excludes source-marked `PHANTOM` records. These are entries to the phone system, **not** arrivals to an agent queue. The original archive and row-level records remain outside Git. The source asks users to notify Prof. Avi Mandelbaum or the SEE team and acknowledge the data; see [data notes](data/README.md) before using it in class.

Open the lab in Jupyter or VS Code with a Python 3 kernel. Its code uses the Python standard library, and the included aggregate CSV is enough for week 1. No SimPy installation or raw-data download is needed to run it.

## Private material

`students/` contains local submissions, exam copies, feedback, grades, and grading work. The entire directory is Git ignored and must never be committed or pushed. Teaching guides, printable quizzes, and answer keys belong in the ignored `instructor/` directory; raw source records belong in ignored `data/raw/`. This clone enables the repository's pre-commit guard. In another clone, enable it with `git config --local core.hooksPath .githooks` before committing. Review staged paths before every commit.
