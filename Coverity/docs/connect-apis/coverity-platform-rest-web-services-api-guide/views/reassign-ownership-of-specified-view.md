---
title: "Reassign ownership of specified view"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/reassign-ownership-of-specified-view.html"
content_id: "rzmvn3_obG4F1teptFseBw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:24.705955+00:00"
---

# Reassign ownership of specified view

Example PUT request to reassign ownership of the specified view from the current owner
(the *source user*) to the specified user (the *target user*). Execution requires the **System Admin**
role at a global level; otherwise returns an error. Returns an error if the source and
target users are the same user.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/views/10016/reassignOwner" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "target_username": "test0" ,
  "target_ldap" : "local"
}'
```
