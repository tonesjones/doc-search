---
title: "iac-scan"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/iac-scan.html"
content_id: "dc8EzBW_MMsBsg4uwPtY~g"
version: "12.0.0"
section: "Detect Properties"
scraped_at: "2026-09-07T21:16:32.526043+00:00"
---

# iac-scan

## IaC Scan Arguments

```
--detect.iac.scan.arguments
```

A space-separated list of additional arguments to use when running the IaC Scanner.

| Details |  |
| --- | --- |
| Added | 7.14.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `--follow-symlinks` |

## IaC Scanner Local Path

```
--detect.iac.scanner.local.path
```

Use this property to specify the path to a local IaC Scanner.

If you are running in an Air Gap environment you may need to download the IaC Scanner(Sigma) binary from Artifactory. See the [Download Locations page.](https://docs%2Eblackduck%2Ecom/r/detect/latest/black%2Dduck%2Ddetect/downloading%2Dand%2Dinstalling%2Ddetect%2Ehtml)

| Details |  |
| --- | --- |
| Added | 7.14.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## IaC Scan Target Paths

```
--detect.iac.scan.paths
```

A comma-separated list of paths to perform IaC scans on.

If this property is set, an IaC scan will be performed on each of the paths provided. If this property is not set, but IaC Scanning is enabled via detect.tools (explicitly, not detect.tools=ALL), the IaC scan target path is the source path (see property detect.source.path).

| Details |  |
| --- | --- |
| Added | 7.14.0 |
| Type | Path List |
| Default Value |  |
| Comma Separated | Yes |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `/user/source/target1,/user/source/target2` |
