# Power BI supporting delivery

Status: Power BI-ready assets only. Native PBIX creation and DAX engine validation require Power BI Desktop on Windows and have not been performed here.

Import the four CSV tables from the current Dataset/processed version. Set company_id and skill_id to whole numbers, job_id to text, observation_date to Date, salary_year_avg to decimal and booleans to whole numbers. Use theme.json through View > Themes > Browse. Keep the unverified-currency and search-target notices visible.

Relationships: company_dim.company_id (1) → job_postings_fact.company_id (*); job_postings_fact.job_id (1) → skills_job_dim.job_id (*); skills_dim.skill_id (1) → skills_job_dim.skill_id (*). All use single-direction filtering toward the bridge or fact. Add Date.Date (1) → job_postings_fact.observation_date (*). Mark Date as the date table. Use explicit TREATAS measures for salary by skill instead of enabling uncontrolled bidirectional relationships.

Create measures from measures.dax. These are source definitions requiring Desktop validation. Check COUNTROWS against query 01; mean against query 05; median against query 06; coverage against query 07; skill demand against query 18. Confirm each slicer changes both the numerator and denominator correctly. A skill slicer must use Skill Mean Salary, not unfiltered Average Salary.

Five original pages:
1. Executive Overview: total postings, mean/median, remote share and salary coverage; observation line, experience bars and arrangement distribution.
2. Salary Analysis: histogram, experience comparison, search-target salary, arrangement and coverage. Show only comparisons with at least 30 salary observations. Units remain unverified source currency.
3. Skills Intelligence: top 15 demand, skill demand/salary scatter, optimal flag, skill category slicer and visible salary sample sizes.
4. Location and Company Insights: map search targets only, top employers and employer benchmark table. A single search country cannot support global comparisons.
5. Career Recommendation: choose one skill; show demand, associated salary with sample count, monthly observation activity and co-required skills imported from query 21. No causal or predictive claim.

Sync date, search-target country, arrangement and experience slicers across all pages. Unknown arrangement must be selectable. Test empty selections, rare skills and groups below salary thresholds. Do not label remote-minus-Unknown as a remote salary premium. Monthly date measures are observation history, not unique job creation or guaranteed year-over-year hiring growth.

Refresh: import a new CSV using the verified Python pipeline, refresh CSV paths to the new immutable version, then Refresh All in Desktop. Validate against that version's query exports and checksum. Package a native PBIX only after checking every page, measures, relationships, slicers and exports. Take genuine Power BI screenshots separately; Streamlit screenshots do not prove PBIX functionality.
