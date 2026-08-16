---
title: "Large IDIRs (12 GB)"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/large-idirs-12-gb-.html"
content_id: "sl~wRavOqiuqkwM4JrzNHw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:51.486103+00:00"
---

# Large IDIRs (12 GB)

Large IDIRs (12 GB) defines, for medium projects with 12 GB
IDIRs, response times for commit pool thread counts in environments with various CPU and
memory resource combinations. For various commit pool threads, determine the number of
CPU cores and memory needed to obtain an estimated throughput.

Table 1. Commit throughput for large IDIRs

| Commit pool threads | CPU cores (minimum) | Memory (GB) with default Queue Size | Memory (GB) with Max Queue Size | Throughput (commits/hr) |
| --- | --- | --- | --- | --- |
| **5** | 8 | 50 | 80 | 21 |
| **10** | 10 | 80 | 110 | 26 |
| **15** | 15 | 100 | 130 | 36 |
| **20** | 20 | 120 | 150 | 49 |
| **25** | 25 | 130 | 160 | 62 |
| **30** | 30 | 144 | 176 | 73 |

The following table specifies the maximum amount of memory needed to support work queues
of large IDIRs.

Table 2. Maximum queue memory usage for large IDIRs

| commitWorkQueueCapacity | Memory (GB) |
| --- | --- |
| (Default) 80 | 10 |
| 150 | 18 |
| 200 | 24 |
| 250 | 30 |
