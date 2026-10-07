---
title: "Operation: refreshLdapGroup"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/operation-refreshldapgroup.html"
content_id: "whg9N2PsywXhjYHcxDpnfA"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:21.212802+00:00"
---

# Operation: refreshLdapGroup

## Name

refreshLdapGroup

## Description

Refresh an LDAP group.

## Parameters

groupId
:   **Type:** 
    groupIdDataObj

    Specification for a user group identifier.

    | Field name | Type | Description |
    | --- | --- | --- |
    | displayName | string | The name of a user group. To retrieve an LDAP group, you use <groupname>@<LDAPserver>. |
    | domain | serverDomainIdDataObj | For an LDAP user group only, the LDAP domain of group. |
    | name | string | Required. Name of the local or LDAP group. |

## Output

None
