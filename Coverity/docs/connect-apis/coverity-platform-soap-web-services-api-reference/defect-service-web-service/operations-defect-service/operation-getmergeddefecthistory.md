---
title: "Operation: getMergedDefectHistory"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getmergeddefecthistory.html"
content_id: "3C51Lk7uxzRiugRtud69LQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:16.144346+00:00"
---

# Operation: getMergedDefectHistory

## Name

getMergedDefectHistory

## Description

Retrieve a date and time stamped list of changes to attributes used to triage a
specified CID.

## Parameters

mergedDefectIdDataObj
:   **Type:** 
    mergedDefectIdDataObj

    Identifier for a software issue. You must pass a cid and/or mergeKey
    value.

    | Field name | Type | Description |
    | --- | --- | --- |
    | cid | long | CID. |
    | mergeKey | string | Numeric key for a CID. |

streamIds
:   **Type:** 
    streamIdDataObj

    Identifier for a stream.

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the stream. You can specify one or more instances of streamIdDataObj. See the example. |

## Output (literal)

The output of this operation is the argument getMergedDefectHistoryResponse having
the structure defined by the following table.

| Name | Type |
| --- | --- |
| return | defectChangeDataObj |

## Remarks
