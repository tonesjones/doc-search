---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/examples.html"
content_id: "RzdvV~UQg2B5IK5EJ6xw~g"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:55.067292+00:00"
---

# Examples

**Example request for JSON output**

`curl --user admin:password
"localhost:8080/api/viewContents/issues/v1/Outstanding%20Defects?projectId=sample-app&rowCount=25"`

**Example request for CSV file**

`curl --header "Accept: text/csv" --user admin:password
"localhost:8080/api/viewContents/issues/v1/Outstanding%20Defects?projectId=sample-app&rowCount=25"
> outputFile.csv`

**Example JSON response body**

```
{
  "viewContentsV1": { 
    "offset": 0, 
    "totalRows": 2, 
    "columns": [ 
      { 
        "name": "cid", 
        "label": "CID" 
      }, 
      { 
        "name": "displayType", 
        "label": "Type" 
      }, 
      { 
        "name": "displayImpact", 
        "label": "Impact" 
      }, 
      { 
        "name": "status", 
        "label": "Status" 
      }, 
      { 
        "name": "firstDetected", 
        "label": "First Detected" 
      }, 
      { 
        "name": "owner", 
        "label": "Owner" 
      }, 
      { 
        "name": "classification", 
        "label": "Classification" 
      }, 
      { 
        "name": "severity", 
        "label": "Severity" 
      } 
    ], 
    "rows": [ 
      { 
        "cid": 12345, 
        "displayType": "Insufficient function coverage", 
        "displayImpact": "Low", 
        "status": "New", 
        "firstDetected": "05/17/14", 
        "owner": "Unassigned", 
        "classification": "Unclassified", 
        "severity": "Unspecified" 
      }, 
      { 
        "cid": 54321, 
        "displayType": "Insufficient function coverage", 
        "displayImpact": "Low", 
        "status": "New", 
        "firstDetected": "05/17/14", 
        "owner": "Unassigned", 
        "classification": "Unclassified", 
        "severity": "Unspecified" 
      }
    ]
  }
}
```
