---
title: "Create an Azure service account secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-an-azure-service-account-secret.html"
content_id: "70ruQl3PH4JJM4k_NXwNQQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:07.366050+00:00"
---

# Create an Azure service account secret

If you are deploying Storage Service in Microsoft Azure, create an Azure service account
secret containing the Azure key as follows:

Note: You should not change the secret key name,
`azure_account_key`.

```
kubectl create secret generic "${AZURE_BLOB_SECRET_NAME}" \
  --namespace "${CNC_NS}" \
  --from-literal=azure_account_key="${AZURE_ACCOUNT_KEY}" \
  -o yaml \
```
