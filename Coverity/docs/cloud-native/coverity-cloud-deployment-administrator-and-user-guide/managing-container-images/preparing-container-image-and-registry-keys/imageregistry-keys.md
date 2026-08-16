---
title: "imageRegistry keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/imageregistry-keys.html"
content_id: "EDeqHcKMto1Dhn9dQFKNug"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:41.846664+00:00"
---

# imageRegistry keys

The `imageRegistry` Helm key, shown below, specifies the registry from
which you pull container images. Depending on whether you will install directly from the
Black Duck private registry or from your own registry,
define the `imageRegistry` Helm key.

The image registry key can be configured as a global key or as service-specific keys that
override the global key:

- `global.imageRegistry` key

  Note: The `global.imageRegistry` key is present
  in both the `cnc` chart and the `scan-services`
  subchart.
- `cnc` chart, `imageRegistry` key
- `scan-services` chart, `imageRegistry` key

The following default key value enables you to define the registry within a script:

```
imageRegistry: "COVERITY_IMAGE_REGISTRY"
```

To install from images in the Black Duck private image registry, you can set the
following value:

```
imageRegistry: repo.blackduck.com/containers/
```

To install from images in your own private image registry, enter your registry URL.

The `imageRegistry` key can be configured as a global key or as
service-specific keys that override the global key:

- `global.imageRegistry` key

  Note: The `global.imageRegistry` key is present
  in both the `cnc` chart and the `scan-services`
  subchart.
- `cnc` chart, `imageRegistry` key
- `scan-services` chart, `imageRegistry` key

See also:

- Global Helm keys.
- Root Helm keys.
