---
title: "Working with nginxConfig Helm keys"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/working-with-nginxconfig-helm-keys.html"
content_id: "EsIECjsqbxo5t7NOFRvMXg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:23.424858+00:00"
---

# Working with nginxConfig Helm keys

Using the following Helm keys, located in the `cnc` Helm chart, you can
change one or more NGINX configuration key values in the NGINX ConfigMap. For these
keys, this avoids needing to edit the NGINX ConfigMap to change configuration
values.

```
cim:
  cimweb:
    tlsSidecar:
      nginxConfig:
        # Core nginx settings
        worker_processes: 1
        worker_connections: 1024
        keepalive_timeout: 65
        client_max_body_size: "100m"

        # SSL/TLS settings
        ssl_protocols: "TLSv1.2 TLSv1.3"
        ssl_ciphers: "AESGCM:CHACHA20:-kRSA:-aNULL"
        ssl_prefer_server_ciphers: "on"
        ssl_ecdh_curve: "X25519:prime256v1"

        # Proxy timeout settings (with units)
        proxy_connect_timeout: "60s"
        proxy_read_timeout: "60s"
        proxy_send_timeout: "60s"
```

For information on the meaning of each configuration key, see the NGINX document page
[Alphabetical index of directives](https://nginx.org/en/docs/dirindex.html).

For information about the proxy timeout keys if you are encountering an NGINX Error 504,
see NGINX HTTP error 504: Gateway Timeout.

To change one or more NGINX ConfigMap values using these Helm keys:

1. In the `cnc` Helm chart, edit the
   `cim.cimweb.tlsSidecar.nginxConfig` key value(s) as
   needed.
2. To apply the new values to the NGINX ConfigMap, you must re-deploy Coverity
   cloud. For example, use a `helm install` or `helm
   upgrade` command and refer to the new or modified
   `values.yaml` file as needed.

## Change the NGINX ingress proxy timeout Helm key values

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

You must follow these conventions when setting NGINX ingress proxy timeout
values:

- Valid units of measure are: s (seconds (default)) | m (minutes) | h (hours)
  | d (days)
- You must use a single unit of measure (90s, not 1m30s).
- The value must be a positive integer,
- The unit of measure must immediately follow the value; no space.

For example, the following have the same value:

```
..._timeout: "3600s"
..._timeout: "60m"
..._timeout: "1h"
```

## Redeploy Coverity cloud

Note: Do not perform this step if you created the proxy timeouts
in an NGINX configMap.

After creating annotations within the Helm chart, in order to apply the new values
and override the default proxy timeout values, you must re-deploy Coverity cloud.
For example, use a `helm install` or `helm upgrade`
command and refer to the new or modified `values.yaml` file as
needed.
