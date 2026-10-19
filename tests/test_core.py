import json,sqlite3
import pandas as pd
import pytest
from src.pipeline import clean,tokens,experience,remote,tables,build_database,current_folder,ROOT
from src.analytics import kpis,filter_data,skill_stats
from src.sql_lab import QUERIES,execute
from src.exports import executive_pdf,excel_bytes
from openpyxl import load_workbook
from pypdf import PdfReader
import io

def fixture(**kwargs):
 d=dict(title=['Data Analyst','Senior Analyst','Junior Analyst','Lead Analyst'],company_name=[' A ','B','C','D'],location=['NY','SF','NY','NY'],description_tokens=["['sql','sql','python']","['excel']","[]","['sql']"],date_time=['2024-01-01']*4,search_location=['United States']*4,salary_standardized=[100000,None,None,500000],salary_yearly=[90000,80000,None,None],salary_hourly=[10,20,25,None],work_from_home=[True,None,False,None])
 d.update(kwargs);return pd.DataFrame(d)
def test_required_schema():
 with pytest.raises(ValueError):clean(pd.DataFrame({'x':[1]}))
def test_empty():
 with pytest.raises(ValueError):clean(fixture().iloc[:0])
def test_priority_and_hourly():
 d,q=clean(fixture());assert d.salary_year_avg.iloc[:3].tolist()==[100000,80000,52000];assert pd.isna(d.salary_year_avg.iloc[3]);assert q['invalid_salary']==1
@pytest.mark.parametrize('value,expected',[(None,'Unknown'),(True,'Remote'),(False,'Onsite'),('no','Onsite'),('garbage','Unknown')])
def test_remote(value,expected):assert remote(value)==expected
@pytest.mark.parametrize('value,expected',[('Sr. Analyst','Senior'),('Junior Analyst','Junior/Entry'),('Manager','Lead/Manager'),('Data Analyst','Mid-Level (inferred)')])
def test_experience(value,expected):assert experience(value)==expected
@pytest.mark.parametrize('value', ["__import__('os').system('echo unsafe')",'{}','not a list',"[1,2]",None])
def test_safe_tokens(value):assert tokens(value)==[]
def test_dedup():
 a=fixture();d,q=clean(pd.concat([a,a.iloc[:1]]));assert len(d)==4;assert q['exact_duplicates_removed']==1
 a.loc[1,['title','company_name','location']]=a.loc[0,['title','company_name','location']];d,q=clean(a);assert len(d)==3;assert q['composite_duplicates_removed']==1
def test_missing_salary():
 d,q=clean(fixture(salary_standardized=[None]*4,salary_yearly=[None]*4,salary_hourly=[None]*4));assert d.salary_year_avg.isna().all();assert q['missing_salary']==4
@pytest.mark.parametrize('v,ok',[(14999,False),(15000,True),(400000,True),(400001,False)])
def test_salary_boundaries(v,ok):
 d,q=clean(fixture(salary_standardized=[v]*4));assert bool(d.salary_valid.iloc[0])==ok

def test_range_units():
 a=fixture(salary_standardized=[None]*4,salary_yearly=[None]*4,salary_hourly=[None]*4,salary_min=[20,60000,3000,1],salary_max=[30,80000,4000,2],salary_rate=['an hour','a year','a month','unknown']);d,_=clean(a);assert d.salary_year_avg.iloc[:3].tolist()==[52000,70000,42000];assert pd.isna(d.salary_year_avg.iloc[3])
def test_db_integrity_and_repeatability(tmp_path):
 d,_=clean(fixture());t=tables(d);p=tmp_path/'x.db'
 for i in range(2):build_database(t,p)
 with sqlite3.connect(p) as c:
  assert not c.execute('PRAGMA foreign_key_check').fetchall();assert c.execute('SELECT COUNT(*) FROM job_postings_fact').fetchone()[0]==4
  c.execute('PRAGMA foreign_keys=ON')
  with pytest.raises(sqlite3.IntegrityError):c.execute("INSERT INTO skills_job_dim VALUES('bad',1)")
def test_filters_and_kpis():
 d,_=clean(fixture());f=filter_data(d,{'skills':['sql'],'remote_status':['Remote']});assert len(f)==1;assert kpis(f)['Postings']==1;assert kpis(f)['Mean salary']==100000;assert skill_stats(f).demand.max()==1
 assert filter_data(d,{'skills':['nonexistent']}).empty
 assert len(filter_data(d,salary=(50000,90000)))==2
 assert len(filter_data(d,dates=('2023-01-01','2023-12-31')))==0

def test_pdf_and_excel():
 d,q=clean(fixture());q.update(snapshot_start='2024-01-01',snapshot_end='2024-01-01',sha256='test fixture')
 b=executive_pdf(d,q);assert len(PdfReader(io.BytesIO(b)).pages)>0
 w=load_workbook(io.BytesIO(excel_bytes(d)));assert w['Cleaned'].max_row==5;assert w['Summary']['B11'].data_type=='f'
@pytest.mark.parametrize('q',QUERIES,ids=lambda q:str(q['id']))
def test_real_sql_executes(q):assert execute(q['id']).columns.size>0

def test_real_kpi_reconciliation():
 from src.pipeline import load
 d,q=load();assert len(d)==q['clean_records'];assert execute(1).iloc[0,0]==len(d);assert execute(6).iloc[0,0]==pytest.approx(d.salary_year_avg.median())

def test_failed_refresh_keeps_pointer(tmp_path):
 from src.pipeline import run
 pointer=(ROOT/'Dataset/current.json').read_bytes();p=tmp_path/'bad.csv';p.write_text('x\n1\n')
 with pytest.raises(ValueError):run(p)
 assert (ROOT/'Dataset/current.json').read_bytes()==pointer

def test_valid_pipeline_refresh_is_idempotent_and_isolated(tmp_path,monkeypatch):
 import src.pipeline as pipeline
 (tmp_path/'SQL').mkdir();(tmp_path/'SQL/schema.sql').write_text((ROOT/'SQL/schema.sql').read_text())
 (tmp_path/'Dataset/raw').mkdir(parents=True);(tmp_path/'Dataset/processed').mkdir()
 source=tmp_path/'fixture.csv';fixture().to_csv(source,index=False)
 monkeypatch.setattr(pipeline,'ROOT',tmp_path)
 first=pipeline.run(source);pointer=(tmp_path/'Dataset/current.json').read_text()
 second=pipeline.run(source);assert first['sha256']==second['sha256'];assert (tmp_path/'Dataset/current.json').read_text()==pointer
 folder=tmp_path/json.loads(pointer)['folder']
 with sqlite3.connect(folder/'job_market.db') as c:assert c.execute('SELECT COUNT(*) FROM job_postings_fact').fetchone()[0]==4
