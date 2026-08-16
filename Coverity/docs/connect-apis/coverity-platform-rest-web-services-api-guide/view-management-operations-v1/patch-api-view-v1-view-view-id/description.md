---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "a9dmsYvdC2g_vslkCR5dqQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:55:40.732463+00:00"
---

# Description

**HTTP Method:** PATCH

**URI format:**
`/api/view/v1/view/`{view_id}

Reassign ownership of the specified view from the current owner (the source user) to the
specified user (the target user). Execution requires the **System Admin** role at a
global level; otherwise returns an error. Returns an error if the source and target users
are the same user.

Following the execution of this operation, the source user will own fewer views. The next
time the source user logs in, Coverity Connect will create new default views for any that
are missing from the source user's set of default views.
