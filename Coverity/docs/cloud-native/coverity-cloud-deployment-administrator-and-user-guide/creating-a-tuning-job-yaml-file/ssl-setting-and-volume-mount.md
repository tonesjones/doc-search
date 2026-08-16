---
title: "SSL setting and volume mount"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ssl-setting-and-volume-mount.html"
content_id: "l9yzLUdoHw9MD81HImJ~Lg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:42:25.180378+00:00"
---

# SSL setting and volume mount

We recommended enabling SSL using the `verify-ca` mode for your PostgreSQL
database communication as described in Select the PostgreSQL sslmode and find the PostgreSQL root certificate for TLS.

If the database is in the same namespace as CNC, you can use the existing Coverity
Connect trust store certificates.

If the database is not in the CNC namespace, create and add the following file volume
mount to the Kubernetes tuning job yaml template, under
`spec:template:volumes:`.

```
- configMap:
    defaultMode: 420
    name: <CONFIG-MAP-NAME>
  name: cnc-cim-trust-stores
- mountPath: /coverity/truststorecerts
    name: cnc-cim-trust-stores
```

You can avoid this volume mount if you disable SSL mode.

For information about creating a config map for SSL trust store certificates, see Creating a truststore ConfigMap for a Connect instance.
