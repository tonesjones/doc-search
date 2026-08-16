---
title: "GCP keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gcp-keys.html"
content_id: "5NyfmE3SLwgb_EPeJ9h6MQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:55.869124+00:00"
---

# GCP keys

If the Cache Service is using a Google Cloud SQL database
(`cache-service.​storageProvider` is `gcp`), set
the following `cache-service` Helm keys:

- `cache-service.gcp.project: ""` with the GCP project name.
- `cache-service.gcp.secret: ""` with the GCP secret name. The key
  name within the secret must be `key.json`.

For information on the keys, refer to the section, scan-services Helm subchart: Helm keys.
