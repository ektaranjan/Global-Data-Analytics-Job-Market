"""Streamlit script-level smoke checks; these are not browser visual checks."""
from pathlib import Path
import pytest
from streamlit.testing.v1 import AppTest
APP=Path(__file__).resolve().parents[1]/'app.py'
PAGES=['Executive Command Center','Salary Intelligence','Skill Demand Intelligence','Global Geographic Intelligence','Company Intelligence','Remote Work Intelligence','Data Explorer','Data Quality and Pipeline Monitor','SQL Analytics Lab','Reports and Download Center','Project Documentation and About']
@pytest.mark.parametrize('page',PAGES)
def test_page_runs(page):
 a=AppTest.from_file(str(APP),default_timeout=120);a.session_state['page']=page;a.run();assert not a.exception,[(e.message) for e in a.exception]

def test_filter_and_reset():
 a=AppTest.from_file(str(APP),default_timeout=120).run();a.sidebar.multiselect(key='filter_experience_level').set_value(['Senior']).run();assert not a.exception
 assert int(a.metric[0].value.replace(',',''))>0
 a.sidebar.button[0].click().run();assert not a.exception
 assert int(a.metric[0].value.replace(',',''))==56004

def test_sql_action():
 a=AppTest.from_file(str(APP),default_timeout=120);a.session_state['page']=PAGES[8];a.run();a.button[0].click().run();assert not a.exception
