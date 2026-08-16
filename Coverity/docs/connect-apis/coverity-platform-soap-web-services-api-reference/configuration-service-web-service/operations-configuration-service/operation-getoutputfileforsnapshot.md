---
title: "Operation: getOutputFileForSnapshot"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getoutputfileforsnapshot.html"
content_id: "jgXmB8LzcUsT8jAtUS_kAA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:52.537880+00:00"
---

# Operation: getOutputFileForSnapshot

## Name

getOutputFileForSnapshot

## Description

Get the specified output file for the specified snapshot. Output files are the files
that Coverity Analysis writes to the intermediate directory's
`output` directory.

## Parameters

snapshotId
:   **Type:** 
    snapshotIdDataObj

    Identifies the snapshot whose output file you want to retrieve.

    | Field name | Type | Description |
    | --- | --- | --- |
    | id | long | Numeric identifier for the snapshot. Required. |

fileName
:   **Type:** string

    Identifies the output file to retrieve.

## Output (Literal)

The output of this operation is the argument getOutputFileForSnapshotResponse of type
getOutputFileForSnapshotResponse having the structure defined by the
following table.

| Name | Type |
| --- | --- |
| return | outputFileDataObj |
