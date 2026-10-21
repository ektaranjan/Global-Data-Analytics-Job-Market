# Live demonstration guide

Allow 10–12 minutes. Rehearse on the same laptop with its existing legitimate snapshot. Open the app before the audience arrives, then reset filters. The source has 56,004 cleaned observations and 9,022 usable salary values; all salary amounts use unverified source units.

## Timed walkthrough and spoken script

### 0:00–1:00 Start and introduce the problem

Run `./start_project.command` from the project folder, or open the already-running http://127.0.0.1:8501 instance. Keep Terminal available.

Say: “My project, Global Data Analytics Job Market, turns historical job-posting observations into a searchable analytics dashboard. Job seekers can inspect requested skills and disclosed compensation, while recruiters can compare the observed requirements of similar roles. The aim is transparent descriptive evidence rather than a claim about every current vacancy.”

### 1:00–2:00 Explain the source and architecture

Say: “The input is a genuine CSV snapshot of Google job-search results distributed through Kaggle. Python validates and cleans it, SQLAlchemy builds a constrained SQLite database, and independent analytics functions feed a Streamlit interface with Plotly charts. This supplied snapshot targets United States searches. Its dates describe collection activity, and its currency metadata is unverified.”

### 2:00–3:30 Executive overview and filters

Select Executive Command Center. Explain 56,004 observations, 13,177 normalized companies, 134 skill tokens and 16.1% usable-salary coverage. In Experience choose Senior; note that the record count narrows. Add Remote under Work arrangement if relevant, then use Reset filters. Different filter dimensions intersect; alternatives within one multiselect use OR.

Say: “The headline metrics are calculated from filtered records. A low salary-disclosure percentage is a limitation of the evidence, not a zero salary. Reset restores the whole snapshot.”

### 3:30–4:30 Salary intelligence

Open Salary Intelligence. Explain the histogram and experience box plot. State the full-snapshot median, 88,400 source units, and mean, about 92,131. Explain minimum salary sample sizes and the preserved screening audit.

Say: “I prefer to show the mean and median together. Missing and invalid salary candidates are excluded, and the interface retains the provenance of each annualized estimate. I cannot call these verified USD figures.”

### 4:30–5:40 Skill demand and co-occurrence

Open Skill Demand Intelligence. Show the top-15/top-30 selector, salary-demand scatter, co-occurrence matrix and optimal candidates. SQL appears in 28,081 cleaned observations. Explain the optimal rule: demand at least 100, valid salary sample at least 30 and mean salary at least the overall median.

Say: “A skill’s salary association can reflect employer mix, seniority and other co-required skills. The chart does not prove that learning one skill causes a salary increase.”

### 5:40–6:30 Geography, company and remote limits

Briefly show Global Geographic Intelligence and Company Intelligence. Explain search-target coverage rather than verified global job locations. Open Remote Work Intelligence and point out Remote and Unknown. Do not label Unknown as Onsite or claim a remote-versus-onsite premium.

### 6:30–7:40 Search and SQL

Open Data Explorer, search a job title or company, choose columns and inspect a record. Open SQL Analytics Lab, search “median”, select the median question and run Execute read-only query. Compare the output with the full-snapshot executive median. Explain that SQL Lab is explicitly independent of sidebar chart filters.

Say: “The lab runs predefined read-only SQL against real database tables. The company and skill dimensions connect through a job-skills bridge, so I avoid double-counting jobs when joining to skills.”

### 7:40–9:00 Quality and refresh

Open Data Quality and Pipeline Monitor. Explain 61,953 raw observations, 5,949 composite duplicates removed and eight invalid salary candidates. Show the source checksum and the CSV upload control. An optional live refresh uses the genuine original raw file; a complete import can take extra time. If time is limited, explain the actual implemented staging/atomic-pointer workflow and show the isolated refresh test results rather than pretending an unperformed upload succeeded.

Say: “An invalid import does not replace the previous valid pointer. Skill tokens are parsed as bounded literal lists, and unknown salaries or work arrangements are not silently invented.”

### 9:00–10:15 Export and verification

Open Reports and Download Center and generate the current executive PDF. Show the analytical workbook or downloaded CSV. Display the current verification summary and the test command `python -m pytest -q`. The exact executed test count must match the final summary, not an older report.

### 10:15–12:00 Limitations and conclusion

Say: “The implementation works with a local historical snapshot. Its principal limits are incomplete salary disclosure, unverified currency, search-country rather than workplace-country metadata and the lack of an explicit onsite control. The Power BI folder contains supporting definitions; a validated native PBIX is not claimed. Future work should improve metadata and data-refresh permissions before adding predictive models. The contribution is a reproducible path from genuine observations to inspectable calculations, SQL and interactive reports.”

## Backup plan

Keep the environment and current data on disk. Core page scripts and calculations were tested with external connections denied in the test process. A disconnected browser map may still need a cached geographic asset; use the computed geography table or existing chart package instead. If a browser or server fails, show the genuine captured screenshots, query CSVs and report while stating the actual failure. These backups do not prove that the failed interaction succeeded.
