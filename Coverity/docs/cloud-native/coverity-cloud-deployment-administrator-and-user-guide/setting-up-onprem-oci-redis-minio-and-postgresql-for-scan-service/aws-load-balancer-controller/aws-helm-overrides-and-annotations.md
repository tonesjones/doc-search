---
title: "AWS: Helm overrides and annotations"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-helm-overrides-and-annotations.html"
content_id: "CW7zEolM4OzzQpt_PZRY_g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:20.796478+00:00"
---

# AWS: Helm overrides and annotations

Configure the following Helm overrides, annotations, and AWS parameters:

1. In the `cnc` chart `values.yaml` file, override the
   `global.ingress.class: "nginx"` Helm key value with:
   `"alb"` as shown here:

   ```
   global.ingress.class: "alb"
   ```
2. In the `cnc` chart, `values.yaml` file, override
   the `global.ingress.path: "/"`Helm key value
   with:`"/*"` as shown here:

   ```
   global.ingress.path: "/*"
   ```
3. Add the following ingress annotations:

   ```
   ...
     alb.ingress.kubernetes.io/backend-protocol: HTTPS
     alb.ingress.kubernetes.io/certificate-arn: >- arn:aws:acm:ap-south-1:<account>:certificate/de263754-cd93-4099-b444-453354631291
     alb.ingress.kubernetes.io/healthcheck-path: /liveness
     alb.ingress.kubernetes.io/listen-ports: '[{"HTTPS":443}, {"HTTP":80}]'
     alb.ingress.kubernetes.io/scheme: internet-facing
     alb.ingress.kubernetes.io/target-type: ip
   ```
4. When you deploy the `cnc` chart, it will generate the load
   balancer URL. For example:

   ```
   k8s-test-123b6b3e39-1784449701.ap-south-1.elb.amazonaws.com
   ```
