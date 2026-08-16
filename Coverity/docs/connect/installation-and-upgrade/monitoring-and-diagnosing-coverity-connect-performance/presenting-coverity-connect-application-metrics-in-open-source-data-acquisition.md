---
title: "Presenting Coverity Connect application metrics in open-source data acquisition and monitoring software"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/presenting-coverity-connect-application-metrics-in-open-source-data-acquisition-and-monitoring-software.html"
content_id: "xNHD9Pp1y9qfZczlRxWCmw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:22.670366+00:00"
---

# Presenting Coverity Connect application metrics in open-source data acquisition and monitoring software

Coverity generates application metric data that enables you to monitor the performance of
your Coverity scans. This metric data can be exported to open-source data acquisition
and monitoring software such as Prometheus and Grafana, enabling you to monitor Coverity
performance.

You can use any of a number of applications to visualize analytics. Black Duck does not
support any specific analytics and interactive visualization web applications. However,
common solutions include:

- Prometheus-master/Grafana
- DataDog
- NewRelic

Note: For information on setting up and working with metrics in a
Coverity cloud deployment, refer to the "Metrics" section in the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide.

To present Coverity Connect metrics, an administrator needs to complete the following
configuration processes which are described in the sections that follow:

- Make Connect metrics available to the
  aggregator tool
- Set up aggregar and presentation tools
  to present the metrics

In this section:

- Coverity Connect application metrics
