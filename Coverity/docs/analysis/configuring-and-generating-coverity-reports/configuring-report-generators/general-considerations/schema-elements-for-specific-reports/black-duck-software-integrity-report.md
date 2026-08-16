---
title: "Black Duck Software Integrity Report"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/black-duck-software-integrity-report.html"
content_id: "i5KlnXaCywceMfJabKwFoA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:04.281441+00:00"
---

# Black Duck Software Integrity Report

The Black Duck Software Integrity report has additional keys for specifying and defining the
analysis date and legal text, as well as keys specifying whether to include false
positive issues information and checker details information.

```
bdsir-report:
    analysis-date: 01/15/2019    
    legal-text:
    show-checker-details: YES
    include-false-positive: YES
```

| Key | Class Type | Description | Default | Required? |
| --- | --- | --- | --- | --- |
| `analysis-date` | String | Specifies when the analysis has been completed. Dates should be entered in MM/DD/YYYY format. | N/A | Yes |
| `include-false-positive` | String | Specifies whether to include defects marked as "intentional" or "false positive" in the report. Possible values: `YES`, `NO`. | `YES` | No |
| `legal-text` | String | Includes legal text. Multiline text should be placed inside double quotes. (For example: "This is Multiline legal text.") | N/A | No |
| `show-checker-details` | String | Specifies whether to display checker details information in the report. Possible values: `YES`, `NO`. | `NO` | No |

For more information about the Black Duck Software Integrity report configuration, see the "Black Duck Software Integrity Report configuration file".
