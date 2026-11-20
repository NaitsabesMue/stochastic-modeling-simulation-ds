"""Read local AnonymousBank records for a morning queue experiment."""

import csv
from datetime import datetime
from pathlib import Path
from typing import NamedTuple

from build_anonymousbank_week01 import EXPECTED_COLUMNS


MORNING_START = 9 * 3600
MORNING_END = 11 * 3600
MORNING_SECONDS = MORNING_END - MORNING_START


class AgentRequest(NamedTuple):
    arrival: int
    wait: int
    served: bool | None
    service_type: str


class AgentService(NamedTuple):
    duration: int
    service_type: str


def clock_seconds(clock):
    hour, minute, second = map(int, clock.split(":"))
    return hour * 3600 + minute * 60 + second


def load_mornings(raw_file: Path):
    """Return requests in clock order and service records, grouped by date."""
    requests, services = {}, {}
    with raw_file.open(encoding="latin-1", newline="") as source:
        reader = csv.DictReader(source, delimiter="\t")
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError("Unexpected AnonymousBank columns")
        for row in reader:
            if None in row or None in row.values():
                raise ValueError(f"Invalid field count on line {reader.line_num}")
            date = datetime.strptime(row["date"].strip(), "%y%m%d").date()
            if date.weekday() in (4, 5):  # Friday and Saturday
                continue
            day_requests = requests.setdefault(date, [])
            day_services = services.setdefault(date, [])

            outcome = row["outcome"].strip()
            if outcome == "PHANTOM":
                continue
            if outcome not in {"AGENT", "HANG"}:
                raise ValueError(f"Unexpected outcome on line {reader.line_num}")

            service_type = row["type"].strip()
            service_start = clock_seconds(row["ser_start"]) if outcome == "AGENT" else 0
            if MORNING_START <= service_start < MORNING_END:
                duration = int(row["ser_time"])
                service_exit = clock_seconds(row["ser_exit"])
                if duration < 0 or (service_exit - service_start) % 86_400 != duration:
                    raise ValueError(f"Inconsistent service duration on line {reader.line_num}")
                if duration >= 10:  # Same screening as in Lecture 4.
                    day_services.append(AgentService(duration, service_type))

            queue_start = clock_seconds(row["q_start"])
            request_time = queue_start or service_start
            if not MORNING_START <= request_time < MORNING_END:
                continue
            wait = int(row["q_time"])
            elapsed = clock_seconds(row["q_exit"]) - queue_start if queue_start else 0
            if wait < 0 or wait != elapsed:
                raise ValueError(f"Inconsistent queue duration on line {reader.line_num}")
            served = outcome == "AGENT"
            if served and not service_start:
                served = None
            day_requests.append(AgentRequest(request_time - MORNING_START, wait, served, service_type))

    for calls in requests.values():
        calls.sort(key=lambda call: call.arrival)
    return requests, services
