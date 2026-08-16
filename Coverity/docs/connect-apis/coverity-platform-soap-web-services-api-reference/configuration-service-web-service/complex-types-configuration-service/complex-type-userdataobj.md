---
title: "Complex type: userDataObj"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/complex-type-userdataobj.html"
content_id: "~rOxOAzNBvw2bqRuqkbLEg"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:52:08.305231+00:00"
---

# Complex type: userDataObj

## Description

Returned properties of a user.

## Derived by

Restricting anyType

## Content model

Contains elements as defined in the following table.

| Component | Type | Description |
| --- | --- | --- |
| [image: image] |  |  |
| dateCreated | dateTime | Date and time that the user was created in the database. |
| dateModified | dateTime | Date and time that the user was modified. Can be the creation date and time. |
| disabled | boolean | Value of *true* if the user is disabled; *false* if not. |
| domain | serverDomainIdDataObj | If an LDAP user, the LDAP domain. |
| email | string | Email address of the user. |
| familyName | string | Last name of the user. |
| givenName | string | First name of the user. |
| groups | string | List of groups to which the retrieved user belongs. |
| local | boolean | Value of *true* if the user is a local user; *false* if an LDAP user. |
| locale | string | Locale of the retrieved user. |
| locked | boolean | Value of *true* if the user is currently locked out; *false* if not. |
| roleAssignments | roleAssignmentDataObj | Role to associate with the user at the global level. See getAllRoles(), getRole(), and getAllPermissions(). Zero or more role associations allowed. If updating role assignments, respecify any global type roles that you want to retain. |
| superUser | boolean | Value of *true* for the built-in Coverity Connect admin user. Otherwise, *false*. |
| userModified | string | Name of the user who last updated the user record. |
| username | string | User name that matches the request. |
