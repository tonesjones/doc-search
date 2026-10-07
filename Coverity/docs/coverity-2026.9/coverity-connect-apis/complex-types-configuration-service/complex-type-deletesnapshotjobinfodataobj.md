---
title: "Complex type: deleteSnapshotJobInfoDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/complex-type-deletesnapshotjobinfodataobj.html"
content_id: "De4d3O0Vxb79sf0OV8AfWw"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:22.914173+00:00"
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
