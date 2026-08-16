---
title: "Push images to your private Docker registry"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/push-images-to-your-private-docker-registry.html"
content_id: "et5h6DG0m_WGSdgTv30imA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:46.451796+00:00"
---

# Push images to your private Docker registry

Push the pulled and tagged container images to your private Docker registry. The
following examples push the tagged `cim-downloads` image file to the
local registry at localhost:5000:

1. If needed, log into your private Docker registry using the `docker
   login` command.
2. Push a tagged image:

   ```
   docker push {tagged_image}
   ```

   where `{tagged_image}` was created with a format such as
   `{target_registry_url}:{port}/{path}/{image_name}:{version}`

   For example, to push the tagged image `localhost:5000/cim-downloads:2026.6.0`:

   ```
   % docker push localhost:5000/cim-downloads:2026.6.0
   The push refers to repository [localhost:5000/cim-downloads]
   dcb03685afb3: Pushed 
   7ba8e0936fd1: Pushed 
   1aa8a8e929ec: Pushed 
   6cbc9fbc3c68: Pushed 
   1ad6e6aa8d29: Pushed 
   625523cb9cce: Pushed 
   2026.6.0: digest: sha256:8de...d size: 1576
   %
   ```

   In this example, the image is pushed to the root directory in the registry at
   localhost:5000.
3. Verify that the image is in the registry. For example, to view a localhost
   registry:

   ```
   % curl localhost:5000/v2/_catalog
   {"repositories":["cim-downloads","anotherimage",...]}
   %
   ```
4. Repeat for all images that need to be pushed to your private Docker registry
   .
5. When finished, logout from your private Docker registry using the `docker
   logout` command.
