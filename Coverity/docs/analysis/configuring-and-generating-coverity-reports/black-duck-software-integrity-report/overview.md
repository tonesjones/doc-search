---
title: "Overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/overview.html"
content_id: "hcgVOi6nP3fNQHDL_Pi7bw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:20.798675+00:00"
---

# Overview

The Black Duck Software Integrity Report summarizes integrity issues existing in a software
development project. The report takes input from the Coverity Analysis testing tools. A
report generator application pulls issue data from each contributing tool, aggregates
the information, and generates data files and a formatted PDF report.

Note: The total number of issues in the report should be equal to the number of matching issues shown in
Connect.

Remember:
From report to report, there might be discrepancies in the CWE Top 25/40 values assigned to issues, but both CWE values are valid.

CWEs have a parent-child relationship. Because of this, a child can be considered the same CWE as its ancestor.
So the discrepancies arise because, when Coverity assigns a Top 25/40 rank to an issue, some reports only consider assigning CWEs from the Top 25,
while other reports consider the Top 40 as well.
