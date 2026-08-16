---
title: "Retrieve all column keys for issues"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-column-keys-for-issues.html"
content_id: "TegXa475flq8mPw8kp9kaQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:02.719324+00:00"
---

# Retrieve all column keys for issues

Example GET request to retrieve all column keys for the view type **Issues: By
Snapshot**.

**cURL request**

```
curl --location \
--request GET \
"http://my_connect_host:8080/api/v2/issues/columns?locale=en_us&queryType=bySnapshot" \
--user  my_username:my_password \
--header 'Accept: application/json'
```

**Response body**

```
[
  {
    "columnKey": "cid",
    "name": "CID"
  },
  {
    "columnKey": "checker",
    "name": "Checker"
  },
  {
    "columnKey": "displayImpact",
    "name": "Impact"
  },
  {
    "columnKey": "displayCategory",
    "name": "Category"
  },
  {
    "columnKey": "displayType",
    "name": "Type"
  },
  {
    "columnKey": "cwe",
    "name": "CWE"
  },
  {
    "columnKey": "displayIssueKind",
    "name": "Issue Kind"
  },
  {
    "columnKey": "status",
    "name": "Status"
  },
  {
    "columnKey": "firstDetected",
    "name": "First Detected"
  },
  {
    "columnKey": "owner",
    "name": "Owner"
  },
  {
    "columnKey": "ownerFullName",
    "name": "Owner Name"
  },
  {
    "columnKey": "externalReference",
    "name": "External Reference"
  },
  {
    "columnKey": "classification",
    "name": "Classification"
  },
  {
    "columnKey": "severity",
    "name": "Severity"
  },
  {
    "columnKey": "action",
    "name": "Action"
  },
  {
    "columnKey": "fixTarget",
    "name": "Fix Target"
  },
  {
    "columnKey": "legacy",
    "name": "Legacy"
  },
  {
    "columnKey": "displayComponent",
    "name": "Component"
  },
  {
    "columnKey": "displayFile",
    "name": "File"
  },
  {
    "columnKey": "displayFunction",
    "name": "Function"
  },
  {
    "columnKey": "functionMergeName",
    "name": "Function Merge Name"
  },
  {
    "columnKey": "mergeExtra",
    "name": "Merge Extra"
  },
  {
    "columnKey": "mergeKey",
    "name": "Merge Key"
  },
  {
    "columnKey": "fileLanguage",
    "name": "Language"
  },
  {
    "columnKey": "ruleStrength",
    "name": "MISRA Category"
  },
  {
    "columnKey": "lastTriaged",
    "name": "Last Triaged"
  },
  {
    "columnKey": "lastTriagedUser",
    "name": "Last Triaged User"
  },
  {
    "columnKey": "occurrenceCount",
    "name": "Count"
  },
  {
    "columnKey": "displayComparison",
    "name": "Comparison"
  },
  {
    "columnKey": "firstSnapshotDate",
    "name": "First Snapshot Date"
  },
  {
    "columnKey": "firstSnapshotId",
    "name": "First Snapshot"
  },
  {
    "columnKey": "firstSnapshotVersion",
    "name": "First Snapshot Version"
  },
  {
    "columnKey": "firstSnapshotTarget",
    "name": "First Snapshot Target"
  },
  {
    "columnKey": "firstSnapshotDescription",
    "name": "First Snapshot Description"
  },
  {
    "columnKey": "firstSnapshotStream",
    "name": "First Snapshot Stream"
  },
  {
    "columnKey": "lastDetected",
    "name": "Last Snapshot Date"
  },
  {
    "columnKey": "lastDetectedId",
    "name": "Last Snapshot"
  },
  {
    "columnKey": "lastDetectedVersion",
    "name": "Last Snapshot Version"
  },
  {
    "columnKey": "lastDetectedTarget",
    "name": "Last Snapshot Target"
  },
  {
    "columnKey": "lastDetectedDescription",
    "name": "Last Snapshot Description"
  },
  {
    "columnKey": "lastDetectedStream",
    "name": "Last Snapshot Stream"
  },
  {
    "columnKey": "score",
    "name": "Score"
  },
  {
    "columnKey": "lineNumber",
    "name": "Line Number"
  },
  {
    "columnKey": "lastTriageComment",
    "name": "Last Triage Comment"
  },
  {
    "columnKey": "column_custom_test",
    "name": "test"
  },
  {
    "columnKey": "column_standard_PCI DSS 2018",
    "name": "Standard: PCI DSS 2018"
  },
  {
    "columnKey": "column_standard_AUTOSAR C++14",
    "name": "Standard: AUTOSAR C++14"
  },
  {
    "columnKey": "column_standard_OWASP Web Top Ten 2017",
    "name": "Standard: OWASP Web Top Ten 2017"
  },
  {
    "columnKey": "column_standard_DISA-STIG V4R10",
    "name": "Standard: DISA-STIG V4R10"
  },
  {
    "columnKey": "column_standard_DISA-STIG V4R3",
    "name": "Standard: DISA-STIG V4R3"
  },
  {
    "columnKey": "column_standard_CERT C",
    "name": "Standard: CERT C"
  },
  {
    "columnKey": "column_standard_DISA-STIG V4R10 Severity",
    "name": "Standard: DISA-STIG V4R10 Severity"
  },
  {
    "columnKey": "column_standard_DISA-STIG V4R3 Severity",
    "name": "Standard: DISA-STIG V4R3 Severity"
  },
  {
    "columnKey": "column_standard_CERT C++",
    "name": "Standard: CERT C++"
  },
  {
    "columnKey": "column_standard_OWASP Mobile Top Ten 2016",
    "name": "Standard: OWASP Mobile Top Ten 2016"
  },
  {
    "columnKey": "column_standard_ISO TS17961 2016",
    "name": "Standard: ISO TS17961 2016"
  },
  {
    "columnKey": "project",
    "name": "Project"
  }
]
```
