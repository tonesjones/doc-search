---
title: "Overview"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/overview.html"
content_id: "p2sm5R_F7PvnEmzWnCQnDg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:27.308905+00:00"
---

# Overview

The Hyundai Coding Standard report aggregates the results of Coverity Static Analysis performed
on a particular project. A project is a collection of one or more streams containing
separately analyzed snapshots. The latest snapshot in each stream is used when reporting
results for a project. A Hyundai report provides information about Hyundai
vulnerabilities detected by the Coverity HYUNDAI checkers described in the Coverity 2026.6.0 Checker Reference (see "HYUNDAI rules").

The Hyundai report provides summary information for outstanding violations by component
and rule, and for dismissed violations. Additionally, for each rule defined in the
standard, the Hyundai report describes the rule, its priority and level, and specifies
whether it is supported and enabled, and the number of times that rule has been
violated.

The "Deviations Details" section of the report lists deviations from the designated
Hyundai standard.

The "Methodology" section of the report explains in detail how rules are defined. It also
explains how Hyundai terminology for violations maps to Coverity terminology for
defects.

Important: To support report generation, you must use the
`--coding-standard-config` option to the `cov-analyze`
command. This option provides the path to a configuration file for a coding standard to
run as part of the analysis. For Hyundai, it might look like this:

```
{   
	version : "4.1",
	standard : "hyundai-c",
	title: "your_title_here"
}
```

Note: Support for Hyundai C 4.0, Hyundai C++ 4.0, and Hyundai Java
4.0 has been deprecated and will be removed in the 2026.9 release.
