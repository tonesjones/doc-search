---
title: "Operation: deleteTriageStore"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-deletetriagestore.html"
content_id: "JL2oYwM3o9t8gulvvd1j5Q"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:35.862734+00:00"
---

# Operation: deleteTriageStore

## Name

deleteTriageStore

## Description

Delete a triage store
to which no streams are
associated.

## Parameters

triageStoreId
:   **Type:** 
    triageStoreIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the triage store. |

## Remarks

If any streams are associated with the triage store, you must dissociate them from
the before you can successfully delete the store. See updateTriageStore().
