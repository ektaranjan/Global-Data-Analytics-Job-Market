# PDF requirements traceability

Source: supplied 52-page internship report; PDF physical page numbering. Generated before application code. All rows start pending; later gate reviews must add verified evidence.

| Source | Requirement | File / function | Application page | Test | Status | Evidence |
|---|---|---|---|---|---|---|
| PDF 7 | 1.1 Background....................................................................................................................1 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 7 | 1.2 Problem Statement.........................................................................................................1 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 7 | 1.3 Existing System............................................................................................................. 2 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 7 | 1.4 Limitations of Existing System..................................................................................... 2 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 7 | 1.5 Proposed System............................................................................................................3 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 7 | 1.6 Objectives...................................................................................................................... 3 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 7 | 1.7 Scope of the Project.......................................................................................................4 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 7 | 1.8 Applications...................................................................................................................4 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 7 | 1.9 Expected Outcome.........................................................................................................5 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 7 | 2.1 Introduction....................................................................................................................6 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 7 | 2.2 Data Analytics............................................................................................................... 6 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 7 | 2.3 Job Market Analytics.....................................................................................................7 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 7 | 2.4 Salary Analytics.............................................................................................................7 | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 7 | 2.5 Skill Demand Analysis.................................................................................................. 8 | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 7 | 2.6 Previous Research..........................................................................................................8 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 8 | 2.7 Research Gap.................................................................................................................9 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 8 | 3.1 Functional Requirements.............................................................................................10 | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 8 | 3.2 Non-Functional Requirements.....................................................................................10 | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 8 | 3.3 Software Requirements................................................................................................11 | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 8 | 3.4 Hardware Requirements.............................................................................................. 11 | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 8 | 3.5 Technology Stack........................................................................................................ 12 | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 8 | 4.1 Project Workflow.........................................................................................................13 | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 8 | 4.2 Architecture Diagram.................................................................................................. 13 | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 8 | 4.3 Data Flow.................................................................................................................... 14 | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 8 | 4.4 Project Modules...........................................................................................................14 | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 8 | 4.5 Folder Structure........................................................................................................... 15 | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 8 | 4.6 Workflow Explanation.................................................................................................16 | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 8 | 5.1 Dataset Source............................................................................................................. 17 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 8 | 5.2 Dataset Overview.........................................................................................................17 | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 8 | 5.3 Column Description.....................................................................................................18 | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 8 | 5.4 Data Dictionary............................................................................................................18 | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 8 | 5.5 Dataset Statistics..........................................................................................................19 | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 8 | 5.6 Data Quality Issues......................................................................................................19 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 8 | 6.1 Missing Values............................................................................................................ 20 | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 8 | 6.2 Duplicate Records........................................................................................................20 | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 9 | 6.3 Data Cleaning.............................................................................................................. 21 | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 9 | 6.4 Data Transformation....................................................................................................21 | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 9 | 6.5 Feature Engineering.....................................................................................................22 | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 9 | 6.6 Exporting Clean Dataset..............................................................................................22 | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 9 | 7.1 Overview......................................................................................................................23 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 9 | 7.2 Salary Distribution.......................................................................................................23 | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 9 | 7.3 Skill Analysis...............................................................................................................24 | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 9 | 7.4 Company Analysis.......................................................................................................24 | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 9 | 7.5 Location Analysis........................................................................................................ 25 | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 9 | 7.6 Experience Analysis.................................................................................................... 25 | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 9 | 7.7 Remote Work Analysis................................................................................................26 | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 9 | 7.8 Key Observations.........................................................................................................26 | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 9 | 8.1 Database Creation........................................................................................................27 | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 9 | 8.2 Table Creation............................................................................................................. 27 | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 9 | 8.3 SQL Queries................................................................................................................ 28 | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 9 | 8.4 Business Questions...................................................................................................... 29 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 9 | 8.5 Query Outputs..............................................................................................................30 | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 9 | 8.6 SQL Insights................................................................................................................ 30 | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 9 | 9.1 Dashboard Design........................................................................................................31 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | intentionally modified | Streamlit equivalent passes script-level checks; native Power BI and screenshots remain blocked |
| PDF 9 | 9.2 KPI Cards.................................................................................................................... 31 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | intentionally modified | Streamlit equivalent passes script-level checks; native Power BI and screenshots remain blocked |
| PDF 9 | 9.3 Salary Dashboard.........................................................................................................32 | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 10 | 9.4 Skill Dashboard........................................................................................................... 32 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | intentionally modified | Streamlit equivalent passes script-level checks; native Power BI and screenshots remain blocked |
| PDF 10 | 9.5 Location Dashboard.....................................................................................................33 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | intentionally modified | Streamlit equivalent passes script-level checks; native Power BI and screenshots remain blocked |
| PDF 10 | 9.6 Remote Work Dashboard............................................................................................ 33 | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 10 | 9.7 Dashboard Explanation................................................................................................34 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | intentionally modified | Streamlit equivalent passes script-level checks; native Power BI and screenshots remain blocked |
| PDF 10 | 10.1 Major Findings.......................................................................................................... 35 | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 10 | 10.2 Business Insights....................................................................................................... 35 | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 10 | 10.3 Recommendations for Job Seekers............................................................................36 | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 10 | 10.4 Recommendations for Recruiters.............................................................................. 36 | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 10 | 10.5 Future Scope.............................................................................................................. 37 | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 11 | 1.1 Background | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 11 | 1.2 Problem Statement | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 11 | 1.3 Existing System | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 12 | 1.4 Limitations of Existing System | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 12 | 1.5 Proposed System | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 13 | 1.6 Objectives | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 13 | 1.7 Scope of the Project | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 14 | 1.8 Applications | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 14 | 1.9 Expected Outcome | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 15 | 2.1 Introduction | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 15 | 2.2 Data Analytics | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 15 | 2.3 Job Market Analytics | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 15 | 2.4 Salary Analytics | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 16 | 2.5 Skill Demand Analysis | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 16 | 2.6 Previous Research | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 16 | 2.7 Research Gap | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 18 | 3.1 Functional Requirements | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 18 | FR-1 Data Ingestion The system shall load the raw job-postings CSV file | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 18 | FR-2 Data Cleaning The system shall remove duplicate records, | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 18 | FR-3 Data Transformation The system shall derive new fields, including | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 18 | FR-4 Skill Extraction The system shall parse the nested skill-token field | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 18 | FR-5 Database Storage The system shall persist the cleaned data into a | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 18 | FR-6 SQL Querying The system shall support analytical SQL queries, | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 18 | FR-7 Dashboard Visualization The system shall present key metrics and trends | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | intentionally modified | Streamlit equivalent passes script-level checks; native Power BI and screenshots remain blocked |
| PDF 18 | FR-8 Insight Generation The system shall produce a structured, written report | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 19 | Table 3.1: Functional Requirements | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 19 | 3.2 Non-Functional Requirements | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 19 | 3.3 Software Requirements | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 20 | Table 3.2: Software Requirements | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 20 | 3.4 Hardware Requirements | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 20 | Table 3.3: Hardware Requirements | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 20 | 3.5 Technology Stack | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 21 | Table 3.4: Technology Stack Summary | README.md; docs/DEPLOYMENT.md / Requirements and environment | Project Documentation and About | Report/environment.txt; Report/sql_validation.json | intentionally modified | Executed SQLite and Streamlit; production portability and visual browser QA remain incomplete |
| PDF 22 | 4.1 Project Workflow | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 22 | 4.2 Architecture Diagram | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 22 | Figure 4.1: Project Architecture | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 22 | 4.3 Data Flow | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 22 | Figure 4.2: Data Flow Diagram | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 23 | 4.4 Project Modules | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 23 | Table 4.1: Project Modules | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 23 | 4.5 Folder Structure | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 24 | 4.6 Workflow Explanation | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |
| PDF 26 | 5.1 Dataset Source | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 26 | 5.2 Dataset Overview | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 26 | Figure 5.1: Dataset Overview (df.info() Output) | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 27 | 5.3 Column Description | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 27 | Table 5.1: Raw Dataset Column Description | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 28 | 5.4 Data Dictionary | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 28 | Table 5.2. | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 28 | Table 5.2: Derived Column Data Dictionary | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 28 | 5.5 Dataset Statistics | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 29 | Table 5.3: Illustrative Dataset Summary Statistics | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 29 | 5.6 Data Quality Issues | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 31 | 6.1 Missing Values | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 31 | 6.2 Duplicate Records | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 31 | 6.3 Data Cleaning | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 32 | 6.4 Data Transformation | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 32 | Table 6.1: Salary Resolution Priority Chain | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 32 | 6.5 Feature Engineering | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 33 | 6.6 Exporting Clean Dataset | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 34 | 7.1 Overview | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 34 | 7.2 Salary Distribution | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 34 | Figure 7.1: Salary Distribution Histogram | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 34 | 7.3 Skill Analysis | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 34 | Figure 7.2: Top 15 In-Demand Skills | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 35 | 7.4 Company Analysis | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 35 | 7.5 Location Analysis | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 35 | Figure 7.3: Postings by Country | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 35 | 7.6 Experience Analysis | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 36 | 7.7 Remote Work Analysis | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 36 | Figure 7.4: Remote vs Onsite Posting Split | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 36 | 7.8 Key Observations | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 37 | 8.1 Database Creation | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 37 | 8.2 Table Creation | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 37 | Table Type Key Columns Purpose | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 37 | Table 8.1: Database Table Summary | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 38 | 8.3 SQL Queries | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 39 | 8.4 Business Questions | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 39 | Table 8.2: Sample Business Questions Answered by SQL | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 40 | 8.5 Query Outputs | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 40 | Table 8.3: Illustrative Optimal Skills Query Output | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 40 | 8.6 SQL Insights | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 41 | 9.1 Dashboard Design | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | intentionally modified | Streamlit equivalent passes script-level checks; native Power BI and screenshots remain blocked |
| PDF 41 | 9.2 KPI Cards | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | intentionally modified | Streamlit equivalent passes script-level checks; native Power BI and screenshots remain blocked |
| PDF 41 | Figure 9.1: Executive Overview Page — KPI Cards | Dashboard/dashboard_documentation.md / Power BI support assets | Streamlit equivalent; native PBIX unavailable | Desktop validation pending | blocked | Power BI Desktop unavailable; browser screenshot access denied; no native PBIX claim |
| PDF 42 | 9.3 Salary Dashboard | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 42 | Figure 9.2: Salary Analysis Page | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 42 | 9.4 Skill Dashboard | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | intentionally modified | Streamlit equivalent passes script-level checks; native Power BI and screenshots remain blocked |
| PDF 42 | Figure 9.3: Skills Intelligence Page | Dashboard/dashboard_documentation.md / Power BI support assets | Streamlit equivalent; native PBIX unavailable | Desktop validation pending | blocked | Power BI Desktop unavailable; browser screenshot access denied; no native PBIX claim |
| PDF 42 | 9.5 Location Dashboard | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | intentionally modified | Streamlit equivalent passes script-level checks; native Power BI and screenshots remain blocked |
| PDF 42 | Figure 9.4: Location & Company Insights Page | Dashboard/dashboard_documentation.md / Power BI support assets | Streamlit equivalent; native PBIX unavailable | Desktop validation pending | blocked | Power BI Desktop unavailable; browser screenshot access denied; no native PBIX claim |
| PDF 43 | 9.6 Remote Work Dashboard | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 43 | Figure 9.5: Remote vs Onsite Comparison | Dashboard/dashboard_documentation.md / Power BI support assets | Streamlit equivalent; native PBIX unavailable | Desktop validation pending | blocked | Power BI Desktop unavailable; browser screenshot access denied; no native PBIX claim |
| PDF 43 | 9.7 Dashboard Explanation | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | intentionally modified | Streamlit equivalent passes script-level checks; native Power BI and screenshots remain blocked |
| PDF 44 | 10.1 Major Findings | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 44 | 10.2 Business Insights | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 45 | 10.3 Recommendations for Job Seekers | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 45 | 10.4 Recommendations for Recruiters | src/analytics.py; scripts/build_outputs.py / grouped / skill_stats / main | Analytical pages 1–6 | test_real_kpi_reconciliation; test_page_runs | implemented | Actual outputs, 22 findings and generated figures; unsupported geography/currency claims corrected |
| PDF 46 | 10.5 Future Scope | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 49 | APPENDIX A: PYTHON LIBRARIES USED | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 49 | Table A.1: Python Libraries and Their Purpose | docs/ACADEMIC_REPORT_SOURCE.md / Report narrative | Project Documentation and About | Report render inspection | implemented | Covered in rendered 89-page report; see Report/render_verification.md |
| PDF 50 | APPENDIX B: SQL QUERIES | SQL/analysis.sql; src/sql_lab.py / execute / validate | SQL Analytics Lab | test_real_sql_executes; test_db_integrity_and_repeatability | implemented | 38 executed query outputs and schemas in Report/sql_validation.json |
| PDF 51 | APPENDIX C: DASHBOARD SCREENSHOTS PLACEHOLDER | Dashboard/dashboard_documentation.md / Power BI support assets | Streamlit equivalent; native PBIX unavailable | Desktop validation pending | blocked | Power BI Desktop unavailable; browser screenshot access denied; no native PBIX claim |
| PDF 51 | Figure C.1: Power BI Dashboard — Executive Overview Page | Dashboard/dashboard_documentation.md / Power BI support assets | Streamlit equivalent; native PBIX unavailable | Desktop validation pending | blocked | Power BI Desktop unavailable; browser screenshot access denied; no native PBIX claim |
| PDF 51 | Figure C.2: Power BI Dashboard — Skills Intelligence Page | Dashboard/dashboard_documentation.md / Power BI support assets | Streamlit equivalent; native PBIX unavailable | Desktop validation pending | blocked | Power BI Desktop unavailable; browser screenshot access denied; no native PBIX claim |
| PDF 51 | Figure C.3: Power BI Dashboard — Salary Analysis Page | src/pipeline.py / clean / tokens / run | Data Quality and Pipeline Monitor | tests/test_core.py | implemented | 81-test suite passed; quality.json contains actual results |
| PDF 51 | Figure C.4: Power BI Dashboard — Location & Company Insights Page | Dashboard/dashboard_documentation.md / Power BI support assets | Streamlit equivalent; native PBIX unavailable | Desktop validation pending | blocked | Power BI Desktop unavailable; browser screenshot access denied; no native PBIX claim |
| PDF 52 | APPENDIX D: GITHUB REPOSITORY STRUCTURE | docs/ARCHITECTURE.md; README.md / Architecture and module specification | Project Documentation and About | test_db_integrity_and_repeatability | implemented | ER and architecture figures generated from implemented design |

