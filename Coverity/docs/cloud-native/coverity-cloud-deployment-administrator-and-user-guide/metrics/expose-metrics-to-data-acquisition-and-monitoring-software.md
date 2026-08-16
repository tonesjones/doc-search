---
title: "Expose metrics to data acquisition and monitoring software"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expose-metrics-to-data-acquisition-and-monitoring-software.html"
content_id: "VFOuXJkntIMRBKA~dCbVpQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:57.918891+00:00"
---

# Expose metrics to data acquisition and monitoring software

In your Helm file (i.e.`values.yaml`), you can configure the Coverity
services (Web service, Cache service, Scan Service and Storage Service) to expose
time-series data to data acquisition and monitoring software (for example, Prometheus
and Grafana) or hide the data.

All Coverity cloud containers can be configured to expose time-series metrics on a
port/path. By default, metrics is exposed for all Coverity services. If needed, you can
use the following helm keys to override exposure of metrics on a service-by-service
basis:

Table 1. Exposing or hiding metrics for each service

| Service | Helm key | Value | Refer to |
| --- | --- | --- | --- |
| CIM web | `cim.cimweb.​exposeMetrics` | - `true` = expose time series metrics in Prometheus   format. (Default) - `false` = Do not expose time series metrics. | cnc Helm chart: Helm keys |
| Cache Service | `cache-service.​​exposeMetrics` | - `true` = expose time series metrics in Prometheus   format. (Default) - `false` = Do not expose time series metrics. | scan-services Helm subchart: Helm keys |
| Scan Service | `scan-service.​observability.​exposeMetrics` | - `true` = expose time series metrics in Prometheus   format. (Default) - `false` = Do not expose time series metrics. |
| Storage Service | `storage-service.​observability.​exposeMetrics` | - `true` = expose time series metrics in Prometheus   format. (Default) - `false` = Do not expose time series metrics. |
