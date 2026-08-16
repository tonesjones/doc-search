---
title: "Create a Cache Service CA certificate secret for Redis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-a-cache-service-ca-certificate-secret-for-redis.html"
content_id: "n_kpLuWU4WuZPlh98XVzCQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:00.151573+00:00"
---

# Create a Cache Service CA certificate secret for Redis

If you are deploying Cache Service, and if you need to use a CA certificate to
communicate with Redis, you need to create a secret with key name
`ca.crt`.

```
kubectl create secret generic "${REDIS_CACERT_SECRET_NAME}" \
  --from-file=ca.crt=./ca.crt \
  -n "$NS" \
```

To create Helm overrides for the Redis CA certificate secret, see:

- For information on setting Redis Helm keys, see Redis keys.
- For further information on the keys, refer to the section, scan-services Helm subchart: Helm keys.
