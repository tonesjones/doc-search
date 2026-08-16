---
title: "Operation: setSkeletonizationConfiguration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-setskeletonizationconfiguration.html"
content_id: "O2kAuiF83QyphmiJRUmVrQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:08.833075+00:00"
---

# Operation: setSkeletonizationConfiguration

## Name

setSkeletonizationConfiguration

## Description

Configure the process that purges snapshot details. Purging these details can help
you reduce and maintain the database size.

## Parameters

skeletonizationConfigurationDataObj
:   **Type:** 
    skeletonizationConfigurationDataObj

    These System settings correspond to the Maintenance options for Snapshot
    Details Purge in Coverity Connect.

    | Field name | Type | Description |
    | --- | --- | --- |
    | daysBeforeSkeletonization | int | Age (in number of days) at which the details of a snapshot can be purged. |
    | fridayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |
    | minSnapshotsToKeep | int | Number of snapshots that must retain their details. Minimum of one is required. |
    | mondayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |
    | saturdayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |
    | sundayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |
    | thursdayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |
    | time | string | Time of day at which the purge should take place. Example for 5:00 a.m.: *05:00* |
    | tuesdayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |
    | wednesdayEnabled | boolean | Value of *true* if a purge should take place on this day. Value of *false* if not. |

## Remarks

See also, getSkeletonizationConfiguration().
