# Stochastic Modeling and Simulation for Data Science

**2026/27 · Six three-hour sessions**

Would another agent shorten the queue at a bank’s call centre? You’ll use the AnonymousBank call records to build a simulation in Python and see how well it reproduces what the bank observed. Over the course, you’ll model arrivals, service times and how long callers are willing to wait. You’ll compare staffing options and explain how much confidence you have in the results.

You should know basic Python. Some probability and statistics will help.

## Before the first session

1. Fork this repository on GitHub and clone your fork. The first notebook shows how to get course updates and set up a local Python environment. [Week 1 notebook and setup](notebooks/lecture1_poisson_warmup.ipynb)
2. Open a copy of the notebook in `students/`. If you use Jupyter, launch it from the repository root. VS Code or another editor that runs Python notebooks is fine.
3. Keep your notebook copies, answers and notes in `students/`. Git ignores this folder. Never commit or push your work.

## In class

- **Lecture.** Close your screen, turn off your phone and save side conversations for the lab.
- **Lab.** Work on your own computer. You can discuss the exercises with your group. Write your own code and answers.

During the lab, you can ask an LLM for a test case or use it to examine a step in an argument. Check any suggestion with a calculation, a Python test or an independent source. Be ready to explain the reasoning yourself. Keep raw call records and student work out of your prompts.

## Evaluation

**Thursday 3 December 2026, 2:00–5:00 p.m.**

- **2:00–2:10 p.m.** Complete an individual multiple-choice quiz.
- **2:10–5:00 p.m.** Work in a group of up to three on a real-world problem. Use the modelling and simulation methods from the course to investigate the problem and explain what your results show.

The Week 1 entrance diagnostic was ungraded.

## Slides and notebooks

| Week | Topic | Slides | Notebook |
| --- | --- | --- | --- |
| 1 | Test a Poisson model for call arrivals | [Slides](slides/lecture1_motivation.pdf) | [Lab](notebooks/lecture1_poisson_warmup.ipynb) |
| 2 | Build a queue simulator and explore what happens as demand grows | [Slides](slides/lecture2_queue_basics.pdf) | [Lab](notebooks/lecture2_queueing.ipynb) |
| 3 | Estimate how much another agent reduces waiting and measure the simulation error | [Slides](slides/lecture3_error_control_sensitivity.pdf) | [Lab](notebooks/lecture3_simulation_error_control.ipynb) |
| 4 | Fit service times and see how the choice of distribution affects waiting | [Slides](slides/lecture4_parameter_estimation.pdf) | [Lab](notebooks/lecture4_parameter_estimation.ipynb) |
| 5 | Model callers who hang up while waiting. Compare arrival and service models using the call log | [Slides](slides/lecture5_evaluation_exercise.pdf) | [Lab](notebooks/lecture5_evaluation_exercise.ipynb) |
| 6 | Check the combined model on December records and revisit the staffing decision | [Slides](slides/lecture6_model_selection_optimisation.pdf) | [Lab](notebooks/lecture6_model_selection_optimisation.ipynb) |

Week 6 includes a project review. Bring one decision from your project. Show how you checked your model, give your estimate with its simulation uncertainty and explain what evidence might change your conclusion.

## Data for the labs

The AnonymousBank data come from the Technion SEE Lab. Weeks 1–4 use the files included here. In Week 1, each count records calls entering the automated phone menu during a 15-minute interval. [AnonymousBank dataset guide](data/anonymousbank_data_guide.md)

For Week 5 you’ll need `November1999.txt`. For Week 6 you’ll also need `December1999.txt`. Download the archive and extract both files into the Git-ignored `data/raw/` folder. [Download and setup instructions](data/README.md#rebuild-and-verify)
