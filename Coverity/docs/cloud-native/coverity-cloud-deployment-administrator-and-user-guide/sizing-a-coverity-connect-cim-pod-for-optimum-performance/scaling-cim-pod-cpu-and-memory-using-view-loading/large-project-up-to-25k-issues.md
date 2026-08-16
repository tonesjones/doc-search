---
title: "Large project (up to 25K issues)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/large-project-up-to-25k-issues-.html"
content_id: "qasQ0Og6A3AHVAmrw1O3kA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:55.561118+00:00"
---

# Large project (up to 25K issues)

Large project (up to 25K issues) defines, for a large project of
25K issues, response times for concurrent queries submitted in environments with various
CPU and memory resource combinations. For various levels of concurrency and 64 GB of
memory, determine the number of CPU cores needed to obtain an estimated performance.

Table 1. Large project (25K issues) - View loading throughput

| Concurrency | Query Response Time (s) | | | | Memory (GB) |
| --- | --- | --- | --- | --- | --- |
| CPU cores | | | |
| 8 | 16 | 24 | 32 |
| **1** | 1.6 | 1.6 | 1.6 | 1.4 | **64** |
| **50** | 12.4 | 4.5 | 3.8 | 3.2 |
| **100** | 21.5 | 8.5 | 7.2 | 6.1 |
| **150** | 32 | 11.2 | 9.3 | 7.8 |
| **200** | 40 | 15 | 11.5 | 9.7 |
| **250** |  | 16 | 13 | 10.9 |
| **300** |  | 18.4 | 15.2 | 12.8 |
| **350** |  | 20.5 | 16.3 | 13.7 |
| **400** |  | 23.5 | 19 | 17 |
| **450** |  |  | 20.5 | 17 |
| **500** |  |  | 22 | 19 |
| **550** |  |  | 24 | 20 |
