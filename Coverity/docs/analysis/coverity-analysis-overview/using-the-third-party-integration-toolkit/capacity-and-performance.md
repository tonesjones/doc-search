---
title: "Capacity and performance"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/capacity-and-performance.html"
content_id: "F0I1h5wsa8R3e8GGVOGm0Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:35:29.027103+00:00"
---

# Capacity and performance

The Third Party Integration Toolkit does not impose any hard limit on the number of
source files, issues, events, and so forth, that can be imported into Coverity Connect.
However, you must make sure that Coverity Connect is properly sized to handle the size
of code base, issue types, and issue density, as well as the number of concurrent
commits, and that the Coverity Connect UI is performing well. See Coverity Platform 2026.6.0 User and Administrator Guide for information about Coverity Connect
tuning.

If you import a high issue density, large source files, and so forth, you might notice
degradation in performance of Coverity Connect. Frequent commits of non-Coverity issues
might cause the database to increase in size, which might result in further performance
degradation, causing Coverity Connect to become unresponsive.

Because of this, it is recommended that the following limits be considered when building
integration with a third party analysis tool. Ignoring one of the following might cause
performance degradation of Coverity Connect:

1. Size of a single source file should not exceed 1MB
2. Number of source files should not exceed 30,000
3. Size of JSON file should not exceed 60MB
4. Database size should not exceed 300GB
5. Density should not exceed 100 issues per thousand lines of code
6. Events per issue should not exceed 25 events per issue
7. Size of a single event should not exceed 300 characters
8. Total Emit directory size should not exceed 8GB
