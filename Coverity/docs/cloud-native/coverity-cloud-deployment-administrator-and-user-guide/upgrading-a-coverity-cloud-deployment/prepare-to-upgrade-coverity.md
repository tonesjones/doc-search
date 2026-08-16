---
title: "Prepare to upgrade Coverity"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/prepare-to-upgrade-coverity.html"
content_id: "utLQbJso4Pp7F9nPD488Uw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:25.295454+00:00"
---

# Prepare to upgrade Coverity

Prepare to upgrade the Coverity:

1. Obtain the new container images. Refer to Coverity container images.
2. Obtain the new Helm chart version. Refer to Downloading the Helm chart from the Black Duck public Docker registry.
3. Update Helm keys to support any release-specific Helm key changes. See Upgrade considerations.
4. If needed, update any secrets:

   Table 1. Updating secrets

   | Secret | Refer to |
   | --- | --- |
   | - If you were assigned new image pull credentials, update   the image pull secret. | - Create a container image pull secret |
   | - If you you are using a new private Docker image   registry, update the `imageRegistry` Helm   key. | - Preparing container image and registry keys |
   | - If you were assigned a new Coverity Connect license,   update the Connect license secret. | - Obtain your Coverity licenses - Create a Connect license secret |
   | - If you were assigned a new Scan Service license, update   the Scan Service license secret. | - Obtain your Coverity licenses - Create a Scan Service license secret |
5. If needed, update Helm keys to support any version or secret changes.
6. Ensure that the PostgreSQL database is backed up.
7. Scale down the Coverity Connect web application to 0. For
   example:

   ```
   kubectl scale deployment/${RELEASE}-cim-webapp -n ${NS} --replicas=0
   ```
