---
title: "Preconfigured container image keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/preconfigured-container-image-keys.html"
content_id: "_6UMdZByUteFcadPapO8qw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:41.193741+00:00"
---

# Preconfigured container image keys

The following container image keys are preconfigured for the Coverity release and do not need
to be changed:

```
# cnc chart:
cim.cimdownloads:
    image: "cim-downloads"
    registry: ""
    version: "CIM_VERSION"
cim.cimtools:
    image: "cim-tools"
    registry: ""
    version: "CIM_VERSION"
cim.cimweb:
    image: "cim-web"
    registry: ""
    version: "CIM_VERSION"
cim.cimweb.tlsSidecar:
    image: "nginx"
    version: "1.27.4"

# scan-services chart:
cache-service:
  image: "cache-service"
  registry: ""
  version: "CACHE_SERVICE_VERSION"

common-infra:
  image: "common-infra"
  registry: ""
  version: "COMMON_INFRA_VERSION"

scan-service:
  image: "scan-service"
  registry: ""
  version: "SCAN_SERVICE_VERSION"

scan-service.migrateJob:
  image: "scan-service-migration"
  registry: ""
  version: "SCAN_SERVICE_VERSION"

storage-service:
  image: "storage-service"
  registry: ""
  version: "STORAGE_SERVICE_VERSION"

storage-service.migrateJob:
  image: "storage-service-migration"
  registry: ""
  version: "STORAGE_SERVICE_VERSION"
```

For further information on these Helm keys, refer to the keys in the related sections:

- cnc Helm chart: Helm keys
- scan-services Helm subchart: Helm keys
