---
title: "View loading considerations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/view-loading-considerations.html"
content_id: "aoQGZR63FlN2VfbRNPUBDQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:56.900457+00:00"
---

# View loading considerations

The greatest benefit from increasing Coverity cloud application resources will be commits
View loading is largely bottlenecked on the database side, however, there are measurable
benefits to increased resources on the application side. Testing with 20 CPUs and 60 GB
memory saw performance improvement up to 20-30% at higher concurrencies (over 200) over
8 CPUs and 32GB in some instances.

Coverity cloud telemetry has metrics that can provide insight to loads that exceed the
hardware capabilities of the system. These metrics include: ‘View loading latency’ and
‘Connect http error count’.

The key bottleneck is database CPU utilization; if the CPU load reaches a sustained load
of 100%, you should increase system resources.
