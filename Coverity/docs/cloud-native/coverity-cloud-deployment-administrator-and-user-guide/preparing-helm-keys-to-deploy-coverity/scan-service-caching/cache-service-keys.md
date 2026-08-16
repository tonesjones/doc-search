---
title: "Cache Service keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cache-service-keys.html"
content_id: "bvQ5L~P7mlDONarq56JGbQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:50.030552+00:00"
---

# Cache Service keys

The following keys enable Cache Service and provide the . You can modify values as needed
for your deployment. For information on the keys, refer to the section, scan-services Helm subchart: Helm keys. You especially need to verify or set the
following:

Enable Cache Service so that it is installed:

```
cache-service:
  enabled: true
```

Specify the name of the Cache Service bucket:

```
cache-service:
  bucketName: ""
```

Specify the Cache Service image version.

```
cache-service:
  version: "CACHE_SERVICE_VERSION"
```

You can accept the default values for the following keys or change as needed:

- the Cache Service image name
- the Cache Service registry name
- the Cache Service logging level

```
cache-service:
  image: "cache-service"
  registry: ""
  logLevel: "INFO"
```
