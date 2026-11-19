"""Summarize AnonymousBank morning services without exporting call records."""

from bisect import bisect_right
import csv
from datetime import datetime
import json
from pathlib import Path

from build_anonymousbank_week01 import EXPECTED_COLUMNS

DATA_DIR = Path(__file__).resolve().parent
RAW_FILE = DATA_DIR / "raw" / "November1999.txt"
OUTPUT_FILE = DATA_DIR / "anonymousbank_nov1999_morning_service_summary.json"
LOWER_EDGES = (0, 10, 30, 60, 90, 120, 180, 240, 360, 480, 600, 900, 1200, 1800)
LONG_SERVICE_SECONDS = 600


def seconds(clock):
    time = datetime.strptime(clock, "%H:%M:%S").time()
    return time.hour * 3600 + time.minute * 60 + time.second


def build_summary(raw_file=RAW_FILE):
    splits = {
        name: {
            "counts": [0] * len(LOWER_EDGES),
            "sum_seconds": 0,
            "sum_squared_seconds": 0,
            "service_groups": {
                category: {"retained_count": 0, "service_seconds": 0,
                           "long_count": 0, "long_seconds": 0}
                for category in ("regular_banking", "other_services")
            },
        }
        for name in ("training", "held_out")
    }
    with raw_file.open(encoding="latin-1", newline="") as source:
        reader = csv.DictReader(source, delimiter="\t")
        if reader.fieldnames != EXPECTED_COLUMNS:
            raise ValueError("Unexpected AnonymousBank columns")
        for row in reader:
            if None in row or None in row.values():
                raise ValueError(f"Invalid field count at line {reader.line_num}")
            if row["outcome"].strip() != "AGENT":
                continue
            day = datetime.strptime(row["date"].strip(), "%y%m%d").date()
            if (day.year, day.month) != (1999, 11):
                raise ValueError(f"Unexpected date at line {reader.line_num}")
            if day.weekday() in (4, 5):  # Friday and Saturday
                continue
            start = seconds(row["ser_start"].strip())
            if not 9 * 3600 <= start < 11 * 3600:
                continue

            duration = int(row["ser_time"])
            end = seconds(row["ser_exit"].strip())
            # Reject inconsistent records for review instead of silently changing them.
            if duration < 0 or (end - start) % 86_400 != duration:
                raise ValueError(f"Inconsistent service duration at line {reader.line_num}")
            split = splits["training" if day.day <= 14 else "held_out"]
            bin_index = bisect_right(LOWER_EDGES, duration) - 1
            split["counts"][bin_index] += 1
            if duration >= LOWER_EDGES[1]:
                split["sum_seconds"] += duration
                split["sum_squared_seconds"] += duration**2
                category = (
                    "regular_banking" if row["type"].strip() in {"PS", "PE"}
                    else "other_services"
                )
                group = split["service_groups"][category]
                group["retained_count"] += 1
                group["service_seconds"] += duration
                if duration >= LONG_SERVICE_SECONDS:
                    group["long_count"] += 1
                    group["long_seconds"] += duration

    return {"lower_edges_seconds": LOWER_EDGES,
            "long_service_seconds": LONG_SERVICE_SECONDS, **splits}


def main():
    if not RAW_FILE.is_file():
        raise SystemExit("Extract November1999.txt into data/raw/ first. See data/README.md.")
    summary = build_summary()
    OUTPUT_FILE.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
