---
title: "Storage Service metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/storage-service-metrics.html"
content_id: "Gr0Ln2cbdW0TCiWjDDwCLQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:11.351752+00:00"
---

# Storage Service metrics

The following table describes Storage Service metrics.

Table 1. Storage service metrics

| Metric | Description | Metric type | Examples: PromQL queries |
| --- | --- | --- | --- |
| `coverity_​storage_​service_​duration_​histogram_​microseconds_​bucket` | **Storage latency histogram**  The `coverity_storage_service_duration_histogram_microseconds_bucket` metric is a histogram that lists the storage latencies.  **Interpreting the metric**  The Storage Latency histogram should follow the baseline values for the most occurring latency. If the Storage Latency shows a bucket of slower than expected latency and higher than expected occurrence, then it means there is a latency issue or the resources available are insufficient (see CPU, disk and memory usage). | | |
| `coverity_​storage_​service_​duration_​histogram_​microseconds_​bucket` | **Storage latency quantiles**  The `coverity_storage_service_duration_histogram_microseconds_bucket` metric is a histogram that lists the storage latencies and can but additionally setup to use histogram quantiles to alternatively visualize the Storage Latencies.  **Interpreting the metric**  The Storage Latency Quantiles should follow the baseline values for the most occurring latency. The Storage Latency Quantile makes it easier to see the 50, 90, and 99th quantile to better understand the performance of the storage service. | | |
| `coverity_​storage_​service_​duration_​histogram_​microseconds_​count` | **Storage GRPC codes**  The `coverity_storage_service_duration_histogram_microseconds_count` metric is a graph that show the rate of the various Storage GRPC Codes.  **Interpreting the metric**  Any of the codes increasing in rate is an indication of how busy the storage system is. The main status codes of interest here are the non-zero ones since they indicate issues with the storage system. Refer to the specific status code to help identify the issue. | | |
