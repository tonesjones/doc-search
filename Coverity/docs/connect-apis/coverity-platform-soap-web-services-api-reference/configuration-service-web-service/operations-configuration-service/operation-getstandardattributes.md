---
title: "Operation: getStandardAttributes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getstandardattributes.html"
content_id: "3rGoBpepgk85IizPxBl60Q"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:59.074285+00:00"
---

# Operation: getStandardAttributes

## Name

getStandardAttributes

## Description

Retrieve a list of all standard attributes.

## Output (Literal)

The output of this operation is the argument getStandardAttributesResponse having the
structure defined by the following table.

| Name | Type |
| --- | --- |
| return | standardAttributeDataObj |

## Remarks

To retrieve a snapshot ID, see getSnapshotForStream(). The ID is also available through the Coverity
Connect UI.
