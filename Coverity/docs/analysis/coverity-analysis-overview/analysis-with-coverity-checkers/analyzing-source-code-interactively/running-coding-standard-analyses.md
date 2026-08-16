---
title: "Running coding-standard analyses"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/running-coding-standard-analyses.html"
content_id: "l9wfTkDsMb_912JpSKWdnQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:33:11.092361+00:00"
---

# Running coding-standard analyses

Coverity Analysis enables you to run code analyses using the supported coding standards
listed in Coverity language support.

For the most consistent and accurate results on coding-standard scans (CERT, MISRA, etc.),
run a separate scan for each coding-standard with all other checkers disabled.
For example, if you want to scan for MISRA and CERT C issues,
run one scan with only MISRA checkers enabled and then run a separate scan with only CERT C checkers enabled.
Running a scan for multiple coding standards simultaneously might suppress some results.

HIS metric analysis is available when running any of the supported MISRA C or C++ coding
standards. However, it is not possible to specify multiple HIS configurations in a
single analysis run. If multiple configurations are specified, the last one on the
command line is used.

For each analysis run, only one configuration can be specified per coding standard. You
can use the same intermediate directory for coding-standards analyses as you do for
regular builds, commits, and other types of analysis.

The coding-standard analysis works on files with the following file extensions:

```
.C, .c, .cc, .cpp, .cu, .cxx, .h, .hh, .hpp, .hxx, .ipp, .java
```

The coding standard analysis workflow follows the typical pattern described in The analysis. The main difference is the use of
the `--coding-standard-config` option:

To run the coding standard analysis for C/C++, you must pass the
`--coding-standard-config` option to
`cov-analyze`.
See the Coverity 2026.6.0 Command Reference for details on
`--coding-standard-config`.
