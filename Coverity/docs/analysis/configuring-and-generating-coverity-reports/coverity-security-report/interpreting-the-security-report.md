---
title: "Interpreting the Security Report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/interpreting-the-security-report.html"
content_id: "lzqRE07AJ7_guuKpyE7U8Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:14.946496+00:00"
---

# Interpreting the Security Report

The report is divided into six basic sections that describe the issues found in
increasing amount of detail:

- **Executive Summary** provides tabular and graphic summary
  information for the issues found.
- **Action Items** explains how the code base was evaluated
  and provides a summary of recommended remediation actions.
- **Security Details** shows the number of issues associated
  with each Technical Impact category.
- **Analysis Details** shows the number of issues associated
  with each OWASP Top 10 category and each CWE/SANS Top 25 category.
- **Detailed Issues Ranked by Severity** lists all issues,
  the name of the source file for that issue and the line number where the issue
  can be found. It also describes the Technical Impact associated with each group
  of issues and recommends remediation actions.
- **Methodology** describes basic elements associated with
  report output.

To interpret report results, you must understand the basic categories used to classify
issues and how report output might vary depending on the severity mapping used when you
configure the report generator. The following sections describe this basic
information.

Note: The total number of issues in the report should be equal to the number of matching issues shown in
Connect.
