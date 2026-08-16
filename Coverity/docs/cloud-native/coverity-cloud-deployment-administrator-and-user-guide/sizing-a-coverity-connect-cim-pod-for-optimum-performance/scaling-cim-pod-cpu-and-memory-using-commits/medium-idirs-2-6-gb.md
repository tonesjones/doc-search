---
title: "Medium IDIRs (2.6 GB)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/medium-idirs-2.6-gb-.html"
content_id: "oeXaPWjaaX2N3lzv2AZ00w"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:50.830068+00:00"
---

# Medium IDIRs (2.6 GB)

Medium IDIRs (2.6 GB) defines, for medium projects with 2.6 GB
IDIRs, response times for commit pool thread counts in environments with various CPU and
memory resource combinations. For various commit pool threads, determine the number of
CPU cores and memory needed to obtain an estimated throughput.

Table 1. Commit throughput for medium IDIRs

| Commit pool threads | CPU cores (minimum) | Memory (GB) with default queue size | Memory (GB) with maximum queue size | Throughput (commits/hr) |
| --- | --- | --- | --- | --- |
| **5** | 8 | 32 | 39 | 110 |
| **10** | 10 | 38 | 45 | 145 |
| **15** | 15 | 80 | 88 | 175 |
| **20** | 20 | 100 | 116 | 239 |
| **25** | 25 | 120 | 128 | 290 |
| **30** | 30 | 144 | 150 | 350 |

The following table specifies the maximum amount of memory needed to support work queues
of medium IDIRs.

Table 2. Maximum queue memory usage for medium IDIRs

| commitWorkQueueCapacity | Memory (GB) |
| --- | --- |
| (Default) 80 | 2 |
| 150 | 4 |
| 200 | 5 |
| 250 | 6.5 |
