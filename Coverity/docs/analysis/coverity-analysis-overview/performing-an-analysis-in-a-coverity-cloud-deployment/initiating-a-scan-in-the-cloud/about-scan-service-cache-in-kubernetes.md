---
title: "About Scan Service cache in Kubernetes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/about-scan-service-cache-in-kubernetes.html"
content_id: "L0nH5adzw0UYrjeCK~4_7Q"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:36.376741+00:00"
---

# About Scan Service cache in Kubernetes

In a Coverity cloud deployment, Scan Service uses caching to speed up analyses. This
cache is maintained by a cache management service such as Redis. This cache is used by
the following commands while performing scans.

1. Running `coverity capture` captures files to be analyzed and
   writes them to an intermediate directory (idir) cache.
2. Running `coverity analyze` accesses the source code from the idir
   cache, performs an analysis, and writes the result to the idir cache.
3. After completing the analysis, running `coverity commit` reads the
   analysis results from the idir cache and commits (pushes) the analysis results
   to Coverity Connect.

Alternatively, running `coverity scan` performs all of these functions
with a single command.

If needed, the cache can be reset by an administrator or service with administrator
privileges using the reset-cache CLI option as described in the "Caching
configuration" section in the Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI.

As a user, you can not refresh the cache using this mechanism, however, you can use a
cache key as described in the section, Cache key.
