# Project explanation for beginners

The CSV is a large table of job observations. Python cleans inconsistent labels and removes repeated rows. A database separates employers, job observations, skills and the links between jobs and skills. This makes it possible to ask questions such as how often SQL appears without storing the same skill definition repeatedly.

Salary can appear in several fields. The pipeline chooses the first available field in the specified priority chain, annualizes hourly amounts using 2,080 hours and preserves where the result came from. Missing salary remains missing. A screening rule removes candidate values outside the baseline interval from salary calculations but keeps them for audit.

The dashboard asks the calculation functions for counts and charts after applying sidebar filters. Selecting Senior and Python means observations that meet both conditions. Selecting Python and SQL within the same skill control means either skill. The SQL Lab is separately labelled as full-snapshot analysis.

A chart cannot prove why a salary differs. It only shows what appears in these observed records. This particular dataset does not prove global geographic coverage, current market conditions or onsite work when a remote flag is absent.
