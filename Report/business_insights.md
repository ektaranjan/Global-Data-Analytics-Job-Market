# Business insights from the executed snapshot

## 1. How many observations survive cleaning?

**Result:** 56,004 retained from 61,953; 5,949 composite duplicates removed.

**Sample Size:** 61953

**Evidence:** quality.json

**Interpretation:** Duplicate indexing inflates raw volume.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Compare cleaned observations rather than raw rows.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 2. How complete is usable salary?

**Result:** 9,022 usable salaries; 16.11% coverage.

**Sample Size:** 56004

**Evidence:** query_07.csv

**Interpretation:** Disclosed salaries represent a selected subset.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Inspect the disclosed sample size before using salary rankings.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 3. What is the observed salary center?

**Result:** Median 88,400; mean 92,131, source units.

**Sample Size:** 9022

**Evidence:** query_05.csv and query_06.csv

**Interpretation:** Mean and median describe different aspects of the salary distribution.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Verify currency and relevant experience before benchmarking.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 4. What is the middle salary spread?

**Result:** 25th percentile 62,400; 75th percentile 116,812.

**Sample Size:** 9022

**Evidence:** charts/salary_distribution.png

**Interpretation:** The middle half describes the disclosed sample.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Research a salary range rather than one point estimate.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 5. How many candidates fail screening?

**Result:** 8 annual salary candidates are outside the baseline.

**Sample Size:** 56004

**Evidence:** query_31.csv

**Interpretation:** The baseline can remove valid atypical compensation.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Inspect exclusions for part-time and leadership roles.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 6. What geography is observed?

**Result:** 1 search-target country: United States

**Sample Size:** 56004

**Evidence:** query_03.csv

**Interpretation:** This does not establish global workplace coverage.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Treat the sample as US search coverage.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 7. How many records explicitly report remote work?

**Result:** 25,053 observations; 44.73%.

**Sample Size:** 56004

**Evidence:** query_08.csv

**Interpretation:** The denominator includes Unknown.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Use positively identified remote records.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 8. How much arrangement information is unknown?

**Result:** 30,951 records.

**Sample Size:** 56004

**Evidence:** query_08.csv

**Interpretation:** Missing flags cannot provide an onsite control.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Do not infer onsite employment from a blank flag.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 9. How many employers are represented?

**Result:** 13,177 normalized names.

**Sample Size:** 56004

**Evidence:** query_02.csv

**Interpretation:** Normalized names are not verified legal entities.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Check employer identity and subsidiaries.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 10. How many rows have no parsed skill?

**Result:** 12,085 records.

**Sample Size:** 56004

**Evidence:** query_26.csv

**Interpretation:** Empty extracted lists do not prove no skills are required.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Read source descriptions before drawing conclusions.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 11. How frequent is sql?

**Result:** 28,081 observations (50.14%); 4,072 usable salaries.

**Sample Size:** 56004

**Evidence:** query_18.csv

**Interpretation:** sql is present in the extracted skill vocabulary.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Prepare a portfolio example when the skill matches your target roles.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 12. How frequent is excel?

**Result:** 17,867 observations (31.90%); 2,681 usable salaries.

**Sample Size:** 56004

**Evidence:** query_18.csv

**Interpretation:** excel is present in the extracted skill vocabulary.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Prepare a portfolio example when the skill matches your target roles.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 13. How frequent is python?

**Result:** 17,050 observations (30.44%); 2,221 usable salaries.

**Sample Size:** 56004

**Evidence:** query_18.csv

**Interpretation:** python is present in the extracted skill vocabulary.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Prepare a portfolio example when the skill matches your target roles.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 14. How frequent is tableau?

**Result:** 15,266 observations (27.26%); 2,330 usable salaries.

**Sample Size:** 56004

**Evidence:** query_18.csv

**Interpretation:** tableau is present in the extracted skill vocabulary.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Prepare a portfolio example when the skill matches your target roles.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 15. How frequent is power_bi?

**Result:** 14,531 observations (25.95%); 1,944 usable salaries.

**Sample Size:** 56004

**Evidence:** query_18.csv

**Interpretation:** power_bi is present in the extracted skill vocabulary.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Prepare a portfolio example when the skill matches your target roles.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 16. How frequent is r?

**Result:** 10,312 observations (18.41%); 1,357 usable salaries.

**Sample Size:** 56004

**Evidence:** query_18.csv

**Interpretation:** r is present in the extracted skill vocabulary.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Prepare a portfolio example when the skill matches your target roles.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 17. How common is Mid-Level (inferred)?

**Result:** 41,438 observations; 7,053 usable salaries; median 81,494 source units.

**Sample Size:** 56004

**Evidence:** query_10.csv

**Interpretation:** Title keywords infer experience; years of experience are not verified.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Confirm actual requirements from descriptions.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 18. How common is Senior?

**Result:** 8,772 observations; 1,262 usable salaries; median 96,500 source units.

**Sample Size:** 56004

**Evidence:** query_10.csv

**Interpretation:** Title keywords infer experience; years of experience are not verified.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Confirm actual requirements from descriptions.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 19. How common is Lead/Manager?

**Result:** 3,579 observations; 413 usable salaries; median 125,000 source units.

**Sample Size:** 56004

**Evidence:** query_10.csv

**Interpretation:** Title keywords infer experience; years of experience are not verified.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Confirm actual requirements from descriptions.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 20. How common is Junior/Entry?

**Result:** 2,215 observations; 294 usable salaries; median 52,000 source units.

**Sample Size:** 56004

**Evidence:** query_10.csv

**Interpretation:** Title keywords infer experience; years of experience are not verified.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Confirm actual requirements from descriptions.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 21. Which company_name has highest observed volume?

**Result:** upwork: 6,572 observations.

**Sample Size:** 56004

**Evidence:** query_16.csv

**Interpretation:** Volume can reflect collection and reposting.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Use counts as a starting point for further research.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

## 22. Which platform has highest observed volume?

**Result:** linkedin: 20,066 observations.

**Sample Size:** 56004

**Evidence:** query_13.csv

**Interpretation:** Volume can reflect collection and reposting.

**Caveat:** Historical, nonrandom snapshot. Source currency unverified. Salary disclosure and collection coverage can bias results; associations are not causal.

**Job Seeker Recommendation:** Use counts as a starting point for further research.

**Recruiter Recommendation:** Verify target-role relevance, currency, geography and current hiring context before acting.

