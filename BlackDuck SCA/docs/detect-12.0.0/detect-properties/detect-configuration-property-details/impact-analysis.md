---
title: "impact-analysis"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/impact-analysis.html"
content_id: "YcHr7WGc2XchtmTqWM4pGg"
version: "12.0.0"
section: "Detect Properties"
scraped_at: "2026-09-07T21:16:33.275101+00:00"
---

# impact-analysis

## Impact Analysis Output Directory

```
--detect.impact.analysis.output.path
```

The path to the output directory for Impact Analysis reports.

If not set, the Impact Analysis reports are placed in a 'impact-analysis' subdirectory of the output directory.

| Details |  |
| --- | --- |
| Added | 6.5.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Vulnerability Impact Analysis Enabled

```
--detect.impact.analysis.enabled=false
```

If set to true, Detect will attempt to look for *.class files and generate a Vulnerability Impact Analysis Report for upload to Black Duck SCA.

| Details |  |
| --- | --- |
| Added | 6.5.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
