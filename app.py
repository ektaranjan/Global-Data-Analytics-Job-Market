"""Job-market snapshot analytics. Launch with streamlit run app.py."""
import io,json,tempfile,zipfile
from pathlib import Path
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from src.pipeline import ROOT,load,run,current_folder,category
from src.analytics import filter_data,kpis,skill_stats,grouped,cooccurrence
from src.sql_lab import QUERIES,execute
st.set_page_config(page_title='Global Data Analytics Job Market Intelligence & Salary Trend Dashboard',page_icon='📊',layout='wide')
PAGES=['Executive Command Center','Salary Intelligence','Skill Demand Intelligence','Global Geographic Intelligence','Company Intelligence','Remote Work Intelligence','Data Explorer','Data Quality and Pipeline Monitor','SQL Analytics Lab','Reports and Download Center','Project Documentation and About']
st.sidebar.caption('JOB MARKET • ANALYTICS WORKSPACE')
st.sidebar.title('Market Intelligence')
page=st.sidebar.radio('Workspace',PAGES,key='page')
light=st.sidebar.toggle('Light presentation',value=False)
if light: st.html('<style>.stApp{background:#F8FAFC;color:#0B1220}[data-testid="stSidebar"]{background:#E2E8F0}h1,h2,h3,p,label{color:inherit}</style>')
st.html('<style>[data-testid="stMetric"]{border:1px solid #263449;border-radius:12px;padding:16px}h1{letter-spacing:-1px}.block-container{padding-top:2rem}button{border-radius:9px}</style>')
@st.cache_data(show_spinner='Loading validated snapshot')
def cached(version):return load()
try:
 version=(ROOT/'Dataset/current.json').read_text();d,q=cached(version)
except FileNotFoundError:
 st.title('Connect a genuine dataset');st.info('Upload gsearch_jobs.csv to begin. No demonstration statistics are fabricated.')
 file=st.file_uploader('CSV snapshot',type=['csv'])
 if file and st.button('Validate and import'):
  with tempfile.NamedTemporaryFile(suffix='.csv') as t:
   t.write(file.getvalue());t.flush()
   try: run(t.name);st.rerun()
   except Exception as e:st.error(str(e))
 st.stop()
st.sidebar.divider();st.sidebar.caption('GLOBAL FILTERS')
if st.sidebar.button('Reset filters'):
 for key in list(st.session_state):
  if key.startswith('filter_'):del st.session_state[key]
 st.rerun()
sel={};dependent=d
for col,label in [('job_country','Search country'),('company_name','Company'),('experience_level','Experience'),('remote_status','Work arrangement'),('employment_type','Employment type'),('skill_type','Skill category'),('skills','Skill')]:
 opts=sorted({s for ss in dependent.skills for s in ss}) if col=='skills' else sorted({category(s) for ss in dependent.skills for s in ss}) if col=='skill_type' else sorted(dependent[col].dropna().astype(str).unique())
 key='filter_'+col
 if key in st.session_state:st.session_state[key]=[v for v in st.session_state[key] if v in opts]
 vals=st.sidebar.multiselect(label,opts,key=key);sel[col]=vals
 dependent=filter_data(dependent,{col:vals})
salary=None
if st.sidebar.checkbox('Restrict to disclosed salary',key='filter_salary_enabled'):
 salary=st.sidebar.slider('Annual salary • source units',15000,400000,(15000,400000),key='filter_salary')
dates=None
if st.sidebar.checkbox('Restrict observation dates',key='filter_date_enabled'):
 dates=st.sidebar.date_input('Observed interval',(pd.to_datetime(d.observation_date.min()).date(),pd.to_datetime(d.observation_date.max()).date()),key='filter_dates')
 if len(dates)!=2:dates=None
