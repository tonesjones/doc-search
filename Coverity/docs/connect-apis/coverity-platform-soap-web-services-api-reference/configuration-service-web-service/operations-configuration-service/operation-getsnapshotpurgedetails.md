---
title: "Operation: getSnapshotPurgeDetails"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getsnapshotpurgedetails.html"
content_id: "98a8eGi~fdG2jYl1C4BDcw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:57.107546+00:00"
---

# Operation: getSnapshotPurgeDetails

## Name

getSnapshotPurgeDetails

## Description

**Deprecated in v8**: Use getSkeletonizationConfiguration() instead to retrieve the configuration
for the process that purges snapshot details. Purging these details can help you
reduce and maintain the database size.

## Output (Literal)

The output of this operation is the argument getSnapshotPurgeDetailsResponse having
the structure defined by the following table.

| Name | Type |
| --- | --- |
| return | snapshotPurgeDetailsObj |
