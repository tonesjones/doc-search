---
title: "Operation: createRole"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-createrole.html"
content_id: "vwK_ew4cF~Se0XIZA7SciA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:27.389417+00:00"
---

# Operation: createRole

## Name

createRole

## Description

Create a role.

## Parameters

roleSpec
:   **Type:** 
    roleSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | deletable | boolean | If the new role can be deleted, set to *true*. If not, set to *false*. Required when using createRole(). Maximum of one specification allowed. |
    | description | string | Description of the role. |
    | editable | boolean | Value of *false* not allowed. Requires value of *true* when using createRole(). Maximum of one specification allowed. |
    | name | string | Name of the new role. Required when using createRole(). |
    | permissionDataObjs | permissionDataObj | Name of a permission to associate with the new role. See getAllPermissions(). Zero or more permissions allowed. When updating role permissions, respecify any permissions you want to retain. |

## Remarks

Needed only if an existing role or set of roles is not associated with the set of
permissions you require. See getAllRoles() and getRole().
