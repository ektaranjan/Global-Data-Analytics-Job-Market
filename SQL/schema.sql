CREATE TABLE company_dim(company_id INTEGER PRIMARY KEY,company_name TEXT NOT NULL UNIQUE);
CREATE TABLE job_postings_fact(job_id TEXT PRIMARY KEY,company_id INTEGER NOT NULL REFERENCES company_dim(company_id),job_title TEXT,location TEXT,job_country TEXT,experience_level TEXT,remote_status TEXT,salary_year_avg REAL,salary_candidate REAL,salary_source TEXT,salary_valid INTEGER,salary_missing INTEGER,salary_band TEXT,observation_date TEXT,posted_month TEXT,employment_type TEXT,platform TEXT,currency_status TEXT);
CREATE TABLE skills_dim(skill_id INTEGER PRIMARY KEY,skill TEXT NOT NULL UNIQUE,skill_type TEXT);
CREATE TABLE skills_job_dim(job_id TEXT REFERENCES job_postings_fact(job_id),skill_id INTEGER REFERENCES skills_dim(skill_id),PRIMARY KEY(job_id,skill_id));
CREATE INDEX ix_company ON job_postings_fact(company_id);
CREATE INDEX ix_country ON job_postings_fact(job_country);
CREATE INDEX ix_date ON job_postings_fact(observation_date);
CREATE INDEX ix_skill ON skills_job_dim(skill_id);
