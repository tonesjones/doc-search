---
title: "Example: global values"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/example-global-values.html"
content_id: "63XCvo4SZTdoB_1HEt5YPQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:16.128812+00:00"
---

# Example: global values

The `cnc` Helm chart and scan-services subchart contain
`global` Helm keys that are common to both the cnc chart and the
scan-services subchart. If you set a
`.Values.global.key=value`Helm override, the override is applied
to template files in both the connect and scan-services subcharts. For example:

```
global:
  imageRegistry: "gcr.io/coverity-cloud-sandbox-dev"
  imagePullPolicy: "Always"
  postgres:
    host: "cim-pg-postgresql"
    password: "postgres"
    port: 5432
    user: "postgres"
    sslmode: "verify-ca"
  redis:
    host: cache-redis-master
    verifyHostName: false
    secure: true
    port: 6379
  trust-stores:
    enabled: true
  ingress:
    enabled: true
    annotations: {}
    hosts:
      - local.connect.example.com
    tls:
      - secretName: "cnc-cim-tls-nginx"
        hosts:
          - local.connect.example.com
```

Assuming there are no other higher-precedence overrides, all of the override values in
the `global:` block above are applied to Helm properties in both the
`cnc` and `scan-services` charts. If you set a Helm
override for a service, that Helm value takes precedence over the global value for that
service. The same behaviour exists for values that are configured using the
`--set` command while executing a `helm install`
command.
