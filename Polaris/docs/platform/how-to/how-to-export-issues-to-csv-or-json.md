---
title: "How to export issues to CSV or JSON"
source_url: "https://docs.blackduck.com/r/polaris/black-duck-polaris-platform/how-to-export-issues-to-csv-or-json.html"
content_id: "8SPAqezGZp9oReYPHawU9g"
product_key: "polaris-platform-latest"
section: "How-to"
scraped_at: "2026-10-04T23:29:19.823700+00:00"
content_hash: "542ee7ca515928d296cebec3e30c03c11ac59e9c380ae7408d52c2edda381db4"
---

# How to export issues to CSV or JSON

From the Issues tab, there are several ways to export issues to a file (CSV/JSON):

- Export an individual issue.
- Batch export by manually selecting multiple issues.
- Batch export by filtering.
- Export all.

See [Ways to triage issues in Polaris](ways-to-triage-issues-in-polaris.md) for details about these selection
methods.

1. Select one or more issues to export, and then select Export Selected.

   [image: A screenshot of the Export Selected Issues panel.]
2. In the Export Selected Issues panel, select File.
3. Select a file type (CSV or JSON).
4. Select Export Issues. The file will download.

## Issue export properties

Table 1. Issue export properties

| Property (CSV) | Property (JSON) | Description |
| --- | --- | --- |
| Issue Type | issueType | The type of issue detected. |
| Severity | severity | The severity of the issue (`Critical`, `High`, `Medium`, `Low`, or `Informational`). |
| Location | location | The URL where the issue is detected (for issues captured in DAST tests), the path to the file in which the issue is detected (for issues captured in SAST tests), or the name of the component in which the issue exists (for issues captured in SCA tests). |
| File Name | fileName | The name of the file in which the issue is detected, if available. |
| Tool Type | toolType | The type of test that detected the issue (`DAST`, `SAST`, or `SCA`). |
| Triage Status | triageStatus | The triage status selected when the issue was triaged most recently (`To Be Fixed`, `Dismissed (Intentional)`, `Dismissed (False Positive)`, `Dismissed (Other)`), or `Not Triaged`. |
| Fix-By | fixByDate | The issue's fix-by date, if available. |
| CVE | cve | The Common Vulnerabilities and Exposures (CVE®) code for the issue, if available. |
| BDSA | bdsa | The Black Duck® Security Advisory (BDSA) code for the issue, if available. |
| CWE | cwe | The Common Weakness Enumeration (CWE™) code for the issue, if available. |
| Application | application | The application in which the issue was detected. |
| Project | project | The project in which the issue was detected. |
| Branch | branch | The branch in which the SAST or SCA issue was detected. |
| Link | link | An absolute link to the issue's details in Polaris. |
