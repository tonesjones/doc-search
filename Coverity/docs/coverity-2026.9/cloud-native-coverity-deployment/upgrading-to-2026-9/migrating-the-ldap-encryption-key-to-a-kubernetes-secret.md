---
title: "Migrating the LDAP encryption key to a Kubernetes Secret"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/migrating-the-ldap-encryption-key-to-a-kubernetes-secret.html"
content_id: "DAdLW1aND~CvwvJtYNcKdw"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:38.955226+00:00"
---

# Migrating the LDAP encryption key to a Kubernetes Secret

Beginning in 2026.9, the LDAP encryption key is stored in a
Kubernetes Secret and referenced through
`cim.ldap.keySecret.existingSecret`.

The `cim.ldap.cimKey.value` Helm key was removed in
2026.9 and is ignored if specified.

Important: If your deployment uses a custom LDAP encryption key, create a
Kubernetes Secret containing the key and configure
`cim.ldap.keySecret.existingSecret` before upgrading to
2026.9.

1. Retrieve the LDAP encryption key from the current
   configuration.

   ```
   cim:
             ldap:
              cimKey:
               value: "<your-key-value>"
   ```
2. Create a Kubernetes Secret that contains the LDAP
   encryption key.

   ```
   kubectl create secret generic <secret-name> \
              --from-literal=key='<your-key-value>' \
              --namespace <namespace>
   ```
3. Configure
   `cim.ldap.keySecret.existingSecret` in
   `values.yaml`.

   ```
   cim:
             ldap:
              keySecret:
               existingSecret: "<secret-name>"
   ```
4. Remove the
   `cim.ldap.cimKey.value` configuration from
   `values.yaml`.
5. Upgrade the deployment.

The deployment uses the LDAP encryption key stored in the
referenced Kubernetes Secret.

If you were previously using the default LDAP encryption key,
no migration is required. If
`cim.ldap.keySecret.existingSecret` is not
configured, the chart uses a chart-managed Secret that contains
the default LDAP encryption key.

Important: If your deployment previously used a custom
LDAP encryption key and
`cim.ldap.keySecret.existingSecret` is not
configured before upgrading, the deployment falls back to the
default LDAP encryption key. LDAP authentication can fail until
the original encryption key is restored.

Important: `helm rollback` is not
supported for this change.

To return to a previous chart version, use:

```
helm upgrade <release> <chart> --version <previous-version>
```
