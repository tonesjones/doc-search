---
title: "Configuring Helm keys to support onPrem or non-platform-specific deployments using Redis and Minio"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-helm-keys-to-support-onprem-or-non-platform-specific-deployments-using-redis-and-minio.html"
content_id: "D1bSyEBnoj8opFGJ8B7KSw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:59.481287+00:00"
---

# Configuring Helm keys to support onPrem or non-platform-specific deployments using Redis and Minio

Note: Some of the following examples use sample values for this
configuration.

Also refer to the following:

- For `scan-services` subchart Helm key descriptions and default values, see
  scan-services Helm subchart: Helm keys.
- For AWS-specific infrastructure setup procedures, see Amazon AWS infrastructure and configuration.
- For Redis and Minio, see also Setting up onPrem OCI Redis, MinIO, and PostgreSQL for Scan Service.

Important:

When overriding any `scan-services` Helm subchart key from outside the
`scan-services` subchart `values.yaml` file, you must
precede the key name with `scan-services` to identify the key as a
`scan-services` chart key:

```
scan-services:
  cache-service:
    #overrides
  scan-service:
    #overrides
  storage-service:
    #overrides
```

For information on subcharts and overrides, see scan-services Helm subchart
and [Subcharts and Global Values](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/).

If you are using Redis and Minio in an on-prem environment, you need to configure the
following Helm keys.

Important: Unless otherwise noted, the Helm keys in this
section are in the `scan-services` subchart.

1. In the `cnc` Helm chart, change the
   `scan-services.enabled:` Helm key to `true` to enable the
   `scan-services` Helm chart and feature.

   ```
   scan-services:
     enabled: "true"
   ```
2. Select the storage provider, Minio:

   ```
   cache-service:
     storageProvider: "minio"
   ```

   Note: Valid platform providers include: `"aws" | "azure" |
   "gcp" | "minio"`
3. Select the storage service, for this instance,
   Minio:

   ```
   storage-service:
     storageType: "minio"
   ```

   Note: Valid storage types include:
   `"s3" | "s3Express" |"azure" | "gcs"`
4. After creating the storage bucket, in the following Helm key, set the name of the storage
   bucket used by the cache service. For example, "cncMinioBucket".

   ```
   cache-service:
     bucketName: "cncMinioBucket"
   ```
5. Verify that the cache service is enabled. For cache service to be enabled, the following
   key must be `true`. This causes capture and analysis output to be
   cached:

   ```
   cache-service:
     enabled: true
   ```
6. For Minio, configure the following cache service Minio
   keys.

   ```
   cache-service:
     minio:
       cacert: ""
       host: ""
       port: 9000
       secret: ""
       secure: true
       verifyHostName: true
   ```

   - `cacert:` The CA certificate to be used for Minio Communication if TLS
     is enabled.
   - `host:` Minio host.
   - `port:` Minio Port.
   - `secret:` The Minio secret containing both the Minio root-user and
     root-password.
   - `secure:` If TLS enabled for communication with Minio.
   - `verifyHostName:` If TLS is enabled, this is a boolean value that
     determines whether or not the host name is verified for Minio communication.
7. For Minio, after creating the storage, configure the following keys to provide Minio
   access to the storage:

   ```
   storage-service:
     minio:
       bucket: ""
       region: ""
       secret:
         name: ""
   ```

   - The name of the storage bucket.
   - The region of the storage bucket.
   - The name of the secret that contains the keys root-user, root-password keys.
8. For Minio, if you are using custom domains for storage service, you must also configure
   the storage service custom domain properties as described in Storage service custom domains.
9. Configure the following global Redis keys or see the next step to configure cache service
   specific Redis. See the Helm key descriptions in the next
   step:

   ```
   global:
     redis:
       authEnabled: false
       cacertSecret: ""
       host: ""
       passwordSecret: ""
       port: 6379
       secure: false
       verifyHostName: false
   ```
10. Configure the following Redis keys as needed for the cache service:

    ```
    cache-service:
      redis:
        authEnabled:
        cacertSecret: ""
        database: "1"
        host: ""
        passwordSecret: ""
        port:
        secure:
        verifyHostName:
    ```

    - `authEnabled:` Enable authentication for Redis. If you set this value
      to `true`, you must also configure
      `passwordSecret:`.
    - `cacertSecret:` The secret that contains the CA certificate which is
      used for Redis communication if TLS is enabled. The secret must contain the
      `ca.crt` key.
    - `database:` Redis database
    - `host:` Redis Host
    - `passwordSecret:` Secret containing Redis password (must contain a key
      named `password`) considering Redis is secured with password
    - `port:` Redis Port
    - `secure:` If TLS enabled for communication with Redis
    - `verifyHostName:` If TLS is enabled, this is a boolean value that
      determines whether or not the host name is verified for Redis communication.
11. You can use the default values for the following cache service readiness probe Helm
    keys.

    ```
    cache-service:
      readinessProbe:
      initialDelaySeconds: 30
      periodSeconds: 180
      timeoutSeconds: 60
      failureThreshold: 3
    ```
