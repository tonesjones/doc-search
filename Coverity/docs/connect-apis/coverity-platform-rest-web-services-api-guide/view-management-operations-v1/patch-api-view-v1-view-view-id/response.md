---
title: "Response"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/response.html"
content_id: "_~DiJ773h1_tbQ_A2vz7aw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:43.360511+00:00"
---

# Response

The response body contains a JSON array defined by the following name-value pairs.

| Name | Value | JSONPath |
| --- | --- | --- |
| Updated View | **Type:** object  An object that represents the view whose ownership has been reassigned. | `$.["Updated View"]` |
| owner | **Type:** object  Identifies the target user (the user to whom ownership of the view has been reassigned). | `$.["Updated View"].owner` |
| username | **Type:** string  Login name of the target user (the user to whom ownership of the view has been reassigned). | `$.["Updated View"].owner.username` |
| ldapServer | **Type:** string  Address of the LDAP server that authenticates the target user (the user to whom ownership of the view has been reassigned). | `$.["Updated View"].owner.ldapServer` |
| viewkey | **Type:** string  Identifies the table that contains the reassigned view. | `$.["Updated View"].viewkey` |
| name | **Type:** string  Name of the reassigned view.  Except in the case of default views, the name is a concatenation of the original name, an underscore, and the source user name, for example: `"Original Table Name_my-source-user-name"`. Default views are not renamed. | `$.["Updated View"].name` |
