---
title: "Create the Cloud SQL server CA certificate and add it to the truststore ConfigMap"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-the-cloud-sql-server-ca-certificate-and-add-it-to-the-truststore-configmap.html"
content_id: "dOZPbKZh9D_NsoLq4UkSfw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:28.523983+00:00"
---

# Create the Cloud SQL server CA certificate and add it to the truststore ConfigMap

Create the Cloud SQL server CA certificate. For example:

```
gcloud sql instances describe \
    --project "${CNC_PROJECT_ID}" "${CNC_CLOUDSQL_NAME}" \
    --format json | jq -r '.serverCaCert.cert'
```

Add the certificate to the Connect truststore when you set up TLS for PostgreSQL. Refer
to:

- for an overview and links to creating a truststore: Create a truststore ConfigMap for Connect communication over TLS
