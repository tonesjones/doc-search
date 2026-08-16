---
title: "MinIO cache Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/minio-cache-helm-keys.html"
content_id: "Ec336rojKEhQxBSNRFVo9A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:56.586680+00:00"
---

# MinIO cache Helm keys

Set the `cache-service.minio:` keys as needed by the Cache Service.
For information on the keys, see also the section, cache-service.minio Helm keys. You can accept the default value
for some MinIO keys.

For MinIO, to enable communications with the cache service, set the following MinIO keys:
The following MinIO keys are needed by cache service:

- `cacert`: If TLS is enabled, specify the CA certificate.
- `host`: Specify the MinIO host name.
- `port`: MinIO port. Accept the default value.
- `secret`: Specify the name of the MinIO secret that contains the
  MinIO root username and root password.
- `secure`: needs to be 'true' if TLS is enabled.
- `verifyHostName`: If Host name need to be verified for MinIO
  communication in case TLS enabled.

For example:

```
cache-service:
  minio:
    cacert: "myCertificate"
    host: "myHost"
    port: 9000
    secret: "minioSecret"
    secure: true
    verifyHostName: true
```

The default values for the MinIO Helm keys are:

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
