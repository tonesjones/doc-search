---
title: "AWS: Generating a CNAME ingress certificate"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/aws-generating-a-cname-ingress-certificate.html"
content_id: "Fb6M91OVThhQtE_0wh5zZA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:21.629276+00:00"
---

# AWS: Generating a CNAME ingress certificate

Create the following AWS ingress certificate and configure related parameters:

1. Either import an ingress certificate, or using AWS Certificate Manager (ACM),
   generate an ingress certificate. To generate a certificate using ACM, see <https://docs.aws.amazon.com/res/latest/ug/acm-certificate.html>.
2. Generate a CNAME in AWS ROUTE 53.
3. Add the certificate ARN as an annotation.
4. If you get CORS error messages while uploading analysis tool files, set the
   following configuration in the ALS UI:

   1. Navigate to EC2 > Loadbalancer.
   2. Select the load balancer.
   3. Select Listeners and select the HTTPS listener.
   4. Select Attributes > Edit.
   5. Set the Application Load Balancer HTTP header configuration shown below.
      This enables CORS (Cross Origin Resource Sharing), which is required for
      a manual tool upload.

      [image: image]

      Note: if you
      have an issue when downloading large files with alb loadbalancer,
      disable `http/2`as follows:
      1. Select the loadbalancer.
      2. Select attributes > edit > disble http/2.
      3. Save the configuration.
