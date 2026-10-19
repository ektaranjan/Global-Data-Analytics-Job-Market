# Global Data Analytics Job Market Intelligence and Salary Trend Dashboard

An MCA major project implementing a reproducible job-posting snapshot pipeline, relational SQL analytics, an 11-page Streamlit application and academic evidence. It supports job seekers researching skill demand and recruiters examining the limits of salary benchmarks.

The supplied report is the original academic scope: Python cleaning and EDA, normalized SQLite storage, SQL questions, Excel supplementary analysis, five Power BI pages and a written insight report. Streamlit, upload validation, immutable snapshot versions, automated tests and provenance are requested enhancements. Predictive models and live APIs remain future scope.

## Data and interpretation

A genuine local gsearch_jobs.csv was found and imported. Source: https://www.kaggle.com/datasets/lukebarousse/data-analyst-job-postings-google-search. The original CSV has 61,953 records and 27 columns. The source snapshot covers observations from November 2022 through April 2025; it is not a live or current market feed. See Dataset/processed/*/quality.json for the checksum, exact dates, processing time and raw/clean missingness.

All search targets are United States. This does not establish actual job-country identity. Salary currency lacks authoritative metadata and is labelled unverified source units throughout. Missing remote flags are Unknown. The dataset license was not established from the source page; verify redistribution terms before uploading raw or derived data publicly. Raw files are ignored by Git.

## Setup on macOS and Linux

Python 3.11 or later is required. Python 3.14 on macOS ARM64 was used for the executed build.

```bash
cd /path/to/job-market-intelligence
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m src.pipeline /path/to/gsearch_jobs.csv
python -m src.sql_lab
python -m scripts.build_outputs
python -m scripts.build_academic_report
python -m pytest -q
python -m streamlit run app.py
```

The virtual environment isolates dependencies. The pipeline validates data and builds the database. The SQL command executes all 38 predefined analytical questions and exports results. build_outputs generates static charts, executive PDF and Excel. Streamlit serves the interactive application, normally at http://localhost:8501. Network is required only to install dependencies or acquire a new snapshot. Existing local snapshots support an offline demonstration.

## Windows PowerShell

```powershell
cd C:\path\to\job-market-intelligence
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m src.pipeline C:\data\gsearch_jobs.csv
python -m src.sql_lab
python -m scripts.build_outputs
python -m scripts.build_academic_report
python -m pytest -q
python -m streamlit run app.py
```

Windows and Linux commands are supplied for reproducibility; native execution on those platforms was not tested. If activation is restricted, invoke .venv\Scripts\python.exe directly. At least 8 GB RAM and 5 GB free storage are recommended. The raw source is roughly 290 MB. The current snapshot database and exported tables are included locally. Do not publish data until its license is confirmed.

## Components

| File | Responsibility | Input | Output |
|---|---|---|---|
| app.py | Native Streamlit controls and interactive Plotly charts | Current snapshot, filters | Dashboard and downloads |
| src/pipeline.py | Validate, clean, feature engineer and publish | Original CSV | CSV tables, quality JSON, SQLite |
| src/analytics.py | Independent filter/KPI/group/skill calculations | Clean records | DataFrames and KPIs |
| src/sql_lab.py | Read-only library execution and validation | SQLite, SQL/queries.json | Query CSVs and timings |
| src/exports.py | Filtered PDF and Excel export | Actual records | Valid PDF and XLSX bytes |
| scripts/build_outputs.py | Static report figures and summary artifacts | Committed snapshot | Report charts, workbook, executive report |
| SQL/schema.sql | Constraints and indexes | Empty SQLite database | Four related tables |
| SQL/analysis.sql | 38 numbered analytical questions | Populated database | Documented SQL outputs |
| Dataset/raw | Original snapshot preserved by checksum | Local CSV | Immutable raw copy |
| Dataset/processed | Versioned transformed data | Validated records | Four normalized tables and jobs_cleaned.csv |
| Dashboard | DAX, theme, relationship and page specifications | Clean tables | Power BI-ready support assets |
| tests | Fixtures and real-data integration checks | Source functions/database | pytest evidence |
| Report | Results, evidence and academic documentation | Executed pipeline | Reports and reproducibility records |
| Screenshots | Real rendered dashboard evidence | Running application | Browser captures where available |

## Page guide

