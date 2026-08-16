---
title: "Complex type: roleSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-rolespecdataobj.html"
content_id: "alrZBrHo4hMxMDjOAHqCkg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:48.625842+00:00"
---

# Complex type: roleSpecDataObj

## Description

Specification for a role.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| deletable | boolean | If the new role can be deleted, set to *true*. If not, set to *false*. Required when using createRole(). Maximum of one specification allowed. |
| description | string | Description of the role. |
| editable | boolean | Value of *false* not allowed. Requires value of *true* when using createRole(). Maximum of one specification allowed. |
| name | string | Name of the new role. Required when using createRole(). |
| permissionDataObjs | permissionDataObj | Name of a permission to associate with the new role. See getAllPermissions(). Zero or more permissions allowed. When updating role permissions, respecify any permissions you want to retain. |
