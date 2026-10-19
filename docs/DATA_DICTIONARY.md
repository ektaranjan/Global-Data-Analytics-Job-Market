# Data dictionary

One cleaned record represents one title/company/location/observation-day combination. It does not necessarily represent a unique vacancy across time.

| Field | Meaning and method |
|---|---|
| job_id | Surrogate hash of cleaned composite identity and deterministic row order |
| source_job_id | Original Google aggregation identifier retained for audit |
| job_title | Whitespace-normalized casefolded raw title |
| company_name | Casefolded employer name; no external entity resolution |
| company_id | Deterministic snapshot surrogate; not stable across different snapshots |
| location | Title-cased source location; not geocoded |
| job_country | search_location alias; a search target, not a verified workplace country |
| observation_date | UTC date parsed from date_time, the collection timestamp |
| posted_month | Observation month, not verified month of job creation |
| experience_level | Lead/Manager, Senior, Junior/Entry, otherwise Mid-Level (inferred) |
| remote_status | Explicit true Remote, explicit false Onsite, missing/other Unknown |
| salary_candidate | First nonmissing fallback candidate before screening |
| salary_year_avg | Candidate screened to inclusive 15,000–400,000; source currency unverified |
| salary_source | Standardized, yearly, hourly × 2,080, annualized range, or Missing |
| salary_missing | No candidate could be derived |
| salary_valid | Candidate within baseline thresholds; no proof of economic plausibility |
| salary_band | Left-closed bins below 60K, 60–90K, 90–120K, at least 120K |
| currency_status | Unverified source currency; no conversion performed |
| skills | Unique normalized skill tokens, safely parsed from a Python list |
| skill_type | Programming, analyst_tools, databases, cloud, libraries, other |
| platform | via prefix removed; casefolded platform name |
| employment_type | Source schedule_type or Unknown |

Raw schema: title, company_name, location, via, description, extensions, job_id, thumbnail, posted_at, schedule_type, work_from_home, salary, search_term, date_time, search_location, commute_time, salary_pay, salary_rate, salary_avg, salary_min, salary_max, salary_hourly, salary_yearly, salary_standardized, description_tokens, and two source index columns.

The reference PDF names salary_avg_min/max; the actual snapshot uses salary_min/max. Range fallback requires known annual/hourly/monthly units. Standardized source salary remains preferred exactly as specified. Missing and invalid salaries are never replaced with zero.
