---
title: "Complex type: groupDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/complex-type-groupdataobj.html"
content_id: "DRi_fYl2SqbxZRb3BMBq2w"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:23.086019+00:00"
---

# Complex type: groupDataObj

## Description

User group data.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| roleAssignments | roleAssignmentDataObj | Role assigned to the group. |
| local | boolean | Value of *true* if the group is local; *false* if LDAP. |
| name | groupIdDataObj | Name of the local or LDAP user group. |
| syncEnabled | boolean | Value of *false* if the group is a local group; defaults to *false*. |
