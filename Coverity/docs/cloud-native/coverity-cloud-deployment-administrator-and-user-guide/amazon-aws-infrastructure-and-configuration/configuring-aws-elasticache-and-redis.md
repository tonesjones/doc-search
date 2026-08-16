---
title: "Configuring AWS ElastiCache and Redis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-aws-elasticache-and-redis.html"
content_id: "8lHXViV49VmAkpKgh13tWA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:17.381381+00:00"
---

# Configuring AWS ElastiCache and Redis

AWS ElastiCache can be used with a Cache Service deployment that includes Redis. You need
to configure the following AWS ElastiCache deployment and Redis properties to fulfill
the Redis requirements:

- Disable ElastiCache `Serverless caching` deployment. The Cache
  Service does not support serverless caching.
- In a custom ElastiCache property group, set the Redis eviction policy to
  `noeviction`. After creating a new property group, set the
  `maxmemory` policy property for the new group to
  `noeviction`. Use this property group when you create the
  ElastiCache instance.
- Disable the Redis `Cluster` mode.
- Set the number of Redis replicas to 0.
- The Redis node memory size depends on usage. We recommend 1GB as an initial
  value. In the future, you can increase this value if needed.
