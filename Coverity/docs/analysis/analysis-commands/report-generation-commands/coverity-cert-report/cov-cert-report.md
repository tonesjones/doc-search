---
title: "cov-cert-report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cov-cert-report.html"
content_id: "3DgB8oYD9SI~KbMi5c71~g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:03.301382+00:00"
---

# cov-cert-report

Launches a GUI application for configuring CERT Report.

## Synopsis

```
cov-cert-report
```

## Description

The `cov-cert-report` command runs the GUI CERT Report application
for configuring and generating a CERT Report. The CERT Report uses analysis results
for a project in Coverity Connect to evaluate a codebase and create a formatted
report. The codebase is evaluated against a policy, which is a set of rules or
standards for determining pass or fail.

The report's policy has 4 elements, and each element must pass for the policy to
pass. The result for each element is presented in the Scorecard in the Executive
Summary of the report.

For information about the CERT Report, see section "Coverity CERT report guide" in the Configuring and Generating Coverity Reports.

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
