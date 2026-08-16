---
title: "MISRA report overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/misra-report-overview.html"
content_id: "RfMp_Lmg~90M91jz3xPDVQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:39.899725+00:00"
---

# MISRA report overview

The MISRA Report uses analysis results for a project in Coverity Connect to evaluate a
codebase and create a formatted report. The codebase is evaluated against a policy,
which is a set of rules for determining whether the project's issues are consistent with
MISRA compliance. The result is presented in the MISRA Compliance section in the
Executive Summary of the report.

Note: The total number of issues in the report should be equal to the sum of
all values in the Count column in Coverity Connect while in
Issues mode. This is not necessarily the same as the number of matching issues shown in
Connect.

Important: To support report generation, you must use the
`--coding-standard-config` option to the
`cov-analyze` command. This option provides the path to a
configuration file for a coding standard to run as part of the analysis. The
configuration file can specify one of several MISRA standards; for
example,

```
{   version : "2.0",
    standard : "misrac2012",
    title: "your_title_here",
    deviations : []
}
```
