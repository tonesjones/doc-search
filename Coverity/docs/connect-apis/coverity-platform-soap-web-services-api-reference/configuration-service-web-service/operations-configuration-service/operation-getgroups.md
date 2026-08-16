---
title: "Operation: getGroups"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getgroups.html"
content_id: "D2frXXoLAG2r20Pz9KefgQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:50:48.593453+00:00"
---

# Operation: getGroups

## Name

getGroups

## Description

Get a list of groups.

## Parameters

filterSpec
:   **Type:** 
    groupFilterSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | ldap | boolean | Value of *true* for LDAP groups only; otherwise, *false*. |
    | namePattern | string | Glob pattern matching the name of one or more groups. |
    | projectIdDataObj | projectIdDataObj | Name of a project with which the group must have a role association. |
    | userList | string | User name of a user that must belong to the group. Multiple names allowed. |

pageSpec
:   **Type:** 
    pageSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | pageSize | int | Required. Number of records to return. Maximum of 1000. |
    | sortAscending | boolean | Set to *false* to return records in reverse alphabetical or numerical order. Defaults to *true*. |
    | sortField | string | Do not specify with getGroups(). Name of the field to use for sorting results. For example, the dateCreated or familyName field for user records returned by getUsers(). You cannot sort by a field that can appear mulitple times for a single record (for example, a single user record can have multiple group fields). For examples of sortField values, see the remark for this data object. |
    | startIndex | int | Zero-based index of user records to return. Defaults to *0*. You might use this field if there are more than 1000 users. You could make separate calls that start the index at 1000 or 2000, for example, until you capture separate lists of all of the users. |

## Output (Literal)

The output of this operation is the argument getGroupsResponse having the structure
defined by the following table.

**Note**: The object that is returned by this operation can include
roleAssignments that are identical. This occurs because roleAssignment objects don't
have an attribute that specifies a name for the type to which they apply (for
example, a project name).

| Name | Type |
| --- | --- |
| return | groupsPageDataObj |
