# Global Data Analytics Job Market Intelligence & Salary Trend Dashboard

A local analytics dashboard for exploring historical job postings, skill demand, employers and disclosed salary trends. Python prepares the data, SQLite supports relational analysis, and Streamlit provides interactive charts, filters, search and downloads.

## Project Report

- [Download PDF Report](Report/Global_Data_Analytics_Job_Market_Report.pdf)
- [Download Editable Word Report](Report/Global_Data_Analytics_Job_Market_Report.docx)

The technical report contains 30 pages covering requirements, methodology, architecture, implementation, results and limitations.

## Run locally

Python 3.11 or later is required. From the project folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

For everyday use, activate the existing environment and run the last command. Open http://localhost:8501 and stop with Control+C. If this port already hosts the application, open that instance.

## Features

- Eleven dashboard pages with global filters and searchable records.
- Salary distributions, skill demand, employer comparisons and observation trends.
- Data quality monitoring and validated CSV refresh.
- Thirty-eight predefined read-only SQL questions.
- Filtered CSV, Excel and executive PDF exports.

## Data and interpretation

Source: [Luke Barousse — Data Analyst Job Postings](https://www.kaggle.com/datasets/lukebarousse/data-analyst-job-postings-google-search).

The supplied source contains 61,953 rows; cleaning retains 56,004 observations. There are 9,022 usable annual salary candidates, with a median of 88,400 in unverified source currency units. Dates span November 2022 to April 2025. These are historical observations, not a live vacancy feed.

Search country represents collection targets rather than verified workplace country. Missing work arrangements remain Unknown. Salary disclosure is incomplete; skill associations do not establish causal salary effects. Redistribution permissions must be verified before sharing the source data.

## Architecture

`src/pipeline.py` validates and transforms CSV input and publishes versioned SQLite/CSV snapshots. `src/analytics.py` calculates filtered metrics. `src/sql_lab.py` executes the predefined SQL library. `src/exports.py` produces downloadable outputs. `app.py` provides the interface.

## Verification and operating limits

```bash
python -m pytest -q
```

The professional report records the checks performed on its documented environment. Re-run tests after changing code or data. Core processing uses local files without API keys or a paid service. Geographic browser assets may require internet access; a fully disconnected map is not verified. First-time dependency installation requires package access.

The verified database is SQLite. Supporting Power BI specifications and PostgreSQL assets are not evidence of a validated native PBIX or production PostgreSQL deployment.

## Credits

Dataset: Luke Barousse. Libraries: Python, pandas, NumPy, SQLAlchemy, Streamlit, Plotly, SciPy, Matplotlib, Seaborn, ReportLab, openpyxl and python-docx. Source attribution and software licenses remain applicable.
