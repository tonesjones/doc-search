---
title: "Issue cutoff schema element"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/issue-cutoff-schema-element.html"
content_id: "Athet7c2zjHW32HFvUyNqA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:56.999508+00:00"
---

# Issue cutoff schema element

The issue cutoff schema should include the following key:

| Key | Class Type | Description | Default | Required? |
| --- | --- | --- | --- | --- |
| `issue-cutoff-count` | Integer | Sets the limit for the maximum number of issues displayed in a report. This setting helps to control the size of the generated report.  It is used for the CVSS, Security, PCIDSS, Mobile OWASP, and OWASP reports.  For the Security Report, the maximum value is 10,000. | 200 | No |
