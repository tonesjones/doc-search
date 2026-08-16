---
title: "Operation: updateUser"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-updateuser.html"
content_id: "20RVCUBeAFegG~_Sb1hX3g"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:16.803895+00:00"
---

# Operation: updateUser

## Name

updateUser

## Description

Update a user specification.

## Parameters

username
:   **Type:** string

userSpec
:   **Type:** 
    userSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | disabled | boolean | To prevent the user from logging in to the UI, set to *true*. Defaults to *false* for createUser(). |
    | domain | serverDomainIdDataObj | For an LDAP user only, the LDAP domain of user. |
    | email | string | Email address of the user. |
    | familyName | string | Last name of the user. |
    | givenName | string | First name of the user. |
    | groupNames | groupIdDataObj | Name of an existing group to which the user should belong. Zero or more group associations allowed. *Supported when updating a user, not when creating a user.* |
    | local | boolean | If an LDAP user, set to *false*. Defaults to *true* with createUser(), specifying a local (non-LDAP) user. |
    | locale | string | The locale of the user. Defaults to *en-US* with createUser(). |
    | locked | boolean | To lock out the new user, set to *true*. Unless password recovery is enabled through the UI, the administrator must reset the password for the locked out user before the user can log in. Defaults to *false* with createUser(). |
    | password | string | Password for the user. Required with createUser(). |
    | roleAssignments | roleAssignmentDataObj | Role to associate with the new user at the global level. See getAllRoles(), getRole(), and getAllPermissions(). Zero or more role associations are allowed. If updating role assignments, respecify any that you want to retain. |
    | username | string | Required. Username for/of the user. Any capitalized (upper case) letters in the name will be converted to lower case when using createUser(). Maximum of one name specification is allowed. |
