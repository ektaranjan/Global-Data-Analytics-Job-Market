from pathlib import Path
import json,re,textwrap,csv
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
r=Path(__file__).resolve().parents[1];doc=Document();sec=doc.sections[0];sec.page_width=Inches(8.5);sec.page_height=Inches(11);sec.top_margin=sec.bottom_margin=Inches(.8);sec.left_margin=sec.right_margin=Inches(.85)
for name in ['Normal','Title','Subtitle','Heading 1','Heading 2','Heading 3']:
 s=doc.styles[name];s.font.name='Calibri';s.font.color.rgb=RGBColor(0,0,0)
doc.styles['Normal'].font.size=Pt(11);doc.styles['Normal'].paragraph_format.space_after=Pt(7)
doc.styles['Normal'].paragraph_format.line_spacing=1.12
doc.styles['Title'].font.size=Pt(28);doc.styles['Heading 1'].font.size=Pt(20);doc.styles['Heading 2'].font.size=Pt(15)
footer=sec.footer.paragraphs[0];footer.alignment=2;footer.add_run('MCA Major Project | ')
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');footer._p.append(fld)
sec.header.paragraphs[0].text='JOB MARKET INTELLIGENCE  |  IMPLEMENTATION AND EVIDENCE'
source=[]
def p(t,style=None):doc.add_paragraph(t,style);source.append(t+'\n')
def h(t,level=1):doc.add_heading(t,level);source.append('#'*level+' '+t+'\n')
def page(title):
 para=doc.add_heading(title,1);para.paragraph_format.page_break_before=True;source.append('# '+title+'\n')
def table(headers,rows):
 t=doc.add_table(rows=1,cols=len(headers));t.autofit=False
 width=6.8/len(headers)
 for i,a in enumerate(headers):t.rows[0].cells[i].text=str(a)
 for row in rows:
  cells=t.add_row().cells
  for c,v in zip(cells,row):c.text=str(v)
 for i,row in enumerate(t.rows):
  for c in row.cells:
   c.width=Inches(width)
   tcPr=c._tc.get_or_add_tcPr();b=OxmlElement('w:tcBorders')
   for edge in ['top','left','bottom','right']:
    x=OxmlElement('w:'+edge);x.set(qn('w:val'),'single');x.set(qn('w:sz'),'4');x.set(qn('w:color'),'D9D9D9');b.append(x)
   tcPr.append(b);shade=OxmlElement('w:shd');shade.set(qn('w:fill'),'172033' if i==0 else 'F1F5F9' if i%2 else 'FFFFFF');tcPr.append(shade)
   for para in c.paragraphs:
    para.paragraph_format.space_after=Pt(3);para.paragraph_format.space_before=Pt(3)
    for run in para.runs:run.font.size=Pt(9);run.font.color.rgb=RGBColor(255,255,255) if i==0 else RGBColor(0,0,0);run.bold=i==0
 repeat=OxmlElement('w:tblHeader');t.rows[0]._tr.get_or_add_trPr().append(repeat)
 source.append('| '+' | '.join(headers)+' |\n'+'\n'.join('| '+' | '.join(map(str,row))+' |' for row in rows)+'\n')
def figure(name,caption):
 doc.add_picture(str(r/'Report/charts'/f'{name}.png'),width=Inches(6.7));p(caption,'Caption');source.append(f'![{caption}](../Report/charts/{name}.png)')
def markdown(path):
 text=(r/path).read_text();lines=text.splitlines();code=False;i=0;mermaid=False
 while i<len(lines):
  line=lines[i];i+=1
  if line.startswith('```'):
   if 'mermaid' in line:mermaid=True;code=True
   else:code=not code;mermaid=False
   continue
  if mermaid or not line.strip():continue
  if line.startswith('|'):
   group=[line]
   while i<len(lines) and lines[i].startswith('|'):group.append(lines[i]);i+=1
   rows=[[x.strip() for x in row.strip('|').split('|')] for row in group]
   rows=[row for row in rows if not all(set(x)<=set('-: ') for x in row)]
   if len(rows)>1:table(rows[0],rows[1:])
   continue
  if line.startswith('#'):
   n=len(line)-len(line.lstrip('#'));h(line.lstrip('#').strip(),min(n+1,3))
  else:
   if line.startswith('Raw schema:'):
    para=doc.add_heading('Raw schema and field aliases',2);para.paragraph_format.page_break_before=True
   para=doc.add_paragraph(line)
   if code:
    for run in para.runs:run.font.name='Consolas';run.font.size=Pt(8)
 source.append(text)

