---
title: "GCP: Install an ingress controller"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/gcp-install-an-ingress-controller.html"
content_id: "Ppl9JlqjZARnjnUsK2Z48g"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:41:27.211503+00:00"
---

# GCP: Install an ingress controller

Install an ingress controller as described in the relevant ingress controller
documentation and Google GCP documentation. Also refer to:

- For further ingress controller information and Coverity ingress controller
  requirements, see Install an ingress controller
- For information on increasing the proxy body size from 1 MB in order to upload
  Coverity tools images, see Set NGINX proxy-body-size for Coverity toolkit tar file upload to Connect

Important: If you are using a Kubernetes/ingress-nginx
controller ([kubernetes/ingress-nginx](https://github.com/kubernetes/ingress-nginx)), be aware of the following
security issue: [CVE-2025-1974: ingress-nginx admission controller RCE
escalation #131009](https://github.com/kubernetes/kubernetes/issues/131009).
