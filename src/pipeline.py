"""Validated snapshot ingestion. Unknown values remain unknown."""
from __future__ import annotations
import ast, hashlib, json, os, re, sqlite3, tempfile
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"title", "company_name", "location", "description_tokens", "date_time", "search_location"}
CATEGORIES = {"programming": {"python","r","sql","java","javascript","scala","sas"}, "analyst_tools": {"excel","tableau","power bi","power_bi","looker","spss"}, "databases": {"mysql","postgresql","sqlite","mongodb","snowflake","sql server"}, "cloud": {"aws","azure","gcp","redshift","bigquery"}, "libraries": {"pandas","numpy","scipy","scikit-learn","tensorflow","pytorch","matplotlib","seaborn"}}
def category(skill: str) -> str:
    return next((k for k,v in CATEGORIES.items() if skill in v), "other")
def tokens(value) -> list[str]:
    if not isinstance(value, str) or len(value)>20000: return []
    try: v=ast.literal_eval(value)
    except (ValueError,SyntaxError,TypeError,RecursionError,MemoryError): return []
    return sorted({x.strip().lower() for x in v if isinstance(x,str) and 0<len(x.strip())<=100}) if isinstance(v,list) else []
def experience(title: str) -> str:
    t=title.lower()
    if re.search(r"\b(lead|manager|director|head)\b",t): return "Lead/Manager"
    if re.search(r"\b(senior|sr)\b",t): return "Senior"
    if re.search(r"\b(junior|jr|entry|intern)\b",t): return "Junior/Entry"
    return "Mid-Level (inferred)"
def remote(value) -> str:
    s=str(value).strip().lower()
    return "Remote" if s in {"true","1","yes"} else "Onsite" if s in {"false","0","no"} else "Unknown"
def clean(raw: pd.DataFrame) -> tuple[pd.DataFrame,dict]:
    missing=REQUIRED-set(raw.columns)
    if missing: raise ValueError("Required columns missing: "+", ".join(sorted(missing)))
    if raw.empty: raise ValueError("CSV has no records")
    q={"raw_records":len(raw),"raw_missing":raw.isna().sum().to_dict()}
    d=raw.drop_duplicates().copy(); q["exact_duplicates_removed"]=len(raw)-len(d)
    for c in ["title","company_name","location","search_location"]:
        d[c]=d[c].fillna("Unknown").astype(str).str.replace(r"\s+"," ",regex=True).str.strip()
        d[c]=d[c].replace("","Unknown")
    d["title"]=d.title.str.lower(); d["company_name"]=d.company_name.str.casefold(); d["location"]=d.location.str.title()
    d["observation_date"]=pd.to_datetime(d.date_time,errors="coerce",format="mixed",utc=True).dt.strftime("%Y-%m-%d")
    # Invalid dates cannot establish duplicate identity; retain those records.
    valid=d.observation_date.notna(); dup=d.duplicated(["title","company_name","location","observation_date"]) & valid
    q["composite_duplicates_removed"]=int(dup.sum()); d=d.loc[~dup].reset_index(drop=True)
    def num(c): return pd.to_numeric(d[c],errors="coerce") if c in d else pd.Series(np.nan,index=d.index)
    lo=num("salary_avg_min").fillna(num("salary_min")); hi=num("salary_avg_max").fillna(num("salary_max"))
    rate=d.get("salary_rate",pd.Series("",index=d.index)).fillna("").str.lower()
    # Source range aliases are annualized only when their unit is explicitly declared.
    midpoint=(lo+hi)/2
    midpoint=midpoint*rate.map({"a year":1,"yearly":1,"an hour":2080,"hourly":2080,"a month":12,"monthly":12})
    candidates=pd.DataFrame({"salary_standardized":num("salary_standardized"),"salary_yearly":num("salary_yearly"),"salary_hourly_x2080":num("salary_hourly")*2080,"range_annualized":midpoint})
    d["salary_candidate"]=candidates.bfill(axis=1).iloc[:,0]
    d["salary_source"]=candidates.notna().idxmax(axis=1).where(candidates.notna().any(axis=1),"Missing")
    d["salary_missing"]=d.salary_candidate.isna(); d["salary_valid"]=d.salary_candidate.between(15000,400000)
    d["salary_year_avg"]=d.salary_candidate.where(d.salary_valid)
    # No currency metadata: never label these numbers verified USD.
    d["currency_status"]="Unverified source currency"
    d["salary_band"]=pd.cut(d.salary_year_avg,[0,60000,90000,120000,float("inf")],right=False,labels=["<60K","60–90K","90–120K","120K+"]).astype("string")
    d["experience_level"]=d.title.map(experience)
    d["remote_status"]=d.get("work_from_home",pd.Series(None,index=d.index)).map(remote)
    d["is_remote"]=d.remote_status.map({"Remote":1,"Onsite":0})
    d["job_title"]=d.title; d["job_country"]=d.search_location
    d["platform"]=d.get("via",pd.Series("Unknown",index=d.index)).fillna("Unknown").str.replace(r"^via\s+","",regex=True).str.strip().str.casefold()
    d["employment_type"]=d.get("schedule_type",pd.Series("Unknown",index=d.index)).fillna("Unknown")
    d["posted_year"]=d.observation_date.str[:4]; d["posted_month"]=d.observation_date.str[:7]
    d["skills"]=d.description_tokens.map(tokens)
    d["source_job_id"]=d.get("job_id",pd.Series("",index=d.index))
    d["job_id"]=[hashlib.sha256(f"{a}|{b}|{c}|{e}|{i}".encode()).hexdigest()[:24] for i,(a,b,c,e) in enumerate(zip(d.title,d.company_name,d.location,d.observation_date))]
    names=sorted(d.company_name.unique()); ids={v:i+1 for i,v in enumerate(names)};d["company_id"]=d.company_name.map(ids)
    q.update(clean_records=len(d),invalid_salary=int((~d.salary_missing & ~d.salary_valid).sum()),missing_salary=int(d.salary_missing.sum()),invalid_dates=int(d.observation_date.isna().sum()),malformed_or_empty_skills=int(d.skills.map(len).eq(0).sum()),processed_at=datetime.now(timezone.utc).isoformat(),clean_missing=d.isna().sum().to_dict())
    return d,q

