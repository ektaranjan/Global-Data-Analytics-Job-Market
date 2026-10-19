# Live demonstration script

Allow 10–15 minutes. Start from the project directory in an activated environment.

```bash
python -m src.sql_lab
python -m pytest -q
python -m streamlit run app.py
```

Minute 0–2: Explain the research question and the Kaggle source. Show the historical date interval, single search country and currency limitation. Distinguish observations from unique vacancies.

Minute 2–4: Show executive KPIs. Select Senior then Remote. Explain the active-record count and reset. Demonstrate salary distribution and coverage. The figures describe a disclosed subset, not all salaries.

Minute 4–6: Show top skills, associated salary sample counts and co-occurrence. Explain why correlations do not show causal salary premiums. Open geography and explain the search-target limitation.

Minute 6–8: Inspect an employer, show company sample thresholds, then Remote/Unknown. Explain why missing flags cannot be used as an onsite comparison.

Minute 8–10: Search SQL questions for median, execute it and export the result. Compare the median with the executive KPI. Show the four-table ER model in documentation.

Minute 10–12: Open quality, inspect the checksum and duplicate counts. Upload the original preserved raw CSV to demonstrate repeatable refresh. Then attempt a malformed CSV and show that the previous valid snapshot remains current.

Minute 12–15: Generate a filtered PDF, download Excel, show the automated test record and discuss limitations. Explain that Power BI assets require Desktop for native PBIX validation.

Offline backup: install dependencies in advance, retain the genuine local raw snapshot and the processed version, then run the same local commands. Do not depend on Kaggle or a live API during the demonstration. If the browser fails, use Report/query_*.csv, generated charts, workbook and execution records as supporting evidence, while honestly stating that the interactive demonstration failed.
