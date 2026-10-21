GLOBAL DATA ANALYTICS
JOB MARKET INTELLIGENCE &
SALARY TREND DASHBOARD

| S.No. | Title | Page No. |
| 1 | Abstract | 1 |
| 2 | Introduction | 2 |
| 3 | Literature Review | 4 |
| 4 | System Analysis and Requirements | 6 |
| 5 | Proposed Methodology | 8 |
| 6 | System Design | 13 |
| 7 | Implementation | 16 |
| 8 | Results and Discussion | 20 |
| 9 | Advantages | 24 |
| 10 | Limitations | 25 |
| 11 | Future Scope | 26 |
| 12 | Conclusion | 27 |
| 13 | References | 28 |

# Abstract

Global Data Analytics Job Market Intelligence & Salary Trend Dashboard provides a reproducible environment for exploring historical data-analyst job observations. The system addresses a practical information problem: job requirements and salary disclosures appear across separate listings, while an individual reader has limited ability to compare patterns across employers, skills and work arrangements. The implemented workflow converts a genuine source snapshot into structured data, database queries, interactive views and downloadable evidence.

The supplied CSV contains 61,953 rows and 27 columns. Validation and documented deduplication retain 56,004 observations. A company dimension, a job-observation fact table, a skill dimension and a job-skills bridge represent the relationships. The application exposes 11 Streamlit pages, eight executive metrics and 38 predefined SQL questions. Excel, PDF, CSV and reproducible static charts support further inspection.

The processed snapshot contains 9,022 usable salary candidates. Its disclosed-salary median is 88,400 and its mean is 92,131, expressed in unverified source units. SQL is the most frequent extracted skill, appearing in 28,081 observations. These values are calculated from the stored records rather than entered as dashboard constants. The current verification run passed 85 automated tests, including page scripts, transformation boundaries, database constraints, exports and launcher preflight cases.

The evidence is historical and nonrandom. Every search target is United States, which does not establish a verified workplace country. Missing remote flags remain Unknown, and the snapshot supplies no explicit onsite comparison group. The browser interface was inspected and genuine screenshots were captured. Core calculations and page scripts also passed a process-level test with external connections denied; a fully disconnected browser map remains a separate limitation. The project therefore supports descriptive exploration while keeping unsupported geographic, monetary and causal conclusions visible.

Keywords: job observations, salary provenance, skill demand, data validation, relational analysis, Streamlit, SQLite, reproducibility.

# Introduction

## Background and motivation

A person researching data-analyst roles can read many advertisements without learning how representative a particular skill combination is. One employer may ask for SQL and a reporting tool; another may emphasize Python, cloud platforms or managerial experience. Salary information is often absent or expressed in incompatible periods. These differences make informal comparisons difficult even when the underlying listings are available.

The project organizes a supplied snapshot into one analytical workspace. Its purpose is to make observed requirements measurable, let users inspect the records behind a chart and preserve the transformation rules that produced each output. It does not replace a job portal or certify that a historic listing remains open. A posting observation is evidence of what was collected at a particular time, not necessarily a newly created vacancy.

## Problem definition

The central problem is the absence of a consistent, reproducible way to connect job titles, employers, skills, work arrangements and disclosed compensation within the available source. Without documented preprocessing, repeated indexing can inflate counts; without salary provenance, annualization assumptions can disappear; without appropriate joins, a job requesting several skills can be counted repeatedly in headline metrics.

The application addresses these issues through a validated Python pipeline, normalized storage, independent analytical functions and a browser interface. A user can filter experience and skills, compare sample-qualified salary groups, inspect employer observations, run a defined SQL question and download the resulting records. Each feature is tied to the supplied data rather than to invented demonstration values.

## Intended users

Job seekers can use the observed skill frequencies to guide further role research and portfolio planning. Recruiters can examine disclosed salary evidence and common requirement combinations, subject to the source limitations. Technical reviewers can inspect SQL, transformation logic and automated checks. These are intended uses; no employment outcome or recruitment-impact metric has been measured.

# Introduction continued

## Project objectives

| Objective | Implemented response |
| Preserve source evidence | Checksum-named raw copy and version metadata |
| Resolve inconsistent fields | Explicit text, date, salary and arrangement rules |
| Represent job-skill relationships | Unique skill dimension and constrained bridge table |
| Answer business questions | 38 predefined SQL queries and reusable analytics |
| Enable independent exploration | 11 pages, dependent filters and searchable records |
| Support repeatable demonstration | Local data, setup guide and prerequisite-checking launcher |

Table 1  Project objectives and implemented responses

## Scope of the delivered system

The completed core is a local descriptive analytics application. It imports CSV snapshots, builds SQLite tables, evaluates analytical questions and presents interactive views. SQL Lab operates on the full current snapshot and states that scope explicitly. Analytical page filters intersect countries, employers, experience categories, arrangements, employment types and skill selections. Optional salary and observation-date restrictions are applied only when enabled.

The source is not a continuously refreshed feed, and the project does not implement a live job-search API. Forecasting, salary prediction and machine learning are not part of the delivered core. The Power BI folder supplies import instructions, measures and layout specifications, but native PBIX execution is not claimed. SQLite is the tested persistence layer; a separate PostgreSQL SQL asset is not equivalent to a verified production backend.

