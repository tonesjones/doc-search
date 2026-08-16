---
title: "Operation: updateGroup"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-updategroup.html"
content_id: "6pEqJB4H3Ou0D_IvRlr7Qg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:11.436115+00:00"
---

# Operation: updateGroup

## Name

updateGroup

## Description

Update a group specification.

## Parameters

groupId
:   **Type:** 
    groupIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | displayName | string | The name of a user group. To retrieve an LDAP group, you use <groupname>@<LDAPserver>. |
    | domain | serverDomainIdDataObj | For an LDAP user group only, the LDAP domain of group. |
    | name | string | Required. Name of the local or LDAP group. |

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
