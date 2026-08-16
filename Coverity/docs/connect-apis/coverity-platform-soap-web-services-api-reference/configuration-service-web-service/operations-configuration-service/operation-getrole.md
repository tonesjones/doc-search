---
title: "Operation: getRole"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getrole.html"
content_id: "THOp85qNG~ypuYuYy0WDxg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:53.836664+00:00"
---

# Operation: getRole

## Name

getRole

## Description

Retrieve the properties of a role, including its associated permissions.

## Parameters

roleId
:   **Type:** 
    roleIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | name | string | Required. Name of the role. |

## Output (Literal)

The output of this operation is the argument getRoleResponse having the structure
defined by the following table.

| Name | Type |
| --- | --- |
| return | roleDataObj |