## What constitutes a defensible result

A useful result has a clear analytical unit, a stated denominator and an inspectable calculation. For example, skill frequency counts a token at most once per retained observation. Salary coverage counts valid, nonmissing annual candidates relative to all filtered records. A company ranking requires a sufficient disclosed sample before it can appear in a salary comparison. The following sections connect those definitions to source fields, implementation files and executed evidence.

# Literature Review

## Foundations of reproducible tabular analysis

The project follows established tabular-analysis practice: retain source evidence, make transformations explicit and separate preparation from presentation. Pandas provides typed column operations, missing-value handling, grouping and joins [2]. These operations are useful only when the analytical unit is defined. A count of collected rows, distinct source identifiers and normalized observation-day combinations can describe different quantities even when all originate in the same CSV.

Relational database methods provide a second foundation. Separating company and skill definitions from job observations allows constraints to express valid relationships. SQLite supports primary keys, foreign keys, grouping, common table expressions and window functions [3]. SQLAlchemy supplies connection and transaction handling [4]. The implementation uses these capabilities to make analytical questions executable and to validate a complete database before publication.

## Interactive analytics and verification

Streamlit supplies native controls, session state and Python-based page construction. Its AppTest interface executes application code and simulates supported user interactions without being a browser [5]. This distinction matters: passing a script-level test does not alone establish that a chart is legible, a responsive layout is usable or a browser-only asset loads while disconnected. Genuine browser inspection provides complementary evidence.

Plotly supports interactive distributions, grouped comparisons, heatmaps and geographic views [6]. A chart must still preserve the source meaning. For this project, a map based on search_location represents search-target coverage, not verified workplace geography. A salary-demand scatter describes association within disclosed records, not the effect of learning a particular skill.

## Data source context

The job-posting snapshot is attributed to the Kaggle source identified in the existing project [1]. Dataset availability does not prove that its observations are representative of the global market or that redistribution terms have been verified. The implementation therefore records provenance and treats coverage, currency and disclosure as empirical constraints rather than inherited assumptions.

# Literature Review continued

## Methodological choices and their consequences

| Analytical choice | Benefit | Remaining limitation |
| Median and mean together | Shows central tendency and upper-tail sensitivity | Both concern a selected disclosed subset |
| Minimum salary samples | Reduces rankings dominated by rare observations | Does not remove confounding or disclosure bias |
| Many-to-many skill bridge | Avoids repeated skill definitions and duplicate tokens | Counts across different skills still overlap |
| Explicit Unknown arrangement | Preserves missing information honestly | Cannot create an onsite control group |
| Read-only SQL library | Makes business questions inspectable and repeatable | A successful query still requires correct interpretation |

Table 2  Methodological choices and limitations

The implemented optimal-skill rule combines demand and salary evidence: at least 100 observations, at least 30 valid salaries and an associated mean at or above the overall median. This rule is transparent and reproducible. It is a heuristic for selecting candidates for further inspection, not a validated model of career success. Roles can co-require several skills, and the same employer or seniority pattern can influence multiple skill-associated salary averages.

Safe parsing is another methodological constraint. description_tokens is a stringified Python list rather than a normalized relation. Python literal parsing accepts literal structures without executing arbitrary expressions, but the Python documentation warns that malformed or resource-intensive inputs still require care [7]. The project bounds token-string size, validates the resulting list and retains only bounded string tokens. It does not treat unrestricted eval as a data-cleaning shortcut.

## Integration achieved by this project

The contribution is an integrated, inspectable implementation rather than a claim of a new labor-market theory. A common source snapshot feeds cleaning, normalized storage, SQL, independent Python metrics, a browser interface and exports. The same definitions are used across these components. Where a source field cannot support a conclusion, the interface and report state the limitation instead of converting absence into an apparently precise answer.

# System Analysis and Requirements

## Functional requirements

| Area | Required behavior | Implemented location |
| Ingestion | Read a bounded CSV and validate required fields | src/pipeline.py: run, clean |
| Preparation | Normalize fields and preserve salary provenance | src/pipeline.py: clean, tokens |
| Persistence | Publish constrained relational tables | tables, build_database |
| Exploration | Apply filters and calculate current KPIs | src/analytics.py and app.py |
| SQL | Select and execute a read-only business question | src/sql_lab.py |
| Reporting | Export records, Excel and current executive PDF | src/exports.py |
| Operation | Explain setup and check prerequisites before launch | start_project.command and guides |

Table 3  Functional requirements and modules

## Quality requirements

Correctness requires that metrics be calculated from the selected records, unknown salaries remain missing and skill joins preserve the intended count. Reliability requires failed imports to retain the previous valid pointer and the database to satisfy referential integrity. Maintainability requires calculation functions to remain independent of the presentation layer. Portability is evaluated against the executed macOS/Apple Silicon environment rather than assumed for an untested server.

Usability requires readable labels, visible active filters, empty-result messages and a route from summary charts to source records. Security requires bounded input, safe literal parsing, predefined read-only SQL and credential-free local operation. Reproducibility requires the source checksum, transformation rules and executable checks. Performance is measured from actual queries on the current dataset, not inferred from interface appearance.

