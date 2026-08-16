---
title: "Retrieve triage history for multiple issues"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-triage-history-for-multiple-issues.html"
content_id: "N5xyY4CtXJKxc0BjpDtM4w"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:08.131604+00:00"
---

# Retrieve triage history for multiple issues

Example POST request to retrieve the triage history for multiple issues.

**cURL request**

```
curl -X 'POST' \
  'http://localhost:8080/api/v2/issues/triageHistory/search?locale=en_us' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "mergedDefectInfo": [
    {
      "cid": 10014,
      "mergeKey": "bazfn0e5d26443ee70a47401a290edf4a982a10021UwF"
    }
  ],
  "streamNames": [
    "my_stream",
    "my_stream1"
  ],
  "defectStateStartDate": "2016-07-17T11:46:38-07:00",
  "defectStateEndDate": "2016-07-17T11:46:38-07:00"
}'
```

**Response body**

```
  {
  "triageHistories": [
    {
      "cid": 10014,
      "currentIssueStateAttributeValues": [
        {
          "attributeName": "Action",
          "attributeValue": "Fix Required"
        }
      ],
      "streamName": "myStreamName",
      "streamDefectAndDefectTriageId": {
        "id": 20045,
        "defectTriageId": 10024,
        "defectTriageVerNum": 2,
        "verNum": 2
      },
      "triageHistories": [
        {
          "issueStateAttributeValues": [
            {
              "attributeName": "Action",
              "attributeValue": "Fix Required"
            }
          ],
          "dateCreated": "string",
          "userCreated": "foo"
        }
      ]
    }
  ]
}
```
