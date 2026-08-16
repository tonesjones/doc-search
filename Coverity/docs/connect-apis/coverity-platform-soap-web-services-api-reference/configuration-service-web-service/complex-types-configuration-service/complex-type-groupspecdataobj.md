---
title: "Complex type: groupSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-groupspecdataobj.html"
content_id: "NIsTUTADc015evqoSvbLBQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:36.629390+00:00"
---

# Complex type: groupSpecDataObj

## Description

Specification for a user group.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| domain | serverDomainIdDataObj | For an LDAP user group only, the LDAP domain of group. Required when using createGroup() for an LDAP group. Maximum of one *domain* specification allowed. |
| local | boolean | Defaults to *true*, specifying a local (non-LDAP) group. If an LDAP group, set to *false* when using createGroup(). Maximum of one *local* specification allowed. |
| name | string | Name for the user group. Required when using createGroup(). |
| roleAssignments | roleAssignmentDataObj | Role to associate with the group at the global level. See getAllRoles(), getRole(), and getAllPermissions(). Zero or more role associations allowed. If updating role assignments, respecify any global type roles that you want to retain. |
| syncEnabled | boolean | If a local group, set to *false* when using createRole(). Defaults to *true*. Applies to an LDAP group only. |
