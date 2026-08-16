---
title: "Operation: createGroup"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-creategroup.html"
content_id: "EgaufqeFwgY2k2Lgccr0dg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:25.348249+00:00"
---

# Operation: createGroup

## Name

createGroup

## Description

Create a user group.

## Parameters

groupSpec
:   **Type:** 
    groupSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | domain | serverDomainIdDataObj | For an LDAP user group only, the LDAP domain of group. Required when using createGroup() for an LDAP group. Maximum of one *domain* specification allowed. |
    | local | boolean | Defaults to *true*, specifying a local (non-LDAP) group. If an LDAP group, set to *false* when using createGroup(). Maximum of one *local* specification allowed. |
    | name | string | Name for the user group. Required when using createGroup(). |
    | roleAssignments | roleAssignmentDataObj | Role to associate with the group at the global level. See getAllRoles(), getRole(), and getAllPermissions(). Zero or more role associations allowed. If updating role assignments, respecify any global type roles that you want to retain. |
    | syncEnabled | boolean | If a local group, set to *false* when using createRole(). Defaults to *true*. Applies to an LDAP group only. |
