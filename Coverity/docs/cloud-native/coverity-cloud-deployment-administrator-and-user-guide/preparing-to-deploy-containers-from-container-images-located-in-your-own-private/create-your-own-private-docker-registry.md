---
title: "Create your own private Docker registry"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/create-your-own-private-docker-registry.html"
content_id: "nW8H0Q2U2lVr8v4fcs7Flg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:44.517740+00:00"
---

# Create your own private Docker registry

This step is optional, however we recommend that you create your own private Docker
registry for container images. This private registry enables you to manage container
images pulled from the Black Duck private registry and
provides the Kubernetes cluster fast private image access. There are many ways that you
can create your own private Docker registry. For information on building a private
Docker registry, refer to the following documentation:

- To deploy a registry and copy images from Docker Hub to the registry: <https://distribution.github.io/distribution/about/deploying/>
- GitHub configure a registry: <https://distribution.github.io/distribution/about/configuration/>
- Amazon ECR: <https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html>
- Google GCP using gcloud: <https://cloud.google.com/sdk/gcloud/reference/artifacts/repositories/create>
- Microsoft Azure: <https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-portal?tabs=azure-cli>
- Red Hat OpenShift: <https://docs.openshift.com/container-platform/3.11/architecture/infrastructure_components/image_registry.html>

## Example: Creating a private Docker registry in GCP

This section provides an example of how you might use the `gcloud artifacts
repositories create` command to create a private Docker registry for
Coverity cloud container images.

```
gcloud artifacts repositories create ${REGISTRY_NAME} \
    --location=${CNC_REGION} \
    --repository-format=docker \
    --labels=created-by=$CREATED_BY_LABEL
```

You will pull container images from the Black Duck
private Docker registry and push the container images to your private registry as
described in Coverity container images.
