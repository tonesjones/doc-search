---
title: "About Kubernetes container image management"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/about-kubernetes-container-image-management.html"
content_id: "LVM1sisNRhPjFBkpfPQxdQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:37.822773+00:00"
---

# About Kubernetes container image management

Kubernetes does not download an image for each pod instance, when the node is created, it
pulls relevant container images from a registry and caches the container images locally
in the node's cache.

Since container images are cached on the node, as pods are scaled up, containers within
the pod are created using the locally-cached images. This makes for rapid, efficient
scaling.

The initial image pull from a registry can take time, especially for a large image and
for a registry that might have a lot of demand. Managing your own registry, especially
if local to the Coverity cloud deployment, can significantly mitigate delays and
increase speed at which nodes are deployed.
