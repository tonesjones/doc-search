---
title: "Operation: getDeleteSnapshotJobInfo"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getdeletesnapshotjobinfo.html"
content_id: "ks5ShjY~xE5Xc4v56dhBeA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:46.608423+00:00"
---

# Operation: getDeleteSnapshotJobInfo

## Name

getDeleteSnapshotJobInfo

## Description

Find out whether a snapshot deletion process succeeded.

## Parameters

snapshotId
:   **Type:** 
    snapshotIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | id | long | Numeric identifier for the snapshot. Required. |

## Output (Literal)

The output of this operation is the argument getDeleteSnapshotJobInfoResponse having
the structure defined by the following table.

| Name | Type |
| --- | --- |
| return | deleteSnapshotJobInfoDataObj |

## Remarks

You need to call this operation after calling deleteSnapshot().
