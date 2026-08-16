---
title: "Disable TLS sidecar on the cim-web pod"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/disable-tls-sidecar-on-the-cim-web-pod.html"
content_id: "wPhznf8IJvU_ZoleQAJbIQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:48.050346+00:00"
---

# Disable TLS sidecar on the cim-web pod

If the Kubernetes deployment is Coverity Connect only (meaning Scan Service is not
deployed), disable TLS sidecar on the cim-web pod. The following Helm key value disables
TLS sidecar. By default, TLS sidecar is disabled; the default Helm chart value as shown
here is 'false'.

```
cim:
  cimweb:
    tlssidecar:
      enabled: false
```

See also:

- For Helm key information: cim.cimweb.tlsSidecar Helm keys
