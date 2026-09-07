---
title: "debug"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/debug.html"
content_id: "yOi2LqR7ggkfaRnWP8P8vw"
version: "12.0.0"
section: "Detect Properties"
scraped_at: "2026-09-07T21:16:28.625405+00:00"
---

# debug

## Diagnostic Archive Output Path

```
--detect.diagnostic.archive.path
```

Custom output path for diagnostic archive. A file named detect-run-.zip will be created under the specified path. An original copy of the diagnostics archive remains in the runs directory as a backup.

See the following for more [Diagnostic Mode information.](https://docs/.blackduck/.com/r/detect/latest/black%2Dduck%2Ddetect/detect%2Ddiagnostic%2Dmode%2Ehtml%5C)

| Details |  |
| --- | --- |
| Added | 12.0.0 |
| Type | String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

### Diagnostic Mode

```
--detect.diagnostic=false
```

When enabled, diagnostic mode collects files valuable for troubleshooting (logs, BDIO file, extraction files, reports, etc.), writes them to a zip file, and logs the path to the zip file.

See the following for more [Diagnostic Mode information.](https://docs%2Eblackduck%2Ecom/r/detect/latest/black%2Dduck%2Ddetect/detect%2Ddiagnostic%2Dmode%2Ehtml)

| Details |  |
| --- | --- |
| Added | 6.5.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
