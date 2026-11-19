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

## Week 4 service duration summary

The [morning service summary](anonymousbank_nov1999_morning_service_summary.json) comes from the same Technion SEE Lab AnonymousBank November file. It pools all service categories with outcome `AGENT` and a service start from 09:00 inclusive to 11:00 exclusive, on Sunday–Thursday. It uses the full `ser_time` in seconds, even when service ends after 11:00. Times are parsed numerically because the hour may have one digit. Selected durations agree with the difference between the recorded end and start times.

| November dates | Use | Selected | Below 10 s | Retained |
| --- | --- | ---: | ---: | ---: |
| 1–14 | Fit | 2,544 | 14 | 2,530 |
| 15–30 | Check | 2,528 | 14 | 2,514 |

Slide 6 applies the same selection before screening to January1999.txt and November1999.txt. In January, 163 of 3,631 selected services lasted under 10 seconds (4.49%). In November, 28 of 5,072 did (0.55%). These figures describe the selected morning services. The explanation for many very short records comes from the bank manager's investigation, reported by Brown et al. (§4.1). The January records are used only for this comparison.

The first bin counts all durations below 10 seconds, including zero. The teaching fit screens these out because some very short services came from agents hanging up. The threshold is a screening choice that can also exclude valid brief calls. The top bin keeps all durations at least 1,800 seconds. Each bin includes its lower edge and excludes the next edge. The two sums over retained services are the sum of durations in seconds and the sum of squared durations in seconds squared. They allow exact calculation of the empirical mean and variance from the aggregate. There are no individual records, identifiers, dates per call, or timestamps in this summary. See [Brown et al. (2005), §4](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Brown-etal-CCdata.pdf) for the documented recording issue and the published analysis.

For each set of dates, `service_groups` separates regular banking (`PS` and `PE`) from all other services. Each group contains four totals for services retained after screening. `retained_count` and `service_seconds` count all retained services and their full duration. `long_count` and `long_seconds` count services at least 600 seconds long and sum their full duration. For example, a 700-second service adds all 700 seconds to both duration sums. These totals let students compare a share of calls with a share of recorded agent work. They pool days and contain no individual records or staffing rosters.

To rebuild, place the official November file in ignored `data/raw/` as above and run `python3 data/build_anonymousbank_week04.py` from the repository root. The JSON SHA-256 is `6ec91f03293fe789b20faa6194333f74957ee00e274b801e78bfd2627b399c0a`. The Week 4 lab runs with this summary and the Week 1 arrival extract alone.
