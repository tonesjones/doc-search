---
title: "Create an Azure Cache Service secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-an-azure-cache-service-secret.html"
content_id: "xS3ERhC7RmBF3UhFQLVCSA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:08.458910+00:00"
---

# Create an Azure Cache Service secret

If you are deploying Cache Service in Microsoft Azure, create a Cache Service secret as
follows:

```
kubectl create secret generic "${COVERITY_CACHE_SERVICE_SECRET_NAME}"\
--from-literal=azure_endpoint="${COVERITY_AZURE_ENDPOINT}" \
--from-literal=azure_tenant_id="${COVERITY_AZURE_TENANT_ID}" \
 --from-literal=azure_client_id="${COVERITY_AZURE_CLIENT_ID}" \
 --from-literal=azure_client_secret="${COVERITY_AZURE_CLIENT_SECRET}" \
--from-literal=azure_subscription_id="${COVERITY_AZURE_SUBSCRIPTION_ID}" \
--from-literal=azure_resource_group="${COVERITY_AZ_RESOURCE_GROUP}" \
--namespace "${COVERITY_NS}" \
```

Note: You can change the secret key names. If you change the key
names, you must also change the Helm override values.
