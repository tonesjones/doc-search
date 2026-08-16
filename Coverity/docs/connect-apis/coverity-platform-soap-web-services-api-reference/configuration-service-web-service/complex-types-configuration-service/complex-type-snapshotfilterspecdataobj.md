---
title: "Complex type: snapshotFilterSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-snapshotfilterspecdataobj.html"
content_id: "T1vWMfw_tHGeATKFddV95A"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:51.234805+00:00"
---

# Complex type: snapshotFilterSpecDataObj

## Description

Filter properties used to return a matching set of snapshots.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| descriptionPattern | string | Glob pattern matching the description of one or more snapshots. |
| endDate | dateTime | Date (and optionally, time) on or before which the snapshot was created. Serves as an upper bound on the IDs to return. (If you do not enter a time, the system is likely to assume 12:00 a.m.) See the sample request below. |
| hasSummaries | boolean | If present, only snapshots with a hasSummaries attribute that is equal to the specified value will be returned. If absent, no filtering on hasSummaries takes place. |
| lastBeforeCodeVersionDate | dateTime | If present, only one snapshot will be returned, specifically, the snapshot with the latest codeVersionDate among those that are before or equal to the specified date. If there is no such snapshot, then the call will return an empty set. |
| startDate | dateTime | Date (and optionally, time) on or after when the snapshot was created. Serves as a lower bound on the IDs to return. (If you do not enter a time, the system is likely to assume 12:00 a.m.) See the sample request below. |
| targetPattern | string | Glob pattern matching the target of the snapshot. |
| versionPattern | string | Glob pattern matching the  version  of the snapshot. |