## System boundary

The system begins with an authorized local CSV and ends with interactive views and generated artifacts. External package installation, obtaining a new source file, publishing to GitHub and native Power BI Desktop validation are outside ordinary local execution. No new GitHub push was performed during this preparation.

# System Analysis and Requirements continued

## Executed software environment

| Component | Verified value | Role |
| Operating environment | macOS / Apple Silicon arm64 | Local development and demonstration |
| Python | 3.14.3 | Application and pipeline runtime |
| Streamlit | 1.66.0 | Native Python interface |
| Pandas / NumPy | 3.0.6 / 2.5.4 | Tabular and numeric calculations |
| SQLAlchemy | 2.1.5 | Transactional SQLite construction |
| Plotly | 7.1.0 | Interactive charts |
| SciPy | 1.18.1 | Conditional statistical comparison |
| pytest | 9.1.1 | Automated verification |

Table 4  Executed software environment

The dependency file also includes Matplotlib and Seaborn for static figures, openpyxl for Excel, ReportLab for the executive PDF, python-docx for editable documentation and pypdf for PDF checks. The existing environment passes pip check, and an offline dependency-resolution dry run reports that the declared requirements are satisfied. This is evidence for the current installation; it is not a claim that every supported version combination has been tested.

## Local prerequisites

A suitable Python, the project source, an installed virtual environment and a genuine processed snapshot are required for the full demonstration. At least 8 GB RAM and approximately 5 GB free disk are practical planning targets for this delivery; the raw source is about 290 MB and processing can require several times its size. No paid service, API credential or external database is needed for the core. Node.js is not part of the application runtime.

The launcher prefers an environment inside the project and supports the existing delivery environment as a fallback. Package installation remains a first-time setup step. The current server was verified at http://127.0.0.1:8501; the loopback binding supports a local demonstration without exposing the app as a public service. The guide distinguishes everyday execution from setup and documents the tool-level restriction on testing a fresh listening process.

# Proposed Methodology

## Source acquisition and provenance

The application uses a genuine preexisting gsearch_jobs.csv with 61,953 observations and 27 columns. It was found locally rather than replaced by fabricated production records. The source URL is recorded in the project, and a SHA-256 identifies the preserved snapshot. The exact original download time is unknown; processing time is recorded separately. The observation interval is 2022-11-04 to 2025-04-18.

| Source group | Relevant fields |
| Identity and labels | title, company_name, location, job_id, via |
| Collection context | date_time, search_location, posted_at, search_term |
| Work description | description, description_tokens, schedule_type, work_from_home |
| Compensation | salary_standardized, salary_yearly, salary_hourly, salary_min, salary_max, salary_rate |
| Additional source data | extensions, thumbnail, commute_time, source indices and salary text |

Table 5  Raw source field groups

The actual column set is treated as evidence. The source uses salary_min and salary_max, while the earlier reference names salary_avg_min and salary_avg_max. The implementation explicitly supports these aliases. search_location remains a search target, and date_time is converted to an observation date. Neither field is silently promoted into a verified workplace country or original posting-creation timestamp.

## Data lineage

The raw copy is preserved by checksum. Each processed version contains cleaned records, four normalized table exports, a SQLite database and a quality report. Dataset/current.json selects the active version. This makes the origin of a displayed result inspectable and lets an operator reproduce processing from the same input. A changed source should produce a newly identified version and requires regeneration of packaged evidence.

Source redistribution terms remain unverified. Large snapshots are therefore retained locally and excluded from Git. A fresh clone requires an authorized source import before real-data integration tests or the full demonstration can run. Historical observations must not be described as a live feed.

# Proposed Methodology continued

## Validation and duplicate handling

The upload path accepts CSV files up to 350 MiB and requires title, company_name, location, description_tokens, date_time and search_location. Missing required columns and empty data raise errors. Numeric salary fields are coerced through controlled conversion, while timestamps are parsed with invalid values reported. Validation is performed before a newly complete version can become current.

Exact raw duplicates are removed first. Text preparation then strips surrounding whitespace, collapses internal whitespace and normalizes case for titles and company names. Location labels are title-cased for grouping. The second duplicate rule compares normalized title, company, location and observation date. Invalid dates cannot reliably establish date identity and are not used to delete composite duplicates.

| Pipeline measure | Actual snapshot value |
| Raw observations | 61,953 |
| Exact duplicate rows removed | 0 |
| Composite duplicate observations removed | 5,949 |
| Retained observations | 56,004 |
| Invalid observation dates | 0 |

Table 6  Duplicate and quality outcomes

This rule removes 5,949 composite duplicates from the supplied source. It reduces repeated same-day indexing but is not a universal vacancy identifier. Different real openings can share the same attributes, while the same opening observed on different dates can remain. The first retained row supplies its fields; the pipeline does not silently merge conflicting salary or skill evidence across duplicate observations.

## Missing values

Missing salary remains missing, not zero. Missing arrangements become Unknown. Empty extracted skill lists do not establish that a role required no skills. Source and cleaned completeness measures are recorded so that a user can understand which subsets support each chart. Text normalization improves consistency but does not perform external employer entity resolution or geocoding.

