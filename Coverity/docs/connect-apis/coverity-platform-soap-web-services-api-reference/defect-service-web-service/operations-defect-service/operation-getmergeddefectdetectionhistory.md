---
title: "Operation: getMergedDefectDetectionHistory"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getmergeddefectdetectionhistory.html"
content_id: "K_BgSNLoSbj_J~2STQ~k~w"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:15.486876+00:00"
---

# Operation: getMergedDefectDetectionHistory

## Name

getMergedDefectDetectionHistory

## Description

Retrieves detection history for a software issue. The return data is similar to the
Detection History information in the Coverity Connect UI.

## Parameters

mergedDefectIdDataObj
:   **Type:** 
    mergedDefectIdDataObj

    The cid and/or merge key for a software issue. At least one of them must
    be provided.

    | Field name | Type | Description |
    | --- | --- | --- |
    | cid | long | CID. |
    | mergeKey | string | Numeric key for a CID. |

streamIds
:   **Type:** 
    streamIdDataObj

    Name of a stream in which the software issue occurs.

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the stream. You can specify one or more instances of streamIdDataObj. See the example. |

## Output (literal)

The output of this operation is the argument getMergedDefectDetectionHistoryResponse
having the structure defined by the following table.

| Name | Type |
| --- | --- |
| return | defectDetectionHistoryDataObj |
