---
title: "Detailed results"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/detailed-results.html"
content_id: "ATn21euZSrHODQq32vs7TQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:27.448178+00:00"
---

# Detailed results

The report generator outputs a zip file containing detailed results for each contributing
tool. The data is provided in a machine-readable form, for use by the developers tasked
with fixing the issues.

## Coverity results

The Coverity results consist of a single table in CSV format
(coverity-issues.csv). The table has one row per issue detected
by Coverity analysis.

Table 1. Coverity Results

| Column Title | Content | Notes |
| --- | --- | --- |
| CID | The CID number of the issue. | This is the ID number of the issue, managed by Coverity Connect. |
| CWE | The CWE number of the issue, if any. | Not all issues have CWE numbers. |
| OWASP Web Top 10 rank | The rank of the issue in the OWASP Top 10, if any. | By default, the Top 10 of 2017 is used. You can configure Coverity Analysis to use the Top 10 of 2021, instead. See "Configuring an OWASP Web Top 10 Report" in the Generating a Coverity OWASP Web Top 10 Report document. |
| CWE/SANS Top 40 rank | The rank of the issue in the CWE/SANS Top 40, if any. | By default, the Top 40 of 2019 is used. You can configure Coverity Analysis to use the Top 40 of 2021, 2022 or of 2023, instead. |
| file name | Name of the file where the main event occurs. |  |
| line number | Line number of the main event in the above file. |  |
| type | A short description of a checker. | E.g., "Unsigned compared against 0." |
| category | Coverity category of the issue. | E.g., "Control flow issues." |
| description | The English text describing the main event. | E.g., "This less-than-zero comparison of an unsigned value is never true. "i < 0U"" |
