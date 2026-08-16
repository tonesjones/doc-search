---
title: "Complex type: userFilterSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-userfilterspecdataobj.html"
content_id: "kuNQ3iuDS0iMeFqTYxl4Yg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:08.948364+00:00"
---

# Complex type: userFilterSpecDataObj

## Description

Filter properties used to return a matching set of user records.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| assignable | boolean | Set to *true* to retrieve only those users who can own software issues; *false* to retrieve only those who cannot. Otherwise, do not set. |
| disabled | boolean | Set to *true* to retrieve *disabled* users only. Set to *false* to retrieve enabled users only. Otherwise, do not set. |
| groupsList | string | Name of user group to which the retrieved users must belong. Zero or more groups allowed. |
| includeDetails | boolean | Set to *false* to prevent the inclusion of role assignments and other user details in the reqponse. Defaults to *true*. |
| ldap | boolean | Set to *true* to retrieve only LDAP users; *false* to retrieve only local users. Otherwise, do not set. |
| locked | boolean | Set to *true* to retrieve only those users who have been locked out; *false* to retrieve only unlocked users. Otherwise, do not set. |
| namePattern | string | Glob pattern that matches the user name of the users to retrieve. |
| projectIdDataObj | projectIdDataObj | Name of project to which the retrieved set of users must have a role association. |
| startId | long | Internal. Do not specify. |