# Proposed Methodology salary preparation

## Annual salary resolution

| Priority | Candidate | Transformation |
| 1 | salary_standardized | Use the source estimate when present |
| 2 | salary_yearly | Use the annual figure when priority 1 is missing |
| 3 | salary_hourly | Multiply by 2,080 when higher priorities are missing |
| 4 | Salary range midpoint | Annualize only when yearly, hourly or monthly units are known |

Table 7  Salary fallback priorities

The first nonmissing candidate is selected and its provenance is stored in salary_source. Hourly conversion assumes 40 hours for 52 weeks; monthly conversion multiplies by 12. A range with an unknown rate does not justify an annual estimate. The procedure does not substitute a lower-priority estimate simply because a nonmissing primary candidate fails the subsequent screen.

The baseline screen retains candidates from 15,000 through 400,000 inclusive. salary_candidate preserves the selected value before screening, salary_valid identifies whether it passes, and salary_year_avg supplies the screened analytical amount. Missing and invalid candidates are distinguished. This snapshot contains 46,974 missing candidates and eight invalid candidates, leaving 9,022 usable salary observations.

## Assumptions and distribution summaries

The screen follows the documented baseline but can exclude legitimate part-time or unusually senior compensation. No currency field was verified, so no conversion, inflation adjustment or verified USD claim is made. The application uses source units in labels. Salary bands are left-closed intervals below 60K, 60–90K, 90–120K and at least 120K; missing values receive no salary band.

Mean, median and percentiles use only usable salaries. The full-snapshot median is 88,400, the mean is approximately 92,131, and the central half ranges from 62,400 to 116,812.5 source units. These are summaries of the disclosed subset rather than estimates of all job compensation. Every filtered comparison requires its own valid salary count.

# Proposed Methodology feature engineering

## Skill extraction and categories

description_tokens contains a string representation of a list. tokens() rejects oversized strings, uses ast.literal_eval, checks the resulting type and keeps bounded string tokens only. Tokens are trimmed, lowercased, deduplicated within an observation and sorted. Malformed or unsupported structures yield an empty parsed list; unrestricted eval is not used [7].

A documented vocabulary assigns programming, analyst tools, databases, cloud, libraries or other. A category is a grouping convention rather than proof of a skill’s only professional use. The unique skill table defines each token once; the bridge records each job-skill pair once. Empty or malformed extracted fields remain part of the quality audit and cannot be interpreted as evidence of skill-free roles.

| Feature | Implementation and limitation |
| Experience level | Manager/lead first, then senior, then junior/entry; unmatched titles are Mid-Level (inferred) |
| Work arrangement | Explicit true is Remote; explicit false is Onsite; absent or unrecognized is Unknown |
| Observation period | UTC date plus year/month from collection timestamp |
| Search country | Preserves search_location; does not geocode workplace location |
| Employer identifier | Snapshot surrogate for the normalized name; not a persistent legal-entity identifier |

Table 8  Derived feature definitions

The supplied data has 25,053 explicitly remote observations and 30,951 Unknown observations. It contains no explicitly labelled onsite group. The remote comparison page therefore explains why a Remote-versus-Onsite test cannot be justified. It never relabels the unknown group just to manufacture a control.

## Derived identity

Each retained observation receives a surrogate job key, and the original source identifier remains available for audit. Company and skill identifiers belong to the processed snapshot. Because the job key also reflects deterministic row ordering, it is not presented as a universal cross-snapshot vacancy identity. Repeated imports replace a version rather than append duplicate facts.

# Proposed Methodology analytical definitions

| Metric or comparison | Definition |
| Postings | Count of retained filtered observations |
| Companies | Unique normalized employer names excluding Unknown |
| Skill demand | Distinct observations containing a token |
| Remote percentage | Explicit Remote observations / all filtered observations × 100 |
| Usable salary coverage | Screened nonmissing salaries / all filtered observations × 100 |
| Salary group chart | At least 30 valid salary observations in the displayed group |
| Optimal skill | Demand ≥100, salary count ≥30, associated mean ≥ overall median |
| Monthly change | LAG comparison of collection-month observation counts |

Table 9  Metric and comparison definitions

The denominator matters. Remote percentage includes Unknown in the denominator, so it differs from a percentage among known arrangements only. Salary coverage does not turn missing pay into zero. A skill can co-occur with several others, so summing skill frequencies or category mentions can exceed the total number of observations. SQL queries use the relevant grain explicitly to avoid misleading headline counts after bridge joins.

## Statistical comparison policy

The remote page implements a two-sided Mann–Whitney U comparison only when Remote and explicitly Onsite groups each contain at least 30 valid salaries. The current snapshot does not satisfy that requirement. No p-value or remote premium is reported for the supplied data. Even a valid future comparison would remain observational and potentially confounded by employer, geography, seniority and employment type [8].

The current mean and median describe disclosed records. Skill salary associations and company benchmarks do not isolate causal effects. Observation trends reflect collection coverage and reposting as well as possible hiring activity. The methodology therefore prioritizes transparent counts, samples and caveats over an unsupported forecast or causal interpretation.

# System Design

Figure 1  Implemented data flow from genuine input to interactive views and exports

