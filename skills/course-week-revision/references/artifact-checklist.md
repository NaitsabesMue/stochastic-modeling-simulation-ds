# Artifact and review checklist

Use this checklist for a complete weekly revision. Adapt it to the week's actual learning goal; do not create an artifact merely to satisfy the list.

## Slides

- Open with what the topic enables students to understand or decide.
- Give one driving question and maintain a visible connection to the course loop.
- Prefer a meaningful diagram, timeline, table, or data plot to decorative visuals.
- Give each slide one main teaching job. Remove overlap between motivation, method, and summary slides.
- Define acronyms, codes, fields, and mathematical symbols before relying on them.
- Label plots with units and the exact aggregation. Say whether a point is one observation, a mean over days, a moving average, or a simulation result.
- If a model is fitted to pooled data, name what was pooled and why the baseline is intentionally simple.
- Show important simulation results rather than only telling students what they should see.
- Distinguish a simulator check from a model validation check.
- Preserve citations, dataset provenance, privacy limits, and the repository link.
- Compile and inspect the PDF after every material layout change.

## Notebook

- State the driving question, data meaning, and the limits of inference.
- Link to the dataset guide instead of duplicating an incomplete data dictionary.
- For Week 1, include repository, local environment, and ignored student-copy setup. Later weeks may link back to those instructions.
- Use short sections that follow observe, model, simulate, validate, decide.
- Ask students to predict or explain before showing an answer when that reveals understanding.
- Make prompts concrete: name the output, comparison, units, and evidence expected.
- Include at least two substantive, scaffolded code-completion blocks in a hands-on notebook. Remove code at steps central to the week's learning, state the required inputs and outputs, and leave enough surrounding code to test the result.
- Explain Python expressions that are likely to be unfamiliar, especially indexing, binning, generators, and random-number logic.
- For calculations on binned data, identify which bins go into each total before asking students to write the slices.
- Use deterministic seeds for reproducibility, then vary seeds to teach simulation noise. Never tune a seed to resemble observed data.
- Check input structure and documented totals before modelling. Avoid assertions tied to a dataset without explaining why they are specific to it.
- Keep code executable from the documented working directory. Use standard-library Python unless an added package is pedagogically justified.
- Do not include solutions in the public notebook. Keep solution material in `instructor/` or another ignored location.

## Private teaching guide

- Give a timed three-hour run of show, including the screen-free opening, computer work, break, and final offline quiz.
- Include diagnostic branches for different student starting levels.
- Record expected numerical results, likely misconceptions, and the boundary of acceptable conclusions.
- Explain how the week connects backward and forward in the course.
- Keep the guide in ignored `instructor/` and never link it as a public course artifact.

## Offline quiz and solution

- Keep all quiz sources, PDFs, keys, and solutions in ignored `instructor/`.
- Test only ideas taught in the slides or completed notebook.
- Use 20 Yes/No statements when the quiz uses the established 0–20 scheme.
- Align question numbers, Yes boxes, No boxes, and wrapped statement text in fixed columns.
- For future quizzes: correct choice only earns +1; wrong choice only earns −1; neither choice earns 0; both choices earn −1. Random guessing must have no positive expected score.
- A written reflection may earn up to 2 bonus points; bound the recorded score at 20.
- Provide a separate solution PDF with a visible boxed X on the correct choice and a private reasoning key.
- Compile and visually inspect both student and solution sheets. Keep each readable and preferably one page.

## Consistency pass

Before handoff, compare all artifacts for:

- terminology and acronyms;
- learning outcomes and task numbering;
- formulas, units, filters, sample sizes, and numerical results;
- course and quiz rules;
- filenames, links, and execution paths;
- privacy and LLM instructions;
- claims about what the data can and cannot answer.

Report what changed, why, how it was checked, and any unresolved teaching choice. Do not commit, push, or publish without explicit authorization.
