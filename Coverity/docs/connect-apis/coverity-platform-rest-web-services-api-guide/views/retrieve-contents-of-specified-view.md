---
title: "Retrieve contents of specified view"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-contents-of-specified-view.html"
content_id: "hWfmtIfhaCdtfeeiVbu4yQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:22.794836+00:00"
---

# Retrieve contents of specified view

Example GET request to retrieve the contents of the specified view.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/views/viewContents/10005?locale\
=en_us&projectId=10007&offset=10&sortKey=codeLineCount&sortOrder=desc&rowCount=5" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "offset": 10,
  "totalRows": 112,
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
  "rows": [
    [
      {
        "key": "file",
        "value": "/usr/include/c++/4.6/x86_64-linux-gnu/bits/gthr-default.h"
      },
      {
        "key": "component",
        "value": "Other"
      },
      {
        "key": "newCount",
        "value": "0"
      },
      {
        "key": "outstandingCount",
        "value": "0"
      },
      {
        "key": "defectDensity",
        "value": "0.0"
      },
      {
        "key": "codeLineCount",
        "value": "637"
      }
    ],
    [
      {
        "key": "file",
        "value": "/usr/include/pthread.h"
      },
      {
        "key": "component",
        "value": "Other"
      },
      {
        "key": "newCount",
        "value": "0"
      },
      {
        "key": "outstandingCount",
        "value": "0"
      },
      {
        "key": "defectDensity",
        "value": "0.0"
      },
      {
        "key": "codeLineCount",
        "value": "634"
      }
    ],
    [
      {
        "key": "file",
        "value": "/usr/include/x86_64-linux-gnu/bits/confname.h"
      },
      {
        "key": "component",
        "value": "Other"
      },
      {
        "key": "newCount",
        "value": "0"
      },
      {
        "key": "outstandingCount",
        "value": "0"
      },
      {
        "key": "defectDensity",
        "value": "0.0"
      },
      {
        "key": "codeLineCount",
        "value": "616"
      }
    ],
    [
      {
        "key": "file",
        "value": "/usr/include/stdlib.h"
      },
      {
        "key": "component",
        "value": "Other"
      },
      {
        "key": "newCount",
        "value": "0"
      },
      {
        "key": "outstandingCount",
        "value": "0"
      },
      {
        "key": "defectDensity",
        "value": "0.0"
      },
      {
        "key": "codeLineCount",
        "value": "564"
      }
    ],
    [
      {
        "key": "file",
        "value": "/usr/include/unistd.h"
      },
      {
        "key": "component",
        "value": "Other"
      },
      {
        "key": "newCount",
        "value": "0"
      },
      {
        "key": "outstandingCount",
        "value": "0"
      },
      {
        "key": "defectDensity",
        "value": "0.0"
      },
      {
        "key": "codeLineCount",
        "value": "498"
      }
    ]
  ],
  "code": null,
  "message": null
}
```
