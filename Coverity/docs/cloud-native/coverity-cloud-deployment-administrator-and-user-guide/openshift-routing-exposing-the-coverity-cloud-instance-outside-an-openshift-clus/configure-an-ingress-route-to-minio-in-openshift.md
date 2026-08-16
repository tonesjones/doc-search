---
title: "Configure an ingress route to MinIO in OpenShift"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configure-an-ingress-route-to-minio-in-openshift.html"
content_id: "nv49Vnts3RZnFtavrIJh4w"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:55.214533+00:00"
---

# Configure an ingress route to MinIO in OpenShift

This section describes how to configure ingress routes to MinIO using the OpenShift UI.
or CLI.

Attention: This procedure assumes that you have
already:

- set up the OpenShift cluster.
- created a route to the Connect UI as described in either:
  - configuring route parameters using the `cnc` Helm chart:
    Manage route creation using the cnc Helm chart
  - configuring route parameters using the OpenShift UI: OpenShift routing - exposing the Coverity cloud instance outside an OpenShift cluster.

Important: If you are using custom domains for storage
service, you must also configure the storage service custom domain properties as
described in Storage service custom domains.

To configure an ingress route to MinIO:

For routing information, see also [OpenShift Secured routes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.12/html/networking/configuring-routes#configuring-default-certificate).

1. Login to either the OpenShift UI or the OpenShift CLI (`oc`) as
   administrator.
2. To set up a new route to the `cnc minio` port, exposing the MinIO
   `/upload` path, create a YAML definition of the secure route
   and include the following annotations:

   ```
   metadata:
     annotations:
       haproxy.router.openshift.io/rewrite-target: /
       haproxy.router.openshift.io/timeout: 5s
   ```

   For example:

   ```
   kind: Route
   apiVersion: route.openshift.io/v1
   metadata:
     name: example-cnc-minio
     namespace: example
     annotations:
       haproxy.router.openshift.io/rewrite-target: /
       haproxy.router.openshift.io/timeout: 5s
   spec:
     host: www.example.com
     path: /upload
     to:
       kind: Service
       name: cnc-minio
       weight: 100
     port:
       targetPort: minio-api
     tls:
       termination: edge
       certificate: |-
         -----BEGIN CERTIFICATE-----
         ...
         -----END CERTIFICATE-----
         -----BEGIN CERTIFICATE-----
         ...
         -----END CERTIFICATE-----
       key: |-
         -----BEGIN EC PRIVATE KEY-----
         ...
         -----END EC PRIVATE KEY-----
       insecureEdgeTerminationPolicy: Redirect
     wildcardPolicy: None
   ```
