---
title: "report"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/report.html"
content_id: "0bjjNXEpL~vZVk5qANUj6w"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:28.735990+00:00"
---

# report

## Generate Notices Report

```
--detect.notices.report=false
```

When set to true, a Black Duck SCA notices report in text form will be created in your source directory.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Generate Risk Report (JSON)

```
--detect.risk.report.json=false
```

When set to true, a Black Duck SCA risk report in JSON form will be created.

| Details |  |
| --- | --- |
| Added | 10.6.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Generate Risk Report (PDF)

```
--detect.risk.report.pdf=false
```

When set to true, a Black Duck SCA risk report in PDF form will be created.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Boolean |
| Default Value | false |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Notices Report Path

```
--detect.notices.report.path
```

The output directory for notices report. Default is the source directory.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Risk Report (JSON) Output Path

```
--detect.risk.report.json.path
```

The output directory for risk report in JSON. Default is the source directory.

| Details |  |
| --- | --- |
| Added | 10.6.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Risk Report (PDF) Output Path

```
--detect.risk.report.pdf.path
```

The output directory for risk report in PDF. Default is the source directory.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
