---
title: "Medium project (10K issues)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/medium-project-10k-issues-.html"
content_id: "zDnXehcdTWuGboBOlEvkEg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:54.817044+00:00"
---

# Medium project (10K issues)

Medium project (10K issues) defines, for a medium size
project of 10K issues, response times for concurrent queries submitted in environments
with various CPU and memory resource combinations. For various levels of concurrency and
64 GB of memory, determine the number of CPU cores needed to obtain an estimated
performance.

Table 1. View loading throughput-Medium project

| Concurrency | Query Response Time (s) | | | | Memory (GB) |
| --- | --- | --- | --- | --- | --- |
| CPU cores | | | |
| 8 | 16 | 24 | 32 |
| **1** | 1.3 | 1.2 | 1.1 | 1.1 | **64** |
| **50** | 5.3 | 3.5 | 3 | 2.6 |
| **100** | 9.1 | 6.3 | 5.5 | 4.7 |
| **150** | 12.9 | 8.6 | 7.7 | 6.6 |
| **200** | 16.1 | 10.9 | 9.5 | 8.1 |
| **250** | 17.6 | 11.6 | 10.3 | 8.8 |
| **300** |  | 13.3 | 11.2 | 9.6 |
| **350** |  | 14.9 | 12.6 | 10.8 |
| **400** |  | 16.3 | 14 | 11.9 |
| **450** |  |  | 15 | 12.8 |
| **500** |  |  | 16 | 13.7 |
| **550** |  |  | 18 | 15.4 |
