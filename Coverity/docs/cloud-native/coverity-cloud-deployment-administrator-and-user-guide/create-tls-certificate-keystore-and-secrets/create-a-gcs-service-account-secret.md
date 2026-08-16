---
title: "Create a GCS service account secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-gcs-service-account-secret.html"
content_id: "IeUzxU2ifzmQRbgW8VM~IA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:09.125417+00:00"
---

# Create a GCS service account secret

If you are deploying Storage Services in Google GCS, you must create a secret with a GCS
service account key as follows:

```
kubectl create secret generic "${GCS_SA_SECRET_NAME}" \
  --namespace "${NS}" \
  --from-file=key.json="${GCS_SERVICE_ACCOUNT_FILE}" \
  -o yaml \
```

Note: You can change the secret key name whose default value is
`key.json`. If you change the key name, you must also change the Helm
key value `storage-service.gcs.secret.key`. See also .
