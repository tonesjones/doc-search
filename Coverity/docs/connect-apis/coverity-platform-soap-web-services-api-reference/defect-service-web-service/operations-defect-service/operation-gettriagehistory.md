---
title: "Operation: getTriageHistory"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-gettriagehistory.html"
content_id: "3_ZPlmP9emkStRAC~rNsLA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:20.338218+00:00"
---

# Operation: getTriageHistory

## Name

getTriageHistory

## Description

Retrieve the triage history for a software issue.

## Parameters

mergedDefectIdDataObj
:   **Type:** 
    mergedDefectIdDataObj

    Specifies a CID and/or merge key for a software issue.

    | Field name | Type | Description |
    | --- | --- | --- |
    | cid | long | CID. |
    | mergeKey | string | Numeric key for a CID. |

triageStoreIds
:   **Type:** 
    triageStoreIdDataObj

    Identifier for a triage store.

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the triage store. |

## Output (literal)

The output of this operation is the argument getTriageHistoryResponse having the
structure defined by the following table.

| Name | Type |
| --- | --- |
| return | triageHistoryDataObj |
