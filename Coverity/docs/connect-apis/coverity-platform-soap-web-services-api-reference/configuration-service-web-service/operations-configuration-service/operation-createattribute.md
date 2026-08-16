---
title: "Operation: createAttribute"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-createattribute.html"
content_id: "C8RLtmGoGqJETziAAJpfdg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:24.050578+00:00"
---

# Operation: createAttribute

## Name

createAttribute

## Description

Create an attribute.

## Parameters

attributeDefinitionSpec
:   **Type:** 
    attributeDefinitionSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | attributeName | string | Name for the attribute. Required when using createAttribute(). |
    | attributeType | string | The type of attribute. Required when using createAttribute(). |
    | attributeValueChangeSpec | attributeValueChangeSpecDataObj | For a LIST_OF_VALUES attribute type only: The set of values available to the attribute. |
    | defaultValue | string | For a LIST_OF_VALUES attribute type only: The default attribute value. |
    | description | string | Description of the attribute. |
    | showInTriage | boolean | If *true*, makes the attribute available for use in the Triage pane of the UI. |
