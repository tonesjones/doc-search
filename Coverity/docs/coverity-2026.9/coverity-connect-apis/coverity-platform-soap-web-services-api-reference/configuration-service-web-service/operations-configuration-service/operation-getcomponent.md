---
title: "Operation: getComponent"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/operation-getcomponent.html"
content_id: "9krxrRAKmfuwClVl8p6O5g"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:19.820077+00:00"
---

# Operation: getComponent

## Name

getComponent

## Description

Retrieve the properties of a component.

## Parameters

componentId
:   **Type:** 
    componentIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of a component in the form ***componentMapName.componentName*** (for example, myComponentMap.myComponent). |

## Output (Literal)

The output of this operation is the argument getComponentResponse having the
structure defined by the following table.

| Name | Type |
| --- | --- |
| return | componentDataObj |
