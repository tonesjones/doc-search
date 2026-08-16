---
title: "Preparing to deploy containers from container images located in your own private registry"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/preparing-to-deploy-containers-from-container-images-located-in-your-own-private-registry.html"
content_id: "eISaEjITyJjPfxrOrapQYg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:43.881692+00:00"
---

# Preparing to deploy containers from container images located in your own private registry

To prepare to deploy Coverity cloud containers from container images located in your own
private registry:

Important: Recommended method.

1. Create your own private registry for Black Duck container
   images. See Create your own private Docker registry.
2. Recommended: Create your own private Docker registry for downloaded Black Duck install images and Helm chart. See Create your own private Docker registry.
3. Access and copy the Black Duck Docker registry
   login credentials. See Access the Black Duck private Docker registry credentials
4. Pull the Black Duck container images and push them to
   your private registry. See Coverity container images.
5. Create a container image pull secret to access your registry. See Create a container image pull secret.
6. Update the following Helm key(s) with the name of the image pull secret.

   For a single repository that is stores both cnc and scan-services container
   images:

   ```
   global:
     imagePullSecret: ""
   ```

   For separate repositories, one for Connect images (cnc chart) and one for scan
   services images (scan-services chart):

   ```
   cnc:
     imagePullSecret: ""

   scan-services:
     imagePullSecret: ""
   ```
7. You need to configure some of the following Helm key values, depending on what
   you are deploying and how you design your repository(s).

   **Global image Helm keys:** Set these values if you create a single repository
   to store all container images. If set, these keys apply to both the cnc chart
   and scan-services subchart, unless overridden.

   ```
   global:
     imagePullSecret: ""
     imageRegistry: "COVERITY_IMAGE_REGISTRY"  # Use this key if you create a single registry for all container images.
     imageVersion: ""
     imageTagSuffix: ""  # If you are deploying on Open Shift, you need to set the value to "-ubi".
   ```

   **cnc chart image Helm keys:** The following values are not global. However,
   they can provide overrides for specific images in the cnc chart. These values
   apply only to images in the cnc chart. The scan-services chart contains an
   equivalent set of these Helm keys that apply only to the scan-services chart.
   The only time you might need to set the following values is if you use different
   repositories for cnc chart container images vs scan-services chart container
   images.

   ```
   imagePullPolicy: ""
   imagePullSecret: ""
   imageRegistry: ""
   imageVersion: ""
   imageTagSuffix: ""
   ```

   In the cnc chart, you can either accept the default values of the following Helm
   keys, or override the value(s) for custom values. These keys specific to
   individual containers and container images in the cnc chart. If you are using a
   single registry and are not customizing the image names and tags, you can accept
   the following default values.

   ```
   cim:
    cimdownloads:
       image: "cim-downloads" 
       registry: ""
       version: "CIM_VERSION" 

    cimtools:
       enabled: true 
       image: "cim-tools"
       registry: ""
       version: "CIM_VERSION" 

     cimweb:
       image: "cim-web"
       registry: ""
       version: "CIM_VERSION"

     cimweb:
       tlsSidecar:
         image: "nginx"
         registry: ""
         version: "1.27.4" 
         enabled: false
   ```

   **scan-services subchart image Helm keys:** The Helm keys that follow are
   specific to individual containers and container images in the scan-services
   chart. In the scan-services subchart, you can either accept the default values
   of the following Helm keys, or override the value(s) for custom values. These
   keys specific to individual containers and container images in the scan-services
   subchart If you are using a single registry and are not customizing the image
   names and tags, you can accept the following default values.

   ```
   cache-service:
     image: "cache-service" 
     registry: ""
     version: "CACHE_SERVICE_VERSION" 

   common-infra:
     image: "common-infra"
     registry: ""
     version: "COMMON_INFRA_VERSION"

   scan-service:
     image: "scan-service" 
     registry: ""
     version: "SCAN_SERVICE_VERSION"

     dispatcher:
       imagePullPolicy: "IfNotPresent" 

     migrateJob:
       image: "scan-service-migration" 
       registry: ""
       version: "SCAN_SERVICE_VERSION" 

     jobRunner:
       image: "job-runner"
       registry: ""
       version: "RUNNER_VERSION"

   storage-service:

     image: "storage-service" 
     registry: ""
     version: "STORAGE_SERVICE_VERSION" 

     migrateJob:
       image: "storage-service-migration"
       registry: ""
       version: "STORAGE_SERVICE_VERSION"
   ```
8. If you are deploying on Red Hat Open Shift, you need to set the -ubi tag as shown in
   the following Helm key:

   ```
   global:
     imageTagSuffix: "-ubi"
   ```
9. To use Docker commands to pull container images from the Black Duck registry. tag
   the images, and push push them to your registry:

   1. Pull container images from the Black Duck
      private Docker registry, See Pull container images from the Black Duck private Docker registry.
   2. Tag the container images,, See Tag images.
   3. Push the container images to your private Docker registry, See Push images to your private Docker registry.

As defined in the Helm chart, Kubernetes will pull images from your registry as needed
for each node so that the specified pods can be created on the node.
