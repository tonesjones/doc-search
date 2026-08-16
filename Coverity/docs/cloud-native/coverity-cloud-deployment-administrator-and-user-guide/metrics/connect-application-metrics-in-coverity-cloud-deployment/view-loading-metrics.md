---
title: "View loading metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/view-loading-metrics.html"
content_id: "S_ycYIcg5zpjTcjoWfBozw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:07.796909+00:00"
---

# View loading metrics

These metrics present Connect view loading latency and count statistics. You can use them
to assess the health and performance of Connect view loading requests and issue queries.

Table 1 describes view loading
request and latency metrics.

Table 1. View Loading metrics

| Metric | Description | Metric type | Examples: PromQL queries |
| --- | --- | --- | --- |
| `connect_stop_​watch_​duration_​histogram_​bucket` | **View loading latency**  This metric is a Histogram that indicates the view loading latency. | Histogram | `connect_stop_watch_​duration_​histogram_​bucket​{topic_key="*/reports/*"}` The `connect_stop_watch_​duration_histogram_​bucket` metric is derived from the `connect_stop_watch_​duration_​histogram` metric.  In this PromQL query example, `topic_key` can point to other REST API URLs such as `*/config/projects/*` or`*/config/streams/*` to get latency for other REST endpoints. |
| **Interpreting the metric**  The view loading latency histogram should follow the original baseline values for the most frequently-occurring latency. Values that show a longer than expected latency and higher than expected occurrence indicate a latency issue which might be caused by connection delays or insufficient resources (CPU, disk, memory). | | |
| `connect_stop_​watch_​duration_​histogram_​count` | **View loading requests count.**  This metric is a histogram counter that provides a running count of the number of view loadings completed since the last Connect start-up. | Histogram counter | `connect_stop_watch_​duration_​histogram_count​{topic_key="*/reports/*"}` The `connect_stop_watch_​duration_​histogram_​count` metric is derived from the `connect_stop_watch_​duration_histogram` metric.  In this PromQL query example. `topic_key` can point to other REST API URLs such as `*/config/projects/*` or `*/config/streams/*`, to get request counts for other REST endpoints. |
| **Interpreting the metric**  If views are being loaded, this number is expected to increase. The slope of this graph indicates how busy the system is at loading views. | | |
