---
title: "Scan Service metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scan-service-metrics.html"
content_id: "GKkh~WWiND6aFw0NQ209jQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:10.683137+00:00"
---

# Scan Service metrics

The following table describes Scan Service metrics.

Table 1. Scan service metrics

| Metric | Description |
| --- | --- |
| `coverity_scan_service_​duration_histogram_​microseconds_count` | **Scan count rate**  The `coverity_scan_service_​duration_​histogram_​microseconds_​count` metric is a graph that shows the current rate of scans.  **Interpreting the metric**  If there are active scans completing, then this number is expected to increase, the slope of this graph indicates how busy the scan system is. |
| `coverity_scan_service_​duration_histogram_​microseconds_sum` | **Scan sum rate**  The `coverity_scan_service_​duration_​histogram_​microseconds_​sum` metric is a graph that shows the current rate of scans.  **Interpreting the metric**  If there are active scans completing, then this number is expected to increase, the slope of this graph indicates how busy the scan system is. |
| `coverity_scan_service_​duration_histogram_​microseconds_bucket` | **Scan latency quantiles**  The `coverity_scan_service_​duration_histogram_​microseconds_bucket` metric is a histogram that lists the scan latencies with their corresponding quantiles such at 50, 90 and 99th quantile.  **Interpreting the metric**  The scan latency quantiles should follow the baseline values for the most occurring latency. The scan latency quantile makes it easier to see the 50, 90, and 99th quantile to better understand the performance of the scan service. |
| `coverity_scan_service_​duration_histogram_​microseconds_count` | **Scan GRPC codes**  This metric (`coverity_scan_service_​duration_histogram_​microseconds_count`) is a graph that show the rate of the various Scan GRPC Codes.  **Interpreting the metric**  Any of the codes increasing in rate is an indication of how busy the scan system is. The main status codes of interest here are the non-zero ones since they indicate issues with the storage system. Refer to the specific status code to help identify the issue. |
| `coverity_scan_service_​duration_histogram_​microseconds_bucket` | **Scan service duration**  The `coverity_scan_service_​duration_​histogram_​microseconds_​bucket` metric is a histogram that shows the scan service durations.  **Interpreting the metric**  The scan service duration histogram should follow the baseline values for the most occurring duration. If the Scan Service Duration shows a bucket of longer than expected duration and higher than expected occurrence, then it means there is an issue causing delays or the resources available are insufficient (see CPU, disk and memory usage). |
| `coverity_scan_service_​dispatch_​duration_​histogram_​microseconds_​bucket` | **Scan service dispatch duration**  The `coverity_scan_service_​dispatch_​duration_​histogram_​microseconds_​bucket` metric is a histogram that shows the Scan Service Dispatch Durations.  **Interpreting the metric**  The scan service dispatch duration histogram should follow the baseline values for the most occurring dispatch duration. If the scan service duration shows a bucket of longer than expected dispatch duration and higher than expected occurrence, then it means there is an issue causing delays in dispatching scans or the resources available are insufficient (see CPU, disk and memory usage). |
| `coverity_scan_service_​event_counter` | **Scan service events**  The `coverity_scan_service_event_counter` metric is a rate that tracks the various scan service events such as dspatch pending Jobs and dispatch sweep.  **Interpreting the metric**  These rates should match the baseline of the system but if they are higher then it indicates that the system is busier than usual. |
