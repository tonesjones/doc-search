---
title: "Complex type: fileContentsDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-filecontentsdataobj.html"
content_id: "80V5iRb7btyYjvMuIPyYdA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:33.630817+00:00"
---

# Complex type: fileContentsDataObj

## Description

Returns the contents of a source code file.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| contents | base64Binary | Base64-encoded contents of the zlib-compressed file that contains the instance of the CID. |
| fileId | fileIdDataObj | ID of the file that contains the instance of the CID. |
