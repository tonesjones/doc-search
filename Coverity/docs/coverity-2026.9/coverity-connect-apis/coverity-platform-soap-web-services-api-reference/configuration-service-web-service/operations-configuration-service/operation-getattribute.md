---
title: "Operation: getAttribute"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/operation-getattribute.html"
content_id: "Ukv15cLQTGpwn9xgKXZPXg"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:19.566012+00:00"
---

# Operation: getAttribute

## Name

getAttribute

## Description

Retrieve the properties of a specified attribute.

## Parameters

attributeDefinitionId
:   **Type:** 
    attributeDefinitionIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the attribute. |

## Output (Literal)

The output of this operation is the argument getAttributeResponse having the
structure defined by the following table.

| Name | Type |
| --- | --- |
| return | attributeDefinitionDataObj |
