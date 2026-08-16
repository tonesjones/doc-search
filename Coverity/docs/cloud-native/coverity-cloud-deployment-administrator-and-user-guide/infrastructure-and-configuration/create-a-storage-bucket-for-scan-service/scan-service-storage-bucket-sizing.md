---
title: "Scan Service storage bucket sizing"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scan-service-storage-bucket-sizing.html"
content_id: "pmc9LzNmrKIJcDKt9k~gmQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:57.531231+00:00"
---

# Scan Service storage bucket sizing

The following table identifies how to size the Scan Service storage bucket.

Table 1. Scan Service storage bucket sizing

| Object Type | Average scan object size | Average Number of Scans | Retention Period | Total Average Size |
| --- | --- | --- | --- | --- |
| Scan Objects | M is the average scan object size in GB | N is the average number of scans per day. | T days | (M * N * T) GB |
| Client CLI Tools | 10 GB | NA | NA | 10 GB |
| Logs | 500 MB | NA | T days | T/2 GB |
| **Total storage bucket size** | | | | (M * N * T) GB + 10 GB + T/2 GB |

For example, if :

- M = 0.25 GB per scan
- N = 100 scans per day
- T = 30 day retention period
- CLI tools use 10 GB total
- Logs use 0.5 GB each

Using the equation: (M * N * T) GB + 10 GB + T/2
GB

For the example, the total storage bucket size is:

750 GB (scan objects) + 10 GB (CLI tools) + 15 GB (logs) = 775
GB
