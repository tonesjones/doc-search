---
title: "Complex type: getOutputFileForSnapshot"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-getoutputfileforsnapshot.html"
content_id: "7Th4avvqWgEMCUgyMrhPoQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:32.694943+00:00"
---

# Complex type: getOutputFileForSnapshot

## Description

Specifies a snapshot output file.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| snapshotId | snapshotIdDataObj | Identifies the snapshot whose output file you want to retrieve. |
| fileName | string | Identifies the output file to retrieve. |
