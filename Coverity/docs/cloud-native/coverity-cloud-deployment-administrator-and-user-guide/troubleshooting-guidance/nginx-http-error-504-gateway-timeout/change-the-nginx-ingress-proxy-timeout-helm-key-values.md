---
title: "Change the NGINX ingress proxy timeout Helm key values"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/change-the-nginx-ingress-proxy-timeout-helm-key-values.html"
content_id: "mWNAzxAH3JGbSgoIjNoqSQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:48.739910+00:00"
---

# Change the NGINX ingress proxy timeout Helm key values

The following Helm keys, shown with their default timeout values (in seconds), can be
used to change the NGINX ingress proxy timeout values.

```
cim:
  cimweb:
    tlsSidecar:
      nginxConfig:
        proxy_connect_timeout: "60s"
        proxy_read_timeout: "60s"
        proxy_send_timeout: "60s"
```

For example, to change the values to 60 minutes (3600 seconds), change the Helm key
values:

```
cim:
  cimweb:
    tlsSidecar:
      nginxConfig:
        proxy_connect_timeout: "60m"
        proxy_read_timeout: "60m"
        proxy_send_timeout: "60m"
```

For Helm key information: cim.cimweb.tlsSidecar Helm keys.

Important:

You must follow these conventions when setting NGINX ingress proxy timeout values:

- Valid units of measure are: s (seconds (default)) | m (minutes) | h (hours) | d
  (days)
- You must use a single unit of measure (90s, not 1m30s).
- The value must be a positive integer,
- The unit of measure must immediately follow the value; no space.

For example, the following have the same value:

```
..._timeout: "3600s"
..._timeout: "60m"
..._timeout: "1h"
```

If you change these values while the cluster is up and running, to apply the changes to
the ConfigMap, you need to run a helm upgrade or install as described in trouble_nginx_change_ingress_proxy_timeout_helm_values.html#nginx_change_ingress_proxy_timeout_helm_values__section_ng4_zsh_gfc.
