---
title: "Creating a truststore ConfigMap for a Connect instance"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/creating-a-truststore-configmap-for-a-connect-instance.html"
content_id: "mx30PKB6cbyb9wmKht~Fqw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:10.815941+00:00"
---

# Creating a truststore ConfigMap for a Connect instance

When creating a truststore ConfigMap for a Coverity Connect instance, consider the
following notes:

Note: You must have all public key certificates that you need to
include in the truststore ConfigMap. The certificates must be in PEM (Privacy-Enhanced
Mail) format.

Note: If you deploy more than one Connect instance, you need to create
a Kubernetes truststore ConfigMap for each Coverity Connsct instance. The truststore
ConfigMap holds public certificates that identify a Connect server.

Note: If the setup involves a certificate chain, ensure that each
intermediate certificate is concatenated to the server certificate. For example, if a
PostgreSQL server is set up on TLS and uses a chain of certificates, concatenate the
intermediate certificate(s) to the PostgreSQL server certificate.

Note: ConfigMaps are for non-sensitive data. Never store sensitive
information like Jira passwords or API tokens directly in a ConfigMap. Use Kubernetes
secrets for such data and reference the secrets.

To add certificates and create a truststore ConfigMap for a Coverity Connect
instance:

1. Using the `kubectl create configmap` command, create a truststore
   ConfigMap that contains the truststore certificates. For
   example:

   ```
   kubectl create configmap "${TruststoreConfigmapName}" \
     --from-file=postgres-root.pem="${PostgresRootCert}" \
     --from-file=proxy-server.pem=<proxy-server.pem> \
     .
     .
     --from-file="${LDAPRootCert}" \
     --from-file="${JiraCert}" \
     --from-file="${BugzillaRootCert}" \
      -n "${NS}"
   ```

   where the following are string variables:

   - `"${TruststoreConfigmapName}"` is the name of the truststore
     ConfigMap that you are creating The default name in the Helm
     `global.trust-stores.configmapName` Helm key is
     `"connect-trust-stores"`. If you use another name, you
     will need to override the `global.trust-stores.configmapName`
     Helm key.
   - `"${PostgresRootCert}"` is the file name of the PostgreSQL
     root certificate file. Add the root certificate for the TLS-enabled
     PostgreSQL database instance to the ConfigMap. The PostgreSQL root
     certificate must be in the key `postgres-root.pem`.

     Important: The PostgreSQL root certificate
     must be named `postgres-root.pem`.
   - `"${ProxyServerRootCert}"` is the name of the proxy server
     root certificate file.
   - `"${JiraCert}"` is the name of the Jira certificate
     file.
   - `"${LDAPRootCert}"` is the name of the LDAP root certificate
     file.
   - `"${BugzillaCert}"` is the name of the Bugzilla certificate
     file.
   - `"${NS}"` is the Connect namespace.

   The filenames are not important, since all files are loaded into a directory
   and then into the Connect truststore.

   For
   example:

   ```
   kubectl create configmap connect-trust-stores \
        --from-file=postgres-root.pem=<postgres-root.pem> \
        --from-file=proxy-server.pem=<proxy-server.pem> \
        --from-file=<LDAP-root-cert> \
        --from-file=<Jira-root-cert> \
        --from-file=<Bugzilla-root-cert> \
        --namespace "$NS"
   ```
2. Load the ConfigMap into the Connect truststore using Helm keys as described in Preparing Helm keys to deploy Coverity. For truststore Helm keys, refer to trust-stores: ConfigMap Helm keys - Connect cim specific.

## Truststore ConfigMap Helm keys

You need to enable truststores by overriding the
`trust-stores.enabled` Helm key with `true`, and
if you did not use the default Connect truststore ConfigMap name,
`"connect-trust-stores"`, you need to override the default
`trust-stores.configmapName` Helm key value with the actual
truststore ConfigMap name. You can override either the `global` Helm
key values, or to impact only the `cnc` chart, override the
`cnc` chart chart Helm key values.

The following are the `global` Helm keys. For reference information on
the following `global` ConfigMap Helm keys, refer to global.trust-stores Helm keys.

```
global:
  trust-stores:
    configmapName: "connect-trust-stores"
    enabled: false
```

The following are the `cnc` chart Helm keys. For reference information
on the following `cnc` chart Helm keys, refer to trust-stores: ConfigMap Helm keys - Connect cim specific.

```
trust-stores:
  configmapName: ""
  enabled:
```
