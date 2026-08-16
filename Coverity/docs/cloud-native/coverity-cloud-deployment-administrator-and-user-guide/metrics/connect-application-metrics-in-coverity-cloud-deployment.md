---
title: "Connect application metrics in Coverity cloud deployment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/connect-application-metrics-in-coverity-cloud-deployment.html"
content_id: "3rFcM34KhA2o7t0~6RmAkg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:02.453544+00:00"
---

# Connect application metrics in Coverity cloud deployment

The following sections contain tables that identify metrics that are available to be
scraped by Prometheus and provided to a monitoring system such as Grafana. Use the
following metrics definitions to view the metrics in a monitoring system such as
Grafana. The examples provide sample Grafana PromQL queries.

Note: Refer to the documentation for your monitoring system, such as Grafana, for
information on the PromQL query language and using PromQL queries in dashboards.

Table 1. Metrics alphabetical list with links

| Metric | Link to metric description |
| --- | --- |
| `active_db_​connections` | Database metrics |
| `com_coverity_​ces_​web_​filter_​CimInstrumented​Filter_​errors_total` | API metrics |
| `com_coverity_​ces_​web_​filter_​CimInstrumented​Filter_​requests_count` |
| `com_coverity_​ces_​web_​filter_​CimInstrumented​Filter_​responseCodes_​badRequest_​total` |
| `com_coverity_​ces_​web_​filter_​CimInstrumented​Filter_​responseCodes_​notFound_​total` |
| `com_coverity_​ces_​web_​filter_​CimInstrumented​Filter_​responseCodes_​serverError_​total` |
| `com_coverity_​ces_​web_​filter_​CimInstrumented​Filter_​timeouts_​total` |
| `connect_active_​commit_count` | Commit metrics |
| `connect_commit_​error_​histogram_​count` |
| `connect_commit_​executor_size` |
| `connect_commit_​latency_bucket` |
| `connect_commit_​latency_count` |
| `connect_commit_​queue_size` |
| `connect_http_​latency_bucket` | API metrics |
| `connect_http_​latency_count` |
| `connect_is_​accepting_​new_commits` | Commit metrics |
| `connect_is_​backup_​in_progress` | Backup and skeletonization metrics |
| `connect_is_​skeletonization_​in_progress` |
| `connect_memory_​used` | Commit metrics |
| `connect_stop_​watch_​duration_​histogram_​bucket` | API metrics |
| `connect_stop_​watch_​duration_​histogram_​bucket` | View loading metrics |
| `connect_stop_​watch_​duration_​histogram_​count` |
| `connect_stop_​watch_​duration_​histogram_​sum` | API metrics |
| `connect_web_​requests_​per_​second` |
| `connect_ws_​requests_​per_​second` |
| `coverity_scan_service_​duration_histogram_​microseconds_count` | Scan Service metrics |
| `coverity_scan_service_​duration_histogram_​microseconds_sum` |
| `coverity_scan_service_​duration_histogram_​microseconds_bucket` |
| `coverity_scan_service_​duration_histogram_​microseconds_count` |
| `coverity_scan_service_​duration_histogram_​microseconds_bucket` |
| `coverity_scan_service_​dispatch_​duration_​histogram_​microseconds_​bucket` |
| `coverity_scan_service_​event_counter` |
| `coverity_​storage_​service_​duration_​histogram_​microseconds_​bucket` | Storage Service metrics |
| `coverity_​storage_​service_​duration_​histogram_​microseconds_​bucket` |
| `coverity_​storage_​service_​duration_​histogram_​microseconds_​count` |
| `db_size` | Database metrics |
| `http_server_​requests_​seconds_​sum` | API metrics |
| `lock_cache_size` | Stream lock metrics |
| `max_db_connections` | Database metrics |
| `no_of_commits_​queued_for_a_​stream` | Stream lock metrics |
| `no_of_​componentmaps` | Software analysis metrics |
| `no_of_custom_​roles` |
| `no_of_projects` |
| `no_of_streams` |
| `no_of_​triagestores` |
| `no_of_​usergroups` |
| `no_of_users` |
| `redis_allocator_allocated_bytes` | Redis cache metrics |
| `redis_allocator_resident_bytes` |
| `redis_allocator_used_bytes` |
| `redis_blocked_clients` |
| `redis_commands_duration_​seconds_​total` |
| `redis_connected_clients` |
| `redis_db_keys` |
| `redis_evicted_keys_total` |
| `redis_expired_keys_total` |
| `redis_keyspace_hits_total` |
| `redis_keyspace_misses_total` |
| `redis_tracking_clients` |
| `stream_locked` | Stream lock metrics |
| `table_size` | Database metrics |
