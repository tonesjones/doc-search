---
title: "cov-security-report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cov-security-report.html"
content_id: "gOwSB30zgDlwuTrOdfUfEQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:16.508232+00:00"
---

# cov-security-report

Launches a GUI application for configuring Security Report.

## Synopsis

```
cov-security-report <config.yaml>
```

## Description

The `cov-security-report` command runs the GUI Security Report
application for configuring and generating a Security Report. The Security Report
uses analysis results for a project in Coverity Connect to evaluate a codebase and
create a formatted report. The codebase is evaluated against a policy, which is a
set of rules or standards for determining pass or fail.

The report's policy has 4 elements, and each element must pass for the policy to
pass. The result for each element is presented in the Scorecard in the Executive
Summary of the report.

For information about the Security Report, see "Coverity Security report" in Configuring and Generating Coverity Reports.

## Exit codes

Most Coverity Analysis commands can return the following exit codes:

- 0: The command successfully completed the requested task.
- 1: The requested task is complete, but it did not return (or find) any results.
  Note that some Coverity Analysis commands do not return this error code.
- 2: The command was unable to complete the requested task. This error typically
  includes an error message and some remediation advice.
- 4: An unexpected error occurred. This error should not occur when the product is
  used in a supported way. Very likely, the requested task was not completed. This
  error typically provides some diagnostic and/or debugging output, such as a
  stack trace.

For exceptions, see cov-commit-defects, cov-analyze, and cov-build.
