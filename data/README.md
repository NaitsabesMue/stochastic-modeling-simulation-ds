# AnonymousBank teaching extract

Start with the student-facing [AnonymousBank data guide](anonymousbank_data_guide.md) for the call journey, definitions of VRU and each outcome, all 17 raw fields, a redacted raw-data example, and the limits of the Week 1 extract. This file documents how the public aggregate was built and checked.

Week 1 uses [`anonymousbank_nov1999_arrivals_15min.csv`](anonymousbank_nov1999_arrivals_15min.csv), an aggregate made from the November 1999 file in the [Technion SEE Lab AnonymousBank archive](https://seelab.net.technion.ac.il/data/). The [source documentation](https://see-center.iem.technion.ac.il/databases/AnonymousBank/Data/AnonymousBank.pdf) describes the 17 fields in each call record. The archive includes caller and agent identifiers; the teaching extract contains only `date`, local `time` (start of a 15-minute interval), and `entries` (number of records in that interval). It contains no call, customer, or agent identifiers.

The extract counts **VRU entries**, not arrivals to an agent queue. It includes records with outcome `AGENT` or `HANG` and excludes `PHANTOM`, as the source documentation recommends. Zero-count intervals are present. The November source file has 41,019 records: 297 `PHANTOM` records were excluded, leaving 40,722 entries in 2,880 intervals. Keep this distinction when asking staffing questions: these counts alone do not give service times, queue arrivals, abandonment behavior, or the effect of adding an agent.

## Rebuild and verify

1. Download `AnonymousBank.rar` from the [official data directory](https://see-center.iem.technion.ac.il/databases/AnonymousBank/Data/) into ignored `data/raw/`.
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

## Lecture 5 original morning records

The Lecture 5 notebook reads the original tab-separated November records on your computer. Download and extract the official Technion SEE Lab archive as described in steps 1 and 2 under [Rebuild and verify](#rebuild-and-verify). The notebook expects `data/raw/November1999.txt` inside the course repository. That directory is Git ignored. Keep the original file and any notebook output showing individual calls local.

Use Sunday–Thursday requests from 09:00 inclusive to 11:00 exclusive. Each request keeps its recorded time to the second. Use the queue start for calls that joined the queue. Use the service start and zero wait for served calls with no recorded queue start. Exclude source-marked `PHANTOM` records and calls that left before reaching the queue. The loader verifies recorded waiting times against the queue start and exit. It follows the outcomes of requests in the window even when the wait ends after 11:00.

Fit the arrival models on 1–14 November (10 mornings, 3,115 requests) and compare their predictions with 15–30 November (12 mornings, 3,584 requests). The earlier Model A uses the Week 3 and 4 generator. It fits the average rate and the Gamma multiplier variance from counts in the full 09:00–11:00 window, then uses exponential gaps at each simulated morning's rate.

Fit the exponential from differences between successive request times within each 09:00–11:00 window. The 3,105 complete gaps total 71,445 seconds, giving a fitted mean of 23.01 seconds. Compare the fixed fitted rate with the same rate multiplied by the earlier Gamma factor. Reuse the same arrival random draws for the exponential variants. Check complete gaps at whole-second resolution and the spread of total requests across mornings.

For Model B, draw a whole fit morning with replacement. From the same draw, build one path by spreading each 15-minute count uniformly within its interval and another by replaying the recorded times. Each pair has the same totals in each quarter-hour. Check the share of requests that arrive before selected clock times and each morning's busiest 60-second window. The busiest-minute check uses whole seconds for observations and simulated times.

Five fit-period requests have a recorded queue start and an `AGENT` label but a missing service start. Use their timestamps for the arrival study. Fit patience and summarize queue outcomes using the 3,110 fit-period requests with known outcomes, including 565 abandonments. Split waiting time across the rate intervals the caller reached. An abandonment at a boundary contributes an event to the interval starting there. Compare the candidates by log likelihood on the 3,581 requests with known outcomes on 15–30 November. The selected model has one rate in each of the first two minutes and a common rate from two minutes onward. See [Brown et al. (2005), Section 5](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Brown-etal-CCdata.pdf) for the censoring issue in this call centre.

The first queue comparison uses Model A for every patience rule. The two Model B paths share the same sampled mornings, service draws, and patience draws. The service-type comparison uses the timestamp version of Model B and takes each request's type from the same sampled record.

For the staffing comparison on the ten fit mornings, use the start and end of positive-duration calls with a recorded agent. Count the part of each service that falls between 09:00 and 11:00, including calls that started earlier. For each second, count each agent on a call once, including when their logged services overlap. There are 10–13 distinct recorded agents handling calls per morning. The daily peak ranges from 9 to 12 and exceeds nine on nine mornings. Across the ten windows, an average of 7.1 agents were on calls at any given time. These counts exclude 14 positive-duration service records with no agent recorded. Staffing records would also account for available idle agents.

Service modelling uses individual durations from the same selection as Lecture 4. Services start from 09:00 to before 11:00 and durations of at least 10 seconds contribute their full observed value. Compare a pooled lognormal fit with one fit for each recorded `type`. Fit on 1–14 November and check observed means by type on 15–30 November. December is reserved for the combined queue check in Lecture 6.

## Lecture 6 December check

Extract both `November1999.txt` and `December1999.txt` from the official archive into the Git-ignored `data/raw/` directory. The [download instructions](#rebuild-and-verify) are above. Use the same request and duration selection as in Lecture 5. The November 1–14 records supply the lognormal service fit and three-rate patience fit. Compare the November arrival profiles and service durations with the corresponding December observations. This comparison uses 10 fit mornings and 22 December mornings.

For the queue check and staffing experiment, draw from the 22 December mornings and replay all their recorded request times to the second. The 6,769 December requests supply arrival times. The 6,757 with known outcomes supply the observed outcome summaries and select the comparable simulated outcomes. Calculate each outcome per morning, then average across mornings. A request whose outcome is unknown still uses its recorded time in the simulation.

For the 09:00 check, use recorded service intervals and agent identifiers locally to count each agent once. For each agent already busy at 09:00, the simulator delays their first availability until the latest end of their calls in progress. The data reader returns remaining service times and activity counts. A separate check counts callers who had joined before 09:00 and were still waiting just after 09:00. The staffing experiment holds one common queue and compares starting with all agents free with starting with the recorded calls already in progress. The log shows how many agents were busy at the same time. An availability roster would also include idle agents.
