"""Build a non-identifying 15-minute arrival-count extract for week 1.

Input: data/raw/November1999.txt from the Technion SEE Lab AnonymousBank archive.
Output: data/anonymousbank_nov1999_arrivals_15min.csv.
No customer, call, or agent identifier is read into the output.
"""

from __future__ import annotations

import csv
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent
RAW_FILE = DATA_DIR / "raw" / "November1999.txt"
OUTPUT_FILE = DATA_DIR / "anonymousbank_nov1999_arrivals_15min.csv"
EXPECTED_COLUMNS = [
    "vru+line", "call_id", "customer_id", "priority", "type", "date",
    "vru_entry", "vru_exit", "vru_time", "q_start", "q_exit", "q_time",
    "outcome", "ser_start", "ser_exit", "ser_time", "server",
]


def build_counts(raw_file: Path = RAW_FILE) -> tuple[Counter[tuple[date, int]], int, int]:
    """Count non-PHANTOM VRU entries by local calendar day and quarter-hour."""
    counts: Counter[tuple[date, int]] = Counter()
    records = phantoms = 0

    with raw_file.open(newline="", encoding="latin-1") as source:
        reader = csv.DictReader(source, delimiter="\t")
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError(f"Unexpected AnonymousBank columns in {raw_file}")

        for row in reader:
            records += 1
            outcome = row["outcome"].strip()
            if outcome == "PHANTOM":
                phantoms += 1
                continue
            if outcome not in {"AGENT", "HANG"}:
                raise ValueError(f"Unexpected outcome on data row {records}")

            day = datetime.strptime(row["date"].strip(), "%y%m%d").date()
            if day.year != 1999 or day.month != 11:
                raise ValueError(f"Unexpected date on data row {records}")
            clock = datetime.strptime(row["vru_entry"].strip(), "%H:%M:%S").time()
            quarter = clock.hour * 4 + clock.minute // 15
            counts[(day, quarter)] += 1

    return counts, records, phantoms


def main() -> None:
    if not RAW_FILE.exists():
        raise SystemExit(f"Extract the official archive into {RAW_FILE.parent} first")

    counts, records, phantoms = build_counts()
    start, end = date(1999, 11, 1), date(1999, 12, 1)
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as target:
        writer = csv.writer(target, lineterminator="\n")
        writer.writerow(["date", "time", "entries"])
        day = start
        while day < end:
            for quarter in range(96):
                hour, minute_quarter = divmod(quarter, 4)
                writer.writerow(
                    [day.isoformat(), f"{hour:02d}:{15 * minute_quarter:02d}", counts[(day, quarter)]]
                )
            day += timedelta(days=1)

    if sum(counts.values()) != records - phantoms:
        raise AssertionError("Output count does not match filtered input")
    print(
        f"{OUTPUT_FILE.name}: {records} raw records, {phantoms} PHANTOM records excluded, "
        f"{sum(counts.values())} entries in 2,880 quarter-hour bins"
    )


if __name__ == "__main__":
    main()
