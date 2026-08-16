---
title: "Operation: deleteGroup"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-deletegroup.html"
content_id: "MoNMdZFZBM7gz3_Psx8Jqg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:31.970658+00:00"
---

# Operation: deleteGroup

## Name

deleteGroup

## Description

Delete a user group.

## Parameters

groupId
:   **Type:** 
    groupIdDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | displayName | string | The name of a user group. To retrieve an LDAP group, you use <groupname>@<LDAPserver>. |
    | domain | serverDomainIdDataObj | For an LDAP user group only, the LDAP domain of group. |
    | name | string | Required. Name of the local or LDAP group. |

## Remarks

To retrieve a list of groups, see getGroups().
