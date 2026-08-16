---
title: "Operation: getFileContents"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getfilecontents.html"
content_id: "SWSA~eH_xBjy~ErPe5REpQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:14.828916+00:00"
---

# Operation: getFileContents

## Name

getFileContents

## Description

Retrieve the Base64-encoded value of the zlib-compressed contents of a file that
contains an instance of a CID.

## Parameters

streamId
:   **Type:** 
    streamIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the stream. You can specify one or more instances of streamIdDataObj. See the example. |

fileId
:   **Type:** 
    fileIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | contentsMD5 | string | Required. MD5 checksum (a fingerprint or message digest) of the file contents. You can get the contentsMD5 and filePathname for an instance of a CID by using getStreamDefects() with the includeDefectInstances filter set to true. |
    | filePathname | string | Required. Path to the file that contains the instance of the CID. You can get the contentsMD5 and filePathname for an instance of a CID by using getStreamDefects() with the includeDefectInstances filter set to true. |

## Output (literal)

The output of this operation is the argument getFileContentsResponse having the
structure defined by the following table.

| Name | Type |
| --- | --- |
| return | fileContentsDataObj |
