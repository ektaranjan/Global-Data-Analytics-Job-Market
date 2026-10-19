# Deliverable status

## Executed and verified

- Original 52-page PDF extracted and audited before application code; subsection, field, figure, table and placeholder inventory retained.
- Genuine local CSV processed: 61,953 raw rows, 56,004 clean observations, 5,949 composite duplicates, 8 invalid salary candidates, 9,022 usable salary observations.
- Four constrained SQLite tables built; referential integrity and repeatable imports tested.
- 38 read-only SQL queries executed and exported with schemas and timings.
- 11 Streamlit pages passed script-level AppTest checks. Filter/reset and SQL actions passed.
- 81 pytest tests passed; no failures or skips in the final executed run.
- Excel workbook and static chart package generated. Packaged workbook recalculated with LibreOffice; cached record count, mean salary and coverage match Python/SQL. Native Microsoft Excel execution is untested.
- 22 numerical observations generated, each with question, sample size, evidence, interpretation, caveat and separate audience recommendations.

## Required limitations and unfinished gates

- Browser access to localhost was denied at the approval gate. No screenshots are fabricated. Visual responsiveness, tooltip appearance and light-mode polish remain unverified.
- Power BI Desktop is unavailable on macOS. Theme, DAX, relationships and layout assets are provided; no PBIX or Power BI screenshots are delivered or claimed.
- Search targets are exclusively United States. Actual job-country data and global comparisons are unsupported.
- Currency metadata is unverified; no USD labels or currency conversion claims are justified.
- Missing remote flags remain Unknown; the sample has no explicit onsite control. Remote-versus-onsite inference is unsupported.
- PostgreSQL support is a separate SQL asset, not an executed production backend.
- Native Excel pivots are not generated; use the documented creation instructions.
- Browser-based upload interaction was not captured; failed-refresh preservation and database repeatability are backend-tested. Large-file/concurrent-user stress testing is pending.
- Full clean-install rehearsal on Windows/Linux and Python 3.11 is pending. The local installation and tests ran on macOS ARM64 Python 3.14.
- Source license must be verified before data redistribution. No public GitHub repository or cloud deployment was created.
- Academic report rendering status is recorded separately in Report/render_verification.md. Student identity, signed declarations/certificates and university formatting approval remain user tasks.

The project is a tested local implementation with explicitly incomplete native Power BI and browser evidence. It must not be called fully submission-ready until those university-required items are completed.
