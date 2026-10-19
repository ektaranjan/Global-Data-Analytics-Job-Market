"""Pure analytics shared by the application, exports and tests."""
import pandas as pd
from .pipeline import category

def filter_data(d, selections=None, salary=None, dates=None, search=""):
    f=d.copy()
    for col,values in (selections or {}).items():
        if values:
            f=f[f.skills.map(lambda ss:bool(set(ss)&set(values)))] if col=="skills" else f[f.skills.map(lambda ss:any(category(s) in values for s in ss))] if col=="skill_type" else f[f[col].isin(values)]
    if salary is not None:f=f[f.salary_year_avg.between(*salary)]
    if dates is not None:f=f[f.observation_date.between(str(dates[0]),str(dates[1]))]
    if search:f=f[f.job_title.str.contains(search,case=False,regex=False,na=False)|f.company_name.str.contains(search,case=False,regex=False,na=False)]
    return f

def kpis(d):
    n=len(d)
    return {"Postings":n,"Companies":d.company_name[d.company_name.str.casefold().ne("unknown")].nunique(),"Search countries":d.job_country.nunique(),"Skills":len({s for ss in d.skills for s in ss}),"Median salary":d.salary_year_avg.median(),"Mean salary":d.salary_year_avg.mean(),"Remote %":100*d.remote_status.eq("Remote").mean() if n else 0,"Usable salary %":100*d.salary_year_avg.notna().mean() if n else 0}

def skill_stats(d):
    e=d[["job_id","skills","salary_year_avg"]].explode("skills").dropna(subset=["skills"])
    a=e.groupby("skills").agg(demand=("job_id","nunique"),salary_n=("salary_year_avg","count"),mean_salary=("salary_year_avg","mean"),median_salary=("salary_year_avg","median")).reset_index().rename(columns={"skills":"skill"})
    a["skill_type"]=a.skill.map(category)
    a["optimal"]=a.demand.ge(100)&a.salary_n.ge(30)&a.mean_salary.ge(d.salary_year_avg.median())
    return a.sort_values("demand",ascending=False)

def grouped(d,col):
    return d.groupby(col,dropna=False).agg(postings=("job_id","count"),salary_n=("salary_year_avg","count"),median_salary=("salary_year_avg","median"),mean_salary=("salary_year_avg","mean"),remote_pct=("remote_status",lambda x:100*x.eq("Remote").mean())).reset_index().sort_values("postings",ascending=False)

def cooccurrence(d,limit=12):
    top=skill_stats(d).head(limit).skill.tolist();m=pd.DataFrame(0,index=top,columns=top)
    for ss in d.skills:
        present=list(set(ss)&set(top))
        for a in present:
            for b in present:m.loc[a,b]+=1
    return m