current=r/json.loads((r/'Dataset/current.json').read_text())['folder'];q=json.loads((current/'quality.json').read_text());qs=json.loads((r/'SQL/queries.json').read_text());validation=json.loads((r/'Report/sql_validation.json').read_text());findings=json.loads((r/'Report/business_insights.json').read_text())
p('Global Data Analytics Job Market Intelligence and Salary Trend Dashboard','Title');p('MCA final year major project implementation report','Subtitle');p('Historical job posting analysis with Python SQLite SQL and Streamlit');p('Prepared 19 October 2026')
p('This report documents an executed local analytics application, its methods, numerical outputs, tests and remaining limitations. It replaces illustrative results from the supplied internship reference with evidence from the genuine CSV snapshot.')
p('Submission metadata has not been invented. The student must add their name, enrollment number, institution, guide, academic year and university-approved declarations before final submission. No certificate or signature is represented as issued.')
p('Execution status: 56,004 cleaned observations; four normalized database tables; 38 executed SQL queries; 11 Streamlit pages checked at script level; 81 automated tests passed. Native Power BI validation and real browser screenshots remain incomplete.')
page('Abstract')
p('The project addresses fragmented evidence about skill requirements, employers and salary disclosure in data analyst job observations. It implements a reproducible pipeline that validates a genuine Kaggle-format CSV, removes documented duplicates, resolves salary candidates with provenance, parses extracted skills safely and persists a four-table relational model. Independent analytical functions and read-only SQL support a Streamlit application with global filters, quality monitoring, searchable records and report downloads.')
p('The supplied raw snapshot contains 61,953 records and 27 columns. The implemented composite rule removes 5,949 duplicate observations, retaining 56,004 records. Of these, 9,022 have screened salary estimates. The disclosed-salary median is 88,400 and the mean is approximately 92,131 in unverified source units. These values are descriptive of the observed disclosed subset and must not be treated as verified current USD compensation benchmarks.')
p('The evidence imposes material limits. All search targets are United States, so the dataset does not establish global workplace-country coverage. Remote flags are either true or missing; missing values remain Unknown and cannot supply an onsite comparison. Observation timestamps span November 2022 to April 2025 rather than the current market. The working cross-platform demonstration is Streamlit. Power BI-ready data, measures and specifications are supplied without claiming an executed native PBIX.')
p('Keywords: job market analytics, salary provenance, skill demand, SQLite, Streamlit, data quality, reproducibility, business intelligence.')
page('Contents and evidence navigation')
for t in ['1 Introduction and objectives','2 Literature and analytical framework','3 Requirements and environment','4 System design','5 Dataset description','6 Preprocessing methodology','7 Exploratory analysis','8 SQL analytical casebook','9 Dashboard and supporting business intelligence','10 Business insights and recommendations','11 Testing and execution evidence','12 Deployment demonstration and future scope','13 Conclusion and references','Appendix A Editable source code listings'] :p(t)
p('The SQL casebook contains the complete 38-query library with actual output samples and observed schemas. CSV exports preserve the full result sets separately. The appendix contains source listings, while the repository supplies the editable original files. Page numbers are carried in the footer. A detailed source-PDF requirement inventory is supplied as docs/PDF_REQUIREMENTS_TRACEABILITY.md.')
page('1 Introduction and objectives')
p('Job seekers frequently encounter role requirements across multiple platforms without a consistent method for comparing requested skills or disclosed pay. Recruiters face a related problem when benchmarking roles with different seniority, skills and arrangements. A central analytical workspace can turn individual observations into transparent descriptive evidence, provided that it preserves the limits of the source rather than inferring unsupported facts.')
p('The project implements the subject and research objectives of the supplied internship report. Its central questions concern skill frequency, salary distributions, employer demand, experience categories, observation activity and work arrangements. The requested Streamlit extension provides the live demonstration interface, while Excel and Power BI assets preserve the supporting objectives of the reference.')
p('The objectives are to preserve the original data, implement repeatable transformations, normalize the many-to-many job-skill relationship, answer business questions using SQL, offer consistent interactive filtering and generate reproducible supporting artifacts. Academic defensibility depends on checking every numerical claim against executed output and distinguishing completed capabilities from future scope.')
h('Scope and analytical unit',2)
p('The application describes a supplied snapshot. It does not scrape live job portals, predict future salaries or certify the number of currently available vacancies. A retained observation is a normalized title, company, location and collection-day combination. Identical listings on different days can remain, while multiple real openings sharing the same composite attributes can be merged. The raw snapshot and documented rule make this tradeoff auditable.')
page('2 Literature and analytical framework')
p('Descriptive analytics summarizes observed records; diagnostic exploration compares groups and possible associations. This project uses these approaches without claiming controlled causal identification. Predictive and prescriptive models are outside the completed core. A salary associated with Python, for example, can reflect seniority or employer mix rather than a salary change caused by learning Python.')
p('The supplied report discusses salary surveys, public SQL tutorials and Kaggle-based job-market analysis. The implemented contribution is integration: a reproducible path from source CSV through validation, relational modeling, query execution, interactive exploration and exported evidence. Public tutorial concepts do not establish that the current snapshot is representative, and the report does not claim a novel labor-market census.')
p('Mean salary is sensitive to magnitude and skew, while the median depends on order. Both exclude missing and invalid candidates. Quantiles and box plots describe spread. Sample thresholds reduce rankings dominated by very small groups, although they cannot remove disclosure selection, reposting or confounding. The optimal-skill definition combines demand with salary evidence as a transparent heuristic, not a guarantee of career success.')
p('References are supplied at the end. The original report is treated as the project reference and requirement source. Its qualitative claims about widespread salary disclosure and global coverage were not inherited as empirical facts; the executed snapshot provides the final evidence.')
page('3 Requirements and environment')
p('The local implementation executes the genuine-data pipeline, the four-table SQLite database and 38 analytical SQL queries. Eleven Streamlit pages passed script-level checks, and the final suite contains 81 passing tests. The supporting workbook, chart package, 22 numerical observations and 65 viva answers are supplied. Detailed acceptance evidence remains in docs/DELIVERABLE_STATUS.md.')
p('Native Power BI Desktop is unavailable, so no PBIX or native BI screenshots are claimed. Browser access to localhost was denied, leaving actual UI screenshots, visual responsiveness and tooltip checks incomplete. Script-level checks do not replace those visual gates.')
p('Global workplace-country comparisons, verified USD labels and Remote-versus-Onsite inference are unsupported by the source metadata. Source licensing must be confirmed before redistribution. Production PostgreSQL, native Excel pivots, concurrent-user stress testing and clean-install rehearsals on other platforms remain pending.')
p('The academic owner must add identity details, approved university declarations and genuine signatures. No internship experience, employer impact or academic certification has been invented.')
page('3 Requirements traceability and quality targets')
p('The source PDF includes eight functional requirements: ingestion, cleaning, derived features, skill extraction, relational persistence, SQL querying, interactive visualization and insight generation. Each is retained in the source traceability matrix, with an implementation file, application scope, verification and status. Figures, tables, chapter sections, field-level formulas and source placeholders are inventoried separately.')
p('Nonfunctional expectations include usability, query response, maintainability, portability and reproducibility. The executed environment is macOS ARM64 with Python 3.14 and a workspace virtual environment. The source minimum hardware guidance is 8 GB RAM and 5 GB disk. The raw CSV alone is approximately 290 MB, and in-memory processing can require several times its size.')
p('The PDF targets SQL query execution under two seconds. Actual timings for every predefined query are recorded rather than inferred. Portability to PostgreSQL remains partial: a separate PostgreSQL function is supplied, but no production server adapter or deployment was executed. Browser visual usability, narrow-screen layout and native PBIX behavior remain unverified because the necessary access or runtime was unavailable.')
table(['Evidence','Executed result'],[['Python environment','Report/environment.txt'],['Test run','81 passed; no failures or skips'],['Query library','38 executed questions'],['Application','11 pages passed Streamlit script-level checks'],['Browser screenshots','Blocked by denied localhost browser access'],['Native Power BI','Not available in the macOS environment']])
page('4 System design')
figure('architecture','Figure 4.1 Implemented architecture from source data through presentation')
p('The pipeline resolves data quality centrally before downstream analysis. The calculation layer is independent of Streamlit, allowing the same functions to support charts, Excel, reports and automated checks. The SQL library executes against the committed SQLite snapshot through read-only connections. The presentation layer handles controls, loading, data inspection and downloads.')
page('4 Relational design and integrity')
figure('er_diagram','Figure 4.2 Four-table relational model and key links')
p('company_dim stores one normalized employer name per company_id. job_postings_fact stores observation attributes and a company foreign key. skills_dim stores unique token names and categories. skills_job_dim links observations and skills using a composite primary key. Indexes on company, search country, date and skill support filters and joins.')
p('Foreign keys are enabled during transactional insertion and checked before publication. A staging database is replaced only after a successful build. The full version directory contains normalized CSVs, the database, cleaned records and the quality report. One atomic current.json pointer selects a complete version. The same checksum does not append repeated observations to the active database.')
page('4 Architecture methods and security')
markdown('docs/ARCHITECTURE.md')
page('5 Dataset description')
p('The source is Luke Barousse’s Data Analyst Job Postings dataset hosted on Kaggle. A genuine local file was found at the user-supplied Downloads location. No substitute production dataset was generated. The application preserves a checksum-named raw copy, records its SHA-256 and stores the exact observation interval in quality.json. Retrieval time is not known for the preexisting local download; processing time is recorded separately and must not be described as source retrieval time.')
table(['Property','Observed value'],[['Raw records',q['raw_records']],['Raw columns',len(q['raw_missing'])],['Clean observations',q['clean_records']],['Observation interval',q['snapshot_start']+' to '+q['snapshot_end']],['Missing salary candidates',q['missing_salary']],['Screened invalid candidates',q['invalid_salary']],['Usable salary observations',9022],['License status','Unverified; confirm before public redistribution']])
p('SHA-256: '+q['sha256'])
p('The actual schema differs from the reference in two material ways. It contains 27 columns rather than the illustrative 24, including source indices and additional descriptive fields. Its range columns use salary_min and salary_max instead of salary_avg_min and salary_avg_max. The pipeline accepts the reference names and explicitly aliases the observed source names.')
page('5 Data dictionary')
markdown('docs/DATA_DICTIONARY.md')
page('5 Raw completeness audit')
table(['Raw field','Missing values'],list(q['raw_missing'].items()))
p('Table 5.1 Actual raw-field missingness replaces the source report’s illustrative dataset overview. Salary availability is measured directly rather than assuming two-thirds disclosure. Thumbnail and commute fields are not imputed to support analysis. Raw descriptions remain in the preserved source but are omitted from the compact analytical export to reduce size.')
page('6 Data preprocessing methodology')
h('Validation and text normalization',2)
p('The input must be a CSV no larger than 350 MiB with title, company_name, location, description_tokens, date_time and search_location. Empty input and missing required fields raise actionable errors. Text columns collapse whitespace; titles and employer names are normalized in case, and locations are title-cased. Platform identifiers have the leading via token removed. These operations make grouping reproducible without pretending to resolve legal employer entities or geocode locations.')
h('Duplicate strategy',2)
p('Exact raw duplicates are removed first. After normalization and timestamp parsing, a second pass checks title, employer, location and observation date. The supplied data has zero exact duplicates and 5,949 composite duplicates under this rule. Missing or invalid dates cannot establish reliable composite-date identity and therefore do not cause date-based deletion. Deduplication preserves the first occurrence and does not silently synthesize skill or salary fields from conflicting duplicates.')
h('Missing values and malformed fields',2)
p('Unknown salary stays missing. Missing work arrangement becomes Unknown, never Onsite. Invalid timestamps are reported. Safe token parsing accepts bounded literal lists and string tokens only; malformed lists become empty and remain visible in the combined empty/malformed quality count. No unrestricted evaluation, script execution or speculative regular-expression skill recovery is performed.')
page('6 Salary resolution and audit')
table(['Priority','Candidate','Assumption'],[['1','salary_standardized','Use source standardized estimate directly'],['2','salary_yearly','Use annual source figure when first is missing'],['3','salary_hourly × 2080','40 hours × 52 weeks'],['4','Range midpoint annualized','Use known annual/hourly/monthly rate only']])
p('The first nonmissing candidate is selected. A nonmissing value outside the screen is preserved as salary_candidate, marked invalid and excluded from salary_year_avg; a lower-priority value is not silently substituted. salary_source records the selected route. The inclusive baseline is 15,000 through 400,000 in source units. This replicates the reference threshold while disclosing that it can remove valid part-time or unusually senior compensation.')
p('The range fallback is deliberately unit-aware. An hourly midpoint is multiplied by 2,080, a monthly midpoint by 12 and a yearly midpoint by one. An unknown rate does not justify annualization. No currency conversion is performed because the CSV lacks a verified currency field. All charts and exports label monetary values as unverified source units rather than USD.')
p('salary_missing distinguishes an unavailable candidate from an invalid one. The current snapshot has 46,974 missing candidates and eight screened invalid candidates. The valid subset therefore contains 9,022 values. Salary bands use left-closed intervals below 60K, 60–90K, 90–120K and at least 120K. Missing salary has no assigned band.')
page('6 Feature engineering and pipeline quality')
figure('quality','Figure 6.1 Counts measured before and after cleaning')
p('Seniority is derived from title keywords. Lead/Manager takes priority, followed by Senior and Junior/Entry. Unmatched titles receive Mid-Level (inferred), explicitly exposing the default assumption. Skills are unique within an observation and categorized into programming, analyst tools, databases, cloud, libraries or other. Category membership is a documented vocabulary and can be extended; it does not identify every synonym.')
p('Observation year and month derive from date_time. They are retained for historical collection trends and do not establish original posting creation dates. Country is retained as the search target and is not relabelled verified global job location. Each version includes raw and cleaned completeness counts, processing time, source URL, checksum and explicit license/currency limitations.')
page('7 Salary exploratory analysis')
figure('salary_distribution','Figure 7.1 Distribution of 9,022 screened annual salary candidates')
p('The valid salary subset has a median of 88,400 and a mean of approximately 92,131 in unverified source units. Mean exceeding median is consistent with an upper tail, but exact shape is shown through the histogram and percentile table rather than assumed for every filtered group. Non-disclosure is extensive, so the distribution cannot be interpreted as the compensation distribution of all observed roles.')
p('The salary page adds box plots by inferred experience, group mean/median comparisons and screening audit records. Group charts require at least 30 valid salary observations. Skill comparisons can overlap because a job can request several skills; this prevents interpreting the displayed difference as a standalone skill premium.')
page('7 Skill demand analysis')
figure('skill_demand','Figure 7.2 Actual top 15 extracted skills by observation count')
p('Skill demand counts distinct observations containing a token, not raw token appearances. The bridge composite key ensures repeated tokens in the source do not inflate frequency. Both demand and salary sample count are reported. A skill can be common but poorly represented in disclosed salaries, so demand and salary evidence must be inspected together.')
p('The optimal-skill heuristic requires at least 100 demand observations, 30 valid salary observations and mean associated salary at least the overall median. The scatter and candidate table make this rule visible. Co-occurrence counts jobs containing two distinct tokens; diagonal cells show each skill’s own count. These relationships describe extracted requirements rather than causal learning returns.')
for name,title,caption,discussion in [
 ('experience','7 Experience analysis','Figure 7.3 Observation volume by inferred experience','Title classification provides a practical but imperfect view of seniority. The unmatched default is visibly marked inferred. The SQL baseline comparison computes a descriptive salary differential relative to this category, without treating it as a controlled return to experience.'),
 ('companies','7 Employer analysis','Figure 7.4 Highest-volume normalized employer names','Employer counts can reflect reposting and intermediary platforms as well as demand. Normalization combines case variants but does not establish corporate family membership. Salary rankings require a valid disclosed sample and should be examined alongside the number of observations.'),
 ('geography','7 Geographic analysis','Figure 7.5 Search-target coverage in the supplied snapshot','Every search target is United States. The map is therefore explicitly a search-coverage map, not global vacancy geography. Location strings remain available for inspection, but no invented country identity or coordinates are inferred.'),
 ('remote','7 Work arrangement analysis','Figure 7.6 Explicit remote versus unknown observations','The source contains true remote flags and missing values. Unknown records cannot be used as an onsite comparison group. The application displays the categories separately and suppresses an unjustified remote-versus-onsite statistical test.'),
 ('activity','7 Observation trends','Figure 7.7 Monthly collection activity','Observation changes may reflect collection schedules, repeated listings and coverage gaps. LAG calculates relative changes in these counts, but a high percentage is not evidence of proportional growth in newly created vacancies.')]:
 page(title);figure(name,caption);p(discussion)
