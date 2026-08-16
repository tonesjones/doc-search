---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "Bxh1rrhuZg6wH58C7ozjQA"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:36.039346+00:00"
---

# Description

**HTTP Method:** PATCH

**URI format:**
`/api/view/v1/username/`{source_user}`/ldap/`{source_ldap}

Reassign ownership of all views owned by one user (the source user) to a different user (the
target user). Execution requires the **System Admin** role at a global
level; otherwise returns an error. Returns an error if the source and target users are the
same user.

Following the execution of this operation, the source user will not own any views. The next
time the source user logs in, Coverity Connect will create a new set of default views for the
source user.
