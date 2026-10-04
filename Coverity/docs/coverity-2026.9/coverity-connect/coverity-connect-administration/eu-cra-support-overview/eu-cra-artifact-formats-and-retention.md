---
title: "EU-CRA artifact formats and retention"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/eu-cra-artifact-formats-and-retention.html"
content_id: "XBZYBVL8IrxTpf3ZXV8uEQ"
version: "2026.9"
section: "Coverity Connect"
scraped_at: "2026-10-04T23:33:15.206383+00:00"
---

# EU-CRA artifact formats and retention

Review the supported formats, storage locations, and retention behavior
for generated EU-CRA artifacts.

## Supported artifact formats

Coverity generates EU-CRA artifacts in the following formats:

Table 1. EU-CRA artifact formats

| Artifact | Format |
| --- | --- |
| EU-CRA report | ZIP archive containing PDF and HTML files |
| CSAF/VEX report | JSON artifact |

## Report storage

Generated reports are stored in the directory specified by the
`reports.base.path` property.

If `reports.base.path` is not configured,
reports are stored in the default reports directory under the
Coverity Connect installation path:

```
${ces.home}${file.separator}reports
```

## Artifact retention

Generated report files are retained according to a configurable
retention policy.

- Default retention period: 30 days
- Valid retention range: 1 through 9125 days
- Default report limit: 100 reports per user
- Valid report-count range: 1 through 200 reports per user

After a report file is removed, report metadata remains
available for audit and tracking purposes.

## Retention configuration properties

`reports.base.path`
:   Specifies the directory where reports are stored.
    The default value is
    `${ces.home}${file.separator}reports`.

`reports.retention.max.count`
:   Specifies the maximum number of reports retained per
    user. Valid values are 1 through 200. The default value
    is 100.

`reports.retention.max.days`
:   Specifies the maximum report age in days. Valid values
    are 1 through 9125. The default value is 30.

For production deployments, these properties can be overridden
in the `web.properties` file.

## Cleanup behavior

The system automatically removes reports when they exceed either
the configured report-count limit or the configured retention
period.

When a new report is generated after the configured report-count
limit is reached, the system deletes the oldest report for that
user to make room for the new report.

Note:
Reports are automatically removed when they exceed either the
maximum number of reports retained per user or the maximum
retention period, whichever limit is reached first.

## Audit and tracking

Generated report files are removed, but report metadata remains available.

Cleanup operations preserve report metadata while removing only
generated report files.
