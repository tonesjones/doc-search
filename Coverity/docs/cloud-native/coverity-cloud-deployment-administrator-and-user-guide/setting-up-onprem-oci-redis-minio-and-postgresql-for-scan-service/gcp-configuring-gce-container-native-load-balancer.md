---
title: "GCP: Configuring GCE container native load balancer"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gcp-configuring-gce-container-native-load-balancer.html"
content_id: "aQAqKccYoYxi8E1IefmyuA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:22.554416+00:00"
---

# GCP: Configuring GCE container native load balancer

Configure Google GCE ingress and load balancer:

Note: For further information on load balancing through ingress in
Google GCP, refer to <https://cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing>.

1. In the `cnc` chart, set the following Helm override:

   ```
   values.cim.ingress.class: "gce"
   ```
2. In the `cnc` chart, create the following annotation:

   ```
   global.ingress.annotations:
     kubernetes.io/ingress.class: "gce"
   ```
3. In the `cnc` chart, create the following annotation:

   ```
   cim.serviceAnnotations:
     cloud.google.com/app-protocols: '{"p8443":"HTTPS","p8080":"HTTP"}'
   ```
4. In the `cnc` chart, set the following Helm override:

   ```
   global.ingress.path: "/*"
   ```
5. In the Google Cloud app, edit the load balancer. Refer to <https://cloud.google.com/app?hl=en>.

   1. In the Google Cloud app, navigate to the
      loadbalancer, then go to
      healthchecks.
   2. Edit the https healthcheck. Update the path from `"/"` to
      `"/liveness"`.
6. Perform a manual tool upload. Edit the loadbalancer as follows:

   1. In the Google Cloud app, navigate to the loadbalancer.
   2. In backend configuration , select the HTTPS listener rule.
   3. Open `advanced configuration`.
   4. Set the configurations shown below.[image: image]
7. Verify that:

   - You have a valid DNS domain with an A record.
   - A TLS certificate is generated.
8. It will automatically create the GCE loadbalancer.
