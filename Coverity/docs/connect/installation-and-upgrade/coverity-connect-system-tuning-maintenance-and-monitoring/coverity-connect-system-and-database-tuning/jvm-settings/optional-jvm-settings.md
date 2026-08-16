---
title: "Optional JVM settings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/optional-jvm-settings.html"
content_id: "BrIOeb0ENR1x5umQ34lxEA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:15.742094+00:00"
---

# Optional JVM settings

The following parameters are optional, but are recommended for optimization:

Table 1. Optional JVM settings

| Parameter | Settings and notes |
| --- | --- |
| `-xx:+UseCompressedOops` | Enable (`+`) the use of 32-bit ordinary object pointers in 64-bit JREs. Enabling this parameter can provide faster and more efficient 32-bit addressing for OOPs at the expense of heap size. Note that the heap will be limited to a maximum of 32Gb. |
| `-XX:-UseGCOVerheadLimit` | Disable (`-`) the garbage collection overhead limit. When this parameter is disabled, `OutOfMemoryExceptions` are suppressed when more than 98% of the total time is spent in garbage collection and less than 2% of the heap is recovered. Note that this might allow the application to hang when the heap is under-provisioned. |
