---
title: "Security report overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/security-report-overview.html"
content_id: "BK_PuY5oSqk7ux0i3ZkCfA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:39:09.449696+00:00"
---

# Security report overview

The Security Report generator uses analysis results for a Coverity Connect project to
evaluate the analyzed codebase. Based on this evaluation, it creates a Security Report.
The codebase is evaluated against a policy, a set of rules or standards for determining
pass or fail. The policy has 4 elements, and each element must pass for the policy to
pass. The result for each element is presented in the Scorecard in the Executive Summary
of the report. The elements include:

- **Security score** represents the severity levels of the
  issues found as a numerical value from 0 to 100, with issues of the highest
  reported severity level having the greatest impact on lowering the score.
- **OWASP Top 10 Count** specifies the number of security issues found that are
  included in OWASP's top ten count.

  The OWASP (Open Web Application Security
  Project) Foundation publishes a report of the most critical web application
  security flaws, in a ranked order based on input from a worldwide group of
  security experts.

  By default, the Top 10 from the year 2021 is used. You can configure Coverity Analysis to use the Top 10 of 2021, instead. See "Configuring an OWASP Web
  Top 10 Report" in the Generating a Coverity OWASP Web Top 10 Report
  document.
- **CWE/SANS Top 25 Count** specifies the number of security
  issues found that are included in the CWE/SANS Top 25 list.

  CWE (Common Weakness Enumeration) is a software community project responsible for
  creating a catalog of software weaknesses and vulnerabilities. The CWE/SANS Top
  25 is a list of weaknesses, taken from the CWE, that are deemed to be the most
  widespread and critical errors that can lead to serious software
  vulnerabilities.
- **Analysis date** specifies the date when the analysis
  produced the data upon which the report is based.

The severity of the issues found during analysis is determined by a *severity
mapping* that maps security flaws to severity levels. The report generator can
use one of three default severity mappings, or it can use a custom severity mapping that
you define when you configure the report generator.

Remember:
From report to report, there might be discrepancies in the CWE Top 25/40 values assigned to issues, but both CWE values are valid.

CWEs have a parent-child relationship. Because of this, a child can be considered the same CWE as its ancestor.
So the discrepancies arise because, when Coverity assigns a Top 25/40 rank to an issue, some reports only consider assigning CWEs from the Top 25,
while other reports consider the Top 40 as well.

In addition to providing a summary of findings, the report also includes sections that
list the remediation actions required and increasingly detailed views of the issues
found. The report also provides a detailed breakdown and cross references between
technical findings and analysis results.

This chapter describes the workflow needed for generating a Security Report and explains
how you interpret report findings.
