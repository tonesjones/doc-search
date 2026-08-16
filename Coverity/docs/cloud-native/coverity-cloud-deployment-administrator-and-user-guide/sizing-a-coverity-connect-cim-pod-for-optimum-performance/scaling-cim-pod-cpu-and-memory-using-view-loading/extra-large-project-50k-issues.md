---
title: "Extra-large project (50K issues)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/extra-large-project-50k-issues-.html"
content_id: "kLyhy~TEDw4BnWPUDwr6lg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:56.239347+00:00"
---

# Extra-large project (50K issues)

The following table defines, for an extra large project of 50K issues, response times for
concurrent queries submitted in environments with various CPU and memory resource
combinations. For various levels of concurrency and 64 GB of memory, determine the
number of CPU cores needed to obtain an estimated performance.

Table 1. Extra-large project (50K issues) - View loading throughput

| Concurrency | Query Response Time (s) | | | | Memory (GB) |
| --- | --- | --- | --- | --- | --- |
| CPU cores | | | |
| 8 | 16 | 24 | 32 |
| **1** | 3.1 | 3.1 | 3.1 | 3.1 | **64** |
| **50** | 12.4 | 7.2 | 5.8 | 4.8 |
| **100** | 21.5 | 12.5 | 10.4 | 9 |
| **150** | 32 | 18 | 14 | 12 |
| **200** | 40 | 22 | 18 | 15 |
| **250** |  | 26 | 20 | 17 |
| **300** |  | 28 | 22.5 | 19 |
| **350** |  | 34 | 26 | 22 |
| **400** |  |  | 30 | 25 |
| **450** |  |  | 32 | 26 |
| **500** |  |  | 35 | 29 |
