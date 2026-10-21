"""Launcher checks cover missing prerequisites and avoid implicit installation."""
import os,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def invoke(extra=None):
 env={**os.environ,**(extra or {})}
 return subprocess.run(['bash',str(ROOT/'start_project.command'),'--check'],cwd='/private/tmp',env=env,capture_output=True,text=True,timeout=20)
def test_launcher_finds_project_from_another_directory():
 p=invoke();assert p.returncode==0,p.stderr;assert 'Dependencies: ready' in p.stdout;assert 'No server started' in p.stdout

def test_launcher_missing_explicit_python():
 p=invoke({'PROJECT_PYTHON':'/nonexistent/project/python'});assert p.returncode!=0;assert 'No project Python environment found' in p.stderr

def test_launcher_rejects_bad_port():
 p=invoke({'PROJECT_PORT':'invalid'});assert p.returncode!=0;assert 'PROJECT_PORT must be an integer' in p.stderr

def test_launcher_does_not_implicitly_install():
 s=(ROOT/'start_project.command').read_text();assert 'pip install' not in s;assert 'brew install' not in s
