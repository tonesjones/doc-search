---
title: "Operation: getStandardAttribute"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getstandardattribute.html"
content_id: "MdDk6WrsPz5Yb5az8WP26g"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:58.418700+00:00"
---

# Operation: getStandardAttribute

## Name

getStandardAttribute

## Description

Retrieve the properties of a specified standard attribute.

## Parameters

standardAttributeIdDataObj

:   **Type:** 
    standardAttributeIdDataObj

    Required. Name of the standard attribute.

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the standard attribute. |

## Output (Literal)

The output of this operation is the argument getStandardAttributeResponse having the
structure defined by the following table.

| Name | Type |
| --- | --- |
| return | standardAttributeDataObj |
