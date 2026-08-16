---
title: "Complex type: roleAssignmentDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-roleassignmentdataobj.html"
content_id: "JPFgyl8CRSCo7DcBThlgHQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:46.677396+00:00"
---

# Complex type: roleAssignmentDataObj

## Description

Role assignment data.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| groupId | groupIdDataObj | Identifier for the user group. Used only if the role applies to a group, not a user. |
| roleAssignmentType | string | Role assignment type. |
| roleId | roleIdDataObj | Identifier for a role. |
| type | string | Role type. |
| username | string | User name associated with *user* roleId only. Does not apply to *group* roleId. |
