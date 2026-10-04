---
title: "AWS: Install an ingress controller"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/aws-install-an-ingress-controller.html"
content_id: "9xlwwzT_tx61nHQBcMY~Qw"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:22.240678+00:00"
---

# AWS: Install an ingress controller

Install an ingress controller as described in the relevant ingress controller
documentation and Amazon AWS documentation. Also refer to:

- For further ingress controller information and Coverity ingress controller
  requirements, see Install an ingress controller
- For information on increasing the proxy body size from 1 MB in order to upload
  Coverity tools images, see Set NGINX proxy-body-size for Coverity toolkit tar file upload to Connect

Important: If you are using a Kubernetes/ingress-nginx
controller ([kubernetes/ingress-nginx](https://github.com/kubernetes/ingress-nginx)), be aware of the following
security issue: [CVE-2025-1974: ingress-nginx admission controller RCE
escalation #131009](https://github.com/kubernetes/kubernetes/issues/131009).
