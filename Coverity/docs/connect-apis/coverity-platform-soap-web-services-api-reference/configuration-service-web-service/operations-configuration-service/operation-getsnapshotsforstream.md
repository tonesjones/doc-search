---
title: "Operation: getSnapshotsForStream"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getsnapshotsforstream.html"
content_id: "4Zd2Z7FOgzYqCxG6pTrZMA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:57.781116+00:00"
---

# Operation: getSnapshotsForStream

## Name

getSnapshotsForStream

## Description

Retrieve a set of snapshots that belong to a specified stream.

## Parameters

streamId
:   **Type:** 
    streamIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the stream. |

filterSpec
:   **Type:** 
    snapshotFilterSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | descriptionPattern | string | Glob pattern matching the description of one or more snapshots. |
    | endDate | dateTime | Date (and optionally, time) on or before which the snapshot was created. Serves as an upper bound on the IDs to return. (If you do not enter a time, the system is likely to assume 12:00 a.m.) See the sample request below. |
    | hasSummaries | boolean | If present, only snapshots with a hasSummaries attribute that is equal to the specified value will be returned. If absent, no filtering on hasSummaries takes place. |
    | lastBeforeCodeVersionDate | dateTime | If present, only one snapshot will be returned, specifically, the snapshot with the latest codeVersionDate among those that are before or equal to the specified date. If there is no such snapshot, then the call will return an empty set. |
    | startDate | dateTime | Date (and optionally, time) on or after when the snapshot was created. Serves as a lower bound on the IDs to return. (If you do not enter a time, the system is likely to assume 12:00 a.m.) See the sample request below. |
    | targetPattern | string | Glob pattern matching the target of the snapshot. |
    | versionPattern | string | Glob pattern matching the  version  of the snapshot. |

## Output (Literal)

The output of this operation is the argument getSnapshotsForStreamResponse having the
structure defined by the following table.

| Name | Type |
| --- | --- |
| return | snapshotIdDataObj |
