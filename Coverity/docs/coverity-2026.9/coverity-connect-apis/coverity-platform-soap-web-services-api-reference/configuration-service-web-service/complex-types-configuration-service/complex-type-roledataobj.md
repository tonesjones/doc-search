---
title: "Complex type: roleDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/complex-type-roledataobj.html"
content_id: "V6SW9GzU0ddnDDy7QF2nzQ"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:24.003506+00:00"
---

# Complex type: roleDataObj

## Description

Returns role data.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| deletable | boolean | Value of *true* if a role can be deleted; otherwise, *false*. |
| description | string | Description of the role. |
| editable | boolean | Value of *true* if a role can be edited; otherwise, *false*. |
| permissionDataObjs | permissionDataObj | List of permissions associated with a role. |
| roleId | roleIdDataObj | Identifier for a role. |