f=filter_data(d,sel,salary,dates)
st.caption('GLOBAL DATA ANALYTICS JOB MARKET INTELLIGENCE & SALARY TREND DASHBOARD')
st.title(page)
st.caption(f'Historical snapshot · {q["snapshot_start"]} to {q["snapshot_end"]} · version {q["sha256"][:12]} · {len(f):,} filtered observations')
st.warning('United States search-target snapshot. Search country is not verified job country. Salary currency is unverified; figures are source units. Missing remote flags remain Unknown. Observation dates are not verified posting dates.')
active={k:v for k,v in sel.items() if v}
st.caption('Active filters: '+(json.dumps(active) if active else 'All records')+(' • salary constrained' if salary else '')+(' • dates constrained' if dates else ''))
if f.empty and page not in PAGES[7:]:st.info('No records match. Reset or broaden the filters.');st.stop()
stats=skill_stats(f)
def chart(fig,interpretation):
 fig.update_layout(template='plotly_white' if light else 'plotly_dark',paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',colorway=['#3B82F6','#14B8A6','#F2C572'],margin=dict(l=15,r=15,t=55,b=25),height=390)
 st.plotly_chart(fig,width='stretch');st.caption(interpretation+' · Source: active snapshot and global filters')
def bar(col,title):
 a=grouped(f,col).head(15);chart(px.bar(a,x='postings',y=col,orientation='h',title=title,hover_data=['salary_n','median_salary']),f'{len(a)} displayed categories; counts describe observations, not unique vacancies over time.')
def trend(col=None):
 a=f.groupby(['posted_month']+([col] if col else [])).size().reset_index(name='observations')
 chart(px.line(a,x='posted_month',y='observations',color=col,title='Observed activity through the snapshot'), 'Changes can reflect collection coverage and repeated listings; no forecasting claim.')
def salary_group(col):
 a=grouped(f,col);a=a[a.salary_n>=30].head(20)
 if a.empty:st.info('No groups meet the minimum of 30 valid salary observations.');return
 chart(px.bar(a,x=col,y='median_salary',hover_data=['postings','salary_n','mean_salary'],title='Median annual salary by '+col,labels={'median_salary':'Annual salary • source units'}),'Only groups with at least 30 usable salaries are shown. Association does not establish a causal premium.')
if page==PAGES[0]:
 vals=kpis(f)
 for row in [list(vals.items())[:4],list(vals.items())[4:]]:
  for c,(k,v) in zip(st.columns(4),row):c.metric(k,'Unavailable' if pd.isna(v) else f'{v:,.1f}' if isinstance(v,float) else f'{v:,}')
 trend();a,b=st.columns(2)
 with a:bar('experience_level','Experience demand')
 with b:bar('job_country','Search geography coverage')
 chart(px.bar(stats.head(15),x='demand',y='skill',orientation='h',title='Top required skills'),'Each skill is counted at most once per observation.')
 chart(px.histogram(f.dropna(subset=['salary_year_avg']),x='salary_year_avg',nbins=40,title='Annual salary distribution',labels={'salary_year_avg':'Annual salary • source units'}),'Salary non-disclosure can bias the visible distribution.')
 bar('remote_status','Reported work arrangements')
 st.subheader('Calculated observations')
 st.write(f'Usable salary coverage is {vals["Usable salary %"]:.1f}% of {len(f):,} filtered records.')
 if not stats.empty:st.write(f'The most frequent skill is {stats.iloc[0].skill}, appearing in {stats.iloc[0].demand:,} observations.')
elif page==PAGES[1]:
 chart(px.histogram(f,x='salary_year_avg',nbins=40,title='Salary distribution'),'Unknown and invalid salaries are excluded.')
 chart(px.box(f,x='experience_level',y='salary_year_avg',title='Salary variation and outliers by inferred experience'),'Points beyond the box are distributional outliers, not necessarily extraction errors.')
 for col in ['experience_level','job_country','company_name','remote_status','employment_type']:salary_group(col)
 a=stats[stats.salary_n>=30].sort_values('median_salary',ascending=False).head(20)
 chart(px.bar(a,x='skill',y='median_salary',hover_data=['salary_n'],title='Salary associated with skills'),'Skills overlap; these are not isolated skill effects.')
 st.dataframe(f.salary_year_avg.describe(percentiles=[.1,.25,.5,.75,.9,.95]).to_frame('Source units'))
 bar('salary_band','Salary bands');st.dataframe(grouped(f,'salary_source'))
 st.subheader('Screening audit');st.dataframe(f.loc[f.salary_valid.eq(False)&f.salary_missing.eq(False),['job_title','salary_candidate','salary_source']].head(200))
elif page==PAGES[2]:
 n=st.radio('Skill ranking size',[15,30],horizontal=True)
 chart(px.bar(stats.head(n),x='demand',y='skill',orientation='h',title='Most requested skills',hover_data=['salary_n','median_salary']),'Demand counts unique observations containing a skill.')
 chart(px.bar(stats.groupby('skill_type',as_index=False).demand.sum(),x='skill_type',y='demand',title='Category skill mentions'),'A job may contribute to several skills within a category; these are mentions, not jobs.')
 a=stats[stats.salary_n>=30]
 chart(px.scatter(a,x='demand',y='mean_salary',color='skill_type',hover_name='skill',size='salary_n',title='Demand versus associated salary'),'Minimum 30 salary observations; no causal interpretation.')
 if len(f)<100000:chart(px.imshow(cooccurrence(f),text_auto=True,title='Frequently co-required skills'),'Diagonal cells count the skill itself; off-diagonal cells count joint appearances.')
 st.dataframe(stats);st.subheader('Optimal skill candidates');st.dataframe(stats[stats.optimal])
 chosen=st.multiselect('Career comparison',stats.skill.tolist(),max_selections=4)
 if chosen:st.dataframe(stats[stats.skill.isin(chosen)]);trend()
elif page==PAGES[3]:
 st.info('No verified job-country field exists. The map shows search-target coverage only; this snapshot cannot establish global geographic differences.')
 a=grouped(f,'job_country');mapping={'United States':'USA','United Kingdom':'GBR','India':'IND','Canada':'CAN','Australia':'AUS'};a['iso']=a.job_country.map(mapping);mapped=a.dropna(subset=['iso'])
 if not mapped.empty:chart(px.choropleth(mapped,locations='iso',color='postings',hover_name='job_country',title='Search-target coverage • not job locations'),'Only explicit country mappings are plotted; unmapped labels remain in the table.')
 st.dataframe(a);bar('location','Raw location labels');salary_group('job_country');trend('job_country')
elif page==PAGES[4]:
 bar('company_name','Top observed employers');salary_group('company_name');st.dataframe(grouped(f,'company_name'))
 employer=st.selectbox('Inspect an employer',sorted(f.company_name.unique()));sub=f[f.company_name.eq(employer)]
 st.dataframe(skill_stats(sub));st.dataframe(grouped(sub,'experience_level'))
 chart(px.line(sub.groupby('posted_month').size().reset_index(name='postings'),x='posted_month',y='postings',title='Employer observation history'),'Collection intensity affects apparent activity.')
elif page==PAGES[5]:
 bar('remote_status','Remote, Onsite and Unknown');salary_group('remote_status');st.dataframe(f.groupby(['remote_status','experience_level']).size().reset_index(name='postings'))
 st.dataframe(skill_stats(f[f.remote_status.eq('Remote')]))
 st.dataframe(f.groupby(['job_country','remote_status']).size().reset_index(name='postings'));trend('remote_status')
 x=f.loc[f.remote_status.eq('Remote'),'salary_year_avg'].dropna();y=f.loc[f.remote_status.eq('Onsite'),'salary_year_avg'].dropna()
 if min(len(x),len(y))>=30:
  from scipy.stats import mannwhitneyu
  result=mannwhitneyu(x,y,alternative='two-sided');st.write({'test':'Mann–Whitney U, two-sided','remote_n':len(x),'onsite_n':len(y),'p_value':result.pvalue});st.caption('Unadjusted observational comparison; country, company and seniority may confound it.')
 else:st.info('No justified Remote versus Onsite test: at least 30 valid salaries per explicitly labelled group are required. Unknown is not an onsite control group.')
elif page==PAGES[6]:
 search=st.text_input('Search job title or company');e=filter_data(f,search=search)
 cols=st.multiselect('Columns',[c for c in e if c!='skills'],default=['job_title','company_name','location','remote_status','salary_year_avg'])
 p=st.number_input('Page',1,max(1,(len(e)+49)//50));st.dataframe(e[cols].iloc[(p-1)*50:p*50],width='stretch')
 st.download_button('Download filtered CSV',e.drop(columns=['skills']).to_csv(index=False),'filtered_jobs.csv','text/csv')
 if st.button('Prepare filtered Excel'):
  from src.exports import excel_bytes
  st.download_button('Download filtered Excel',excel_bytes(e),'filtered_jobs.xlsx')
 if not e.empty:
  record=st.selectbox('Inspect record',e.job_id.tolist());st.json(e[e.job_id.eq(record)].iloc[0].to_dict(),expanded=False)
 st.dataframe(e.isna().sum().to_frame('Missing'));st.markdown((ROOT/'docs/DATA_DICTIONARY.md').read_text())
elif page==PAGES[7]:
 st.caption('Pipeline metrics describe the full source snapshot; filtered analysis is shown separately.')
 for c,(k,v) in zip(st.columns(4),[(k,q[k]) for k in ['raw_records','clean_records','exact_duplicates_removed','composite_duplicates_removed']]):c.metric(k.replace('_',' ').title(),v)
 st.json(q,expanded=False)
 chart(px.bar(pd.DataFrame({'field':list(q['raw_missing']),'missing':list(q['raw_missing'].values())}),x='field',y='missing',title='Raw missing-value counts'),'Full snapshot quality; no salary imputation is performed.')
 upload=st.file_uploader('Upload updated snapshot • CSV, up to 350 MiB',type=['csv'])
 if upload and st.button('Validate and atomically refresh'):
  with tempfile.NamedTemporaryFile(suffix='.csv') as t:
   t.write(upload.getvalue());t.flush()
   try:
    with st.spinner('Validating snapshot and building relational database'):run(t.name)
    st.cache_data.clear();st.success('Validated snapshot committed');st.rerun()
   except Exception as e:st.error('Import rejected. Previous committed snapshot retained. '+str(e))
elif page==PAGES[8]:
 st.info('SQL Lab operates on the complete committed snapshot, independently of global chart filters. Each predefined query is read-only.')
 search=st.text_input('Search business questions');qs=[a for a in QUERIES if search.lower() in a['question'].lower()]
 if qs:
  chosen=st.selectbox('Business question',qs,format_func=lambda x:f'{x["id"]:02}. {x["question"]}');st.code(chosen['sql'],language='sql');st.caption(chosen['assumptions'])
  if st.button('Execute read-only query'):
   result=execute(chosen['id']);st.dataframe(result);st.download_button('Export query result',result.to_csv(index=False),'query_result.csv')
 else:st.info('No questions match this search.')
elif page==PAGES[9]:
 st.info('On-demand reports and Excel respect the global filters. Packaged project artifacts document the full snapshot.')
 from src.exports import executive_pdf,excel_bytes
 st.download_button('Generate current executive PDF',executive_pdf(f,q),'executive_report.pdf','application/pdf')
 if st.button('Prepare analytical workbook'):
  st.download_button('Download workbook',excel_bytes(f),'analysis.xlsx')
 st.download_button('Download cleaned filtered records',f.drop(columns=['skills']).to_csv(index=False),'cleaned.csv')
 st.download_button('Download quality report',json.dumps(q,indent=2),'quality.json')
 for path in sorted((ROOT/'Report').glob('*')):
  if path.is_file() and path.stat().st_size<30_000_000:st.download_button(path.name,path.read_bytes(),path.name,key=str(path))
 for path in sorted((ROOT/'docs').glob('*.md')):st.download_button(path.name,path.read_bytes(),path.name,key=str(path))
else:
 st.markdown((ROOT/'README.md').read_text());st.markdown((ROOT/'docs/ARCHITECTURE.md').read_text())
