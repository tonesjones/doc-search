---
title: "Manage automatic route creation using existing ingress settings"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/manage-automatic-route-creation-using-existing-ingress-settings.html"
content_id: "ar7JQmqmaq9DNBIhCL1UUg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:53.241570+00:00"
---

# Manage automatic route creation using existing ingress settings

The simplest way to enable routes is to set `cim.route.enabled: true` in
the `cnc` chart. The route will automatically inherit all settings from
your existing ingress configuration:

```
cim:
  route:
    enabled: true
```

The following cnc chart `values.yaml` file example illustrates the minimal
configuration needed to inherit route characteristics from the existing ingress
controller configuration. This example enables ingress, identifies hosts and TLS secret,
and enables OpenShift routing with `cim.route.enabled: true`.

```
cim:
  ingress:
    enabled: true
    hosts: ["cnc.company.com"]
    tls:
      - secretName: "cnc-tls"
        hosts: ["cnc.company.com"]
  
  route:
    enabled: true  # Automatically uses cnc.company.com with cnc-tls secret
```

Using Global ingress values that are shared across all services: The following cnc chart
`values.yaml` file example illustrates the minimal configuration
needed to inherit route characteristics for all services from the existing ingress
controller configuration. This example enables ingress, identifies global hosts and the
global TLS secret, and enables OpenShift routing with `cim.route.enabled:
true`.

```
global:
  ingress:
    hosts: ["cnc.global.com"]
    tls:
      - secretName: "global-tls"
        hosts: ["cnc.global.com"]

cim:
  route:
    enabled: true
    annotations:
      route.openshift.io/cookie_name: "cnc-session"
```
