---
title: "Java options"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/java-options.html"
content_id: "JARN91lD5LSxrp5lYbsXFg"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:31.699173+00:00"
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
