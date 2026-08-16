---
title: "Ingress headers: creating an Ingress annotation for Google GCP"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ingress-headers-creating-an-ingress-annotation-for-google-gcp.html"
content_id: "seYWUaEvBrVDo2ABqIt~qw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:44.755884+00:00"
---

# Ingress headers: creating an Ingress annotation for Google GCP

This section describes how to resolve an issue where, in GCP, the SAML Assertion Consumer
Service URL uses http instead of https within a Coverity cloud cluster. This issue
affects communication between the IdP and the SP. All communications must use https, not
http.

To solve this issue, upload your TLS certificate and key directly to Google Cloud, and
provide an annotation that directs the GKE Ingress controller to use the uploaded
certificate. For example:

```
ingress.gcp.kubernetes.io/pre-shared-cert
```
