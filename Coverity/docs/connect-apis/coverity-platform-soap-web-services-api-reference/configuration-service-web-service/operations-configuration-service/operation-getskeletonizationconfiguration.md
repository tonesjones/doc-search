---
title: "Operation: getSkeletonizationConfiguration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getskeletonizationconfiguration.html"
content_id: "HExBydAyVNepYcPxyxImuw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:55.813587+00:00"
---

# Operation: getSkeletonizationConfiguration

## Name

getSkeletonizationConfiguration

## Description

Retrieve the configuration for the process that purges snapshot details. Purging
these details can help you reduce and maintain the database size.

## Output (Literal)

The output of this operation is the argument getSkeletonizationConfigurationResponse
having the structure defined by the following table.

| Name | Type |
| --- | --- |
| return | skeletonizationConfigurationDataObj |

## Remarks

See also setSkeletonizationConfiguration().
