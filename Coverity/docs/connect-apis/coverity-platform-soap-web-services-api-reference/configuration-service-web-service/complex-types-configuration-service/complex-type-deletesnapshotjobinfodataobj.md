---
title: "Complex type: deleteSnapshotJobInfoDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-deletesnapshotjobinfodataobj.html"
content_id: "De4d3O0Vxb79sf0OV8AfWw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:31.402500+00:00"
---

# Complex type: deleteSnapshotJobInfoDataObj

## Description

Returns the status of a snapshot deletion request.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| snapshotId | long | Identifier for the snapshot. Available though the UI. |
| status | deleteSnapshotJobStatus | Indication of whether the snapshot deletion process succeeded or failed. |

## Remarks

See also, deleteSnapshot().
