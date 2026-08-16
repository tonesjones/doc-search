---
title: "Example workflow"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example-workflow.html"
content_id: "rgEjZzKJnQ_nHjeFrfcCpQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:32.932431+00:00"
---

# Example workflow

**Task**

Retrieve, in Japanese locale, all of the issues in snapshot `10011` in
project `testcpp` whose **Impact** is `High` and whose
**Category** is NOT `Memory - illegal accesses`. Return the
**CID**, **Category**, and **Impact** columns.

**One-time setup:**

1. Call `GET /api/v2/issues/columns` to retrieve the column keys for the
   **CID**, **Category**, and **Impact** columns.

   In the response, find
   the `columnKey` values that correspond to the column
   `name` values `CID`,
   `Category`, and `Impact`. (The
   `columnKey` values are `cid`,
   `displayCategory`, and
   `displayImpact`.)
2. Call `GET /api/v2/locales` to retrieve the code for the Japanese
   locale. The value returned is `ja_JP`.

**For each query, run this loop:**

1. Set `$offset = 0`.
2. Call `POST
   /api/v2/issues/search?includeColumnLabels=true&locale=ja_JP&offset=$offset`
   (note that `offset` begins at `0` and increments on
   each iteration). Use this request body:

   ```
   {
     "filters":[
       {
         "columnKey":"project",
         "matchMode":"oneOrMoreMatch",
         "matchers":[
           {
             "class":"Project",
             "name":"testcpp",
             "type":"nameMatcher"
           }
         ]
       },
       {
         "columnKey":"displayImpact",
         "matchMode":"oneOrMoreMatch",
         "matchers":[
           {
             "key":"High",
             "type":"keyMatcher"
           }
         ]
       },
       {
         "columnKey":"displayCategory",
         "matchMode":"noneMatch",
         "matchers":[
           {
             "key":"Memory - illegal accesses",
             "type":"keyMatcher"
           }
         ]
       }
     ],
     "columns":[
       "cid",
       "displayImpact",
       "displayCategory"
     ],
     "snapshotScope":{
       "show":{
         "scope":"10011",
         "includeOutdated":false
       }
     }
   }
   ```
3. Receive the response:

   ```
   {
     "offset":0,
     "totalRows":1,
     "columns":[
       "cid",
       "displayImpact",
       "displayCategory"
     ],
     "rows":[
       [
         {
           "key":"cid",
           "value":"10030"
         },
         {
           "key":"displayImpact",
           "value":"高"
         },
         {
           "key":"displayCategory",
           "value":"変数の未初期化"
         }
       ]
     ]
   }
   ```
4. If `totalRows <= 200`, break out of this loop. (We use
   `200` here because `rowCount` is at its default
   value of `200`.)
5. Set `offset += 200`.
6. Go to step 2.
