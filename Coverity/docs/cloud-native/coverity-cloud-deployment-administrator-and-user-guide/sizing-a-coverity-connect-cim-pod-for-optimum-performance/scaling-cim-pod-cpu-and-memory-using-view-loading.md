---
title: "Scaling cim pod CPU and memory using view loading"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scaling-cim-pod-cpu-and-memory-using-view-loading.html"
content_id: "72r9fxEKQwZRpEAW1~yLBw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:54.089336+00:00"
---

# Scaling cim pod CPU and memory using view loading

The following sections contain tables that provide estimated response times for various
numbers of concurrent issues submitted to environments with various resource
combinations running scans with medium, large and extra large issue counts. The
estimated response time is called the view loading throughput. The tables are provided
as a guide to scale your cloud hardware resources for expected performance given your
project issue count and concurrent issue request counts.

Important: You need to size resources for each Connect
`cim` pod that you deploy.

To use the view loading hardware scaling tables:

1. Find your largest Coverity cloud project with the highest number of total issues.
   and refer to the corresponding table:

   - Medium – as many as 10,000 issues in the largest project
   - Large – as many as 25,000 issues in the largest project
   - Extra large – as many as 50,000 issues in the largest project
2. Choose your target highest concurrency and the desired response time and use the
   corresponding minimum requirements for processors, and memory available to the
   Coverity cloud external database.

   Note: The empty cells denote when the concurrency has a
   non-zero error rate.
