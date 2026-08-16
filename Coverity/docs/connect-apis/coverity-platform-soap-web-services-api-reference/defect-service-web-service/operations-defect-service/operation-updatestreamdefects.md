---
title: "Operation: updateStreamDefects"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-updatestreamdefects.html"
content_id: "PgnZmAfDLYeYFXNF_nCzWQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:21.666744+00:00"
---

# Operation: updateStreamDefects

## Name

updateStreamDefects

## Description

Update the one or more attribute values for *all* instances of a CID found in a
given stream. Note that this update will apply to all instances of the CID in all
streams that share the same triage store.

## Parameters

streamDefectIds
:   **Type:** 
    streamDefectIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | defectTriageId | long | Internal value for the last known triage ID. This ID changes when developers triage the issue that is associated with the *id*. |
    | defectTriageVerNum | int | Internal value for the last known triage version. This number changes when developers triage the issue that is associated with the *id*. |
    | id | long | Internal identifier for the software issue within the context of the stream. |
    | verNum | int | Version number associated with the *id*. |

defectStateSpec
:   **Type:** 
    defectStateSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | defectStateAttributeValues | defectStateAttributeValueDataObj | Attribute name/value pair. One or more pairs required. |

## Remarks

Limit of 500 streamDefectIds. To retrieve a list of *streamDefectIdDataObj*
values for a CID, see getStreamDefects().