## Figures
- PDF 22: Figure 4.1: Project Architecture
- PDF 22: Figure 4.2: Data Flow Diagram
- PDF 26: Figure 5.1: Dataset Overview (df.info() Output)
- PDF 34: Figure 7.1: Salary Distribution Histogram
- PDF 34: Figure 7.2: Top 15 In-Demand Skills
- PDF 35: Figure 7.3: Postings by Country
- PDF 36: Figure 7.4: Remote vs Onsite Posting Split
- PDF 41: Figure 9.1: Executive Overview Page — KPI Cards
- PDF 42: Figure 9.2: Salary Analysis Page
- PDF 42: Figure 9.3: Skills Intelligence Page
- PDF 42: Figure 9.4: Location & Company Insights Page
- PDF 43: Figure 9.5: Remote vs Onsite Comparison
- PDF 51: Figure C.1: Power BI Dashboard — Executive Overview Page
- PDF 51: Figure C.2: Power BI Dashboard — Skills Intelligence Page
- PDF 51: Figure C.3: Power BI Dashboard — Salary Analysis Page
- PDF 51: Figure C.4: Power BI Dashboard — Location & Company Insights Page

## Tables
- PDF 19: Table 3.1: Functional Requirements
- PDF 20: Table 3.2: Software Requirements
- PDF 20: Table 3.3: Hardware Requirements
- PDF 21: Table 3.4: Technology Stack Summary
- PDF 23: Table 4.1: Project Modules
- PDF 27: Table 5.1: Raw Dataset Column Description
- PDF 28: Table 5.2.
- PDF 28: Table 5.2: Derived Column Data Dictionary
- PDF 29: Table 5.3: Illustrative Dataset Summary Statistics
- PDF 32: Table 6.1: Salary Resolution Priority Chain
- PDF 37: Table Type Key Columns Purpose
- PDF 37: Table 8.1: Database Table Summary
- PDF 39: Table 8.2: Sample Business Questions Answered by SQL
- PDF 40: Table 8.3: Illustrative Optimal Skills Query Output
- PDF 49: Table A.1: Python Libraries and Their Purpose