![Figure 1  Implemented data flow from genuine input to interactive views and exports](Report/figures/architecture_workflow.png)

The architecture separates preparation, persistence, analysis and presentation. pipeline.py validates a CSV and publishes a complete processed version. SQLite and normalized CSVs preserve the relational output. analytics.py calculates filtered metrics from records; sql_lab.py answers predefined questions from the active database. app.py controls navigation, widgets and chart presentation. exports.py builds downloadable artifacts from the selected records.

The analytical functions do not require Streamlit session state. This makes them reusable in scripts and tests and reduces the risk that a chart and an export silently use unrelated formulas. The browser interface reads the active version pointer and caches loaded records against that version. A successful refresh clears the cache so the next view reads the newly committed snapshot.

Ordinary demonstration uses local files and the embedded database. The design has no required remote API or external database connection. The core remains usable with an already-installed environment and legitimate local snapshot. Browser geographic assets are a separate consideration from local data processing.

# System Design relational storage

Figure 2  Four-table schema and one-to-many key relationships

![Figure 2  Four-table schema and one-to-many key relationships](Report/figures/database_structure.png)

| Table | Key and responsibility |
| company_dim | company_id primary key; unique normalized employer name |
| job_postings_fact | job_id primary key; company_id foreign key; observed attributes |
| skills_dim | skill_id primary key; unique skill and category |
| skills_job_dim | Composite (job_id, skill_id) primary key; both columns reference parents |

Table 10  Relational tables and responsibilities

The bridge resolves the many-to-many relationship between observations and skills. Its composite key prevents the same token from being recorded twice for one observation. Foreign keys are enforced during import and verified before publication. Indexes on company, search country, observation date and skill support the selected analytical access paths.

The active database contains 13,177 employer rows, 56,004 fact rows, 134 skill rows and 181,468 bridge rows. The current integrity check returns ok and the foreign-key check returns zero violations. These checks establish database consistency, not the real-world accuracy of every source advertisement.

# System Design refresh and security

Figure 3  Version publication and preservation of the previous valid pointer

![Figure 3  Version publication and preservation of the previous valid pointer](Report/figures/refresh_sequence.png)

SQLAlchemy builds a staging SQLite file inside a transaction. The completed database must pass a foreign-key check before its replacement. The pipeline then writes normalized tables, cleaned records and quality metadata into a version directory. A temporary pointer file is atomically replaced as current.json after the version is complete. A failed validation or build does not publish a new pointer. The isolated refresh tests check that invalid input retains the previous state and repeated fixture imports preserve the expected row count.

SQL Lab accepts predefined question identifiers rather than arbitrary modification statements and opens SQLite in read-only/query-only mode. Search treats user input literally rather than as unrestricted regex or SQL. Uploads are type/size/schema constrained, skill parsing is bounded and Excel formula-leading source strings are escaped. Credentials are not required for the core local app.

The implementation is intended for one trusted local operator. It does not supply authentication, concurrent-import coordination or durable multiuser cloud storage. A future shared deployment requires those controls and must validate data redistribution permissions before exposure.

# Implementation

Figure 4  Source modules used by the Streamlit entry point

![Figure 4  Source modules used by the Streamlit entry point](Report/figures/module_interaction.png)

| Module | Important functions and behavior |
| src/pipeline.py | clean, tokens, tables, build_database, run, load |
| src/analytics.py | filter_data, kpis, grouped, skill_stats, cooccurrence |
| src/sql_lab.py | execute predefined read-only query; validate complete library |
| src/exports.py | excel_bytes and executive_pdf from actual records |
| app.py | Native page navigation, session filters, Plotly and downloads |

Table 11  Source module functions

The application is started with python -m streamlit run app.py, not by serving a separate JavaScript frontend. Streamlit owns browser controls and presentation; Python modules perform the calculations and persistence. Supported HTML/CSS supplies local styling, while native widgets handle interaction. No hidden external service or model is required to produce the displayed metrics.

The preparation removed an unused expression that rendered an accidental None and changed the interface branding to the genuine project title. It added the startup script and operating guides while preserving calculations, source data, existing reports and Git history.

# Implementation filtering and exploration

Figure 5  Genuine Data Explorer page from the running local application

![Figure 5  Genuine Data Explorer page from the running local application](Screenshots/07_explorer.jpg)

Global selections are applied consistently to analytical records. Different dimensions intersect, while multiple values within a dimension act as alternatives. Later option lists narrow after earlier selections. Salary range excludes unknown salaries only when enabled, and observation dates remain labelled as collection dates. Reset clears filter state, and empty results receive an explanatory message.

Data Explorer adds literal title/company search, selected columns, 50-row pagination, record inspection, missingness and a data dictionary. CSV and Excel downloads use the filtered records. The screenshot is a browser capture of the implemented page, not a generated dashboard illustration. Quality metrics and SQL Lab intentionally retain full-snapshot scope and state it visibly.

The interface provides separate pages for salary, skill demand, geography, companies, remote work, data quality and reporting. A desktop browser was used for the captured views. Narrow layout and light presentation require their own checks rather than being inferred from successful backend tests.

# Implementation read only SQL

Figure 6  Executed median-salary business question in the actual SQL Lab

