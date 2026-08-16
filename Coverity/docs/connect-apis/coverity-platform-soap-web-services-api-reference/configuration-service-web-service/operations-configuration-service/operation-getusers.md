---
title: "Operation: getUsers"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/operation-getusers.html"
content_id: "Cdu5FsXNW_Auvho89QUeug"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:51:02.974952+00:00"
---

# Operation: getUsers

## Name

getUsers

## Description

Get users (filtered or unfiltered).

## Parameters

filterSpec
:   **Type:** 
    userFilterSpecDataObj

    | Field name | Type | Description |
    | --- | --- | --- |
    | assignable | boolean | Set to *true* to retrieve only those users who can own software issues; *false* to retrieve only those who cannot. Otherwise, do not set. |
    | disabled | boolean | Set to *true* to retrieve *disabled* users only. Set to *false* to retrieve enabled users only. Otherwise, do not set. |
    | groupsList | string | Name of user group to which the retrieved users must belong. Zero or more groups allowed. |
    | includeDetails | boolean | Set to *false* to prevent the inclusion of user details in the response. Defaults to *true*. |
    | ldap | boolean | Set to *true* to retrieve only LDAP users; *false* to retrieve only local users. Otherwise, do not set. |
    | locked | boolean | Set to *true* to retrieve only those users who have been locked out; *false* to retrieve only unlocked users. Otherwise, do not set. |
    | namePattern | string | Glob pattern that matches the user name of the users to retrieve. |
    | projectIdDataObj | projectIdDataObj | Name of project to which the retrieved set of users must have a role association. |
    | startId | long | Internal. Do not specify. |

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

The output of this operation is the argument getUsersResponse having the structure
defined by the following table.

| Name | Type |
| --- | --- |
| return | usersPageDataObj |
