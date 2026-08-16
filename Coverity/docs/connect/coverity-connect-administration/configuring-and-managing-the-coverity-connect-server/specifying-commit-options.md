---
title: "Specifying commit options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/specifying-commit-options.html"
content_id: "ZXLFkiM_~RkKip7YflGBqQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:07.317457+00:00"
---

# Specifying commit options

Note: If Coverity is deployed in the cloud, commit options are automatically configured through
Helm. For information on these commit options, see "Coverity Connect (cim) Helm keys" in the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide.

You can use the following properties of cim.properties to modify the
queue-related behavior for commits of analysis results to the Coverity Connect
database:

- commitWorkQueueCapacity: Specifies the number of commits that
  can wait in the queue. Minimum 15. Maximum 255. Default 80.
- commitPoolThreads: Specifies the number of concurrent threads
  to process commits off of the queue. Minimum 5. Maximum 50. Default 5.

Note: Prior to 6.5.1, commitWorkQueueCapacity had lower Max/Default
values, which were: Minimum 15. Maximum 100. Default 20.

## Commit processing during system startup

Traditionally, Coverity Connect preloads certain caches related to commit processing
during server startup. This leads to noticably delayed startup, especially with
large databases.

In the 2022.12 release, this behaviour has changed. Instead of preloading caches
during startup, the caches are allowed to warm up at runtime. Administrators might
notice that the server boots more quickly, but might also notice that initial
commits following a cold boot are somewhat slower than before. No action is
required; as the server processes commits, its internal caches will populate and
performance will return to normal.