1. Executive Command Center: eight calculated KPIs, observation trend, experience, search geography, skills, salary and arrangement.
2. Salary Intelligence: histogram, box plot, qualified group comparisons, salary statistics, bands and screening audit.
3. Skill Demand Intelligence: top 15/30, categories, salary-demand scatter, co-occurrence and optimal candidates.
4. Global Geographic Intelligence: explicit search-target map, location labels and observed history. Global job-country conclusions are unsupported.
5. Company Intelligence: hiring volume, sample-qualified salary comparisons and employer inspection.
6. Remote Work Intelligence: Remote/Onsite/Unknown, skills, trends, and statistical testing only with sufficient explicitly labelled groups.
7. Data Explorer: literal title/company search, columns, pagination, record inspection, missingness, dictionary, CSV and Excel.
8. Data Quality and Pipeline Monitor: raw and cleaned counts, missingness, provenance and transactional upload refresh.
9. SQL Analytics Lab: question search, visible SQL, read-only execution and CSV results; full-snapshot scope is explicit.
10. Reports and Download Center: filtered executive PDF, Excel, cleaned records, quality and packaged evidence.
11. Project Documentation and About: operating guidance, architecture and assumptions.

Use the sidebar to intersect country, company, experience, arrangement, employment, skill category and skill choices. Options narrow after preceding choices. Reset clears all filter state. Salary and observation-date restrictions are opt-in. The current counts and selected dimensions are shown above charts. SQL Lab and original pipeline quality explicitly use the full snapshot. A no-results state invites a broader selection.

## Calculations and validation

Remote percentage = explicitly Remote records / all filtered records × 100; it does not describe remote share among known arrangements only. Usable salary coverage = screened nonmissing salaries / all filtered records. Mean and median exclude unknown/invalid salaries. Skill demand counts distinct records requiring a token. Group salary charts require at least 30 usable salaries. See docs/DATA_DICTIONARY.md and docs/ARCHITECTURE.md for fallback formulas, assumptions and the ER model.

Run python -m pytest -q for data loading/schema, duplicates, salary boundaries and annualization, skill parsing, foreign keys, idempotent database import, filters, KPIs, exports, malformed refresh and SQL checks. Report/tests.xml and Report/tests.log preserve the executed results; Report/sql_validation.json records output schemas and timings. A 2-second query target from the PDF is checked through the actual timing record; do not infer performance on untested machines.

## Updated snapshots and exports

On the quality page choose a CSV and select Validate and atomically refresh. Required fields and the 350 MiB limit are checked. Only a complete validated version becomes current. A failed import retains the previous pointer. Use one local operator at a time. Rebuild packaged charts, workbook and academic evidence after importing a new snapshot; packaged artifacts do not refresh automatically with sidebar filters.

Excel contains full cleaned analytical columns, filterable tables, formula-based KPI checks, preaggregations and a chart. Native Excel pivots are not generated; creation instructions are supplied. The packaged workbook was recalculated with LibreOffice and its cached count, mean and coverage match Python/SQL. New application-generated workbooks require recalculation in Excel or LibreOffice. Power BI assets contain importable normalized tables, relationships, DAX and a five-page plan. A PBIX has not been built or validated because Power BI Desktop is unavailable here.

## Deployment and troubleshooting

Streamlit Community Cloud entry point is app.py with requirements.txt at repository root. Include only data you are authorized to redistribute. Local filesystem persistence on hosted sessions is not durable shared storage. Production PostgreSQL integration is documented future work; the executed application uses SQLite. No connection to a production PostgreSQL server was tested. No live data API is claimed. Authentication is not implemented; keep the default loopback binding for a local examiner demonstration.

If imports fail, check the selected Python environment and reinstall requirements. If the data pointer is absent, import the CSV before launching, or upload it at the app start screen. If a chart is empty, inspect filters, salary disclosure and sample thresholds. If the port is in use, add --server.port 8502. Raw title strings and employer names are escaped in Excel exports; SQL search never accepts arbitrary modification statements.

## Academic submission


Credits: Luke Barousse dataset on Kaggle; original supplied internship report; Python, pandas, NumPy, SQLAlchemy, SQLite, Streamlit, Plotly, SciPy, Matplotlib, Seaborn, ReportLab, openpyxl and python-docx. No internship employment or business-impact metrics are asserted. The source repository has not been published to GitHub. Optional live refresh, verified geocoding, currency metadata and properly evaluated predictive models remain future extensions.
