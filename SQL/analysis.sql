-- 01: How many postings are in the snapshot?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT COUNT(*) AS postings FROM job_postings_fact;

-- 02: How many distinct companies?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT COUNT(*) AS companies FROM company_dim;

-- 03: Which search countries are represented?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT job_country, COUNT(*) postings FROM job_postings_fact GROUP BY job_country;

-- 04: How many unique skills?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT COUNT(*) skills FROM skills_dim;

-- 05: What is the mean valid salary?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT AVG(salary_year_avg) mean_salary,COUNT(salary_year_avg) salary_n FROM job_postings_fact;

-- 06: What is the median valid salary?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
WITH ranked AS (SELECT salary_year_avg,ROW_NUMBER() OVER(ORDER BY salary_year_avg) rn,COUNT(*) OVER() n FROM job_postings_fact WHERE salary_year_avg IS NOT NULL) SELECT AVG(salary_year_avg) median_salary FROM ranked WHERE rn IN ((n+1)/2,(n+2)/2);

-- 07: What share has usable salary?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT 100.0*COUNT(salary_year_avg)/NULLIF(COUNT(*),0) usable_pct FROM job_postings_fact;

-- 08: How are work arrangements reported?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT remote_status,COUNT(*) postings FROM job_postings_fact GROUP BY remote_status;

-- 09: What are the most recent observations?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT job_id,job_title,observation_date FROM job_postings_fact ORDER BY observation_date DESC LIMIT 50;

-- 10: How do volume and salary vary by experience?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT experience_level,COUNT(*) postings,COUNT(salary_year_avg) salary_n,AVG(salary_year_avg) mean_salary FROM job_postings_fact GROUP BY experience_level ORDER BY postings DESC;

-- 11: How do volume and salary vary by search geography?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT job_country,COUNT(*) postings,COUNT(salary_year_avg) salary_n,AVG(salary_year_avg) mean_salary FROM job_postings_fact GROUP BY job_country ORDER BY postings DESC;

-- 12: How do volume and salary vary by employment type?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT employment_type,COUNT(*) postings,COUNT(salary_year_avg) salary_n,AVG(salary_year_avg) mean_salary FROM job_postings_fact GROUP BY employment_type ORDER BY postings DESC;

-- 13: How do volume and salary vary by platform?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT platform,COUNT(*) postings,COUNT(salary_year_avg) salary_n,AVG(salary_year_avg) mean_salary FROM job_postings_fact GROUP BY platform ORDER BY postings DESC;

-- 14: How do volume and salary vary by salary band?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT salary_band,COUNT(*) postings,COUNT(salary_year_avg) salary_n,AVG(salary_year_avg) mean_salary FROM job_postings_fact GROUP BY salary_band ORDER BY postings DESC;

-- 15: How do volume and salary vary by arrangement?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT remote_status,COUNT(*) postings,COUNT(salary_year_avg) salary_n,AVG(salary_year_avg) mean_salary FROM job_postings_fact GROUP BY remote_status ORDER BY postings DESC;

-- 16: Which companies hire most?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT c.company_name,COUNT(*) postings,RANK() OVER(ORDER BY COUNT(*) DESC) company_rank FROM job_postings_fact j JOIN company_dim c ON j.company_id=c.company_id GROUP BY c.company_id ORDER BY postings DESC;

-- 17: Which companies have salary evidence from 30 or more jobs?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT c.company_name,COUNT(j.salary_year_avg) salary_n,AVG(j.salary_year_avg) mean_salary FROM company_dim c JOIN job_postings_fact j ON c.company_id=j.company_id GROUP BY c.company_id HAVING COUNT(j.salary_year_avg)>=30 ORDER BY mean_salary DESC;

-- 18: Which skills are most demanded?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT s.skill,COUNT(*) demand FROM skills_job_dim b JOIN skills_dim s ON b.skill_id=s.skill_id GROUP BY s.skill_id ORDER BY demand DESC;

-- 19: Which skills have high observed salaries?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT s.skill,COUNT(j.salary_year_avg) salary_n,AVG(j.salary_year_avg) mean_salary FROM skills_dim s JOIN skills_job_dim b ON s.skill_id=b.skill_id JOIN job_postings_fact j ON b.job_id=j.job_id GROUP BY s.skill_id HAVING COUNT(j.salary_year_avg)>=30 ORDER BY mean_salary DESC;

-- 20: Which skills are optimal under the defined rule?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
WITH demand AS (SELECT s.skill,COUNT(*) demand,COUNT(j.salary_year_avg) salary_n,AVG(j.salary_year_avg) mean_salary FROM skills_dim s JOIN skills_job_dim b ON s.skill_id=b.skill_id JOIN job_postings_fact j ON j.job_id=b.job_id GROUP BY s.skill_id), r AS (SELECT salary_year_avg,ROW_NUMBER() OVER(ORDER BY salary_year_avg) rn,COUNT(*) OVER() n FROM job_postings_fact WHERE salary_year_avg IS NOT NULL), med AS (SELECT AVG(salary_year_avg) v FROM r WHERE rn IN ((n+1)/2,(n+2)/2)) SELECT * FROM demand WHERE demand>=100 AND salary_n>=30 AND mean_salary>=(SELECT v FROM med) ORDER BY mean_salary DESC;

