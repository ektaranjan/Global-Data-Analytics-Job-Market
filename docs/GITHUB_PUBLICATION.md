# GitHub distribution notes

The GitHub repository contains application source, SQL, generated analytical query results, charts, the Excel workbook, the academic DOCX/PDF report and project documentation. Screenshots/README.md records why genuine dashboard screenshots are absent; generated charts are not presented as application screenshots.

Original files remain in the local project folder. The following local-only artifacts are excluded from Git:

- Dataset/raw: the original CSV is about 290 MB and exceeds GitHub's per-file limit.
- Dataset/processed and Dataset/current.json: generated dataset snapshots, including the 77 MB cleaned CSV and 33 MB SQLite database. Source redistribution terms remain unverified. These artifacts are rebuilt from an authorized source snapshot.
- DELIVERY_MANIFEST.md: contains absolute paths specific to the owner's computer.
- SHA256SUMS.json: describes the complete local delivery rather than the GitHub subset.
- Report/tests.xml, Report/final_validation.json and execution logs: include machine paths or hostname metadata. Report/github_validation_summary.json retains test counts and validation results without machine identifiers.
- Virtual environments, Python caches, credentials, editor settings and temporary files.

The supplied Excel report and query CSVs contain analytical records derived from the public job-posting source. Keep the repository private unless the owner approves public visibility and confirms redistribution rights for the source and derived artifacts. No dataset or report has been deleted from the local delivery.

## Reproduce after cloning

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m src.pipeline /absolute/path/to/gsearch_jobs.csv
python -m src.sql_lab
python -m scripts.build_outputs
python -m pytest -q
python -m streamlit run app.py
```

On Windows, create the environment using `py -3 -m venv .venv` and activate `.venv\Scripts\Activate.ps1`. Download an authorized snapshot from the source documented in README.md. The dashboard also presents an upload screen when no committed snapshot exists.

The full test suite includes actual-dataset checks and expects the delivered source snapshot for its recorded counts. Import the genuine snapshot before attempting the full test run. Tests are not expected to pass without that source data.

No public visibility change is authorized by this preparation. Remote publication status must be verified separately; this document alone does not establish that a repository or push exists.
