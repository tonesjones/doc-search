---
title: "Java options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/java-options.html"
content_id: "JARN91lD5LSxrp5lYbsXFg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:31.249204+00:00"
---

# Java options

The following Helm keys specify additional Java options to add to a Connect invocation.

- `cim.cimweb.javaOpts` in the `cnc` chart. See
  cnc Helm chart: Helm keys.
- `cache-service.javaOpts` in the `scan-services`
  chart. See scan-services Helm subchart: Helm keys.

To see default cimweb options, run:

```
docker run --rm -ti COVERITY_IMAGE_REGISTRY/cim-web:COVERITY_IMAGE_VERSION cat cim.sh
```
