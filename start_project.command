#!/bin/bash
# Local launch only: never installs packages or changes system configuration.
set -euo pipefail
PROJECT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJECT_DIR"
PORT="${PROJECT_PORT:-8501}"
CHECK_ONLY=0
if [[ "${1:-}" == "--check" ]]; then CHECK_ONLY=1; shift; fi
if [[ $# -ne 0 ]]; then printf 'Usage: %s [--check]\n' "$0" >&2; exit 2; fi
PYTHON="${PROJECT_PYTHON:-}"
if [[ -z "$PYTHON" ]]; then
  for candidate in "$PROJECT_DIR/.venv/bin/python" "$PROJECT_DIR/../../work/venv/bin/python"; do
    if [[ -x "$candidate" ]]; then PYTHON="$candidate"; break; fi
  done
fi
if [[ -z "$PYTHON" || ! -x "$PYTHON" ]]; then
  printf 'No project Python environment found.\nRead LOCALHOST_SETUP_AND_RUN_GUIDE.md for first-time setup.\n' >&2
  exit 1
fi
export PYTHONUTF8=1
export STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
export MPLCONFIGDIR="${TMPDIR:-/tmp}/global-job-market-matplotlib"
"$PYTHON" - "$PORT" "$CHECK_ONLY" <<'PY'
import importlib.util,json,socket,sys
from pathlib import Path
if sys.version_info < (3,11):raise SystemExit('Python 3.11 or later is required.')
modules=['streamlit','pandas','numpy','sqlalchemy','plotly','scipy','matplotlib','seaborn','openpyxl','reportlab','docx','pytest','pypdf']
missing=[m for m in modules if importlib.util.find_spec(m) is None]
if missing:raise SystemExit('Missing packages: '+', '.join(missing)+'\nInstall requirements in this environment using the setup guide.')
try:
 port=int(sys.argv[1]);assert 1024<=port<=65535
except (ValueError,AssertionError):raise SystemExit('PROJECT_PORT must be an integer between 1024 and 65535.')
pointer=Path('Dataset/current.json')
if pointer.exists():
 try:
  p=json.loads(pointer.read_text());folder=(Path.cwd()/p['folder']).resolve()
  if not folder.is_relative_to(Path.cwd()/'Dataset/processed'):raise ValueError('Snapshot path is outside Dataset/processed')
  for name in ['jobs_cleaned.csv','quality.json','job_market.db']:
   if not (folder/name).is_file():raise ValueError('Missing snapshot file: '+name)
  quality=json.loads((folder/'quality.json').read_text());print(f"Snapshot ready: {quality['clean_records']:,} records, {quality['snapshot_start']} to {quality['snapshot_end']}")
 except (KeyError,ValueError,OSError) as e:raise SystemExit('Snapshot check failed: '+str(e)+'\nSee the missing-data steps in the setup guide.')
else:print('No imported snapshot. The application will show its CSV upload screen.')
print('Python:',sys.version.split()[0]);print('Dependencies: ready')
if sys.argv[2]!='1':
 with socket.socket() as s:
  try:s.bind(('127.0.0.1',port))
  except PermissionError:raise SystemExit('This environment blocks local listening sockets. Run this script directly in macOS Terminal.')
  except OSError:raise SystemExit(f'Port {port} is already occupied. Use the existing dashboard or choose another PROJECT_PORT.')
print(f'Local URL: http://127.0.0.1:{port}')
PY
if [[ "$CHECK_ONLY" == 1 ]]; then printf 'Preflight completed. No server started.\n'; exit 0; fi
ACTIVATE="$(dirname -- "$PYTHON")/activate"
if [[ -f "$ACTIVATE" ]]; then source "$ACTIVATE"; fi
printf '\nOpen http://127.0.0.1:%s in your browser.\nStop with Control+C in this Terminal window.\n\n' "$PORT"
exec "$PYTHON" -m streamlit run "$PROJECT_DIR/app.py" --server.address 127.0.0.1 --server.port "$PORT" --server.headless true --browser.gatherUsageStats false
