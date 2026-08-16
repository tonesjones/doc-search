---
title: "Complex type: attributeDefinitionSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-attributedefinitionspecdataobj.html"
content_id: "fDQD6~W4MzwFkg5xbI2OLQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:19.526891+00:00"
---

# Complex type: attributeDefinitionSpecDataObj

## Description

Specification used to set the properties of an attribute.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| attributeName | string | Name for the attribute. Required when using createAttribute(). |
| attributeType | string | The type of attribute. Required when using createAttribute(). |
| attributeValueChangeSpec | attributeValueChangeSpecDataObj | For a LIST_OF_VALUES attribute type only: The set of values available to the attribute. |
| defaultValue | string | For a LIST_OF_VALUES attribute type only: The default attribute value. |
| description | string | Description of the attribute. |
| showInTriage | boolean | If *true*, makes the attribute available for use in the Triage pane of the UI. |
