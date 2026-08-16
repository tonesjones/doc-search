---
title: "Complex type: attributeValueDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-attributevaluedataobj.html"
content_id: "EdHgOSFmvahdacWWgyfKFQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:21.573858+00:00"
---

# Complex type: attributeValueDataObj

## Description

Metadata that pertain to a value of a LIST_OF_VALUES (Pick list) attribute type.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| attributeValueId | attributeValueIdDataObj | Identifier for an attribute value. |
| deprecated | boolean | Value of *true* if the attribute value is deprecated. Otherwise, *false*. |
| displayName | string | Name of the attribute that appears in the UI. |
| issueKindList | string | Issue kind. Multiple issue kinds allowed. |
