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

Each session begins with a lecture and discussion with **screens closed, phones off, and no side conversations**. Students then work on notebooks and exercises on their own computers. They may discuss the work with their group, but must not copy code or answers. End-of-session printed multiple-choice quizzes take place in the **last ten minutes**, individually without devices or LLMs. The number and schedule of graded quizzes are **to be confirmed**. Quiz sheets and keys are kept outside Git. Week 1 begins with an **ungraded paper diagnostic** so teaching pace can respond to the class.

## Assessment

The number of graded multiple-choice quizzes is **to be confirmed**. Let `N` be the total number scheduled for the class, including any a student misses. An absence gives a score of **0**. Each student has one “free card”: remove the **single lowest** score, whether from an absence or a completed quiz, and average the remaining `N − 1` scores to obtain continuous control (`CC`). Quiz scores are recorded out of 20. Within a quiz, a correct answer earns +1, an incorrect answer earns −1, a blank earns 0, and the written response can earn up to 2 bonus points; scores are bounded between 0 and 20.

`CC = (sum of all N scores − lowest score) / (N − 1)`

`Final mark = (Exam + CC) / 2`

For illustration, if there were six quizzes, scores of `0, 10, 12, 14, 16, 18` give `CC = 14` after dropping the zero. With `Exam = 12`, the final mark is `13`. If a student misses two quizzes, only one zero is removed. The Week 1 entrance diagnostic does not count toward `CC`.

## Week 1 materials

- [Lecture slides](slides/lecture1_motivation.pdf) and [source](slides/lecture1_motivation.tex)
- [Python lab](notebooks/lecture1_poisson_warmup.ipynb)
- [AnonymousBank dataset guide](data/anonymousbank_data_guide.md)
- [Data provenance and rebuild instructions](data/README.md)

The lab uses a non-identifying 15-minute arrival-count extract from the [Technion SEE Lab AnonymousBank data](https://seelab.net.technion.ac.il/data/). It contains November 1999 VRU-entry counts and excludes source-marked `PHANTOM` records. These are entries to the phone system, **not** arrivals to an agent queue. The original archive and row-level records remain outside Git. The source asks users to notify Prof. Avi Mandelbaum or the SEE team and acknowledge the data; see [data notes](data/README.md) before using it in class.

The lab follows the lecture: inspect the 96 unaveraged counts from 1 November, recall the Poisson process, fit one baseline rate to all 2,880 November intervals, check the simulator against theoretical predictions, then compare with the observed data. Time-of-day variation comes first; differences between weekdays are a further check requiring multiple days.

Save your completed notebook and notes under ignored `students/`; never commit or push student work. Start Jupyter from the repository root when running that copy so the loader finds the data. Open the lab in Jupyter or VS Code with a Python 3 kernel. Its code uses the Python standard library, and the included aggregate CSV is enough for week 1. No SimPy installation or raw-data download is needed to run it.

## Private material

`students/` contains local submissions, exam copies, feedback, grades, and grading work. The entire directory is Git ignored and must never be committed or pushed. Teaching guides, printable quizzes, and answer keys belong in the ignored `instructor/` directory; raw source records belong in ignored `data/raw/`. This clone enables the repository's pre-commit guard. In another clone, enable it with `git config --local core.hooksPath .githooks` before committing. Review staged paths before every commit.
