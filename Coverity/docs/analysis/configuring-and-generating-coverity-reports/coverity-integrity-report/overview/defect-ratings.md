---
title: "Defect ratings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/defect-ratings.html"
content_id: "f4k57dINWJwNyuWBq5ETCQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:33.929232+00:00"
---

# Defect ratings

To rate your code and code components in relation to the software industry, the report
relies on defect density, which is equal to the number of high-risk and medium-risk
defects found in 1000 lines of code (LOC). For example, 100 defects in 100,000 LOC
yields a defect density of 1 (because 100/100000 = 1 defect per 1000 LOC). The defect
densities identified in the report exclude low-risk defects, as well as defects that
developers dismissed as intentional in Coverity Connect. Except for the Level 3 rating,
the report also excludes defects that developers report as false positives.

Table 1. Software Integrity Report levels

| Level | Description |
| --- | --- |
| Level Not Achieved | Indicates that the target level rating criteria are not met because the software has too many unresolved static analysis defects. To achieve the target integrity level rating, more defects should be reviewed and fixed. |
| Level 1 | The defect density is close to the average for the software industry average: < 1 defect per 1000 lines of code. |
| Level 2 | The defect density is in the 90th percentile for the software industry: < 0.1 defect per 1000 LOC. |
| Level 3 | The defect density is in the 99th percentile for the software industry (< 0.01 defect per 1000 LOC). Developers have marked fewer than 20% of the defects as false positives and set no defects to major severity in Coverity Connect. A Coverity audit of the false positives can alter the 20% limit. |

The report contains additional information about these levels. You can view this
information in a sample report after extracting the Software Integrity Report file in
Generating a Integrity report.

Note: The results of checkers that developers create by using the Coverity Software
Development Kit or the earlier Coverity Extend are excluded from the defect density
because they do not have risk categories.
