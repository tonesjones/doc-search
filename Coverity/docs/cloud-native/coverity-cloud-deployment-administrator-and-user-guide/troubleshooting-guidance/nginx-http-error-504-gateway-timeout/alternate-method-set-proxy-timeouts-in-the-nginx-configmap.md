---
title: "Alternate method: Set proxy timeouts in the NGINX configMap"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/alternate-method-set-proxy-timeouts-in-the-nginx-configmap.html"
content_id: "RbOh0Butyhx4Gi2NWeYcGA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:50.761973+00:00"
---

# Alternate method: Set proxy timeouts in the NGINX configMap

Alternatively, you can elect to add the new override values to the NGINX configMap, and
NOT add annotations to the Helm chart. The following example defines proxy values in an
NGINX configMap named `nginx-config`:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: nginx-config
data:
  proxy_body_timeout: "<timeout-value>"
  proxy_connect_timeout: "<timeout-value>"
  proxy_read_timeout: "<timeout-value>"
  proxy_send_timeout: "<timeout-value>"
```

Important:

You must follow these conventions when setting NGINX ingress proxy timeout values:

- Valid units of measure are: s (seconds (default)) | m (minutes) | h (hours) | d
  (days)
- You must use a single unit of measure (90s, not 1m30s).
- The value must be a positive integer,
- The unit of measure must immediately follow the value; no space.

For information on working with configMaps, see:

- To learn about ConfigMaps: [ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/).
- For F5 NGINX ConfigMap documentation: [ConfigMap resources](https://docs.nginx.com/nginx-ingress-controller/configuration/global-configuration/configmap-resource/).
