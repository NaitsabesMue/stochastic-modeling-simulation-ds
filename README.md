# Stochastic Modeling and Simulation for Data Science

## 2026/27 course

Some questions about a real system cannot be answered from its existing records. Would another agent shorten a call-center queue? Would a machine cope with twice the load? The records describe the system **as it was**, while these questions ask what would happen **after a change**. In this course we observe a process, build a stochastic model, simulate it, compare its output with observed data, revise assumptions that fail, and use the model to assess a decision.

Queueing systems are the worked setting. Students learn to describe random arrivals and service, fit model inputs to data, check simulation uncertainty, compare models, and explain which assumptions drive a recommendation. Coding is in Python. LLMs may be used to suggest code or challenge a theoretical argument; their output must be checked against a derivation, a reproducible computation, or an independent source. Never upload raw customer records or student work to an LLM.

The course has seven three-hour hands-on sessions and ends in a project. Basic Python is required. Some probability and statistics help. The slides and notebooks for Weeks 1–4 are linked below. The `2025-26` branch preserves the previous course materials.

## Course route

| Week | Question | Main activity |
| --- | --- | --- |
| 1 | What do the records show, and what can they not answer? | Diagnose starting level; inspect real arrivals; test a first Poisson model. |
| 2 | How do arrivals and limited servers create a queue? | Build a queue simulation in plain Python. |
| 3 | Is a simulated difference larger than simulation noise? | Quantify uncertainty. |
| 4 | How long does a human agent stay busy? | Fit and check service distributions, then measure how they affect the Week 3 staffing scenario. |
| 5 | Who requests an agent, and how long will they wait? | Build an arrival profile for agent requests, estimate patience from waits and abandonments, and add abandonment to the queue. |
| 6 | Does the combined queue reproduce observed mornings? | Compare predicted and observed waits and abandonment. Compare model variants and test one staffing change. |
| 7 | What decision can the evidence support? | Present and review the complete workflow, sensitivity checks, and conditions for a staffing decision. |

### The final AnonymousBank case

By Week 7, the worked case should trace one morning staffing question from records to a decision. Start with how calls reach an agent. Fit arrival, service, and patience inputs, state the routing and staffing assumptions, and check the queue against later observed mornings. Then compare staffing policies using paired simulations and report how both Monte Carlo error and changes to the model affect the conclusion. If the evidence leaves the choice unresolved, identify what measurement would resolve it.

Week 5 should deliver a working queue with abandonment and reserve later dates for the combined model check. Week 6 should deliver the model comparison and staffing experiment. Week 7 uses these results for the final review. If an eighth session is available, use it to stress test the conclusion across call types or time windows. The main analysis fits within seven sessions.

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

Save your completed notebook and notes under ignored `students/`; never commit or push student work. Start Jupyter from the repository root when running that copy so the loader finds the data. Open the lab in Jupyter or VS Code with a Python 3 kernel. Its code uses the Python standard library, and the included aggregate CSV is enough for week 1. No raw-data download is needed to run it.

## Week 2 materials

- [Lecture slides on queues and capacity](slides/lecture2_queue_basics.pdf)
- [Python lab on building a queue simulator](notebooks/lecture2_queueing.ipynb)

## Week 3 materials

- [Lecture slides on Monte Carlo error and sensitivity](slides/lecture3_error_control_sensitivity.pdf)
- [Python lab on repeated staffing comparisons](notebooks/lecture3_simulation_error_control.ipynb)

## Week 4 materials

- [Lecture slides on fitting service durations](slides/lecture4_parameter_estimation.pdf)
- [Python lab on fitting and checking service models](notebooks/lecture4_parameter_estimation.ipynb)
- [Service duration extract and provenance](data/README.md#week-4-service-duration-summary)

## Private material

`students/` contains local submissions, exam copies, feedback, grades, and grading work. The entire directory is Git ignored and must never be committed or pushed. Teaching guides, printable quizzes, and answer keys belong in the ignored `instructor/` directory; raw source records belong in ignored `data/raw/`. This clone enables the repository's pre-commit guard. In another clone, enable it with `git config --local core.hooksPath .githooks` before committing. Review staged paths before every commit.
