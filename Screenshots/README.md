# Current screenshot evidence

On 21 October 2026, browser access to the existing local server was explicitly authorized and genuine screenshots were captured at a 1366 × 900 desktop verification viewport. These files come from the rendered Streamlit application; none is generated dashboard artwork.

- 01_executive.jpg: full-snapshot executive KPIs and observed activity.
- 02_salary.jpg and 03_skills.jpg: salary and skill views.
- 04_geography.jpg, 05_company.jpg and 06_remote.jpg: source-limited geography, employer and arrangement pages.
- 07_explorer.jpg: source-record exploration.
- 08_quality.jpg and 13_upload_control.jpg: quality metrics and the implemented upload control. A screenshot of the control does not claim a completed live import.
- 09_sql.jpg: the actual executed median query and its 88,400 source-unit result.
- 10_reports.jpg: report/download controls; the executive PDF was downloaded and parsed successfully.
- 11_about.jpg: project documentation page.
- 12_explorer_search.jpg and 14_senior_filter.jpg: search and global-filter interaction evidence. Senior narrows the executive view to 8,772 observations.

The professional 30-page report embeds selected genuine captures and reproducible charts. Refresh screenshots and evidence after a data or UI change. Backend refresh tests use an isolated temporary dataset; test fixtures do not supply production results.

## Previous status recorded on 19 October 2026

The following original note is historical and is superseded by the captures above:

# Screenshot evidence status

No dashboard screenshots were captured. Browser access to localhost was denied at the approval gate. Streamlit script-level tests are in Report/tests.xml; they do not establish browser visual quality. To complete this gate, run the app locally and capture all eleven pages, the upload/refresh interaction and a tooltip/filter interaction with an authorized browser. Use genuine browser images, never generated artwork.
