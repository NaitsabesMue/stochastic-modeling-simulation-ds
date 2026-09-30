# AnonymousBank teaching extract

Start with the student-facing [AnonymousBank data guide](anonymousbank_data_guide.md) for the call journey, definitions of VRU and each outcome, all 17 raw fields, a redacted raw-data example, and the limits of the Week 1 extract. This file documents how the public aggregate was built and checked.

Week 1 uses [`anonymousbank_nov1999_arrivals_15min.csv`](anonymousbank_nov1999_arrivals_15min.csv), an aggregate made from the November 1999 file in the [Technion SEE Lab AnonymousBank archive](https://seelab.net.technion.ac.il/data/). The [source documentation](https://see-center.iem.technion.ac.il/databases/AnonymousBank/Data/AnonymousBank.pdf) describes the 17 fields in each call record. The archive includes caller and agent identifiers; the teaching extract contains only `date`, local `time` (start of a 15-minute interval), and `entries` (number of records in that interval). It contains no call, customer, or agent identifiers.

The extract counts **VRU entries**, not arrivals to an agent queue. It includes records with outcome `AGENT` or `HANG` and excludes `PHANTOM`, as the source documentation recommends. Zero-count intervals are present. The November source file has 41,019 records: 297 `PHANTOM` records were excluded, leaving 40,722 entries in 2,880 intervals. Keep this distinction when asking staffing questions: these counts alone do not give service times, queue arrivals, abandonment behavior, or the effect of adding an agent.

## Rebuild and verify

1. Download `AnonymousBank.rar` from the [official data directory](https://see-center.iem.technion.ac.il/databases/AnonymousBank/Data/) into ignored `data/raw/`. The source asks academic users to notify Prof. Avi Mandelbaum or the SEE team and acknowledge the data source in work that uses it; arrange that notification before teaching with the data. Do not commit the raw archive or extracted files.
2. Extract the RAR archive into `data/raw/`. On this machine, `bsdtar -xf data/raw/AnonymousBank.rar -C data/raw` produced twelve `*1999.txt` files.
3. Run `python3 data/build_anonymousbank_week01.py` from the repository root. It validates the November column names, dates, times, and outcomes and rewrites the aggregate deterministically.

The downloaded archive used for this build has SHA-256 `110527823a296e3163566f5d10d687e13859c60d963fd403d4623d89c7cadc4b`; the generated CSV has SHA-256 `2b7a5ab4fd46a91e5755dd965554b2d3a3f2885254b911f20fbc1206fbcd612c`.

We checked all twelve extracted files for tab-separated field counts, and checked dates and VRU-entry times on the rows with the expected 17 fields. November has no malformed rows; 12 rows across August, July, September, and October have extra tab fields and need a documented repair before those months are used. The [call-center study by Brown and coauthors](https://aviman.technion.ac.il/files/References/JASA_callcenter.pdf) also documents spuriously short agent-service records, especially before November. Week 1 uses only arrival counts, so it does **not** delete short-service calls. Service-time cleaning must be specified when that variable is modeled later.
