---
title: "Create a Scan Service license secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-scan-service-license-secret.html"
content_id: "ja1ZBx45TVc6~Pk_KMJFqw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:05.430180+00:00"
---

# Create a Scan Service license secret

If you deploy Scan Service, you need to create a Scan Service license secret that
contains the Scan Service license. This license type is a SAVE license. Black Duck
provides this as a `license.zip` file that you must uncompress to make
the `license.dat` file available.

The following command creates a license secret for the Coverity Scan Service located in a
specified namespace (NS) and containing the SAVE license file provided by Black Duck:

```
kubectl create secret generic "${SCAN_SERVICE_LICENSE_SECRET}" \
  --namespace "${NS}" \
  --from-file=license.dat
```

where:

- `"${SCAN_SERVICE_LICENSE_SECRET}"` is a string that specifies the
  name of the Scan Service license secret.
- `"${NS}"` is a string that specifies the Scan Service namespace.
- `license.dat` is the extracted Scan Service SAVE license file
  provided by Black Duck.

When you set the Helm overrides, specify this secret name in the licenseSecretName key as
described in Specify the name of the Scan Service license secret. This license will be
used by runners at runtime.
