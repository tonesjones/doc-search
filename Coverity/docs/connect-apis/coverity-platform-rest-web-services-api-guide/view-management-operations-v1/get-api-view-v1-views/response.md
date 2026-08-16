---
title: "Response"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/response.html"
content_id: "vnLQA7aQdLo4KidXaryYGA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:46.586292+00:00"
---

# Response

The response body contains a JSON array defined by the following name-value pairs.

| Name | Value | JSONPath |
| --- | --- | --- |
| All Views Status | **Type:** array  An array whose elements represent the views visible to the current user. | `$.["All Views Status"]` |
| viewId | **Type:** number  Identifier for the view. | `$.["All Views Status"][*].viewId` |
| viewName | **Type:** string  Name of the view. | `$.["All Views Status"][*].viewName` |
| owner | **Type:** object  Identifies the user who owns the view. | `$.["All Views Status"][*].owner` |
| username | **Type:** string  Login name of the user who owns the view. | `$.["All Views Status"][*].owner.username` |
| ldapServer | **Type:** string  LDAP server that authenticates the user who owns the view. | `$.["All Views Status"][*].owner.ldapServer` |
| sharedUsers | **Type:** array  Identifies users who share the view. The array is empty if no users share the view. | `$.["All Views Status"][*].sharedUsers` |
| sharedGroups | **Type:** array  Identifies groups that share the view. The array is empty if no groups share the view. | `$.["All Views Status"][*].sharedGroups` |
| hasViewNotifications | **Type:** boolean  Indicates whether the view has notifications.   - `true` – the view has notifications. - `false` – the view does not have notifications.  . | `$.["All Views Status"][*].hasViewNotifications` |
| ownerActive | **Type:** boolean  Indicates whether the user who owns the view is active.   - `true` – the user who owns the view is active. - `false` – the user who owns the view is not active. | `$.["All Views Status"][*].ownerActive` |
| ownerDeleted | **Type:** boolean  Indicates whether the user who owns the view has been deleted.   - `true` – the user who owns the view has been   deleted. - `false` – the user who owns the view has not been   deleted. | `$.["All Views Status"][*].ownerDeleted` |