page('8 SQL analytical casebook')
p('The following 38 questions were executed against the actual committed SQLite database. Each case includes the business question, complete SQL, observed output schema, a short sample, elapsed execution time and interpretation limits. Full CSV result sets are stored separately in Report/query_01.csv through Report/query_38.csv. Tests confirm execution and independently reconcile headline counts and median; execution success alone does not prove every possible business interpretation.')
p('All statements use the predefined query library. Database connections are read-only and query_only is enabled. Users select questions rather than submit arbitrary SQL. Queries operate on the complete committed snapshot, a scope explicitly shown in the application. Global page filters apply to interactive analytical pages, while the SQL Lab retains this documented full-snapshot scope.')
p('The query library covers filtering, grouping, HAVING, inner and outer joins, nested queries, CTEs, conditional aggregation, ranking, ROW_NUMBER, NTILE, LAG, co-occurrence and median. Source-country and currency limitations carry through every query. NULL salary candidates are excluded from salary aggregates, and bridge joins use the appropriate grain for their business question.')
for query,v in zip(qs,validation):
 title=f'8 Query {query["id"]:02} {query["question"].rstrip("?")}'
 if query['id']%2==1 or query['id']==20:page(title)
 else:h(title,2)
 p('Business purpose: '+query['question'])
 sql=query['sql'];sql=re.sub(r'\b(FROM|WHERE|GROUP BY|HAVING|ORDER BY|JOIN|LEFT JOIN|WITH|SELECT|UNION|LIMIT)\b',r'\n\1',sql).strip()
 for line in sql.splitlines():
  for part in textwrap.wrap(line,width=94,break_long_words=False,replace_whitespace=False) or ['']:
   para=doc.add_paragraph();para.paragraph_format.space_after=Pt(1);run=para.add_run(part);run.font.name='Consolas';run.font.size=Pt(8)
 source.append('```sql\n'+query['sql']+'\n```\n')
 p(f'Execution evidence: passed; {v["rows"]:,} output rows; {v["seconds"]:.4f} seconds in the recorded local run. Output file: Report/query_{query["id"]:02}.csv.')
 with open(r/'Report'/f'query_{query["id"]:02}.csv') as f:sample=list(csv.reader(f))
 headers=sample[0];rows=sample[1:5]
 # Long job IDs are summarized only in this printed sample; CSV keeps exact values.
 def display(x):
  try:
   if '.' in x and len(x)>9:return f'{float(x):,.2f}'
  except ValueError:pass
  return str(x)[:36] if len(str(x))>36 else str(x)
 rows=[[display(x) for x in row] for row in rows]
 if rows:table(headers,rows)
 else:p('The query returned no records. This is an observed empty result, not a missing implementation.')
 p('Table 8.'+str(query['id'])+' Recorded result sample. Full rows and precision remain in the CSV.')
 if 'skill' in query['question'].lower():meaning='Skill totals overlap because one observation can request several skills. Salary evidence describes a disclosed subset, and association does not establish the causal value of learning a skill.'
 elif 'salary' in query['question'].lower():meaning='Salary results exclude missing and invalid candidates. Check sample counts and provenance; source currency is unverified, with no causal, inflation or conversion adjustment.'
 elif 'month' in query['question'].lower() or 'observ' in query['question'].lower():meaning='Dates are collection timestamps. Coverage changes and repeated listings affect observed trends; these are neither verified new vacancies nor forecasts.'
 elif 'compan' in query['question'].lower():meaning='Employer normalization does not establish legal-entity relationships. Observed listing volume can reflect intermediaries, syndication and reposting rather than successful hires.'
 else:meaning='Check the stated grouping before adding totals. Unknown values remain unknown and do not establish that an attribute is absent.'
 p('Interpretation and limitations: '+meaning)

