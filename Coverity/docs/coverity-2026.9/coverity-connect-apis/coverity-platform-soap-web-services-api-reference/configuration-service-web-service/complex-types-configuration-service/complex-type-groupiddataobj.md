---
title: "Complex type: groupIdDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/complex-type-groupiddataobj.html"
content_id: "ohgkgpJV_ak_AVxy7DcQlA"
version: "2026.9"
section: "Coverity Connect APIs"
scraped_at: "2026-10-04T23:35:23.172125+00:00"
---

# Complex type: groupIdDataObj

## Description

Identifier for a user group.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| displayName | string | The name of a user group. To retrieve an LDAP group, you use <groupname>@<LDAPserver>. |
| domain | serverDomainIdDataObj | For an LDAP user group only, the LDAP domain of group. |
| name | string | Required. Name of the local or LDAP group. |
