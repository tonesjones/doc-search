---
title: "Configure LDAP"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-ldap.html"
content_id: "F8X4YeNkZ3h1D4BO7yvXOA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:40.373035+00:00"
---

# Configure LDAP

If you use LDAP, you need to configure and maintain LDAP, and add the LDAP certificate to
the Connect truststore ConfigMap.

## Configure LDAP for the first time

If you use LDAP and are deploying Coverity cloud for the first time, you must
configure LDAP using the Coverity Connect UI as described in the section "Integrating with LDAP
servers" in the Coverity Platform 2026.6.0 User and Administrator Guide.

## Change configured LDAP values

If you have have already deployed Coverity in the cloud and configured LDAP, you can
change configured LDAP values using the `cim.ldap` Helm keys. To
update a configured LDAP value:

1. Enter the new value in the in the relevant `cim.ldap` Helm
   key. For example, to change the bind password to a new secret:

   ```
   cim
     ldap
       bindPassword: "LDAPpasswordSecretNew"
   ```
2. Set the `updateConfig` key as `true` to enable
   LDAP updates:

   ```
   cim:
     ldap:
       updateConfig: true
   ```
3. Apply the change using the helm upgrade command: For example:

   ```
   helm upgrade cnc -f values.yaml
   ```

For information on the `cim.ldap` Helm keys, refer to cim.ldap Helm keys.

## Add the LDAP certificate to the Connect truststore ConfigMap

For TLS LDAP, add the LDAP certificate to the `connect-trust-stores`
ConfigMap as described in Creating a truststore ConfigMap for a Connect instance.
