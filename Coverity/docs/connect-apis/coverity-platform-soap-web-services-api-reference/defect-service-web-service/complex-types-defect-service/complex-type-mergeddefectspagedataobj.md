---
title: "Complex type: mergedDefectsPageDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-mergeddefectspagedataobj.html"
content_id: "oiEIk0Z9sKn3M1qYStBYgA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:38.448761+00:00"
---

# Complex type: mergedDefectsPageDataObj

## Description

Returns data on the requested CIDs.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| mergedDefectIds | mergedDefectIdDataObj | Merge key and/or CID for a defect. |
| mergedDefects | mergedDefectDataObj | Properties of a CID. See the responses in the Example, below. |
| totalNumberOfRecords | int | Total number of records returned by the request. |
