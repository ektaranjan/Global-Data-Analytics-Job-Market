# Technical interview preparation

Explain the project as a snapshot analytics system rather than a vacancy search engine. Start with the genuine input, the composite identity and the exact salary fallback chain. Discuss why a job-skills bridge prevents ambiguous comma-separated queries and how distinct job counts prevent exploded joins from inflating KPIs.

Describe a failure path: malformed uploaded CSV fails required-column validation, so the atomic current pointer never changes. A version is visible only after a complete database with referential integrity has been built. Discuss the limitation that concurrency across imports is not supported.

Be prepared to derive the SQL median using row positions, explain LAG for observation changes, ROW_NUMBER for top salary per employer and NTILE for quartiles. Describe why a missing salary is NULL rather than zero and why a statistical sample threshold does not remove confounding.

Resume description: Built a Python and Streamlit job-market analytics pipeline using a genuine Kaggle snapshot, normalized SQLite tables, read-only SQL analytics, salary provenance, data-quality monitoring and reproducible exports. State executed test and query counts only after reading the evidence files.

GitHub description: Reproducible job market analytics project with transparent snapshot provenance, normalized job/skill data, interactive filters, sample-qualified salary analysis and documented limitations. No paid API or production cloud database required for local operation.
