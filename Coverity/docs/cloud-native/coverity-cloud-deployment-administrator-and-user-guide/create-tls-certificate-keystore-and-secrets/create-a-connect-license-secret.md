---
title: "Create a Connect license secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-connect-license-secret.html"
content_id: "L7sHMvf4rEVA7MJ8MW2HKA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:02.181044+00:00"
---

# Create a Connect license secret

Create a Coverity Connect license secret that contains the Coverity Connect license. This
license type is a Platform license. Black Duck provides this as a
`license.zip` file that you must uncompress to make the
`license.dat` file available.

The following command creates a license secret for Coverity Connect located in a Coverity
namespace (NS) and containing the Platform license file provided by Black Duck:

```
kubectl create secret generic "${CONNECT_LICENSE_SECRET}" \
  --namespace "${NS}" \
  --from-file=license.dat
```

where:

- `"${CONNECT_LICENSE_SECRET}"` is a string that specifies the name of
  the Connect license secret.
- `"${NS}"` is a string that specifies the Scan Service namespace.
- `license.dat` is the extracted Connect Platform license file provided
  by Black Duck.

When you set the Helm overrides, specify this secret name in the
`licenseSecretName` key as described in Specify the name of the Connect license secret.
