---
title: "Complex type: getOutputFileForSnapshotResponse"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/complex-type-getoutputfileforsnapshotresponse.html"
content_id: "rp0SUsQ3FdVFpFbmA5DVCA"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:23.043959+00:00"
---

# Complex type: getOutputFileForSnapshotResponse

## Description

Returns a snapshot output file.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| return | outputFileDataObj | The output file from the snapshot that matches the specified file name, or null if none is found. |
