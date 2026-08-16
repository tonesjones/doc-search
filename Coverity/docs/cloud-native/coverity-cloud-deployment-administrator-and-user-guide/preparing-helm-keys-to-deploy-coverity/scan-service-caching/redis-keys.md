---
title: "Redis keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/redis-keys.html"
content_id: "S4nj9BlxGVLtSMcxitTvrg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:57.417153+00:00"
---

# Redis keys

Set the `cache-service.redis:` keys as needed by the Cache Service.

- For information on the keys, refer to the section, scan-services Helm subchart: Helm keys.
- To create the Redis CA certificate secret, see Create a Cache Service CA certificate secret for Redis.

Redis is needed by the Cache Service. Set the following Redis keys for your Cache Service
implementation.

- `authEnabled`: Enable authentication for Redis. In case set to true,
  password secret also need to be provided.
- `cacertSecret`: If TLS is enabled, specify the name of the Redis
  secret that contains the CA certificate to be used for Redis communication.
- `database`: Specify the Redis database.
- `host`: Specify the Redis host name.
- `passwordSecret`: Specify the name of the secret that contains the
  Redis password (must contain a key named `password`). Redis is secured with
  password.
- `port`: Redis port. Accept the default value.
- `secure`: If TLS enabled for communication with Redis.
- `verifyHostName`: If Host name need to be verified for Redis
  communication in case TLS enabled.

For example:

```
cache-service:
  redis:
    authEnabled: false
    cacertSecret: "cacertSecret"
    database: "1"
    host: "redisHost"
    passwordSecret: "redisSecret"
    port: 6379
    secure: true
    verifyHostName: true
```

The default values for the Cache Service Redis keys are:

```
cache-service:
  redis:
    authEnabled: false
    cacertSecret: ""
    database: "1"
    host: ""
    passwordSecret: ""
    port: 6379
    secure: true
    verifyHostName: true
```