-- 21: Which skill pairs co-occur most?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT s.skill skill_a,t.skill skill_b,COUNT(*) pair_count FROM skills_job_dim a JOIN skills_job_dim b ON a.job_id=b.job_id AND a.skill_id<b.skill_id JOIN skills_dim s ON s.skill_id=a.skill_id JOIN skills_dim t ON t.skill_id=b.skill_id GROUP BY a.skill_id,b.skill_id ORDER BY pair_count DESC LIMIT 30;

-- 22: What is the top-paying job per company?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
WITH r AS (SELECT *,ROW_NUMBER() OVER(PARTITION BY company_id ORDER BY salary_year_avg DESC,job_id) rn FROM job_postings_fact WHERE salary_year_avg IS NOT NULL) SELECT company_id,job_title,salary_year_avg FROM r WHERE rn=1;

-- 23: What salary quartile contains each disclosed posting?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT job_id,salary_year_avg,NTILE(4) OVER(ORDER BY salary_year_avg) salary_quartile FROM job_postings_fact WHERE salary_year_avg IS NOT NULL;

-- 24: How does monthly observed volume change?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
WITH m AS (SELECT posted_month,COUNT(*) postings FROM job_postings_fact WHERE posted_month IS NOT NULL GROUP BY posted_month),t AS (SELECT *,LAG(postings) OVER(ORDER BY posted_month) previous FROM m) SELECT *,100.0*(postings-previous)/NULLIF(previous,0) change_pct FROM t;

-- 25: What is the observed seniority differential?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
WITH g AS (SELECT experience_level,AVG(salary_year_avg) mean_salary,COUNT(salary_year_avg) salary_n FROM job_postings_fact GROUP BY experience_level) SELECT *,100*(mean_salary/(SELECT mean_salary FROM g WHERE experience_level='Mid-Level (inferred)')-1) differential_pct FROM g;

-- 26: Which jobs have no parsed skills?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT j.job_id,j.job_title FROM job_postings_fact j LEFT JOIN skills_job_dim b ON j.job_id=b.job_id WHERE b.job_id IS NULL;

-- 27: How many jobs require each skill category?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT s.skill_type,COUNT(DISTINCT b.job_id) postings FROM skills_dim s JOIN skills_job_dim b ON s.skill_id=b.skill_id GROUP BY s.skill_type;

-- 28: Which jobs exceed the snapshot mean salary?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT job_id,salary_year_avg FROM job_postings_fact WHERE salary_year_avg>(SELECT AVG(salary_year_avg) FROM job_postings_fact) ORDER BY salary_year_avg DESC;

-- 29: How many remote jobs does each company report?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT company_id,SUM(CASE WHEN remote_status='Remote' THEN 1 ELSE 0 END) remote_jobs,SUM(CASE WHEN remote_status='Unknown' THEN 1 ELSE 0 END) unknown_jobs,COUNT(*) postings FROM job_postings_fact GROUP BY company_id;

-- 30: How are annual salaries derived?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT salary_source,COUNT(*) postings,COUNT(salary_year_avg) valid_salaries FROM job_postings_fact GROUP BY salary_source;

-- 31: How many candidate salaries fail screening?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT COUNT(*) invalid_salary FROM job_postings_fact WHERE salary_missing=0 AND salary_valid=0;

-- 32: Which locations have the most observations?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT location,COUNT(*) postings FROM job_postings_fact GROUP BY location ORDER BY postings DESC LIMIT 30;

-- 33: Which companies have no usable salary observations?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT c.company_name FROM company_dim c LEFT JOIN job_postings_fact j ON c.company_id=j.company_id GROUP BY c.company_id HAVING COUNT(j.salary_year_avg)=0;

-- 34: How many skills are requested per posting?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
WITH n AS (SELECT j.job_id,COUNT(b.skill_id) skill_count FROM job_postings_fact j LEFT JOIN skills_job_dim b ON j.job_id=b.job_id GROUP BY j.job_id) SELECT skill_count,COUNT(*) postings FROM n GROUP BY skill_count ORDER BY skill_count;

-- 35: Which skills appear in reported remote roles?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT s.skill,COUNT(*) postings FROM skills_dim s JOIN skills_job_dim b ON s.skill_id=b.skill_id JOIN job_postings_fact j ON j.job_id=b.job_id WHERE j.remote_status='Remote' GROUP BY s.skill_id ORDER BY postings DESC;

-- 36: How does monthly salary coverage vary?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT posted_month,COUNT(*) postings,100.0*COUNT(salary_year_avg)/COUNT(*) coverage_pct FROM job_postings_fact GROUP BY posted_month ORDER BY posted_month;

-- 37: How does experience vary by remote status?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT experience_level,remote_status,COUNT(*) postings FROM job_postings_fact GROUP BY experience_level,remote_status;

-- 38: What are the salary extremes after screening?
-- Snapshot observation dates; source currency unverified; Unknown remote is distinct from Onsite. Salary aggregates exclude missing and invalid values.
SELECT MIN(salary_year_avg) minimum,MAX(salary_year_avg) maximum FROM job_postings_fact;