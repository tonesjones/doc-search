---
title: "Setting up metrics presentation"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-up-metrics-presentation.html"
content_id: "OJ4v8eLXR_yPFxY8wAdfOw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:25.122537+00:00"
---

# Setting up metrics presentation

Coverity Connect makes telemetry data available as described above. As a customer, you
need to set up your software to ingest, store, and use telemetry data effectively. You
need to:

- Choose and deploy telemetry aggregator tools.
- Set up a query interface.
- Set up dashboards.
- Set up alerts.
- Set up exporters, or ensure that all infrastructure is exposing metrics and that
  these are scrapeable by their aggregators.

For example, you might configure a Prometheus server that is connected to a Grafana
Dashboard system.

Refer to documentation provided with your open-source data acquisition and monitoring
software.
