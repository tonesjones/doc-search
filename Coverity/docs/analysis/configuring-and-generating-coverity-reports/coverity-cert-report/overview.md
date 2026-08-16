---
title: "Overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/overview.html"
content_id: "hv_s8_qFyrfsFOW5_jKHkw"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:06.857487+00:00"
---

# Overview

The Coverity CERT Report aggregates the results of Coverity Static Analysis performed on a
particular project. A project is a collection of one or more streams containing
separately analyzed snapshots. The latest snapshot in each stream is used when reporting
results for a project. A CERT Report provides information about CERT vulnerabilities
detected by the Coverity CERT checkers described in the Coverity 2026.6.0 Checker Reference (see "SEI
CERT rules")

The CERT Report provides summary information for outstanding violations by component and
rule, and for dismissed violations. Additionally, for each rule defined in the standard,
the CERT Report describes the rule, its priority and level, and specifies whether it is
supported and enabled, and the number of times that rule has been violated.

The "Deviations Details" section of the report lists deviations from the designated CERT
standard.

The "Methodology" section of the report explains in detail how rules are defined,
and how their priority and level are determined. It also explains how CERT terminology
for violations maps to Coverity terminology for defects.

Important: To support report generation, you must use the
`--coding-standard-config` option to the
`cov-analyze` command. This option provides the path to a
configuration file for a coding standard to run as part of the analysis. For CERT, it
might look like this:

```
{   version : "2.0",
    standard : "cert-c",
    title: "your_title_here",
    deviations : []
}
```
