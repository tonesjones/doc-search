---
title: "Extra Large IDIRs (36 GB)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/extra-large-idirs-36-gb-.html"
content_id: "ka~btvzIuVpTzmSbcxc~Gw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:52.134424+00:00"
---

# Extra Large IDIRs (36 GB)

Extra Large IDIRs (36 GB) defines, for medium projects with 36 GB
IDIRs, response times for commit pool thread counts in environments with various CPU and
memory resource combinations. For various commit pool threads, determine the number of
CPU cores and memory needed to obtain an estimated throughput.

Table 1. Commit throughput for extra large IDIRs

| Commit pool threads | CPU cores (minimum) | Memory (GB) with default Queue Size | Memory (GB) with max Queue Size * | Throughput (commits/hr) |
| --- | --- | --- | --- | --- |
| **5** | 8 | 56 | 146 | 5 |
| **10** | 10 | 120 | 210 | 10 |
| **15** | 15 | 160 | 250 | 12 |
| **20** | 20 | 200 | 290 | 13 |
| **25** | 25 | 220 | 310 | 14 |
| **30** | 30 | 264 | 354 | 16 |

The following table specifies the maximum amount of memory needed to support work queues
of extra large IDIRs.

The following table is likely more for reference. Under most circumstances, it would be
advisable to plan the Queue memory requirements using the Large sized IDIR table.

Note: It is not likely to fill a queue of 250 Extra-Large size (36 GB)
IDIRs. Therefore, a better recommendation would be to use the maximum queue memory usage
table for large IDIRs (12 GB) which would require 30 GB vs 90 GB for a full
queue.

Table 2. Maximum queue memory usage for extra large IDIRs

| commitWorkQueueCapacity | Memory (GB) |
| --- | --- |
| (Default) 80 | 29 |
| 150 | 54 |
| 200 | 72 |
| 250 | 90 |
