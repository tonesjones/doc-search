---
title: "Operation: updateTriageForCIDsInTriageStore"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/operation-updatetriageforcidsintriagestore.html"
content_id: "GqsJ~meaJHx1KaNOeRWXaQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:25.973158+00:00"
---

# Operation: updateTriageForCIDsInTriageStore

## Name

updateTriageForCIDsInTriageStore

## Description

Update one or more attribute values for a CID in a specified triage store.

## Parameters

triageStore
:   **Type:** 
    triageStoreIdDataObj

    Identifier for a triage store.

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the triage store. |

mergedDefectIdDataObjs
:   **Type:** 
    mergedDefectIdDataObj

    Identifier for a software issue. A cid and/or mergeKey is required. Multiple specifications
    are allowed, up to a limit of 100.

    | Field name | Type | Description |
    | --- | --- | --- |
    | cid | long | CID. |
    | mergeKey | string | Numeric key for a CID. |

defectState
:   **Type:** 
    defectStateSpecDataObj

    An triage attribute name/value pair.

    | Field name | Type | Description |
    | --- | --- | --- |
    | defectStateAttributeValues | defectStateAttributeValueDataObj | Attribute name/value pair. One or more pairs required. |
