---
title: "bd-integrity-report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/bd-integrity-report.html"
content_id: "vyYTxWMievEgi6RC7KdsxQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:43:19.104677+00:00"
---

# bd-integrity-report

Launches a GUI application for configuring the Black Duck Software Integrity
report.

## Synopsis

```
bd-integrity-report
```

## Description

The `bd-integrity-report` command runs the GUI for the Black Duck Software Integrity
report () application, for configuring and generating a Black Duck Software Integrity report.
The  uses analysis results for a project in Coverity Connect
to evaluate a codebase and create a formatted report.

For information about the Black Duck Software Integrity report, see "Black Duck Software Integrity report" in Configuring and Generating Coverity Reports.

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
