---
title: "Complex type: attributeDefinitionDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-attributedefinitiondataobj.html"
content_id: "09EGTB98BVP38s5wOZ~ESg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:18.193308+00:00"
---

# Complex type: attributeDefinitionDataObj

## Description

Returns the properties of an attribute.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| attributeDefinitionId | attributeDefinitionIdDataObj | Name of an attribute. |
| attributeType | string | Attribute type. |
| builtIn | boolean | Value of true for a built-in attribute; otherwise, *false*. |
| configurableValues | attributeValueDataObj | For a LIST_OF_VALUES attribute type only: The set of values available to the attribute. |
| defaultValue | string | For a LIST_OF_VALUES attribute type only: The default attribute value. |
| description | string | Description of the attribute. |
| displayDescription | string | Description of the attribute that appears in the UI. |
| displayName | string | Name of the attribute that appears in the UI. |
| showInTriage | boolean | Value of *true* if the attribute appears in the Triage pane; otherwise, *false*. |
