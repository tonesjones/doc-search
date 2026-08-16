---
title: "Configure NGINX ingress-class controllers or the gateway API"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-nginx-ingress-class-controllers-or-the-gateway-api.html"
content_id: "aNpbFvByfFX9u_zV1KuK~g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:43:22.764415+00:00"
---

# Configure NGINX ingress-class controllers or the gateway API

The 2026.6.0 release deprecates the NGINX ingress controller as it is end-of-life and not
supported. However, other NGINX ingress-class controllers can be used and configured
using `cim.ingress` and other ingress Helm keys. Therefore, all NGINX
ingress Helm keys and functionality remain intact.

## Configure NGINX ingress-class controllers

If you are using an NGINX ingress-class controller, in the `cnc`
chart, specify the ingress controller. As specified by `cim.ingress.class:
"nginx"`, the default `values.yaml` file assumes that you
are using an NGINX ingress-class controller, however ingress is disabled by
default.

To enable ingress, you need to set `cim.ingress.enabled` to
`true`. For example:

```
cim:
  ingress:
    enabled: true
    class: "nginx"
```

If you are not using an NGINX ingress-class controller, override the default Helm key
values with the appropriate ingress controller class:

- `cim.ingress.class: "<ingress_class>"`

For information on ingress Helm keys, refer to cim.ingress Helm keys.

## Configure gateway API

Alternatively, this release introduces the use of an ingress gateway API to deploy
and manage compatible Kubernetes ingress controllers. For information on installing
and configuring the gateway API, see Gateway API.
