---
title: "Azure: Create Storage Service secrets and ConfigMap"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/azure-create-storage-service-secrets-and-configmap.html"
content_id: "c6wagDRIv_uUnM_kHEK2iw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:50.590221+00:00"
---

# Azure: Create Storage Service secrets and ConfigMap

To support communication within the infrastructure, you will need to create Coverity
cloud deployment secrets and ConfigMaps, including for storage service.

For high-level deployment guidance, refer to:

- Coverity deployment scenarios

When you create storage access secrets, refer to Create TLS certificate, keystore, and secrets.

Get the Redis TLS CA certificate. For example, you can add and manage certificates using
Azure App Service. Refer to

- <https://learn.microsoft.com/en-us/azure/app-service/configure-ssl-certificate?tabs=apex>

Create storage secrets to provide access to the Redis cache and storage containers. Refer
to:

- Coverity deployment scenarios
- Create TLS certificate, keystore, and secrets

Add the Redis CA certificate to the truststore. Refer to:

- Create a truststore ConfigMap for Connect communication over TLS
