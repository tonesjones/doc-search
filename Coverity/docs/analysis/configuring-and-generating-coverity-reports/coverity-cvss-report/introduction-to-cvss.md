---
title: "Introduction to CVSS"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/introduction-to-cvss.html"
content_id: "5kk1AMw6A~fTDJerS3H2~g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:13.684400+00:00"
---

# Introduction to CVSS

The Coverity Common Vulnerability Scoring System (CVSS) Report details the application
security activities carried out to assess software vulnerabilities. Based upon the CVSS
framework, it calculates CVSS scores and provides a summary of findings. It uses CWE
data and input from the master file or user-defined profile. The codebase is then
evaluated against published policy requirements and its results are described in the
report, along with required remediation actions. The CVSS Report also analyzes the
issues returned by Coverity and calculates a **CVSS Score**, based
on the triage attributes. Each policy element (or attribute) must pass for the policy to
pass.

Note: The total number of issues in the report should be equal to the number of matching issues shown in
Connect.

Remember:
From report to report, there might be discrepancies in the CWE Top 25/40 values assigned to issues, but both CWE values are valid.

CWEs have a parent-child relationship. Because of this, a child can be considered the same CWE as its ancestor.
So the discrepancies arise because, when Coverity assigns a Top 25/40 rank to an issue, some reports only consider assigning CWEs from the Top 25,
while other reports consider the Top 40 as well.
