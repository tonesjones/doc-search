---
title: "Operation: getGroup"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getgroup.html"
content_id: "R8iU0DPlw1QsSs8xtGkK4A"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:47.928571+00:00"
---

# Operation: getGroup

## Name

getGroup

## Description

Retrieve the properties of a user group.

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

## Output (Literal)

The output of this operation is the argument getGroupResponse having the structure
defined by the following table.

| Name | Type |
| --- | --- |
| return | groupDataObj |
