---
title: "Redis cache metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/redis-cache-metrics.html"
content_id: "3EQNAyzTdk6rFAYXu5Sg6g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:13.328272+00:00"
---

# Redis cache metrics

The following table describes Redis cache metrics.

Table 1. Redis cache metrics

| Metric | Description | Metric type |
| --- | --- | --- |
| `redis_allocator_allocated_bytes` | **Cache memory usage**  These metrics are gauges that track the currently-used cache memory, including allocated, resident, and used cache:  **Interpreting the metric**  The cache memory usage metrics provide insight into the cache memory, and more specifically how much cache is allocated, how much cache is used, and how much cache is resident. | Gauge |
| `redis_allocator_resident_bytes` |
| `redis_allocator_used_bytes` |
| `redis_connected_clients` | **Cache clients**  These metrics are gauges that track the number of clients that are currently using the cache service including how many Clients are connect, blocked, or tracking.  **Interpreting the metric**  The Cache Clients gives insight into how many clients are connected to the cache and their status. | Gauge |
| `redis_blocked_clients` |
| `redis_tracking_clients` |
| `redis_db_keys` | **Cache DB keys**  The `redis_db_keys` metric is a gauge that tracks the current number of database keys in the cache.  **Interpreting the metric**  The Cache DB Keys should track with the baseline of the system. | Gauge |
| `redis_evicted_keys_total` | **Cache key hits and misses**  These metrics are gauges that tracks the status of the cache keys, evicted, expired as well as cache hits and misses.  **Interpreting the metric**  The rate of cache evictions, cache expirations, cache hits, and cache misses can give insight into how effectively the cache is configured. Ideally cache hits should be high and cache misses should be low. Cache evictions and expirations should ideally be low and otherwise could point to latency issues in the system. | Gauge |
| `redis_expired_keys_total` |
| `redis_keyspace_hits_total` |
| `redis_keyspace_misses_total` |
| `redis_commands_duration_​seconds_​total` | **Cache command duration**  This metric is a gauge that tracks the duration of cache commands.  **Interpreting the metric**  The cache command duration metric should track with the baseline of the system. | Gauge |
