---
title: "Response"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/response.html"
content_id: "YqIGvpJCz9ix~xlGIVTlnA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:38.770251+00:00"
---

# Response

The response body contains a JSON array defined by the following name-value pairs.

| Name | Value | JSONPath |
| --- | --- | --- |
| Updated Views | **Type:** array  An array whose elements represent the views whose ownership has been reassigned. | `$.["Updated Views"]` |
| owner | **Type:** object  Identifies the target user (the user to whom ownership of the view has been reassigned). | `$.["Updated Views"][*].owner` |
| username | **Type:** string  Login name of the target user (the user to whom ownership of the view has been reassigned). | `$.["Updated Views"][*].owner.username` |
| ldapServer | **Type:** string  Address of the LDAP server that authenticates the target user (the user to whom ownership of the view has been reassigned). | `$.["Updated Views"][*].owner.ldapServer` |
| viewkey | **Type:** string  Identifies the table that contains the reassigned view. | `$.["Updated Views"][*].viewkey` |
| name | **Type:** string  Name of the reassigned view.  Except in the case of default views, the name is a concatenation of the original name, an underscore, and the source user name, for example: `"Original Table Name_my-source-user-name"`. Default views are not renamed. | `$.["Updated Views"][*].name` |
