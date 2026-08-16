---
title: "Retrieve all views accessible to the current user"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-views-accessible-to-the-current-user.html"
content_id: "MqESGMpJsFlMvtknL8Ks3A"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:22.157079+00:00"
---

# Retrieve all views accessible to the current user

Example GET request to retrieve all views accessible to the current user.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/views/user" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "views": [
    {
      "id": 10024,
      "name": "All Hierarchies",
      "type": "hierarchies",
      "columns": [
        {
          "columnKey": "hierarchyName",
          "name": "Hierarchy"
        },
        {
          "columnKey": "hierarchyDescription",
          "name": "Description"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10004,
      "name": "All In Project",
      "type": "snapshots",
      "columns": [
        {
          "columnKey": "snapshot",
          "name": "Snapshot ID"
        },
        {
          "columnKey": "streamName",
          "name": "Stream"
        },
        {
          "columnKey": "snapshotDate",
          "name": "Date"
        },
        {
          "columnKey": "snapshotDescription",
          "name": "Description"
        },
        {
          "columnKey": "totalDetected",
          "name": "Total Detected"
        },
        {
          "columnKey": "newlyDetectedDefectCount",
          "name": "Newly Detected"
        },
        {
          "columnKey": "newlyEliminatedDefectCount",
          "name": "Newly Eliminated"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10016,
      "name": "All In Project",
      "type": "issuesByProject",
      "columns": [
        {
          "columnKey": "cid",
          "name": "CID"
        },
        {
          "columnKey": "displayType",
          "name": "Type"
        },
        {
          "columnKey": "displayImpact",
          "name": "Impact"
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
          "columnKey": "displayComponent",
          "name": "Component"
        },
        {
          "columnKey": "displayCategory",
          "name": "Category"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10023,
      "name": "All In Project",
      "type": "checkers",
      "columns": [
        {
          "columnKey": "checker",
          "name": "Checker"
        },
        {
          "columnKey": "newCount",
          "name": "New"
        },
        {
          "columnKey": "outstandingCount",
          "name": "Outstanding"
        },
        {
          "columnKey": "totalCount",
          "name": "Total"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10022,
      "name": "All In Project",
      "type": "owners",
      "columns": [
        {
          "columnKey": "owner",
          "name": "Owner"
        },
        {
          "columnKey": "newCount",
          "name": "New"
        },
        {
          "columnKey": "outstandingCount",
          "name": "Outstanding"
        },
        {
          "columnKey": "totalCount",
          "name": "Total"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10018,
      "name": "All In Project",
      "type": "components",
      "columns": [
        {
          "columnKey": "component",
          "name": "Component"
        },
        {
          "columnKey": "newCount",
          "name": "New"
        },
        {
          "columnKey": "outstandingCount",
          "name": "Outstanding"
        },
        {
          "columnKey": "totalCount",
          "name": "Total"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10017,
      "name": "All Projects",
      "type": "projects",
      "columns": [
        {
          "columnKey": "project",
          "name": "Project"
        },
        {
          "columnKey": "projectDescription",
          "name": "Description"
        },
        {
          "columnKey": "lastSnapshotDate",
          "name": "Last Commit"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10001,
      "name": "All Tests",
      "type": "test",
      "columns": [
        {
          "columnKey": "testName",
          "name": "Name"
        },
        {
          "columnKey": "testState",
          "name": "State"
        },
        {
          "columnKey": "lastRun",
          "name": "Last Run"
        },
        {
          "columnKey": "lastSuccess",
          "name": "Last Success"
        },
        {
          "columnKey": "lastFailure",
          "name": "Last Failure"
        },
        {
          "columnKey": "duration",
          "name": "Duration(ms)"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10002,
      "name": "Currently Failing",
      "type": "test",
      "columns": [
        {
          "columnKey": "testName",
          "name": "Name"
        },
        {
          "columnKey": "testState",
          "name": "State"
        },
        {
          "columnKey": "lastRun",
          "name": "Last Run"
        },
        {
          "columnKey": "lastSuccess",
          "name": "Last Success"
        },
        {
          "columnKey": "lastFailure",
          "name": "Last Failure"
        },
        {
          "columnKey": "duration",
          "name": "Duration(ms)"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10008,
      "name": "High CCM (>15)",
      "type": "functions",
      "columns": [
        {
          "columnKey": "function",
          "name": "Function"
        },
        {
          "columnKey": "fileName",
          "name": "File"
        },
        {
          "columnKey": "component",
          "name": "Component"
        },
        {
          "columnKey": "newCount",
          "name": "New"
        },
        {
          "columnKey": "outstandingCount",
          "name": "Outstanding"
        },
        {
          "columnKey": "lineCount",
          "name": "Line Count"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10011,
      "name": "High Impact Outstanding",
      "type": "issues",
      "columns": [
        {
          "columnKey": "cid",
          "name": "CID"
        },
        {
          "columnKey": "displayType",
          "name": "Type"
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
          "columnKey": "displayComponent",
          "name": "Component"
        },
        {
          "columnKey": "displayCategory",
          "name": "Category"
        },
        {
          "columnKey": "displayFile",
          "name": "File"
        },
        {
          "columnKey": "displayFunction",
          "name": "Function"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10021,
      "name": "High Issue Density (>1)",
      "type": "components",
      "columns": [
        {
          "columnKey": "component",
          "name": "Component"
        },
        {
          "columnKey": "newCount",
          "name": "New"
        },
        {
          "columnKey": "outstandingCount",
          "name": "Outstanding"
        },
        {
          "columnKey": "totalCount",
          "name": "Total"
        },
        {
          "columnKey": "defectDensity",
          "name": "Issue Density"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10005,
      "name": "In Latest Snapshot",
      "type": "files",
      "columns": [
        {
          "columnKey": "file",
          "name": "File"
        },
        {
          "columnKey": "component",
          "name": "Component"
        },
        {
          "columnKey": "newCount",
          "name": "New"
        },
        {
          "columnKey": "outstandingCount",
          "name": "Outstanding"
        },
        {
          "columnKey": "defectDensity",
          "name": "Issue Density"
        },
        {
          "columnKey": "codeLineCount",
          "name": "Code Lines (LOC)"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10007,
      "name": "In Latest Snapshot",
      "type": "functions",
      "columns": [
        {
          "columnKey": "function",
          "name": "Function"
        },
        {
          "columnKey": "fileName",
          "name": "File"
        },
        {
          "columnKey": "component",
          "name": "Component"
        },
        {
          "columnKey": "newCount",
          "name": "New"
        },
        {
          "columnKey": "outstandingCount",
          "name": "Outstanding"
        },
        {
          "columnKey": "lineCount",
          "name": "Line Count"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10015,
      "name": "My Outstanding",
      "type": "issues",
      "columns": [
        {
          "columnKey": "cid",
          "name": "CID"
        },
        {
          "columnKey": "displayType",
          "name": "Type"
        },
        {
          "columnKey": "displayImpact",
          "name": "Impact"
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
          "columnKey": "displayComponent",
          "name": "Component"
        },
        {
          "columnKey": "displayCategory",
          "name": "Category"
        },
        {
          "columnKey": "displayFile",
          "name": "File"
        },
        {
          "columnKey": "displayFunction",
          "name": "Function"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10012,
      "name": "Outstanding Issues",
      "type": "issues",
      "columns": [
        {
          "columnKey": "cid",
          "name": "CID"
        },
        {
          "columnKey": "displayType",
          "name": "Type"
        },
        {
          "columnKey": "displayImpact",
          "name": "Impact"
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
          "columnKey": "displayComponent",
          "name": "Component"
        },
        {
          "columnKey": "displayCategory",
          "name": "Category"
        },
        {
          "columnKey": "displayFile",
          "name": "File"
        },
        {
          "columnKey": "displayFunction",
          "name": "Function"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10014,
      "name": "Outstanding Test Rules Violations",
      "type": "issues",
      "columns": [
        {
          "columnKey": "cid",
          "name": "CID"
        },
        {
          "columnKey": "displayType",
          "name": "Type"
        },
        {
          "columnKey": "displayImpact",
          "name": "Impact"
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
          "columnKey": "displayComponent",
          "name": "Component"
        },
        {
          "columnKey": "displayCategory",
          "name": "Category"
        },
        {
          "columnKey": "displayFile",
          "name": "File"
        },
        {
          "columnKey": "displayFunction",
          "name": "Function"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10010,
      "name": "Outstanding Untriaged",
      "type": "issues",
      "columns": [
        {
          "columnKey": "cid",
          "name": "CID"
        },
        {
          "columnKey": "displayType",
          "name": "Type"
        },
        {
          "columnKey": "displayImpact",
          "name": "Impact"
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
          "columnKey": "displayComponent",
          "name": "Component"
        },
        {
          "columnKey": "displayCategory",
          "name": "Category"
        },
        {
          "columnKey": "displayFile",
          "name": "File"
        },
        {
          "columnKey": "displayFunction",
          "name": "Function"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10003,
      "name": "Project Lifetime",
      "type": "trends",
      "columns": [
        {
          "columnKey": "dateOfData",
          "name": "Date"
        },
        {
          "columnKey": "newCount",
          "name": "New"
        },
        {
          "columnKey": "outstandingCount",
          "name": "Outstanding"
        },
        {
          "columnKey": "resolvedCount",
          "name": "Resolved"
        },
        {
          "columnKey": "totalCount",
          "name": "Total"
        },
        {
          "columnKey": "defectDensity",
          "name": "Issue Density"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10009,
      "name": "Uncovered By Tests",
      "type": "functions",
      "columns": [
        {
          "columnKey": "function",
          "name": "Function"
        },
        {
          "columnKey": "fileName",
          "name": "File"
        },
        {
          "columnKey": "component",
          "name": "Component"
        },
        {
          "columnKey": "newCount",
          "name": "New"
        },
        {
          "columnKey": "outstandingCount",
          "name": "Outstanding"
        },
        {
          "columnKey": "lineCount",
          "name": "Line Count"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10006,
      "name": "Uncovered By Tests",
      "type": "files",
      "columns": [
        {
          "columnKey": "file",
          "name": "File"
        },
        {
          "columnKey": "component",
          "name": "Component"
        },
        {
          "columnKey": "newCount",
          "name": "New"
        },
        {
          "columnKey": "outstandingCount",
          "name": "Outstanding"
        },
        {
          "columnKey": "defectDensity",
          "name": "Issue Density"
        },
        {
          "columnKey": "codeLineCount",
          "name": "Code Lines (LOC)"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10020,
      "name": "With Outstanding Issues",
      "type": "components",
      "columns": [
        {
          "columnKey": "component",
          "name": "Component"
        },
        {
          "columnKey": "newCount",
          "name": "New"
        },
        {
          "columnKey": "outstandingCount",
          "name": "Outstanding"
        },
        {
          "columnKey": "totalCount",
          "name": "Total"
        }
      ],
      "groupBy": false
    },
    {
      "id": 10019,
      "name": "With Untriaged Issues",
      "type": "components",
      "columns": [
        {
          "columnKey": "component",
          "name": "Component"
        },
        {
          "columnKey": "newCount",
          "name": "New"
        },
        {
          "columnKey": "outstandingCount",
          "name": "Outstanding"
        },
        {
          "columnKey": "totalCount",
          "name": "Total"
        }
      ],
      "groupBy": false
    }
  ],
  "code": null,
  "message": null
}
```
