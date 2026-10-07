---
title: "Operation: updateAttribute"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/operation-updateattribute.html"
content_id: "UHnOZfhwtHDDIwsUz0IF6Q"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:21.516364+00:00"
---

# Operation: updateAttribute

## Name

updateAttribute

## Description

Update an attribute specification.

## Parameters

attributeDefinitionId
:   **Type:** 
    attributeDefinitionIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the attribute. |

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
