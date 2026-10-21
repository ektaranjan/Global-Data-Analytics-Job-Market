# Localhost setup and run guide

This guide runs the existing Global Data Analytics Job Market application on your Mac without Codex. The verified computer uses macOS on Apple Silicon (arm64), Python 3.14.3, Streamlit 1.66.0 and a local SQLite snapshot. No Node.js application, paid API, external database server or API key is required.

## Everyday use on this Mac

1. Press Command + Space, type Terminal and press Return.
2. Paste this command and press Return:

```bash
cd "/Users/ektaranjan/Documents/Codex/2026-10-19/files-mentioned-by-the-user-mca/outputs/job-market-intelligence"
```

3. Start the existing environment through the launcher:

```bash
./start_project.command
```

4. Open http://127.0.0.1:8501 in Safari or Chrome. Keep Terminal open. Stop the server with Control + C in that Terminal window. To restart, run the same launcher again.

You can also double-click start_project.command in Finder; it is executable and resolves its own folder. macOS may require you to use Open from Finder for a script downloaded from GitHub. The Terminal method above remains the fallback; do not disable operating-system security protections.

The launcher prefers `.venv/bin/python` inside the project. On this existing delivery it falls back to `../../work/venv/bin/python`, which already has the required packages. It checks Python, packages, snapshot paths and the port, prints the URL, activates the selected environment and starts Streamlit. It never installs packages automatically. It will stop with an explanation if prerequisites are missing.

A server was already listening on 127.0.0.1:8501 and was verified through the actual browser during this preparation. If the launcher says that port is occupied, open that URL first. The preflight and error branches were tested; starting an additional listening server from the preparation tool was blocked by that tool's process permissions. This limitation does not establish that macOS Terminal itself will block the launcher.

## Manual everyday startup

From the project folder, use the installed environment directly:

```bash
source ../../work/venv/bin/activate
python -m streamlit run app.py --server.address 127.0.0.1 --server.port 8501 --browser.gatherUsageStats false
```

If you created the recommended project-local environment instead, activate it using `source .venv/bin/activate` before the same Streamlit command. The main entry point is app.py. The current data is already imported; do not reimport it just to open the dashboard.

## First-time setup on another Mac or a fresh clone

Check prerequisites:

```bash
python3 --version
uname -m
```

Python must be 3.11 or newer. This project was tested on Python 3.14.3 / arm64; other Python versions and platforms were not independently rehearsed here. If Python is missing, install a supported macOS Python release from https://www.python.org/downloads/macos/ before continuing. Installing a new system Python was not necessary on the verified Mac and was not performed.

Navigate to the project folder using `cd`, then create and activate an isolated environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip check
```

A Python 3.14 virtual-environment creation probe and activation were successfully executed in a separate temporary directory. The existing environment passes `pip check`, and an offline dry run confirms all declared requirements are already satisfied. Downloading packages into a newly empty environment needs internet and was not repeated during this preparation. These are the setup commands for this repository, not a claim of a second clean installation.

A GitHub clone excludes the large raw and processed snapshots. Obtain an authorized gsearch_jobs.csv from the dataset source listed in README.md. On the original Mac, the supplied source is in Downloads. Import it once:

```bash
python -m src.pipeline "$HOME/Downloads/gsearch_jobs.csv"
```

To rebuild supporting query exports and charts after importing, run:

```bash
python -m src.sql_lab
python -m scripts.build_outputs
```

The second command regenerates existing supporting outputs, including the workbook. Keep a backup if you need the old evidence. It is unnecessary for ordinary startup. Run the application with `./start_project.command` after setup. No `.env` file is required for the core project.

## Preflight and optional settings

```bash
./start_project.command --check
```

This validates dependencies and snapshot files without starting a server. To choose another port, for example:

```bash
PROJECT_PORT=8503 ./start_project.command
```

Use a port that is free on your computer. To select another already-created virtual environment, set PROJECT_PYTHON to its absolute bin/python path. These are optional launcher settings; they are not required application secrets.

## Offline use

Keep the installed environment and Dataset/current.json plus its processed snapshot on the laptop. Local data loading, calculations, SQLite SQL, exports and all 11 page scripts passed automated checks with external socket connections denied in the test Python process. There were no attempted external connections during that run. This is process-level evidence, not a claim that the operating system Wi-Fi was switched off.

Ordinary local charts use the bundled application libraries and processed records. The geographic choropleth may request Plotly geographic assets in a browser; a fully disconnected browser rendering of that map is not proven. Use the geographic table/location bars and the included report charts as the offline fallback. Downloading Python packages, obtaining a new source snapshot and GitHub operations require internet. No live job-market API is part of this application.

## Troubleshooting

| Symptom | What to do |
|---|---|
| `command not found: python` | Activate the project environment; use python3 to create an environment if necessary. |
| `command not found: streamlit` | Use `python -m streamlit run app.py` after activation. |
| No environment found | Complete first-time setup, or use the current Mac's existing environment with the manual method. |
| Missing package / ModuleNotFoundError | Check `which python`; then run `python -m pip install -r requirements.txt` in that environment while online. |
| Python older than 3.11 | Install a supported Python, create a new environment with it and reinstall requirements. Do not replace an existing working environment blindly. |
| Permission denied for the launcher | From the project folder run `bash start_project.command`; the supplied file is already executable. |
| Port already in use | Open the existing local URL, or choose a free PROJECT_PORT. Do not terminate another process merely because its port is occupied. |
| Missing snapshot / upload screen | Import the genuine CSV with src.pipeline, or use the dashboard's CSV upload screen. Do not use test fixtures as production data. |
| Snapshot file missing | Keep current.json together with the matching processed folder, or reimport the authorized source. |
| Empty chart | Reset filters; salary comparisons require at least 30 usable salaries. Unknown is a separate work arrangement. |
| Broken page | Preserve the complete Terminal error, identify the selected page and run `python -m pytest -q` from the repository root. |
| Internet or API error | The core has no API keys. Check whether the error concerns initial package/data download or an optional browser map asset. |
| Browser cannot connect | Keep the server Terminal open and check its printed address/port. Starting only Python without Streamlit does not serve the UI. |
| Missing environment variables | None are mandatory for the core; remove incorrect optional PROJECT_PYTHON or PROJECT_PORT overrides. |

## What to keep for a demonstration

Keep app.py, src, SQL, requirements, the activated environment, the genuine processed snapshot and existing Report/Screenshots files. Store the original raw CSV for repeatable refresh demonstrations. Never present a historical observation date as a current job-market feed. Salary currency and actual workplace-country metadata remain unverified.
