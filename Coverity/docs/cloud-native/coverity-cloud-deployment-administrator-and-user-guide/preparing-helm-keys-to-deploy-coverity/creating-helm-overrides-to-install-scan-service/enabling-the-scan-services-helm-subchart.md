---
title: "Enabling the scan-services Helm subchart"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/enabling-the-scan-services-helm-subchart.html"
content_id: "Wfh9zgj6zUl9sqR1moQmbg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:38.412187+00:00"
---

# Enabling the scan-services Helm subchart

In order to be able to deploy the Scan Services, in the `cnc` chart, you
need to set the `scan-services.enabled` Helm key to
`true`. This enables use of the `scan-services` Helm
subchart and allows deployment of Scan Services as configured in the
`scan-services` subchart.

For example, in the `cnc` chart:

```
scan-services:
  enabled: true
```

As described in cnc Helm chart and the Chart.yaml file, this satisfies the
`scan-services` dependency located in the `Chart.yaml`
file within the `cnc` chart.

Note: This Helm key enables use of the `scan-services`
subchart which in turn can deploy Scan Services in Kubernetes as configured in the
`scan-services` subchart.

See also scan-services.enabled Helm key.
