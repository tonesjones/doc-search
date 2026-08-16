---
title: "Setting up Helm keys to add annotations for scraping"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-helm-keys-to-add-annotations-for-scraping.html"
content_id: "UwYD1d5x3sKlimiiHTNROQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:58.562427+00:00"
---

# Setting up Helm keys to add annotations for scraping

Cloud native Connect also has the following Helm overrides set to `true`
by default.

```
# cnc chart:

cim:
  cimweb:
    exposeMetrics: true
  
# scan-services chart:

cache-service:
  exposeMetrics: true
  
scan-service:
  exposeMetrics: true
  
storage-service:
  exposeMetrics: true
```

When these Helm overrides are set to `true`, annotations are added to
containers which tell an aggregator whether to scrape metrics data or not, and the
port/path to use.

Note: The following annotations are added by the Helm chart and should
not be added manually:

- `prometheus.io/port: "8089"`
- `prometheus.io/scrape: true`
- `prometheus.io/path: "/abcdef/metrics"`

  where
  `/abcdef` is the Connect web application context path
  specified in the `cim.cimweb.contextPath` Helm key.

Metrics must be **pulled** from a containers’ port/path. Therefore, containers do not
need to know about the metrics aggregator. All Connect application metrics are published
at the `/metrics` endpoint on port `8089` (configured in
Helm charts as described above) by default. This endpoint is not available on any other
port. **For security purposes, visiting the `/metrics` endpoint will
throw a 403 forbidden status code**.
