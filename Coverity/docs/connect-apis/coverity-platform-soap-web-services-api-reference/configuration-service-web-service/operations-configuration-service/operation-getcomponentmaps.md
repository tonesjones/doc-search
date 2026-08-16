---
title: "Operation: getComponentMaps"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getcomponentmaps.html"
content_id: "dREt~t15jcAJF~Vg9XdjBA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:45.313202+00:00"
---

# Operation: getComponentMaps

## Name

getComponentMaps

## Description

Retrieve a list of component maps that matches a component name pattern.

## Parameters

filterSpec
:   **Type:** 
    componentMapFilterSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | namePattern | string | Glob pattern matching the name of one or more component maps. |

## Output (Literal)

The output of this operation is the argument getComponentMapsResponse having the
structure defined by the following table.

| Name | Type |
| --- | --- |
| return | componentMapDataObj |
