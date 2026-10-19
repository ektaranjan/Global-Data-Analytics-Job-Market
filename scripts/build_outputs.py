"""Rebuild supporting artifacts from the committed genuine snapshot."""
import json,zipfile
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from src.pipeline import ROOT,load
from src.analytics import kpis,skill_stats,grouped
from src.exports import excel_bytes,executive_pdf

def main():
 d,q=load();out=ROOT/'Report';charts=out/'charts';charts.mkdir(exist_ok=True)
 (out/'Analytical_Workbook.xlsx').write_bytes(excel_bytes(d));(out/'Executive_Report.pdf').write_bytes(executive_pdf(d,q))
 sns.set_theme(style='whitegrid',palette=['#3B82F6','#14B8A6','#F2C572'])
 def save(name,title,xlabel,ylabel):
  plt.title(title);plt.xlabel(xlabel);plt.ylabel(ylabel);plt.tight_layout();plt.savefig(charts/(name+'.png'),dpi=220);plt.close()
 plt.figure(figsize=(9,4.8));plt.hist(d.salary_year_avg.dropna(),bins=40,color='#3B82F6');save('salary_distribution','Screened annual salary distribution','Annual salary - unverified source units','Observations')
 a=skill_stats(d).head(15).iloc[::-1];plt.figure(figsize=(9,5.5));plt.barh(a.skill,a.demand,color='#14B8A6');save('skill_demand','Top 15 requested skills','Observations','Skill')
 for col,name,title in [('experience_level','experience','Experience inferred from title'),('remote_status','remote','Reported work arrangements'),('job_country','geography','Search-target coverage'),('company_name','companies','Top employers by observed volume')]:
  a=grouped(d,col).head(10).iloc[::-1];plt.figure(figsize=(9,5));plt.barh(a[col],a.postings,color='#3B82F6');save(name,title,'Observations',col.replace('_',' ').title())
 a=d.groupby('posted_month').size();plt.figure(figsize=(10,4.8));plt.plot(a.index,a.values,color='#3B82F6');plt.xticks(rotation=65);save('activity','Observation activity by month','Observation month','Observations')
 a={'Raw records':q['raw_records'],'Clean records':q['clean_records'],'Composite duplicates':q['composite_duplicates_removed'],'Missing salaries':q['missing_salary'],'Invalid salaries':q['invalid_salary']};plt.figure(figsize=(9,5));plt.barh(list(a),list(a.values()),color='#14B8A6');save('quality','Pipeline quality audit','Records','Stage or issue')
 for name,labels in [('architecture',['Raw CSV','Validation and cleaning','Normalized SQLite','SQL and Python analytics','Streamlit and exports']),('er_diagram',['company_dim  PK company_id','job_postings_fact  PK job_id / FK company_id','skills_job_dim  PK job_id + skill_id','skills_dim  PK skill_id'])]:
  fig,ax=plt.subplots(figsize=(10,5));ax.axis('off')
  for i,label in enumerate(labels):
   y=.9-i*.18;ax.text(.5,y,label,ha='center',va='center',fontsize=12,bbox=dict(boxstyle='round,pad=.6',fc='#E2E8F0',ec='#3B82F6'))
   if i<len(labels)-1:ax.annotate('',xy=(.5,y-.12),xytext=(.5,y-.04),arrowprops=dict(arrowstyle='->',color='#172033'))
  plt.tight_layout();plt.savefig(charts/(name+'.png'),dpi=220);plt.close()
 findings=[]
 def add(question,result,n,evidence,interpretation,recommendation):
  findings.append(dict(question=question,result=result,sample_size=int(n),evidence=evidence,interpretation=interpretation,caveat='Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.',job_seeker_recommendation=recommendation,recruiter_recommendation='Verify target-role relevance, currency, geography and current hiring context before acting.'))
 k=kpis(d)
 add('How many observations survive cleaning?',f'{len(d):,} retained from {q["raw_records"]:,}; {q["composite_duplicates_removed"]:,} composite duplicates removed.',q['raw_records'],'quality.json','Duplicate indexing inflates raw volume.','Compare cleaned observations rather than raw rows.')
 add('How complete is usable salary?',f'{d.salary_year_avg.notna().sum():,} usable salaries; {k["Usable salary %"]:.2f}% coverage.',len(d),'query_07.csv','Disclosed salaries represent a selected subset.','Inspect the disclosed sample size before using salary rankings.')
 add('What is the observed salary center?',f'Median {k["Median salary"]:,.0f}; mean {k["Mean salary"]:,.0f}, source units.',d.salary_year_avg.notna().sum(),'query_05.csv and query_06.csv','Mean and median describe different aspects of the salary distribution.','Verify currency and relevant experience before benchmarking.')
 a=d.salary_year_avg.dropna();add('What is the middle salary spread?',f'25th percentile {a.quantile(.25):,.0f}; 75th percentile {a.quantile(.75):,.0f}.',len(a),'charts/salary_distribution.png','The middle half describes the disclosed sample.','Research a salary range rather than one point estimate.')
 add('How many candidates fail screening?',f'{q["invalid_salary"]} annual salary candidates are outside the baseline.',len(d),'query_31.csv','The baseline can remove valid atypical compensation.','Inspect exclusions for part-time and leadership roles.')
 add('What geography is observed?',f'{d.job_country.nunique()} search-target country: '+', '.join(d.job_country.unique()),len(d),'query_03.csv','This does not establish global workplace coverage.','Treat the sample as US search coverage.')
 add('How many records explicitly report remote work?',f'{d.remote_status.eq("Remote").sum():,} observations; {k["Remote %"]:.2f}%.',len(d),'query_08.csv','The denominator includes Unknown.','Use positively identified remote records.')
 add('How much arrangement information is unknown?',f'{d.remote_status.eq("Unknown").sum():,} records.',len(d),'query_08.csv','Missing flags cannot provide an onsite control.','Do not infer onsite employment from a blank flag.')
 add('How many employers are represented?',f'{k["Companies"]:,} normalized names.',len(d),'query_02.csv','Normalized names are not verified legal entities.','Check employer identity and subsidiaries.')
 add('How many rows have no parsed skill?',f'{q["malformed_or_empty_skills"]:,} records.',len(d),'query_26.csv','Empty extracted lists do not prove no skills are required.','Read source descriptions before drawing conclusions.')
 for row in skill_stats(d).head(6).itertuples():
  add(f'How frequent is {row.skill}?',f'{row.demand:,} observations ({100*row.demand/len(d):.2f}%); {row.salary_n:,} usable salaries.',len(d),'query_18.csv',f'{row.skill} is present in the extracted skill vocabulary.','Prepare a portfolio example when the skill matches your target roles.')
 for row in grouped(d,'experience_level').itertuples(index=False):
  add(f'How common is {row.experience_level}?',f'{row.postings:,} observations; {row.salary_n:,} usable salaries; median {row.median_salary:,.0f} source units.',len(d),'query_10.csv','Title keywords infer experience; years of experience are not verified.','Confirm actual requirements from descriptions.')
 for col,query in [('company_name','query_16.csv'),('platform','query_13.csv')]:
  top=grouped(d,col).iloc[0];add(f'Which {col} has highest observed volume?',f'{top[col]}: {int(top.postings):,} observations.',len(d),query,'Volume can reflect collection and reposting.','Use counts as a starting point for further research.')
 (out/'business_insights.json').write_text(json.dumps(findings,indent=2))
 text='# Business insights from the executed snapshot\n\n'
 for i,x in enumerate(findings,1):text+=f'## {i}. {x["question"]}\n\n'+'\n\n'.join(f'**{key.replace("_"," ").title()}:** {v}' for key,v in x.items() if key!='question')+'\n\n'
 (out/'business_insights.md').write_text(text)
 with zipfile.ZipFile(out/'Chart_Package.zip','w',zipfile.ZIP_DEFLATED) as z:
  for p in charts.glob('*.png'):z.write(p,p.name)
 print(json.dumps(k,indent=2));print('Insights',len(findings))
if __name__=='__main__':main()
