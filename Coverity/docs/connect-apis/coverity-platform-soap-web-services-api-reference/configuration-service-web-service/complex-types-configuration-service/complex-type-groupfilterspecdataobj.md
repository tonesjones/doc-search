---
title: "Complex type: groupFilterSpecDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-groupfilterspecdataobj.html"
content_id: "vhog2a97tI1q4SrsrzNR~A"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:34.658391+00:00"
---

# Complex type: groupFilterSpecDataObj

## Description

Filter properties used to return a matching set of user groups.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| ldap | boolean | Value of *true* for LDAP groups only; otherwise, *false*. |
| namePattern | string | Glob pattern matching the name of one or more groups. |
| projectIdDataObj | projectIdDataObj | Name of a project with which the group must have a role association. |
| userList | string | User name of a user that must belong to the group. Multiple names allowed. |
