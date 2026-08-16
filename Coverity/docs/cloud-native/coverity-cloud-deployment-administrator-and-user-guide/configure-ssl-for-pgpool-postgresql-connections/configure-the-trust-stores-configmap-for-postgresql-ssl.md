---
title: "Configure the trust-stores ConfigMap for PostgreSQL SSL"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-the-trust-stores-configmap-for-postgresql-ssl.html"
content_id: "UgSnxVzcpFYioqAjVDj~rg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:12.751140+00:00"
---

# Configure the trust-stores ConfigMap for PostgreSQL SSL

Create a ConfigMap that provides the CA configuration required for PostgreSQL SSL
connections.

PostgreSQL SSL connections require CA configuration to validate server
certificates.

This configuration is provided through a trust-stores ConfigMap.

1. Create a file named `postgres-root.pem`.
2. (Optional) If multiple CA entries are required, add all entries to the same
   file. This is required for GCP CloudSQL deployments, where each instance can use
   a different CA configuration.
3. Create the ConfigMap.

   ```
   kubectl create configmap trust-stores \
   --from-file=postgres-root.pem \
   -n <your-namespace>
   ```
4. Reference the ConfigMap in your deployment configuration.

PostgreSQL connections use the configured trust-stores ConfigMap for SSL
validation.
