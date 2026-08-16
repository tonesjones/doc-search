---
title: "Performance metrics"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/performance-metrics.html"
content_id: "CP4qvYxVjfgouVxzsmEdcw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:04.977148+00:00"
---

# Performance metrics

The following CPU, memory and disk usage metrics are useful for monitoring performance.

Table 1. Performance metrics

| Metric | How to use the metric |
| --- | --- |
| CPU usage | Look for spikes to 100% CPU usage. Extended full CPU usage (90-100%) indicates that the resources are not sufficient for the load; performance and stability will suffer. Add CPUs. |
| Memory usage | Ideal memory usage should be approximately 70% of the total memory, up to maximum of 80%. Anything sustained above 80% indicates that memory is no longer sufficient for the load. Add memory. |
| JVM memory usage | This is similar to total system memory usage and follows similar guidelines. Recommended is 70% of the total up to 80%. Anything sustained above 80% and sustained indicates that memory is no longer sufficient for the load. Add memory. |
| Disk space | This needs to be monitored to avoid running out of disk space or filling the database. The disk space used should not exceed 85-90% (10-15% free disk space). If this frequently occurs,perform an automated disk cleanup of temporary files and logs older than a certain age. |
| Disk I/O usage | This can be monitored to see if there is high disk usage. This can indicate that the system is busy, or that caching is ineffective. |
