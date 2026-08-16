---
title: "Operation: deleteSnapshot"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-deletesnapshot.html"
content_id: "YYK3siIWazsBrSUf9RgoqQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:34.577855+00:00"
---

# Operation: deleteSnapshot

## Name

deleteSnapshot

## Description

Delete a snapshot.

## Parameters

snapshotId
:   **Type:** 
    snapshotIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | id | long | Numeric identifier for the snapshot. Required. |

## Remarks

You need to check on the status of the deletion after making the request. See getDeleteSnapshotJobInfo().

This operation is asynchronous. The snapshot deletion process might take some time
for a large snapshot, but the Web Service invocation returns quickly, while the
snapshot deletion process continues in the background. If you want to script
multiple snapshot deletions from the same stream, keep in mind that while a snapshot
is being deleted from the stream, subsequent invocations of this operation, with the
original process still running, will fail with a SOAP Fault with error code 1500 and
display the following message: Another process has locked the channel {channel
name}. Only a single process may commit data to or delete snapshots from a channel
at a time. Please retry later.