def tables(d):
    companies=d[["company_id","company_name"]].drop_duplicates()
    skills=sorted({s for row in d.skills for s in row})
    dim=pd.DataFrame({"skill_id":range(1,len(skills)+1),"skill":skills,"skill_type":[category(x) for x in skills]})
    ids=dict(zip(dim.skill,dim.skill_id)); pairs=[(j,ids[s]) for j,ss in zip(d.job_id,d.skills) for s in ss]
    bridge=pd.DataFrame(pairs,columns=["job_id","skill_id"])
    cols=["job_id","company_id","job_title","location","job_country","experience_level","remote_status","salary_year_avg","salary_candidate","salary_source","salary_valid","salary_missing","salary_band","observation_date","posted_month","employment_type","platform","currency_status"]
    return {"company_dim":companies,"job_postings_fact":d[cols],"skills_dim":dim,"skills_job_dim":bridge}

def build_database(t, path):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_suffix(".staging.db"); temp.unlink(missing_ok=True)
    engine=create_engine("sqlite:///"+str(temp))
    try:
        with engine.begin() as c:
            for statement in (ROOT/"SQL/schema.sql").read_text().split(";"):
                if statement.strip(): c.exec_driver_sql(statement)
            c.exec_driver_sql("PRAGMA foreign_keys=ON")
            for name,frame in t.items(): frame.to_sql(name,c,if_exists="append",index=False,chunksize=2000)
            if c.exec_driver_sql("PRAGMA foreign_key_check").fetchall(): raise ValueError("Foreign key failure")
        engine.dispose();os.replace(temp,path)
    finally:
        engine.dispose();temp.unlink(missing_ok=True)

def run(source: str|Path) -> dict:
    source=Path(source)
    if source.suffix.lower()!=".csv" or source.stat().st_size>350*1024*1024: raise ValueError("CSV required, maximum 350 MiB")
    raw=pd.read_csv(source,low_memory=False); d,q=clean(raw)
    digest=hashlib.file_digest(source.open("rb"),"sha256").hexdigest()
    q.update(sha256=digest,source_url="https://www.kaggle.com/datasets/lukebarousse/data-analyst-job-postings-google-search",license="Unverified; confirm dataset license before redistribution",snapshot_start=str(d.observation_date.min()),snapshot_end=str(d.observation_date.max()),geography="Search target, not verified job country",currency="Unverified; no cross-currency comparison justified")
    # Immutable version directory; a single atomic pointer commits a complete snapshot.
    folder=ROOT/"Dataset/processed"/digest[:16]; folder.mkdir(parents=True,exist_ok=True)
    t=tables(d);build_database(t,folder/"job_market.db")
    for name,frame in t.items():frame.to_csv(folder/(name+".csv"),index=False)
    d.assign(skills=d.skills.map(json.dumps)).drop(columns=["description","thumbnail","extensions"],errors="ignore").to_csv(folder/"jobs_cleaned.csv",index=False)
    (folder/"quality.json").write_text(json.dumps(q,indent=2,default=int))
    raw_folder=ROOT/"Dataset/raw";raw_folder.mkdir(exist_ok=True)
    import shutil
    target=raw_folder/(digest[:16]+".csv")
    if not target.exists():shutil.copy2(source,target)
    pointer=ROOT/"Dataset/current.json";tmp=pointer.with_suffix(".tmp")
    tmp.write_text(json.dumps({"version":digest[:16],"folder":str(folder.relative_to(ROOT))}));os.replace(tmp,pointer)
    return q

def current_folder():
    p=ROOT/"Dataset/current.json"
    if not p.exists():raise FileNotFoundError("Import a genuine gsearch_jobs.csv snapshot first")
    return ROOT/json.loads(p.read_text())["folder"]

def load():
    p=current_folder();d=pd.read_csv(p/"jobs_cleaned.csv",low_memory=False);d["skills"]=d.skills.map(json.loads)
    return d,json.loads((p/"quality.json").read_text())

if __name__=="__main__":
    import argparse
    p=argparse.ArgumentParser();p.add_argument("source");a=p.parse_args();print(json.dumps(run(a.source),indent=2,default=int))