![Figure 6  Executed median-salary business question in the actual SQL Lab](Screenshots/09_sql.jpg)

The library contains 38 questions covering filtering, grouping, HAVING, joins, nested queries, common table expressions and window functions. ROW_NUMBER selects a deterministic top result within a group, NTILE divides ordered salaries into quartiles, and LAG compares monthly observation counts. Co-occurrence uses a self-join on the bridge, while the portable median averages the central ordered row positions.

Each question has a readable SQL statement, assumptions and an exportable result. Read-only connections prevent the question interface from modifying source tables. The median question was selected and executed in the live browser; its result is consistent with the independent Python median. Full query CSVs and recorded schemas allow later inspection without relying on a screenshot alone.

SQL Lab is explicitly full-snapshot analysis. It does not imply that a selected global chart filter modifies every predefined SQL statement. This clear scope distinction avoids contradictory comparisons when a user moves from a filtered chart to a fixed analytical question.

# Implementation exports and local operation

## Everyday launch

```
./start_project.command --check
./start_project.command
```
The executable macOS script resolves its own directory, selects an existing environment, validates Python/dependencies and checks the snapshot. It prints the loopback URL, activates the selected environment and dispatches Streamlit. It never silently installs software. The project-local .venv is preferred; the existing delivery environment is a documented fallback. Manual startup remains available if Finder handling or environment selection fails.

## Exports and evidence

| Artifact | Implemented behavior |
| Current executive PDF | Built from filtered records with provenance and sample limits |
| CSV | Filtered cleaned observations or selected SQL result |
| Excel workbook | Cleaned analytical columns, tables, chart, formulas and preaggregated sheets |
| Static figures | Executable Matplotlib/Seaborn output from genuine records |
| Technical report | Editable Word source with matching rendered PDF and verified index |

Table 12  Export formats and behavior

The existing packaged workbook was previously recalculated through LibreOffice and reconciled with Python and SQL. Newly generated workbook bytes require recalculation in an office engine to evaluate formula caches. Native Excel PivotTable objects are not claimed. Power BI support consists of table imports, relationships, DAX and page specifications; no validated native PBIX is represented as delivered.

## Operational verification limits

Launcher preflight, dependency resolution and error cases were tested. The existing server was inspected in the actual browser. Creating an additional listening process from the preparation tool was blocked by its socket permissions, so this report does not claim a successful fresh launcher/server cycle in that tool. The setup guide supplies the exact current-Mac and manual commands for independent Terminal use.

# Results and Discussion

Figure 7  Genuine executive dashboard with calculated full-snapshot metrics

![Figure 7  Genuine executive dashboard with calculated full-snapshot metrics](Screenshots/01_executive.jpg)

| Metric | Measured result |
| Retained observations | 56,004 |
| Normalized employer names | 13,177 |
| Unique extracted skill tokens | 134 |
| Usable salary coverage | 16.11% |
| Explicit Remote / all observations | 44.73% |

Table 13  Executive results

The overview connects volume, coverage and compensation rather than presenting salary without its disclosed sample. The single search country is a coverage constraint, not evidence that all jobs physically occur in that country. Counts represent retained observations, so repeated collection on different days can remain. The dashboard displays these qualifications alongside the metrics.

# Results and Discussion salary evidence

Figure 8  Reproducible histogram of the 9,022 usable annual candidates

![Figure 8  Reproducible histogram of the 9,022 usable annual candidates](Report/charts/salary_distribution.png)

| Statistic | Unverified source units |
| 10th percentile | 43,680 |
| 25th percentile | 62,400 |
| Median | 88,400 |
| Mean | 92,131.04 |
| 75th percentile | 116,812.50 |
| 90th percentile | 145,000 |

Table 14  Salary distribution summaries

The mean exceeds the median in the disclosed subset, and the histogram shows the distribution rather than asserting that every subgroup has the same shape. The central half spans more than 54,000 source units. These observations can guide further benchmarking, but they do not establish pay for records with missing salary, verify currency or predict a future offer. Differences by experience or skill remain potentially confounded.

# Results and Discussion skill evidence

Figure 9  Top extracted skill tokens counted once per retained observation

![Figure 9  Top extracted skill tokens counted once per retained observation](Report/charts/skill_demand.png)

| Skill | Demand observations | Usable salary sample |
| sql | 28,081 | 4,072 |
| excel | 17,867 | 2,681 |
| python | 17,050 | 2,221 |
| tableau | 15,266 | 2,330 |
| power_bi | 14,531 | 1,944 |
| r | 10,312 | 1,357 |

Table 15  Skill demand and salary samples

SQL appears in 28,081 records, followed by Excel and Python in the extracted vocabulary. The denominator is the full retained snapshot; empty extraction fields remain in it. Skill-associated salaries use a smaller disclosed subset. Demand can support role research and portfolio prioritization, but token extraction may omit synonyms and co-required skills make causal salary attribution inappropriate.

# Results and Discussion verification

