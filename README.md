# Stochastic Models and Simulation for Real-World Systems

<!-- MathJax support for LaTeX in Markdown (local HTML renderers) -->
<script>
window.MathJax = {
  tex: {
    inlineMath: [["$", "$"], ["\(", "\)"]],
    displayMath: [["$$","$$"], ["\[","\]"]],
    processEscapes: true,
    tags: "none"
  },
  options: {
    skipHtmlTags: ["script", "noscript", "style", "textarea", "pre", "code"]
  }
};
</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

This repository hosts materials for an optional M2 Data Science course on Poisson processes, and queueing systems. The course emphasizes intuition, simulation, and real-world modeling rather than formal proofs. The overarching goal is to use data and simulation to make well-argued decisions in the presence of variability (e.g., comparing system designs, parameter choices, or policies).

> **Course Materials & Contributions**  
> These notebooks, slides, and exercises were used in a complete run of the course and remain available for self-study and future iterations. Suggestions, improvements, new notebooks, or extensions are still very welcome—feel free to open a pull request or raise an issue.

## Contents
- Lecture slides (PDF)
  - `slides/lecture1_motivation.pdf` — motivation + Poisson refresher
  - `slides/lecture2_queue_basics.pdf` — queueing theory essentials, M/M queues, non-Markov outlook
  - `slides/lecture3_error_control_sensitivity.pdf` — simulation error control and sensitivity
  - `slides/lecture4_parameter_estimation.pdf` — parameter estimation for stochastic models
  - `slides/lecture5_evaluation_exercise.pdf` — integrated evaluation exercise
  - `slides/lecture6_model_selection_optimisation.pdf` — model selection and optimisation
- Python notebooks (SimPy simulations, estimation, evaluation)
  - `notebooks/SimPy_introduction.ipynb` — quick SimPy warm-up
  - `notebooks/lecture1_poisson_warmup.ipynb` (+ solution)
  - `notebooks/lecture2_queueing.ipynb` (+ solution)
  - `notebooks/lecture3_simulation_error_control.ipynb`
  - `notebooks/lecture4_parameter_estimation.ipynb`
  - `notebooks/lecture5_evaluation_exercise.ipynb` 
  - `notebooks/lecture6_model_selection_optimisation.ipynb`
- Exam and evaluation material in `evaluation/`
- Case-study data and CSV files in `data/`

## Course Format
- 7 sessions, each running for 3 hours
- Mix of theory, discussion, and hands-on coding (mostly in Python)
- Progressive release of notebooks so you can prepare before class

## Assessment
- **Continuous Control (CC)**: mid-term checkpoint combining theoretical questions and a short coding task.
- **Exam / Final Project**:
  - Team or individual project built around a stochastic system of your choice.
  - 10-minute presentation during the final session.
  - Concise written report (~5 pages) summarising model, assumptions, experiments, and insights.
- **Final Mark**:

  $$
  \max\!\left(\text{Exam},\ 0.5\,\text{CC} + 0.5\,\text{Exam}\right)
  $$

  In other words, a strong CC can compensate a weaker final project, but never the opposite.

## Get Started
- Clone this repository and create a Python environment.
- Install the main dependencies, for example:
  - `pip install simpy numpy pandas matplotlib scipy`
- Launch Jupyter (or VS Code) and explore the notebooks in order:
  - optional warm-up: `notebooks/SimPy_introduction.ipynb`
  - lecture notebooks 1–6 to mirror the slides.
