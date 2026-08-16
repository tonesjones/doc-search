---
title: "Operation: getSnapshotInformation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getsnapshotinformation.html"
content_id: "Z_wBBDyPfsPC4dv4UMdAGg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:56.467857+00:00"
---

# Operation: getSnapshotInformation

## Name

getSnapshotInformation

## Description

Retrieve information about a snapshot in a stream.

## Parameters

snapshotIds
:   **Type:** 
    snapshotIdDataObj

    Identifier for a snapshot.

    | Field name | Type | Description |
    | --- | --- | --- |
    | id | long | Numeric identifier for the snapshot. Required. |

## Output (Literal)

The output of this operation is the argument getSnapshotInformationResponse having
the structure defined by the following table.

| Name | Type |
| --- | --- |
| return | snapshotInfoDataObj |

## Remarks

To retrieve a snapshot ID, see getSnapshotForStream(). The ID is also available through the Coverity
Connect UI.