page('9 Dashboard design and page responsibilities')
p('The Streamlit application is the primary interactive demonstration. It uses the requested Midnight Navy, Slate, Electric Blue, Teal and Gold presentation palette, native controls, Plotly figures and supported HTML/CSS styling. The sidebar owns global filters and navigation. Every analytical page displays snapshot date range, version, active count and material provenance notices. Light presentation is implemented, but browser appearance and responsive visual quality have not been verified.')
markdown('README.md')
page('9 Power BI supporting implementation')
markdown('Dashboard/dashboard_documentation.md')
page('9 DAX definitions for Desktop validation')
markdown('Dashboard/measures.dax')
page('9 Excel supplementary analysis')
p('The workbook includes Summary, Skills, Salary, Countries, Companies, Cleaned and Instructions sheets. It contains the full cleaned analytical columns, filterable Excel tables, a top-skills chart and formula-based checks for record count, mean salary and disclosure coverage. Preaggregated analytical tabs provide supplementary views without claiming native PivotTable objects.')
p('Formula values must be evaluated in an office engine before treating their cached values as evidence. Independent Python and SQL calculations provide a separate baseline. The clean-data table retains raw analytical grain, while the Summary links directly to the relevant columns. Text that begins with formula-control characters is escaped before export so employer or title strings do not become spreadsheet formulas.')
p('Native pivot construction instructions are included in the workbook and README. Excel and Power BI should be refreshed only after a new snapshot has been validated and committed. Packaged workbooks, figures and academic documentation do not silently update when the interactive sidebar changes; users must regenerate those full-snapshot artifacts.')
page('10 Business insights and recommendations')
p('The following observations are generated from the actual processed records. Each states a question, numerical result, sample size, evidence reference, interpretation, caveat and recommendations for job seekers and recruiters. They describe the available snapshot rather than current labor-market conditions. A transparent limitation is itself useful evidence: this dataset cannot support a global workplace comparison or an explicit onsite control.')
for i,x in enumerate(findings,1):
 if i>1 and i%2==1:page('10 Business insights continued')
 h(f'{i} {x["question"].rstrip("?")}',2)
 for key,label in [('result','Observed result'),('sample_size','Sample size'),('evidence','Evidence'),('interpretation','Interpretation'),('caveat','Caveat'),('job_seeker_recommendation','For job seekers'),('recruiter_recommendation','For recruiters')]:p(label+': '+str(x[key]))
