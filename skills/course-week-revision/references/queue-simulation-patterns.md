# Queue simulation teaching patterns

Read this reference when a week develops a queue simulator, generates arrivals from aggregate counts, uses a queueing result to choose scenarios, or asks students to verify simulation code.

## Build the mechanism before generalizing it

- Introduce an event in plain language as an occurrence that changes the system state. Name the actual events in the model.
- Use the domain term consistently. In the call-centre setting, use **agent** in prose, tables, diagrams, and Python variable names rather than alternating with **server**.
- Start with a hand trace for one agent. Then repeat with two agents using the same arrivals and service durations so the staffing effect is visible.
- Include enough arrivals for both agents to become busy and for later callers to wait. A comparison where every wait is zero does not expose the multi-agent rule.
- Keep table columns in the process order students must reason about: arrival, wait, service start, service duration, departure, and assigned agent when applicable.
- Explain the general update rule only after the traces establish what the state variables mean.

## Turn examples into executable checks

- Run the small example through the code, then verify the resulting schedule by hand. Compare assigned agent, service start, wait, and departure for every customer.
- State invariants with observable consequences, such as nonnegative waits, departure equal to start plus service, reproducibility under the same seed, and monotonic responses to slower service or higher demand when other inputs are fixed.
- Introduce a unit test as a small automatic check with a known answer. Convert the hand traces and limiting cases into tests and retain a test whenever a bug is corrected.
- Use tolerant comparisons for computed floating-point times.
- Passing examples and unit tests support the implementation; they do not prove that every implementation path is correct or that the stochastic model represents the real system.

## Record and summarize the system state

Distinguish the population over which each distribution is defined:

- **Across customers:** waiting time and time in system; report the mean, median, selected upper quantiles, and fraction with positive wait.
- **Over time:** queue length; report a time-weighted mean, selected quantiles, maximum, and fraction of time the queue is nonempty.
- **Over time:** number or fraction of agents busy; report time-weighted utilization and the fraction of time exactly 0, 1, ..., c agents are busy.

Record event times and state changes needed for time-weighted summaries. Sampling the state only at event epochs gives a different distribution and must not be presented as the fraction of elapsed time in each state.

## Generate arrivals from aggregate counts

For a parametric Poisson generator, explain the simulation operation rather than saying only “generate exponential gaps”:

1. Define the rate and its units.
2. Draw the time to the next arrival from an exponential distribution whose mean is the reciprocal of the rate.
3. Add the gap to the clock and repeat until the time horizon.

For an empirical bootstrap, make the design choice explicit. Plausible resampling units include a complete comparable day or morning, individual clock intervals, or adjacent blocks. Explain the tradeoff:

- Whole-period profiles retain ordering and shared quiet or busy periods but offer only as many distinct profiles as observed periods.
- Independent interval resampling creates more combinations but breaks dependence between intervals.
- Block resampling retains some local dependence but introduces a block-length and joining choice.

When using a whole-morning or whole-day bootstrap, select one ordered count vector for one simulation repetition and keep its bins in clock order. Do not describe uniform placement of arrivals inside a bin as part of the bootstrap: it is an additional assumption used because aggregate counts omit exact event times.

## Use theory to choose the simulation experiment

Present a reference queueing model before using its result. For an M/M/c model, define the two memoryless assumptions, c parallel agents, FIFO discipline, waiting-room and abandonment assumptions, and the infinite time horizon.

Explain capacity through rates:

- arrival rate: λ;
- service rate per agent: μ;
- combined capacity while all agents are busy: cμ;
- utilization: ρ = λ/(cμ).

State that the infinite-horizon M/M/c queue has a stationary distribution exactly when ρ < 1. This is a capacity screen, not a prediction of short waits in a finite window.

Apply the criterion to the scenario in a separate step. Use it to identify a small range of staffing levels around the capacity boundary. Simulate that range with common arrival and service inputs, then focus the marginal comparison on adjacent staffing levels. This lets theory locate the informative experiment and simulation describe waiting, queue length, occupancy, and unfinished work.

When service times and resource identifiers are available, check the assumed staffing against recorded activity in the same window. Count each resource once at each time. Distinguish the number of distinct resources recorded across the window, the peak number busy at once, and available capacity including idle resources.

## Give the LLM a task with value even when the code is correct

Ask the LLM to design minimal edge cases, state predicted schedules, identify workflow failure modes, or propose independent checks. Include cases such as simultaneous arrivals, agent-availability ties, congestion, excess capacity, and invalid inputs when they apply.

Students must calculate expected valid schedules independently, decide the expected behavior for invalid input, implement useful cases as tests, and correct the LLM when its prediction is unsupported. For workflow audits, trace the conclusion through data selection, fitted model, random generator, queue implementation, and reported summary.