## Placeholders and illustrative claims
- PDF 1: [Student Name]
- PDF 1: Enrollment No.: [Enrollment Number]
- PDF 1: [Guide / Mentor Name]
- PDF 1: [University / Institute Name]
- PDF 1: [Academic Year]
- PDF 2: Salary Trend Dashboard” has been carried out by [Student Name], Enrollment No. [Enrollment
- PDF 2: Computer Applications (MCA) during the academic year [Academic Year].
- PDF 3: guidance of [Guide Name].
- PDF 3: [Student Name]
- PDF 3: Enrollment No.: [Enrollment Number]
- PDF 4: I would like to express my sincere gratitude to my project guide, [Guide Name], for their invaluable
- PDF 4: Computer  Applications,  [University/Institute  Name],  for  providing  the  necessary  resources,
- PDF 4: [Student Name]
- PDF 10: Appendix C: Dashboard Screenshots Placeholder............................................................ 41
- PDF 22: [ Project Architecture — Insert Screenshot / Diagram Here ]
- PDF 22: [ Data Flow Diagram — Insert Screenshot / Diagram Here ]
- PDF 26: [ Dataset Overview (df.info() Output) — Insert Screenshot / Diagram Here ]
- PDF 26: within a single column, description_tokens, as a Python-list-formatted string (for example, "['sql',
- PDF 29: Value (Illustrative — replace with live
- PDF 29: Total job postings (post-cleaning) [X]
- PDF 29: Unique companies [X]
- PDF 29: Unique countries [X]
- PDF 29: Unique skills identified [X]
- PDF 29: Postings with salary disclosed [X]%
- PDF 29: Average annual salary (USD) $[X]
- PDF 29: Median annual salary (USD) $[X]
- PDF 29: Table 5.3: Illustrative Dataset Summary Statistics
- PDF 34: [ Salary Distribution Histogram — Insert Screenshot / Diagram Here ]
- PDF 34: [ Top 15 In-Demand Skills — Insert Screenshot / Diagram Here ]
- PDF 35: [ Postings by Country — Insert Screenshot / Diagram Here ]
- PDF 36: [ Remote vs Onsite Posting Split — Insert Screenshot / Diagram Here ]
- PDF 40: correct and returns a logically sound result set for the given schema. Illustrative output for the
- PDF 40: [skill] [X] $[X]
- PDF 40: [skill] [X] $[X]
- PDF 40: [skill] [X] $[X]
- PDF 40: Table 8.3: Illustrative Optimal Skills Query Output
- PDF 41: [ Executive Overview Page — KPI Cards — Insert Screenshot / Diagram Here ]
- PDF 41: measure: Total Postings ([Total Postings] = COUNTROWS(job_postings_fact)), Average Salary
- PDF 41: ([Average Salary] = AVERAGE(job_postings_fact[salary_year_avg])), Percentage Remote ([%
- PDF 42: [ Salary Analysis Page — Insert Screenshot / Diagram Here ]
- PDF 42: [ Skills Intelligence Page — Insert Screenshot / Diagram Here ]
- PDF 42: [ Location & Company Insights Page — Insert Screenshot / Diagram Here ]
- PDF 43: [ Remote vs Onsite Comparison — Insert Screenshot / Diagram Here ]
- PDF 48: Barousse, L. (2024). Data Analyst Job Postings (Google Search Results) [Data set]. Kaggle.
- PDF 51: [ Power BI Dashboard — Executive Overview Page — Insert Screenshot / Diagram Here ]
- PDF 51: [ Power BI Dashboard — Skills Intelligence Page — Insert Screenshot / Diagram Here ]
- PDF 51: [ Power BI Dashboard — Salary Analysis Page — Insert Screenshot / Diagram Here ]
- PDF 51: [ Power BI Dashboard — Location & Company Insights Page — Insert Screenshot /

## Methodology corrections
- Original PDF scope preserved; Streamlit is the requested primary interface enhancement.
- Native PBIX requires Power BI Desktop; never claim a PBIX from documentation alone.
- Source raw file has 27 columns, with salary_min/salary_max rather than salary_avg_min/salary_avg_max. Explicit aliases required.
- search_location describes the search target, not verified job country. Preserve this distinction.
- Null remote flags mean Unknown, not Onsite.
- date_time is observation time; do not call it a verified original posting date.
- No currency column exists: salary currency must remain unverified unless source evidence is obtained.
- Source claims about two-thirds salary coverage require replacement by measured data.

## Field-level coverage

| Source physical pages | Field / formula | Implementation | Verification | Status |
|---|---|---|---|---|
| 27–39 | title/company_name/location: Whitespace normalization, casefolding and location title case | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | via: Prefix removal and platform casefold | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | date_time: UTC observation date and observed month | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | work_from_home: Remote/Onsite/Unknown mapping | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | description_tokens: Bounded literal parsing and unique tokens | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | salary_standardized: First fallback priority | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | salary_yearly: Second fallback priority | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | salary_hourly: Third priority × 2,080 | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | salary_avg_min/max: Explicit actual-schema alias salary_min/max; range annualization only with known units | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | search_location: Preserved search target, not verified job country | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | job_id: Preserved source ID plus surrogate fact ID | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | posted_at: Raw relative text preserved; no unsupported date anchoring | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | schedule_type: employment_type; Unknown when absent | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | salary_band: Left-closed 60K/90K/120K cutpoints | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | experience_level: Manager, Senior, Junior, inferred Mid-Level | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | salary outliers: Inclusive 15K–400K baseline; preserve candidate values | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | mean / median: Nonmissing screened salaries only | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | remote percentage: Explicit Remote / all filtered records | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | salary coverage: Valid screened salaries / all filtered records | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | optimal skill: Demand ≥100, salary sample ≥30, mean salary ≥overall median | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | co-occurrence: Distinct tokens per observation; bridge self-join | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |
| 27–39 | month-over-month: Observation-month counts with LAG; no vacancy creation claim | src/pipeline.py; src/analytics.py; SQL/analysis.sql | tests/test_core.py; query validation | implemented |

## Open evidence and intentionally changed claims

- Native Power BI screenshots and PBIX remain blocked by unavailable Desktop.
- Real browser screenshots remain blocked by denied localhost browser access. AppTest verifies script execution, not responsive layout, tooltips or light-mode appearance.
- Dataset global-country and USD claims are unsupported. Search target and unverified source units replace them throughout.
- PostgreSQL server portability and stored-function execution remain pending.
- GitHub publication, signed certificate, student metadata and institutional approval require the owner.


## Front matter and chapter-level audit

| Source pages | Commitment | Implementation / status | Evidence |
|---|---|---|---|
| 1–4 | Student identity, certificate, declaration, acknowledgements | pending owner input; no fabricated credentials or signatures | Academic_Report cover and submission checklist |
| 5–6 | Abstract and quantitative claims | intentionally modified to actual results and limitations | Academic_Report abstract |
| 7–10 | Table of contents | implemented for generated report | Academic_Report contents |
| 11–14 | Chapter 1 introduction and objectives | implemented | Report chapter 1 |
| 15–17 | Chapter 2 literature and research framework | implemented; no invented novelty claims | Report chapter 2 |
| 18–21 | Chapter 3 functional and quality requirements | implemented with explicit incomplete gates | Traceability and Report chapter 3 |
| 22–25 | Chapter 4 architecture and modules | implemented | Architecture figures and repository |
| 26–30 | Chapter 5 dataset source, schema, statistics and issues | implemented; source statistics replaced | quality.json, dictionary and report chapter 5 |
| 31–33 | Chapter 6 cleaning, normalization and exports | implemented | pipeline.py and tests |
| 34–36 | Chapter 7 EDA and observations | implemented; unsupported global/onsite claims removed | Generated charts and Python analytics |
| 37–40 | Chapter 8 database and SQL | implemented for SQLite; PostgreSQL validation pending | 38 results and separate PostgreSQL asset |
| 41–43 | Chapter 9 five-page Power BI report | blocked native PBIX; supporting definitions and Streamlit equivalent supplied | Dashboard assets and AppTest |
| 44–46 | Chapter 10 observations and recommendations | implemented from actual records | 22 structured findings |
| 47 | Chapter 11 conclusion | implemented with remaining gates | Final report conclusion |
| 48 | References | implemented with source and tool references | Final report references |
| 49 | Appendix A library list | implemented with actual versions | Report/environment.txt |
| 50 | Appendix B SQL library | implemented; complete SQL and result casebook | SQL/analysis.sql and report chapter 8 |
| 51 | Appendix C native dashboard screenshots | blocked by unavailable Power BI Desktop and denied browser origin access | Screenshots/README.md |
| 52 | Appendix D repository structure and publication | local Git repository initialized; GitHub publication pending | README and local .git; no remote claimed |
