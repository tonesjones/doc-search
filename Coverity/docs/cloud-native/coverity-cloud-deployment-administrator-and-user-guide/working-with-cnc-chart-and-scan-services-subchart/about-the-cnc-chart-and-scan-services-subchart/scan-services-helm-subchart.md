---
title: "scan-services Helm subchart"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scan-services-helm-subchart.html"
content_id: "jNf7yh8BOdDR2LoMzKzZyQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:14.843854+00:00"
---

# scan-services Helm subchart

Important: The `scan-services` Helm
subchart is not used with a Connect-only deployment. If the deployment is Connect-only,
in the chart, the `scan-services.enabled` Helm key value must be
`false`.

As defined in the parent cnc chart's `Chart.yaml` file, the
`scan-services` Helm subchart is a dependency subchart that is
bundled within the cnc Helm chart. The `scan-services` chart's
`Chart.yaml` file is:

```
apiVersion: v2
name: scan-services
description: scan services
type: application
version: 0.0.1
appVersion: "2026.6.0"
keywords:
  - scan-services
```

For information on the Helm key that satisfies the `scan-services` chart
dependency, see also Enabling the scan-services Helm subchart and scan-services.enabled Helm key.

The `scan-services` Helm subchart includes the following services as
defined in scan-services Helm subchart: Helm keys:

- cache-service
- common-infra
- ingress
- postgres
- scan-service
- storage-service
- trust-stores

## Working with subchart overrides

When overriding any `scan-services` Helm subchart key from outside the
`scan-services` subchart `values.yaml` file, you
must precede the key name with `scan-services` to identify the key as
a `scan-services` chart key.

```
scan-services:
  cache-service:
    #overrides
  scan-service:
    #overrides
  storage-service:
    #overrides
```

For example, to enable the cache service from a command line or script, the syntax
for the Helm key:

```
cache-service.enabled: true
```

must be:

```
scan-services.cache-service.enabled: true
```

Alternatively, within a yaml file other than the subchart's
`values.yaml` file, the syntax is:

```
scan-services:
  cache-service:
    enabled: true
```

For further information on subcharts, see [Subcharts and Global Values](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/).
