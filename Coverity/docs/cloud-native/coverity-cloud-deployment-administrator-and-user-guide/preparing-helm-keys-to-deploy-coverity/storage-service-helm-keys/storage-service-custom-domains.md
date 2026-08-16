---
title: "Storage service custom domains"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/storage-service-custom-domains.html"
content_id: "hPP~_jOwxyuF8i86E3WpwQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:43.695427+00:00"
---

# Storage service custom domains

If you are using custom domains for storage service, when you create a domain, you also
need to specify the URL of each domain as
`storage.service.custom.domains` annotations in the Helm chart. This
sets the Content Security Policy (CSP) in the ingress controller to enable secure access
to the custom domain. This applies with any cloud or on-prem platform that uses storage
service custom domains.

The custom domain URL values must comply with the following requirements:

- You can specify multiple domains separated by commas. For example:
  `storage.example.com, *.example.com`
- If the `storage.service.custom.domains` property is provided without
  a value, the default value must be an empty string: `""`.

The following examples demonstrate valid domain name formats:

- standard subdomain names: `storage.example.com`
- wildcard prefix: `*.example.com`

The following are default custom domain names: If you use one of these domains, you do
not need to create a `storage.service.custom.domains` annotation.

- For AWS storage: `*.amazonaws.com`
- For Google storage: `storage.googleapis.com`
- For Azure blob storage: `*.blob.core.windows.net`

Note: For custom domains such as `*.blob.core.<customDomain>.net`, you need to configure the custom
domain properties as described in the custom domain sections that follow.

Invalid domains are logged with a Warning and are not added to the ingress Content
Security Policy. For example:

- If a domain name contains illegal characters (space, consecutive dots, etc.), a
  Warning is logged and the domain is not added to the ingress Content Security
  Policy.
- If an invalid domain is encountered, a Warning is logged and the domain is not added
  to the ingress Content Security Policy.

Important: If you are using a custom domain with Microsoft
Azure Entra ID, see also Using an Azure Entra ID client secret for RBAC and storage-service.azure Helm keys.

## Configure storage service custom domain properties using Helm annotations

To configure storage service custom domain properties, including the domain URL,
using annotations in the Helm chart:

Use the `cim.cimweb.extraProperties` Helm key in the
`cnc` chart. The following example configures a custom domain
with the URL `storage.example.com`: See also cim.cimweb Helm keys.

```
cim:
  cimweb:
    extraProperties:
    - storage.service.custom.domains: <custom-domain-url>
```

For example:

```
cim:
  cimweb:
    extraProperties:
    - storage.service.custom.domains: "*.example.com"
```

Note: When using a *, ?, &, # within a value in a Helm chart,
encase the value within quotes. Other requirements exist.

## Minio: Set storage service custom domain properties on the Minio host

If you are using Minio, when you set custom domains using
`cim.cimweb.extraProperties:`, you must also set the custom
domain values on the Minio host. For example, you can create a
`minio.yaml` file in which you specify the custom domain
hostname, with the path:

```
fullnameOverride: "cnc-minio"
 
  image:
    debug: true
 
  ingress:
    enabled: true
    ingressClassName: nginx
    hostname: <INGRESS_DOMAIN>
```

where `<INGRESS_DOMAIN>` is the full path of the storage service
custom domain that is configured in
`cim.cimweb.extraProperties:`.

Note: To apply these changes, you must include the new
`minio.yaml` override file in any `helm upgrade`
or `helm install` command.

## Custom storage service domain: Create a truststore ConfigMap and enable a scan service certificate

1. Create a configmap that contains the custom certificate (.crt). For example,
   for `minio.crt`:

   ```
   kubectl create configmap connect-trust-stores \          
                   --from-file=minio.crt=<cert-path>/minio.crt -n <namespace>
   ```

   The default trust stores ConfigMap name for Coverity Connect is
   `connect-trust-stores`, which is the default value of the
   Helm key `global.trust-stores.configmapName:
   "connect-trust-stores"`. The following example creates a
   connect-trust-stores ConfigMap:

   ```
   kubectl create configmap connect-trust-stores \          
                   --from-file=minio.crt=/opt/trust-stores/ssl/minio.crt -n <namespace>
   ```
2. In the `scan-services` Helm chart `values.yaml`
   file, enable the global truststore:

   ```
   global:
     trust-stores:
       configmapName: "connect-trust-stores"
       enabled: true
   ```

   or use the override:
   `scan-services.trust-stores.enabled: true`
3. In the `scan-services` Helm chart `values.yaml`
   file, set the following scan-service `TLS_CUSTOM` environment
   variables:

   ```
   scan-service:
     environment:
       TLS_CUSTOM_CERT_PATH: /opt/trust-stores/ssl/<your-custom-cert>
       TLS_CUSTOM_ENABLED: true
   ```

   For example, to specify `minio.crt` in the path
   `/opt/trust-stores/ssl/`:

   ```
   TLS_CUSTOM_CERT_PATH: /opt/trust-stores/ssl/minio.crt
   ```

   For further information on these Helm keys, see scan-service.environment Helm keys in the chapter: scan-services Helm subchart: Helm keys.

## Custom S3 storage service domain: Configure MinIO for storage service

Note: The examples that follow override
`scan-services` Helm chart values.

1. Set `storage-service.endpoint.internal.url` and
   `storage-service.endpoint.external.url` to the storage
   endpoint:

   ```
   storage-service:
     endpoint:
       external:
         url: <storage-endpoint-url>
       internal:
         url: <storage-endpoint-url>
   ```
2. Create an S3 storage bucket secret with credentials.
3. In the `scan-services` chart `values.yaml`
   file, configure S3 storage bucket information:

   ```
   storage-service:
     s3: 
       bucket: <storage-bucket-name>
       region: <storage-bucket-region>
       secret:
         name: <storage-bucket-secret-name>
     storageType: s3
   ```

## Apply changes to a running depoyment

If you made any Helm chart changes (overrides, annotations, property values, etc) to
a running deployment, to apply the changes, you need to pass the Helm overrides to
the running deployment. For example, you can perform a `helm
upgrade`.

## Specify custom domains in the cim.properties file

The following is an Administrator task. For any and all custom domains that you
create, you need to add the URLs into the `cim.properties` file using
the following example syntax, where the URLs are separated by commas:

```
# Coverity cloud deployment: Administrator: Specify any Storage Service custom domains. (Separate multiple domains with commas)
storage.service.custom.domains= *.example.com, *.abcd.com
```

Note: For information on specifying custom domains in the
`cim.properties` file, refer to Using the Coverity Point and Scan UI.
