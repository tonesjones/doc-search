---
title: "Manage route creation using the cnc Helm chart"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/manage-route-creation-using-the-cnc-helm-chart.html"
content_id: "e6IMBfMeH_loyl9C5Qqixg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:53.894004+00:00"
---

# Manage route creation using the cnc Helm chart

This is an advanced feature that, if implemented without default values, requires
knowledge of OpenShift routing and using Helm chart annotations to manage routing
features. For further information on security and advanced features used by Coverity
cloud, see also the section: Advanced OpenShift route considerations.

For custom route settings, you can override route parameters using the
`cim:route` keys in the `cnc` Helm chart
`values.yaml` file as outlined here and in the `cnc`
chart reference section: cim.route Helm keys for Red Hat OpenShift route creation.

Creating routes by using either the simplest method of enabling
`cim.route` in the cnc Helm chart or by enabling and configuring
route parameters through the Helm chart as described in this page, has the following
benefits

- Routes automatically use existing ingress settings. This is especially true if you
  simply enable `cim.route` in the `cnc` chart.
- Uses native OpenShift route resources instead of ingress workarounds.
- Existing deployments remain unaffected.
- Uses TLS certificate management and custom annotations.
- Routes are created on only OpenShift clusters.

To manage OpenShift route configuration using the `cnc` Helm chart:

1. Required to manage OpenShift routing through the Helm chart: Enable OpenShift
   routing:

   ```
   cim:
     route:
       enabled: true
   ```
2. Optional: Create annotations that define specific OpenShift route parameters. For
   these parameters, see the appropriate sections in [Configuring Routes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.11/html/networking/configuring-routes#route-configuration).

   ```
   cim:
     route:
       annotations:
         route.openshift.io/timeout: "60s"
         route.openshift.io/cookie_name: "cnc-session"
   ```
3. Optional: Create custom host names. If host names are not specified, the host
   name is inherited from the ingress controller.

   ```
   cim:
     route:
       hosts:
         - "custom-cnc.example.com"
   ```
4. Optional: Configure a custom target port:

   ```
   cim:
     route:
       targetPort: 8080
   ```
5. Configure the following TLS parameters:

   - Enable TLS.
   - Optional: Specify the TLS termination type:

     - `"edge"` - Default value. The Ingress controller
       decrypts incoming TLS traffic.
     - `"passthrough"` - The Ingress controller forwards the
       encrypted TLS traffic directly to the backend service. It does not
       terminate the TLS connection.
     - `"reencrypt"` - The Ingress controller terminates the
       client-side TLS connection, decrypts the traffic, and then
       re-encrypts it before forwarding it to the backend service
   - Optional: List custom TLS secrets. If you do not provide a value, the secret
     name is inherited from ingress.
   - Optional: Set the `insecureEdgeTerminationPolicy`. Valid
     values are:

     - `"None"` or `""`- Default value. HTTP
       requests to the route are blocked or rejected.
     - `"Allow"` - Allow both secure (HTTPS) and insecure
       (HTTP) traffic to reach the route.
     - `"Redirect"` - Redirect insecure (HTTP) traffic to
       the secure (HTTPS) scheme.

   ```
   cim:
     route:
       tls:
         enabled: true
         termination: "edge"
         
         secrets:
           - secretName: "custom-tls-secret"
             hosts: ["custom-cnc.example.com"]

         insecureEdgeTerminationPolicy: "Redirect"
   ```
6. Optional: Set wildcard policy.

   ```
   cim:
     route:
       wildcardPolicy: "None"
   ```

   - `"None"` - Default value. Allow only the exact hostname
     specified in the route.
   - `"Subdomain"` - Allow all subdomains of the specified
     host.
