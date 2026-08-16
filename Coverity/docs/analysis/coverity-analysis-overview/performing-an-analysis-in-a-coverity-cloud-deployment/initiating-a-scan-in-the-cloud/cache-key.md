---
title: "Cache key"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/cache-key.html"
content_id: "mjlG701s8uqtS5tnTVNdGg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:37.017643+00:00"
---

# Cache key

If caching is used in a Coverity cloud deployment, the `-o
commit.connect.stream=project-name` option specifies
the cache key. For information on the `stream` option, see "Connect configuration" in
the Guide to the Coverity 2026.6.0 Point and Scan UI and the Coverity CLI and Initiating a scan in the cloud.

A cache key, used for a project, maintains the Coverity results cache across scans for a
project. Using a different cache key resets the results cache. When analyzing and
re-analyzing a project, use the same cache key. Use different cache keys to analyze
different projects. If you use the same key for two different projects, the cache will
contain results for both projects, increasing the amount of time needed for cache
downloads and uploads. For efficient use of the cache, if you need to analyze a
different project, or if a project accumulates enough changes to degrade scan
performance, you should use a different cache key. Failing to choose the cache key
wisely will eventually have noticeable effects.
