---
title: "Complex type: defectChangeDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-defectchangedataobj.html"
content_id: "Zq6_74FfL3yvxouL4ht0EQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:27.647904+00:00"
---

# Complex type: defectChangeDataObj

## Description

Returns data on the CID.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| affectedStreams | streamIdDataObj | Name of the stream that contains the specified CID. |
| attributeChanges | fieldChangeDataObj | Changes to an attribute for the CID. |
| comments | string | Comment on the CID. |
| dateModified | dateTime | Date and time the CID was created or modified. |
| userModified | string | Username of user who triaged the CID. |