| Verification area | Executed evidence |
| Automated suite | 85 passed; 0 failed; 0 skipped; 0 errors |
| Data transformations | Schema, duplicate rules, safe tokens, salary boundaries and annualization |
| Database | Repeatable imports, key constraints, integrity ok, zero foreign-key violations |
| Analytics and exports | Known-fixture filters/KPIs, real median reconciliation, readable PDF/XLSX |
| Application | All 11 page scripts, filter/reset and SQL action checks |
| Launcher | Preflight from another folder, missing interpreter and invalid port checks |
| Offline process test | Non-loopback socket connections denied; no external attempts observed |
| SQL performance | 38 executed queries; maximum 0.304 seconds in the recorded local run |

Table 16  Verification coverage

The current automated evidence was rerun after the presentation and launcher changes. Small fixtures remain confined to tests; the production dashboard reads the genuine snapshot. A separate invalid-import test confirms that a failure preserves the active pointer, while a valid fixture refresh is exercised in an isolated directory. No test fixture is presented as a live market dataset.

Browser evidence complements AppTest [5]. Genuine views of the actual local interface were captured, including the executive dashboard, exploration and SQL execution. These images establish what was rendered at capture time. They do not independently prove every possible filter combination, a completed browser upload, a fresh server launch or fully disconnected geographic rendering. Those limits remain explicit rather than being hidden by the passing test count.

## Practical interpretation

The system produces repeatable descriptive observations with inspectable denominators. The most consequential result is the limited compensation evidence: only about 16.1% of retained records have usable salary. The workflow therefore makes missingness, provenance and sample size part of ordinary exploration, helping users avoid stronger conclusions than the source supports.

# Advantages

## Traceable analysis

The source checksum and retained raw copy provide an audit path from input to output. Explicit transformation functions make assumptions visible and repeatable. A reviewer can inspect a salary candidate before screening, identify its source route and distinguish a missing estimate from a rejected one. This is more informative than a cleaned file that silently discards provenance.

## Consistent calculations and efficient exploration

The same independent analytics functions support KPIs, charts and exports. Native sidebar filters narrow relevant observations without requiring a user to edit code, while Data Explorer supplies record-level inspection. A normalized bridge handles job-skill relationships without duplicating definitions, and a predefined SQL library makes business questions readable and repeatable. The executed queries all completed within the recorded local subsecond range, although that observation is not a performance guarantee for other machines or data sizes.

## Practical local operation

SQLite avoids external database setup. The existing genuine snapshot and installed environment permit a local demonstration without a paid API or live job-portal dependency. The new launcher separates prerequisite checking from installation and offers an explicit manual fallback. Documentation explains first-time setup, everyday launch, stopping, restarting and common errors so that operation does not depend on an assistant being present.

## Transparent technical boundaries

The interface preserves Unknown arrangements, unverified currency and search-target geography rather than turning missing metadata into confident claims. The project reports what is executed in SQLite and Streamlit separately from the supporting Power BI and PostgreSQL assets. Current tests and real screenshots provide complementary evidence without treating either as complete proof of all runtime behavior.

| Need | Project advantage |
| Inspect a headline result | KPI definitions, SQL and record explorer |
| Repeat a calculation | Deterministic rules and preserved snapshot |
| Compare skills responsibly | Demand and salary sample counts together |
| Demonstrate locally | Embedded database and documented startup |
| Extend the system | Separated preparation, analysis and presentation modules |

Table 17  User needs and implemented features

# Limitations

## Source and inference limitations

The snapshot is historical, nonrandom and limited to United States search targets. It does not identify verified workplace countries or current vacancy availability. Collection dates cannot be treated as original job-creation dates, and repeated observations across days can remain. Employer normalization does not resolve legal entities, subsidiaries or intermediaries. Source redistribution terms were not independently established.

Only 9,022 of 56,004 retained observations have usable annual salary candidates. Disclosure selection can bias compensation comparisons. Currency is unverified, and the baseline salary screen can remove legitimate atypical roles. Hourly annualization assumes full-time hours. Experience is inferred from title keywords, with an explicitly labelled default category. Extracted skill tokens can omit synonyms or requirements that were not recognized by the source.

The source has Remote and Unknown arrangements but no explicit onsite control. A remote-versus-onsite premium or hypothesis test is therefore unsupported for the supplied snapshot. Group thresholds limit small-sample rankings but do not control confounding. No causal salary effect, forecast or guaranteed career outcome is established.

## Implementation and verification limits

SQLite is the verified backend. Native Power BI Desktop and production PostgreSQL were not executed. Native Excel pivots are not supplied, and newly exported formula caches require office-engine recalculation. The application lacks an authentication layer and concurrent-import coordination, so the local upload workflow is intended for a trusted operator rather than an exposed multiuser service.

The test-process offline check does not prove an offline browser map: geographic assets may be fetched separately. A fully disconnected browser session remains unverified. Additional-server creation from the preparation tool was blocked by process socket permissions, so only launcher preflight/error behavior and the existing live server are claimed as tested. The browser upload control was inspected, while backend refresh behavior was verified in isolated tests; an unperformed live import is not represented as completed.

# Future Scope

## Improve the evidence before extending inference

The first priority is verified metadata. A future source should provide workplace country, explicit compensation currency, reliable posting dates, stable vacancy identifiers and clearly defined work arrangements. Improved metadata would support meaningful geographic comparisons, period-aware salary normalization and stronger control of repeated listings. Source terms and refresh permissions must be established before building an automated collection service.

