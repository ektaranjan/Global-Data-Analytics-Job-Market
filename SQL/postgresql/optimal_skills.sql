-- PostgreSQL-only supporting function; not executed in this environment.
-- Load equivalent tables first; this is not a SQLite stored procedure.
CREATE OR REPLACE FUNCTION top_paying_skills(min_demand integer DEFAULT 100,min_salary_n integer DEFAULT 30)
RETURNS TABLE(skill text,demand bigint,salary_n bigint,mean_salary double precision)
LANGUAGE sql STABLE AS $$
 SELECT s.skill::text, COUNT(*) demand, COUNT(j.salary_year_avg) salary_n,
 AVG(j.salary_year_avg)::double precision mean_salary
 FROM skills_dim s JOIN skills_job_dim b ON s.skill_id=b.skill_id
 JOIN job_postings_fact j ON j.job_id=b.job_id
 GROUP BY s.skill_id,s.skill
 HAVING COUNT(*)>=min_demand AND COUNT(j.salary_year_avg)>=min_salary_n
 ORDER BY mean_salary DESC;
$$;
