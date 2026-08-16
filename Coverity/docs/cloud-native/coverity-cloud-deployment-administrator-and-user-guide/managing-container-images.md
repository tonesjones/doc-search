---
title: "Managing container images"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/managing-container-images.html"
content_id: "OcH3RqBPi4sz176KRxiEXA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:37.178084+00:00"
---

# Managing container images

This chapter describes how to manage container images used in both Connect pods and scan
services pods.

This chapter assumes that you have completed the following tasks presented in the
chapter, Obtaining Black Duck Community access, Coverity licenses, registry credentials, Helm chart, and client software.

- Requestd and obtained access to Black Duck Community.
- Requested and obtained Coverity Connect and Coverity Analysis node-unlocked
  licenses.
- Requested and obtained Black Duck Docker registry
  credentials.
- Downloaded the Helm chart from the Black Duck public
  Docker registry. See Downloading the Helm chart from the Black Duck public Docker registry.

This chapter:

- Introduces how Kubernetes manages container images, and describes the advantage of
  having your own private registry for container images. See About Kubernetes container image management.
- Describes how to create registry keys and container image pull secret keys. You need
  this for access to the registry during deployment in order to pull container images
  from the registry. See Create a container image pull secret.
- Describes how to deploy container images. You can use either of the following
  methods to manage and deploy container images, however Black Duck recommends that you create your own private
  registry to store and deploy container images:

  - Recommended: Create your own private Docker registry to store and deploy
    Black Duck container images. See Preparing to deploy containers from container images located in your own private registry.

    If you create your own container image registry, how to pull from the
    Black Duck private registry, tag, and push images to your registry. See
    Pull container images from the Black Duck private Docker registry.

    Important: When new nodes are created,
    they should become available faster if they pull container images from
    your own registry and save them in the node cache, especially if the
    registry is located near the deployment. This improves install
    performance.
  - Alternate: Deploy container images directly from the Black Duck registry.
    See Preparing to deploy containers from container images located in the Black Duck registry.

    Important: Downloading images from the
    Black Duck registry might take longer,
    resulting in a delay in new nodes becoming available, reducing install
    performance.
  - Describes how to create your own image registry. See Create your own private Docker registry.
  - Describes how to pull files from the Black Duck registry and push them to
    your private registry. See Pull container images from the Black Duck private Docker registry.
- Alternatively, describes how to deploy container images directly from the Black Duck
  registry. See Preparing to deploy containers from container images located in the Black Duck registry.
