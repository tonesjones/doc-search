---
title: "Add SQL users"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/add-sql-users.html"
content_id: "F9azy9we61ndGeCr3Z2gHQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:29.172000+00:00"
---

# Add SQL users

Optionally, you can add SQL users. For example:

```
gcloud sql users create "${CNC_PG_USER}" \
    --instance="${CNC_CLOUDSQL_NAME}" \
    --password="${CNC_PG_USER_PASSWORD}" \
    --type=BUILT_IN
```
