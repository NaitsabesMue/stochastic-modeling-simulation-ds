"""
Generate synthetic event-log data for a dentist clinic.

Conceptual true system (hierarchical):
- Three treatment rooms (chairs) that can host patients in parallel.
- One dentist in the baseline who moves from room to room and performs the
  actual procedures; dental assistants may prepare patients in rooms.
- Arrivals join a single waiting room (outside the treatment rooms). When a
  room becomes free, the next patient is sent from the waiting room into a
  room. The time spent in the waiting room is the queueing time we care about.
- Once in a room, each patient spends a random amount of time there
  (preparation + waiting-in-chair + treatment). This total in-room time is
  modeled as a shifted exponential S = delta + Exp(theta).
- A fraction of patients (priority = 0) are handled with higher priority in
  the waiting room: whenever a room is free, priority patients are taken from
  the waiting room before normal ones (non-preemptive priority).

What we actually simulate here is a single-stage queue with 3 parallel
\"room servers\" whose service times equal the total in-room time. The waiting
room is modeled explicitly via a queue; queue_len_at_arrival counts only
patients still in the waiting room, not those already in rooms.

We simulate several clinic days. Each day:
- Opening hours: 8h (480 minutes) from t = 0 to t = 480.
- New arrivals are allowed only until t = 450 (7h30); after that no new
  arrivals occur but the clinic stays open until all patients of the day
  have been served.

Output:
- CSV file data/dentist_priority_case_study.csv with columns:
  arrival_time, queue_len_at_arrival (waiting room only), service_time,
  start_service_time, completion_time, wait_time, system_time, priority.

This is intended as tutor code; students only see the CSV and an exam notebook.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Optional
import csv

import numpy as np


@dataclass
class Job:
    job_id: int
    arrival_time: float
    service_time: float
    priority: int  # 0 = high priority, 1 = normal
    queue_len_at_arrival: int
    start_service_time: Optional[float] = None
    completion_time: Optional[float] = None

    @property
    def wait_time(self) -> Optional[float]:
        if self.start_service_time is None:
            return None
        return self.start_service_time - self.arrival_time

    @property
    def system_time(self) -> Optional[float]:
        if self.completion_time is None:
            return None
        return self.completion_time - self.arrival_time


def generate_arrivals(
    lambda_rate: float,
    arrival_window: float,
    rng: np.random.Generator,
) -> List[float]:
    """Simulate Poisson arrivals on [0, arrival_window] and return sorted arrival times."""
    t = 0.0
    arrivals: List[float] = []
    while True:
        t += rng.exponential(1.0 / lambda_rate)
        if t > arrival_window:
            break
        arrivals.append(t)
    return arrivals


def simulate_dentist_case(
    lambda_rate: float = 0.24,
    delta: float = 2.0,
    theta: float = 1 / 8.0,
    c: int = 3,
    p_priority: float = 0.1,
    days: int = 5,
    day_length: float = 8 * 60.0,  # 8h per day
    arrival_window: float = 7.5 * 60.0,  # last arrival at 7h30
    seed: int = 1234,
) -> List[Job]:
    """
    Simulate multiple days of a dentist clinic with 3 rooms and a waiting room queue.
    Time unit is minutes; arrival_time is absolute from the beginning of day 0.
    """
    rng = np.random.default_rng(seed)

    jobs: List[Job] = []
    day_offset = 0.0

    for _ in range(days):
        # Generate arrivals for this day in local time [0, arrival_window]
        arrivals_day = generate_arrivals(lambda_rate, arrival_window, rng)

        # State for this day
        t = 0.0
        busy = 0
        completions: List[tuple[float, int]] = []  # (completion_time, job_id)
        prio_queue: List[int] = []  # high-priority waiting-room queue
        norm_queue: List[int] = []  # normal waiting-room queue

        def schedule_service(job_id: int, now: float) -> None:
            nonlocal busy
            job = jobs[job_id]
            busy += 1
            job.start_service_time = day_offset + now
            completion_time = now + job.service_time
            job.completion_time = day_offset + completion_time
            completions.append((completion_time, job_id))
            completions.sort(key=lambda x: x[0])

        i_arr = 0
        n_arr = len(arrivals_day)

        # Process all arrivals for the day and serve until the system empties
        while i_arr < n_arr or completions:
            next_arrival = arrivals_day[i_arr] if i_arr < n_arr else math.inf
            next_completion = completions[0][0] if completions else math.inf
            if next_arrival <= next_completion:
                # Arrival event (during arrival window)
                t = next_arrival
                # Waiting-room queue length (patients not yet in rooms)
                queue_len_waiting = len(prio_queue) + len(norm_queue)
                service_time = delta + rng.exponential(1.0 / theta)
                priority_flag = 0 if rng.random() < p_priority else 1
                job = Job(
                    job_id=len(jobs),
                    arrival_time=day_offset + t,
                    service_time=service_time,
                    priority=priority_flag,
                    queue_len_at_arrival=queue_len_waiting,
                )
                jobs.append(job)
                if busy < c:
                    schedule_service(job.job_id, t)
                else:
                    if priority_flag == 0:
                        prio_queue.append(job.job_id)
                    else:
                        norm_queue.append(job.job_id)
                i_arr += 1
            else:
                # Completion event
                t, job_id = completions.pop(0)
                busy -= 1
                # Assign next from waiting room, priority first
                while busy < c and (prio_queue or norm_queue):
                    if prio_queue:
                        next_id = prio_queue.pop(0)
                    else:
                        next_id = norm_queue.pop(0)
                    schedule_service(next_id, t)

        # Move to next day (absolute time offset)
        day_offset += day_length

    return jobs


def main() -> None:
    jobs = simulate_dentist_case()
    out_path = "data/dentist_priority_case_study.csv"
    fieldnames = [
        "arrival_time",
        "queue_len_at_arrival",
        "service_time",
        "start_service_time",
        "completion_time",
        "wait_time",
        "system_time",
        "priority",
    ]
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for job in jobs:
            if job.start_service_time is None or job.completion_time is None:
                continue
            writer.writerow(
                {
                    "arrival_time": f"{job.arrival_time:.3f}",
                    "queue_len_at_arrival": job.queue_len_at_arrival,
                    "service_time": f"{job.service_time:.3f}",
                    "start_service_time": f"{job.start_service_time:.3f}",
                    "completion_time": f"{job.completion_time:.3f}",
                    "wait_time": f"{job.wait_time:.3f}" if job.wait_time is not None else "",
                    "system_time": f"{job.system_time:.3f}" if job.system_time is not None else "",
                    "priority": job.priority,
                }
            )
    print(f"Generated dataset with {len(jobs)} rows at {out_path}")


if __name__ == "__main__":
    main()
