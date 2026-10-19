import json, sqlite3, time
import pandas as pd
from .pipeline import ROOT,current_folder
QUERIES=json.loads((ROOT/"SQL/queries.json").read_text())
def execute(query_id, folder=None):
    q=next(q for q in QUERIES if q["id"]==query_id)
    path=(folder or current_folder())/"job_market.db"
    with sqlite3.connect(path.as_uri()+"?mode=ro",uri=True) as c:
        c.execute("PRAGMA query_only=ON")
        return pd.read_sql_query(q["sql"],c)
def validate():
    results=[]
    for q in QUERIES:
        t=time.perf_counter();d=execute(q["id"])
        results.append(dict(id=q["id"],rows=len(d),columns=list(d.columns),seconds=time.perf_counter()-t,status="passed"))
        d.to_csv(ROOT/"Report"/f"query_{q['id']:02}.csv",index=False)
    (ROOT/"Report/sql_validation.json").write_text(json.dumps(results,indent=2));return results
if __name__=="__main__":print(json.dumps(validate(),indent=2))
