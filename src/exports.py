"""Reproducible exports from records; no invented findings."""
import io,json
from xml.sax.saxutils import escape
import pandas as pd
from openpyxl import Workbook,load_workbook
from openpyxl.chart import BarChart,Reference
from openpyxl.styles import Font,PatternFill,Alignment
from openpyxl.worksheet.table import Table,TableStyleInfo
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table as PDFTable
from reportlab.lib.styles import getSampleStyleSheet
from .analytics import kpis,grouped,skill_stats

def safe_value(v):
    if pd.isna(v):return None
    if isinstance(v,str) and v.startswith(('=','+','-','@')):return "'"+v
    return v.item() if hasattr(v,'item') else v

def excel_bytes(d):
    """Create the requested openpyxl workbook; preaggregations replace native pivots."""
    w=Workbook();w.remove(w.active)
    cols=['job_id','job_title','company_name','location','job_country','experience_level','remote_status','salary_year_avg','salary_source','observation_date']
    sheets={'Summary':pd.DataFrame(kpis(d).items(),columns=['Metric','Value']),'Skills':skill_stats(d),'Salary':grouped(d,'experience_level'),'Countries':grouped(d,'job_country'),'Companies':grouped(d,'company_name'),'Cleaned':d[cols]}
    for name,frame in sheets.items():
        s=w.create_sheet(name);s.append(frame.columns.tolist())
        for row in frame.itertuples(index=False,name=None):s.append([safe_value(x) for x in row])
        s.freeze_panes='A2';s.sheet_view.showGridLines=False
        for c in s[1]:c.font=Font(color='FFFFFF',bold=True);c.fill=PatternFill('solid',fgColor='172033');c.alignment=Alignment(wrap_text=True)
        s.row_dimensions[1].height=30
        for col in s.columns:s.column_dimensions[col[0].column_letter].width=min(52,max(20,len(str(col[0].value))+3,max((len(str(c.value or '')) for c in list(col)[:200]),default=0)))
        if s.max_row>1:
            t=Table(displayName=name+'Table',ref=s.dimensions);t.tableStyleInfo=TableStyleInfo(name='TableStyleMedium2',showRowStripes=True);s.add_table(t)
        for row in s.iter_rows(min_row=2):
            for c in row:
                c.alignment=Alignment(wrap_text=True,vertical='center')
                if isinstance(c.value,float):c.number_format='#,##0.0'
            import math
            s.row_dimensions[row[0].row].height=max(24,min(75,15*max(math.ceil(len(str(c.value or ''))/max(1,s.column_dimensions[c.column_letter].width-2)) for c in row)))
    summary=w['Summary'];last=len(d)+1
    summary.append(['Formula checks','Source records'])
    summary.append(['Postings from data',f'=COUNTA(Cleaned!A2:A{last})'])
    summary.append(['Mean salary from data',f'=IFERROR(AVERAGE(Cleaned!H2:H{last}),0)'])
    summary.append(['Salary disclosure coverage',f'=IFERROR(COUNT(Cleaned!H2:H{last})/COUNTA(Cleaned!A2:A{last}),0)']);summary.cell(summary.max_row,2).number_format='0.0%'
    summary.column_dimensions['A'].width=34;summary.column_dimensions['B'].width=23
    summary['B12'].number_format='#,##0.0'
    for row in summary.iter_rows(min_row=10):
        summary.row_dimensions[row[0].row].height=32
        for c in row:c.alignment=Alignment(wrap_text=True,vertical='center')
    chart=BarChart();chart.title='Most requested skills';chart.y_axis.title='Observation count';chart.x_axis.title='Skill'
    chart.add_data(Reference(w['Skills'],min_col=2,min_row=1,max_row=min(16,w['Skills'].max_row)),titles_from_data=True);chart.set_categories(Reference(w['Skills'],min_col=1,min_row=2,max_row=min(16,w['Skills'].max_row)));summary.add_chart(chart,'D2')
    s=w.create_sheet('Instructions')
    for text in ['Historical job-market snapshot. Salary figures use unverified source currency.','Source: https://www.kaggle.com/datasets/lukebarousse/data-analyst-job-postings-google-search','Country describes search target, not verified job location.','Unknown remote flags are not onsite roles.','Rebuild with python -m scripts.build_outputs after importing a new snapshot.','Preaggregated analytical tabs are supplied. Native PivotTables are not created.','To build a pivot: select CleanedTable, Insert > PivotTable, choose dimensions and Count of job_id.','Formula cells recalculate when opened in Excel. This generator does not calculate formula caches.']:
        s.append([text])
    s.column_dimensions['A'].width=110;s.sheet_view.showGridLines=False
    out=io.BytesIO();w.save(out);return out.getvalue()

def executive_pdf(d,q):
    out=io.BytesIO();styles=getSampleStyleSheet();story=[]
    def p(text,style='BodyText'):story.append(Paragraph(escape(str(text)),styles[style]));story.append(Spacer(1,10))
    p('Job Market Intelligence Executive Report','Title');p('Historical snapshot analysis generated from actual processed records.')
    p(f'Observed interval: {q["snapshot_start"]} to {q["snapshot_end"]}. Snapshot checksum: {q["sha256"]}.')
    p('Salary currency is unverified. Country is search target. Unknown remote flags do not establish onsite work. Salary associations are not causal premiums.')
    for k,v in kpis(d).items():p(f'{k}: {v:,.2f}' if isinstance(v,float) else f'{k}: {v:,}')
    p('Skill demand','Heading2')
    for row in skill_stats(d).head(10).itertuples():p(f'{row.skill}: {row.demand:,} observations; {row.salary_n:,} valid salary observations.')
    p('Use these descriptive results to prioritize further research. Recruiters should verify currency, location, seniority and current market conditions before compensation decisions.')
    SimpleDocTemplate(out).build(story);return out.getvalue()
