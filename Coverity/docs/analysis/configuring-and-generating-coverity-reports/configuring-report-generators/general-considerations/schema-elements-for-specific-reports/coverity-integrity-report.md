---
title: "Coverity Integrity Report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-integrity-report.html"
content_id: "4aySqWuaTdw01pSN4KlfyA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:02.901419+00:00"
---

# Coverity Integrity Report

The Coverity Integrity Report has additional keys for report specification:

```
cir-report:
    project-description:
    project-details:
    target-integrity-level:
    high-severity-name:
    unspecified-severity-name:
    trial:
    loc-multiplier:
```

| Key | Class Type | Description | Default | Required? |
| --- | --- | --- | --- | --- |
| `high-severity-name` | String | Lists the name of the highest severity value. | Major | No |
| `loc-multiplier` | String | Sets the LOC multiplier for the number of lines of code that have been inspected. | 1 | No |
| `project-description` | String | States the project description. | Coverity Connect description | No |
| `project-details` | String | States the details of the project. | N/A | No |
| `target-integrity-level` | Integer | Defines the target's integrity levels.  These are the standard target integrity levels:  - 1: < 1 defect per thousand lines of code - 2: < .1 defects per thousand lines of code - 3: < .01 defects per thousand lines of code, and other   requirements | 1 | No |
| `trial` | Boolean | Activates the trial flag. The trial flag should be set to `True` if page three of the report should not be printed. (Page three contains severity data which is not applicable to a trial.) | false | No |
| `unspecified-severity-name` | String | Lists the names of any unspecified severity values. | Unspecified | No |

For more information about the Integrity Report configuration, see the "Coverity Integrity Report configuration file".