page('11 Testing and execution evidence')
p('The final executed suite contains 81 passing tests, with zero failures and zero skips. The earlier backend run contained 67 passing tests; the final run added an isolated valid-refresh check, 11 page-level Streamlit tests plus filter/reset and SQL action checks. Fixtures are clearly test-only and are never used as production dashboard data. Actual XML and text records are retained in Report/tests.xml and Report/tests.log.')
coverage=[['Schema and loading','Missing required fields and empty CSV rejection'],['Duplicates','Exact and normalized composite behavior'],['Salary','Fallback priority, hourly/range units, missing values, inclusive screening boundaries'],['Features','Title experience categories and Remote/Onsite/Unknown mapping'],['Safe parsing','Malformed, non-list and executable-looking token input'],['Database','Repeated build, primary/foreign keys and referential integrity'],['Filters and KPIs','Intersection, salary/date restriction, empty result and known fixture values'],['Exports','Readable PDF and workbook structure/formula presence'],['Refresh','Malformed import preserves prior current pointer'],['Real-data SQL','All 38 queries execute; count and median independently reconcile'],['Application','All 11 scripts run; filter/reset and SQL action checks']]
table(['Test area','Evidence and purpose'],coverage)
p('AppTest executes the Streamlit script and supported widget events. It is a meaningful runtime smoke test, but it does not prove browser rendering, hover interactions, upload screenshots or mobile layout. Browser access to localhost was denied at the approval gate. That blocker is recorded rather than worked around or replaced by artificial screenshots.')
page('11 Query performance and integrity evidence')
table(['Query','Rows','Seconds'],[[v['id'],v['rows'],f'{v["seconds"]:.4f}'] for v in validation])
p('Table 11.1 Measured query timings from the supplied local snapshot. Performance depends on hardware, cache state and dataset size. Foreign-key checks passed during build and were independently tested with an invalid reference. A repeated fixture import preserved the expected fact count.')
page('12 Deployment and reproducibility')
markdown('docs/DEPLOYMENT.md')
page('12 Live demonstration and offline backup')
markdown('docs/LIVE_DEMO_SCRIPT.md')
page('13 Conclusion and remaining work')
p('The project implements and executes the core local analytics workflow using genuine data. It provides validated preprocessing, a normalized database, a 38-query analytical library, 11 Streamlit pages, filtered downloads, Excel support, reproducible chart generation and transparent business observations. Independent tests reconcile critical values and exercise failure preservation rather than accepting written code as proof of operation.')
p('The final acceptance gate is intentionally incomplete. Native Power BI validation requires Desktop, genuine dashboard screenshots require allowed browser access, and the owner must supply academic identity and approved certificate/declaration wording. Global job-country claims, verified USD comparisons and remote-versus-onsite inference are unsupported by the supplied source. Production PostgreSQL, native Excel pivots and multi-platform clean-install rehearsals remain additional work.')
p('Future work should first improve evidence quality: verified country and currency metadata, a permitted refreshed snapshot, controlled browser QA and native BI validation. Predictive modeling should follow only after train/test separation, leakage controls, baseline comparisons, uncertainty reporting and meaningful evaluation. No experimental model has been added merely to increase apparent complexity.')
h('References',2)
for t in ['Supplied MCA_Internship_Report.pdf, 52 physical pages. Used as requirement reference, not as evidence of executed numerical results.','Luke Barousse. Data Analyst Job Postings. Kaggle. https://www.kaggle.com/datasets/lukebarousse/data-analyst-job-postings-google-search. Local source checksum recorded in the dataset audit.','pandas documentation. https://pandas.pydata.org/docs/','Python ast documentation. https://docs.python.org/3/library/ast.html','SQLite documentation. https://www.sqlite.org/docs.html','SQLAlchemy documentation. https://docs.sqlalchemy.org/','Streamlit documentation. https://docs.streamlit.io/','Plotly Python documentation. https://plotly.com/python/','Microsoft Power BI documentation. https://learn.microsoft.com/power-bi/','SciPy statistics documentation. https://docs.scipy.org/doc/scipy/reference/stats.html'] :p(t)
page('Appendix A Editable source code listings')
p('These listings correspond to the separately delivered editable repository. They are included as text rather than screenshots. Source comments and line breaks may wrap for print. Tests and SQL files remain available in their original formats for execution.')
for path in [r/'app.py',*sorted((r/'src').glob('*.py')),*sorted((r/'scripts').glob('*.py')),*sorted((r/'tests').glob('*.py')),r/'SQL/schema.sql',r/'SQL/postgresql/optimal_skills.sql']:
 if not path.read_text().strip():continue
 h(str(path.relative_to(r)),2)
 for line in path.read_text().splitlines():
  wrapped=textwrap.wrap(line,width=106,replace_whitespace=False,drop_whitespace=False) or ['']
  for part in wrapped:
   para=doc.add_paragraph();para.paragraph_format.space_after=Pt(0);para.paragraph_format.line_spacing=1;run=para.add_run(part);run.font.name='Consolas';run.font.size=Pt(8)
 source.append('```\n'+path.read_text()+'\n```')
(r/'docs/ACADEMIC_REPORT_SOURCE.md').write_text('\n'.join(source))
for style in doc.styles:
 if style.type==1:
  for borders in list(style.element.iter(qn('w:pBdr'))):borders.getparent().remove(borders)
for borders in list(doc.element.iter(qn('w:pBdr'))):borders.getparent().remove(borders)
doc.save(r/'Report/Academic_Report.docx');print('DOCX saved')
