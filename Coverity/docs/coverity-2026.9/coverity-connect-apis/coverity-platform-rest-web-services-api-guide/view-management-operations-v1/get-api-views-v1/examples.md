---
title: "Examples"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/examples.html"
content_id: "nI41tWZ_X8Yvoos4OgYohQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:37:12.818923+00:00"
---

# Examples

**Example request**

`curl --user admin:password "localhost:8080/api/views/v1"`

**Example JSON response body**

```
{
  "views": [ 
    { 
      "id": 12345,
      "type": "files", 
      "name": "All Files", 
      "groupBy": false, 
      "columns": [ 
        { 
          "name": "cid", 
          "label": "CID" 
        }, 
        { 
          "name": "displayType", 
          "label": "Type" 
        } 
      ] 
    }, 
    { 
      "id": 54321, 
      "type": "issuesByProject", 
      "name": "All In Project", 
      "groupBy": false,
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
          "name": "firstDetected", 
          "label": "First Detected" 
        }, 
        { 
          "name": "owner", 
          "label": "Owner" 
        }
      ] 
    }
  ]
}
```
