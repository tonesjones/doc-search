---
title: "Complex type: snapshotPurgeDetailsObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-snapshotpurgedetailsobj.html"
content_id: "ClHBcUaqKZBLhkISgkneuA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:53.272800+00:00"
---

# Complex type: snapshotPurgeDetailsObj

## Description

Deprecated specification for snapshot purge settings.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| daysBeforeSkeletonization | int | Age (in number of days) at which the details of a snapshot can be purged. Defaults to 0. |
| fridayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |
| minSnapshotsToKeep | int | Number of snapshots that must retain their details. Defaults to 0. |
| mondayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |
| saturdayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |
| sundayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |
| thursdayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |
| timeOfDay | string | Require Time of day at which the purge should take place. Example for 5:00 a.m.: *05:00* |
| tuesdayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |
| wednesdayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |
