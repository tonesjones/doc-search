---
title: "Specify the name of the Scan Service license secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specify-the-name-of-the-scan-service-license-secret.html"
content_id: "4sdixjdHHvKPv~LfXxgiIg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:39.714467+00:00"
---

# Specify the name of the Scan Service license secret

In the `scan-services` chart, specify the name of the Scan Service license
secret that contains the Coverity Analysis license. Use the secret name that you created
earlier in Create a Scan Service license secret.

1. Set the Scan Service license secret name in the `licenseSecretName`
   Helm
   key:

   ```
   scan-service.​licenseSecretName: ${SCAN_SERVICE_LICENSE_SECRET}
   ```

   where
   `${SCAN_SERVICE_LICENSE_SECRET}` is a string variable that
   specifies the name of the Scan Service license secret. Refer to:

   - Create a Scan Service license secret
   - `scan-service.licenseSecretName` Helm key in the
     `scan-services` subchart scan-service Helm keys.
