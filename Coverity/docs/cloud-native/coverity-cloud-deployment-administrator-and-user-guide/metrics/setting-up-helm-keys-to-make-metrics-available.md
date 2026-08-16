---
title: "Setting up Helm keys to make metrics available"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-helm-keys-to-make-metrics-available.html"
content_id: "~ffSdiajKWgABc5qDqlkkw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:57.272516+00:00"
---

# Setting up Helm keys to make metrics available

During a Coverity cloud deployment, in the `cnc` Helm chart, you can
choose whether or not to make metrics available to the monitoring system such as
Grafana.

Presenting application metrics to the `/metrics` endpoint is disabled by
default in the `cnc` Helm chart. In this case, the
`cim.cimweb.exposeMetrics` Helm key value does not matter since
metrics is disabled. For example:

```
cim:
  cimweb:
    extraProperties:
      connect.enable.metrics: false
```

To enable application metrics, during a deployment, you must change the
`connect.enable.metrics:` value to `true`. Also, set
the `cim.cimweb.exposeMetrics` Helm key to `true` in order
to expose time-series metrics in Prometheus format. For example:

```
cim:
  cimweb:
    exposeMetrics: true
    extraProperties:
      connect.enable.metrics: true
```

See the `cim.cimweb.exposeMetrics` and
`cim.cimweb.extraProperties` Helm keys in cim.cimweb Helm keys.
