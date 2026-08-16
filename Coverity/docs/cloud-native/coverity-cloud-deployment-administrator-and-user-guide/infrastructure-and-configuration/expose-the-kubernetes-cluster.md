---
title: "Expose the Kubernetes cluster"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/expose-the-kubernetes-cluster.html"
content_id: "DvCQqv_hWCq6h2YxOJVrNA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:53.017420+00:00"
---

# Expose the Kubernetes cluster

You must provide an ingress controller, load balancer, or other means of exposing
Coverity cloud applications outside the Kubernetes cluster. Coverity cloud does not
require an ingress controller, however, it is the most common way to provide access from
outside a Kubernetes cluster to applications running in containers within the
cluster.
