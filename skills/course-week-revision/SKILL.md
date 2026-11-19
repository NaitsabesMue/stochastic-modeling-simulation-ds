---
name: course-week-revision
description: Revise an existing week of the Stochastic Modeling and Simulation course into a coherent real-data teaching unit, aligning slides, a plain-Python notebook, private instructor guidance, and an offline quiz. Use for Week 2 onward and for later refinements that should preserve the teaching style learned in Week 1.
---

# Course Week Revision

Revise one course week at a time. Treat the current files and the instructor's manual edits as the source of truth. Inspect the working-tree diff before editing and never replace, reformat, clear outputs from, or “clean up” manual changes unless the user asks.

## Course spine

Build the session around a real operational question that existing records alone cannot answer. Make the week advance the course loop:

`observe → model → simulate → validate → decide`

Use real data and concrete decisions at the expense of unnecessary mathematical breadth, while keeping statistical reasoning and model assumptions sound. Use transparent Python that exposes the event and random-number logic. Do not mention discarded software or previous course implementations in student-facing material. Introduce mathematics when it explains a model, a diagnostic, or a decision.

Do not leave a demonstrated model failure hanging without a useful response. Either fit and check a first credible alternative during the same week or state precisely which missing idea will make that possible and when it will be introduced.

## Revision workflow

1. Read `AGENTS.md`, repository status, the current course outline, the complete target-week artifacts, and their diffs. If the week exists only on the archive branch, inspect it with `git show` or `git ls-tree`; do not switch branches in a dirty worktree.
2. State the week's driving decision, the observed evidence, the model contribution, and the boundary of what students can conclude by the end.
3. Check prerequisites against earlier weeks. Reintroduce a prerequisite briefly when students need it in order to act, rather than relying on an unexplained reference.
4. Prepare a coherent first pass across artifacts, then review the slides with the instructor one slide at a time. After each manual edit, reread the current file and preserve it.
5. Keep student-facing facts, terminology, numerical results, formulas, filenames, and policies consistent across slides, notebook, README, data guide, and quiz. Keep solutions and teaching notes private.
6. Run the relevant notebook code from supported working directories, compile every changed TeX source, and visually inspect rendered slides or handouts when layout matters.
7. Remove unfinished placeholders, vague prompts, unexplained thresholds, stale references, accidental local paths, and prose that sounds generated rather than taught. Stop when the material is clear and sufficiently verified.
8. After the slide-by-slide review, compare the first pass with the instructor's later corrections. Promote only reusable lessons into this skill or its references; do not encode one-off wording preferences as universal rules.

## Teaching decisions

- Define domain terms before using them. Distinguish recorded fields, system stages, outcomes, model quantities, and decisions.
- Choose one domain term for each concept and use it consistently in prose, notation, diagrams, and code. Do not alternate between a domain term and a generic technical synonym unless their relationship is explicitly taught.
- Define every mathematical symbol on first use, including its unit or indexing role, and give a concrete numerical example when the notation could hide the model's mechanics.
- Show exactly how a displayed value was produced. State the population, interval, units, filters, pooling, averaging, and whether the display contains raw aggregate observations or a transformed summary.
- Motivate a latent quantity with an observed-data graphic before introducing its distribution. Separate the model definition, parameter fitting, and simulation choice across slides when combining them would hide the reasoning.
- Start with an interpretable baseline whose assumptions students can state. Separate checks of parsing and code from checks of the stochastic model.
- Replace vague instructions such as “check the logic” with an observable procedure: name the input, the expected output or invariant, and what a mismatch would mean.
- Make randomness explicit: expected values are not exact outcomes, seeds change simulated samples rather than model assumptions, and matching a fitted mean is not validation.
- Match model resolution to the amount of data. When fine time bins leave too few repeated observations, pool adjacent bins using training data, state whether boundaries were chosen by eye or by a rule, treat manual boundaries as provisional, and check them on held-out data.
- For arrival-count models, compare held-out means and variances in the periods that drive the decision. A fitted mean alone does not justify a Poisson model. If the variance fails materially, introduce and check a simple source of extra variation, such as a shared day-level rate multiplier, before using the arrivals in a queue experiment.
- When an empirical simulation alternative is useful, state the resampling unit, what is sampled with replacement, what dependence is preserved or broken, and how one resample becomes one simulation repetition. Keep ordered time bins in clock order unless exchangeability is justified. Treat reconstruction of event times inside aggregate bins as a separate assumption. Compare plausible empirical and parametric generators when their choice could affect the decision.
- Use training and held-out data when fitting alternatives. Distinguish time-of-day variation, day-type variation, dependence, and overdispersion.
- When theory supplies a useful diagnostic, introduce the theoretical reference model and its assumptions before presenting the result. Apply the result numerically, state its scope, and use it to select the simulation range. Keep infinite-horizon stability conclusions separate from finite-horizon performance conclusions.
- For simulation outputs, distinguish distributions across entities from distributions over time. Record enough state changes to summarize waiting times, queue length, and resource occupancy rather than reporting only means.
- Show the mean outcome under each policy before discussing changes. Give a comparison of two policy effects its own label and explain which two effects are being subtracted.
- End each analysis with the strongest supported conclusion, the remaining limitation, and the next evidence or model required for a decision.
- For a case that spans several weeks, give each week a result the next one can use. Schedule the combined model check and policy experiment before the project review. Reserve evaluation dates before tuning and state what can be concluded if a required input was never recorded.
- When revisiting estimation, use the earlier fitting routine as a short setup. Give the lab a new question about what the fitted input does to workload, queue performance, or a decision.
- Parse event timestamps as times before filtering records. Check the selection boundary and reconcile recorded durations with their start and end timestamps when both are available.
- Distinguish a cutoff used to screen records from a bound assumed by the model. Use the full retained measurements when fitting unless the lesson gives a reason to transform them.

## LLM use

Frame LLMs as tools for precise delegation, follow-up questions, counterexamples, alternative derivations, and deeper understanding. Give tasks that remain useful when the existing work is correct: design adversarial tests, identify failure modes, trace an inference through the workflow, or propose independent checks. Do not presuppose that a bug or contradiction exists. A fluent one-shot answer may be wrong or merely acceptable. Require students to record the claim or code, assumptions, independent check, correction, and useful follow-up. Never send raw records, identifiers, student work, private assessment material, or answer keys to an LLM.

## Repository boundaries

Follow `AGENTS.md` without exception. Student work belongs only in ignored `students/`. Raw or identifiable data belongs only in ignored `data/raw/` or `data/private/`. Teaching guides, quizzes, solutions, and grading notes belong only in ignored `instructor/`. Student-facing materials belong on `main`; `2025-26` is an archive. Never commit or push unless the user explicitly asks.

For the detailed artifact and review checklist, read [references/artifact-checklist.md](references/artifact-checklist.md) whenever revising a complete week.

When the week includes a queue simulator, capacity reasoning, aggregate-count arrival generation, or simulator testing, also read [references/queue-simulation-patterns.md](references/queue-simulation-patterns.md).
