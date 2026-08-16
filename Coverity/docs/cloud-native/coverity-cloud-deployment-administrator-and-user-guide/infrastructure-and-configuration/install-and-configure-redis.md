---
title: "Install and configure Redis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/install-and-configure-redis.html"
content_id: "tiRLiqjUUm2qn0maaUwJpQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:58.818416+00:00"
---

# Install and configure Redis

Install and configure Redis, using the following requirements and recommendations:

- Requirement: Redis must be configured without eviction. The cache service design
  requires that all metadata be resident in Redis at all times. If Redis is not
  correctly configured, the cache service will refuse to start.
- Recommendation: The Redis memory limit should be 1 GB, however this should be
  adjusted based on your requirements.

  Note: Cache-service checks the memory usage of the Redis
  server at start-up and will not start if memory usage is more than 99% of the
  server limit.
- Recommendation: Coverity does not use Redis persistence, therefore configure
  Redis without persistence. If persistence is enabled, the Redis pod memory limit
  must be significantly higher than the Redis server memory limit.
- Recommendation: Configure Redis with authentication.
- Recommendation: Configure Redis with TLS.

Install Redis in either the namespace (embedded) or in the GCP Memorystore, AWS
ElastiCache, or Azure cache (external).

Important: For AWS ElastiCache and Redis configuration for
ElastiCache, see also Configuring AWS ElastiCache and Redis.

Retain all Redis setup data. When you set up the Helm chart, you will need to enter Redis
values as part of the cache storage setup. Refer to:

- For Redis Helm keys, see Redis keys.
- For Redis Helm keys, see cache-service.redis Helm keys
- scan-services Helm subchart: Helm keys
