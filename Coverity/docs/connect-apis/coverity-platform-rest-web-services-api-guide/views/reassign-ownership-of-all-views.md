---
title: "Reassign ownership of all views"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/reassign-ownership-of-all-views.html"
content_id: "vCqALT5rx6kYuj795ucZIA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:24.067494+00:00"
---

# Reassign ownership of all views

Example PUT request to reassign ownership of all views owned by one user (the *source user*) to a different user (the *target user*). Execution requires the **System Admin**
role at a global level; otherwise returns an error. Returns an error if the source and
target users are the same user.

**cURL request**

```
curl --location \
--request PUT "http://my_connect_host:8080/api/v2/views/reassignOwner" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--user my_username:my_password \
--data-raw \
'{
  "username": "admin",
  "ldap": "local",
  "target_username": "test2" ,
  "target_ldap": "local"
}'
```