## Strengthen operational reliability

A shared deployment should add authentication, upload authorization, concurrency controls, migrations and durable storage. A PostgreSQL backend should be implemented and validated end to end rather than inferred from an isolated SQL asset. Browser regression checks should cover desktop and narrow layouts, filters, downloads and empty states. Geographic assets should be served locally or replaced with a verified offline representation before claiming full browser independence from the network.

## Complete supporting tool validation

Power BI Desktop can be used to build and test a native PBIX from the documented tables and measures. Native Excel PivotTables and office-engine recalculation checks can be added to the supplementary workflow. Any new supporting artifact should be compared against the same committed snapshot and its SQL outputs. A fresh launcher/server lifecycle should be rehearsed in an unrestricted local Terminal on the target laptop.

## Evaluate predictive work only when justified

Salary estimation or trend forecasting would require suitable data, explicit target definitions, leakage prevention, train/test separation, meaningful baselines and uncertainty reporting. Randomly splitting repeated observations could exaggerate accuracy, so grouping by stable vacancy or employer identity would need consideration. The current descriptive system provides an inspectable foundation, but no predictive model is claimed. Experimental features should not replace the more immediate need for trustworthy metadata and reliable operation.

| Priority | Proposed extension | Acceptance evidence |
| 1 | Verified country/currency/date metadata | Source contract and validated field mappings |
| 2 | Offline browser assets and UI regression | Disconnected rendering and interaction checks |
| 3 | Shared deployment and database adapter | Authorization, concurrency and integrity tests |
| 4 | Optional predictive evaluation | Separated evaluation, baselines and error analysis |

Table 18  Future extensions and acceptance evidence

# Conclusion

Global Data Analytics Job Market Intelligence & Salary Trend Dashboard implements a genuine local analytics workflow from source observations to inspectable results. Python validates and prepares the snapshot, a constrained four-table SQLite model represents employers and skills, independent functions calculate filtered metrics, and Streamlit supplies the interactive workspace. The SQL library and downloadable artifacts let a reviewer examine results beyond their visual presentation.

The supplied snapshot produces 56,004 retained observations after removing 5,949 normalized same-day duplicates. It contains 134 extracted skill tokens and 9,022 usable salary candidates. The median disclosed amount is 88,400 source units. SQL appears in 28,081 retained observations. These numerical observations come from the actual processed records and remain qualified by missingness, unverified currency and the collection scope.

Verification includes 85 passing automated checks, all 38 SQL questions, successful integrity checks and real browser captures. The local setup guide, demonstration script, question set and prerequisite-checking launcher support independent operation on the target Mac. The report index follows its section order and printed body-page numbers, while the Word source remains editable. Existing project files and Git history were preserved, and this preparation did not push changes to the remote repository.

## Responsible use of the results

The dashboard supports descriptive exploration, not a claim of current global hiring coverage or guaranteed compensation. Search target is not verified job location; an absent remote flag is not an onsite requirement; and an associated salary is not a causal skill premium. The next improvements should address those evidence gaps and complete the remaining runtime checks before expanding the inferential scope.

The practical outcome is a reproducible, locally operated analytics application with transparent methods and reviewable evidence. A user can start the existing environment, inspect the snapshot, apply filters, run a defined SQL question and export a report while explaining the limits of each result. That connection between working software and defensible interpretation is the project’s central contribution.

# References

## [1] Dataset source

Luke Barousse. Data Analyst Job Postings (Google Search Results), Kaggle. The local snapshot is identified by SHA-256 in its quality metadata.

https://www.kaggle.com/datasets/lukebarousse/data-analyst-job-postings-google-search

## [2] Pandas documentation

The pandas development team. User Guide: missing data, grouping and data manipulation.

https://pandas.pydata.org/docs/user_guide/

## [3] SQLite documentation

SQLite project. SQL language reference, foreign keys and window functions.

https://www.sqlite.org/docs.html

## [4] SQLAlchemy documentation

SQLAlchemy project. Working with transactions and the DBAPI.

https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html

## [5] Streamlit application testing

Streamlit documentation. AppTest executes application code and simulates supported interactions; browser verification is complementary.

https://docs.streamlit.io/develop/api-reference/app-testing

## [6] Plotly geographic and interactive charts

Plotly Python documentation. Choropleth maps and base-map configuration.

https://plotly.com/python/choropleth-maps/

## [7] Python literal parsing

Python documentation. ast.literal_eval and documented resource considerations.

https://docs.python.org/3.14/library/ast.html#ast.literal_eval

## [8] Statistical comparison

SciPy documentation. scipy.stats.mannwhitneyu. The current dataset does not meet the application’s explicit onsite sample requirement.

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html

## [9] Local implementation evidence

Repository source, SQL library, Report/DEMO_VERIFICATION.json and genuine Screenshots captures. The source repository address is supplied by the project owner.

https://github.com/ektaranjan/Global-Data-Analytics-Job-Market

Documentation access and local verification date: 21 October 2026. Dataset processing date and original acquisition time are separate provenance fields; an unknown acquisition time is not inferred from the verification date.
