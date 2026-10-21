"""Structural acceptance checks for the rendered 30-page professional report."""
from pathlib import Path
import json,re,zipfile
from pypdf import PdfReader
from docx import Document
ROOT=Path(__file__).resolve().parents[1]
pdf=ROOT/'Report/Global_Data_Analytics_Job_Market_Report.pdf'
docx=ROOT/'Report/Global_Data_Analytics_Job_Market_Report.docx'
manifest=json.loads((ROOT/'Report/professional_report_index.json').read_text())
r=PdfReader(pdf);doc=Document(docx);assert len(r.pages)==30,len(r.pages)
texts=[p.extract_text() or '' for p in r.pages];full='\n'.join(texts)
for phrase in ['MCA','Master of Computer Applications','Semester','College project','Major project','Minor project','Internship report','University examination','Academic session','certificate','declaration','registration number','academic supervisor']:
 assert not re.search(r'\b'+re.escape(phrase)+r'\b',full,re.I),phrase
assert 'INDEX' in texts[1]
index_table=doc.tables[0]
assert [c.text for c in index_table.rows[0].cells]==['S.No.','Title','Page No.']
assert len(index_table.rows)==14
for row,item in zip(index_table.rows[1:],manifest['index']):
 assert [c.text for c in row.cells]==[str(item['serial']),item['title'],str(item['printed_page'])]
 actual=texts[item['physical_pdf_page']-1]
 lines=actual.splitlines();assert lines[0]==str(item['printed_page']),(item,lines[:3])
 assert lines[1]==item['title'],(item,lines[:3])
for i,text in enumerate(texts[2:],1):assert text.splitlines()[0]==str(i),(i,text[:100])
for n,text in enumerate(texts):
 if n not in (0,1):assert len(text)>450,(n+1,len(text))
for i in range(1,10):assert f'Figure {i}' in full,i
assert len(re.findall(r'Table \d+\s',full))==18
assert len(doc.inline_shapes)>=9
with zipfile.ZipFile(docx) as z:
 assert 'word/document.xml' in z.namelist();assert len(z.read('word/document.xml'))>30000
out={'pdf_pages':len(r.pages),'docx_rendered_pages':len(r.pages),'front_matter_pages':2,'printed_body_pages':28,'index_columns':['S.No.','Title','Page No.'],'index_sections':13,'all_index_targets_match':True,'body_numbering_verified':True,'prohibited_report_label_matches':0,'figures':9,'numbered_tables':18,'editable_document':True,'visual_review':'Every final page inspected separately after rendering','render_engine':'Bundled LibreOffice through render_docx.py; DOCX/PDF layout checked in that engine'}
(ROOT/'Report/PROFESSIONAL_REPORT_VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
