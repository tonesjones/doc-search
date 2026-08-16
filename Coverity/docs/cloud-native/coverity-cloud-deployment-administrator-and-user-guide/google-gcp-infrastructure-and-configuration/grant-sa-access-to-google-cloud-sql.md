---
title: "Grant SA access to Google Cloud SQL"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/grant-sa-access-to-google-cloud-sql.html"
content_id: "LRdNuavFmDp7N_j7Bkqf0w"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:34.359948+00:00"
---

# Grant SA access to Google Cloud SQL

```
gcloud projects add-iam-policy-binding "${CNC_PROJECT_ID}" \
  --member "serviceAccount:${CNC_STORAGE_SA}@${CNC_PROJECT_ID}.iam.gserviceaccount.com" \
  --role "roles/cloudsql.client"
```
