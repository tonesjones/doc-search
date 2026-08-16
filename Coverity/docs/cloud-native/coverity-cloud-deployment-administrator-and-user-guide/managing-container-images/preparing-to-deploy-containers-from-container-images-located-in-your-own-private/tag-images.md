---
title: "Tag images"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/tag-images.html"
content_id: "HfqQxuMmSQvW5Dsvt4iUqg"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:45.815900+00:00"
---

# Tag images

Tag the pulled container images to provide version or other metadata information:

1. List the pulled images that are in the host node and locate the image to tag. For
   example, we will tag the images identified in bold:

   ```
   % docker images
   REPOSITORY                                               TAG        IMAGE ID       CREATED      SIZE
   registry                                                            8db46f9d7550   8 days ago   24.2MB
   repo.blackduck.com/containers/scan-service-migration     2026.6.0   b66ba81729c1   2 weeks ago  223MB
   repo.blackduck.com/containers/scan-service               2026.6.0   5c44d4c6cd16   2 weeks ago  68.6MB
   repo.blackduck.com/containers/job-runner                 2026.6.0   633cb2e03c61   2 weeks ago  1.01GB
   repo.blackduck.com/containers/cim-downloads              2026.6.0   11147c2d8404   2 weeks ago  913MB
   repo.blackduck.com/containers/cim-web                    2026.6.0   700087b322a3   2 weeks ago  555MB
   repo.blackduck.com/containers/cim-tools                  2026.6.0   82bcf6c2311f   2 weeks ago  447MB
   repo.blackduck.com/containers/cache-service              2026.6.0   69e2df321765   7 weeks ago  270MB
   repo.blackduck.com/containers/storage-service-migration  2026.6.0   246635a4f3d0   7 weeks ago  223MB
   repo.blackduck.com/containers/storage-service            2026.6.0   d55ebbdaa389   7 weeks ago  28.7MB
   repo.blackduck.com/containers/common-infra               2026.6.0   d98a723afac7   7 weeks ago  37.7MB
   ...
   %
   ```
2. Map an image to your registry and tag the image with version or other information
   using the syntax:

   ```
   docker tag {REGISTRY_FROM}/{image_name}:{version_tag} {REGISTRY_TO}/{image_name}:{version_tag}
   ```

   For example, to map the `repo.blackduck.com/containers/cim-downloads:2026.6.0` image to a localhost registry and tag
   it with the image version:

   ```
   % docker tag repo.blackduck.com/containers/cim-downloads:2026.6.0 localhost:5000/cim-downloads:2026.6.0
   ```

   Another example, to map the `repo.blackduck.com/containers/job-runner:2026.6.0` image to a localhost registry and tag
   it with the image version:

   ```
   % docker tag repo.blackduck.com/containers/job-runner:2026.6.0
      localhost:5000/job-runner:2026.6.0
   ```
3. List the images and find the newly-tagged images. For example, in bold:

   ```
   % docker images
   REPOSITORY                                              TAG        IMAGE ID       CREATED       SIZE
   registry                                                           8db46f9d7550   8 days ago    24.2MB
   repo.blackduck.com/containers/scan-service-migration    2026.6.0   b66ba81729c1   2 weeks ago   223MB
   repo.blackduck.com/containers/scan-service              2026.6.0   5c44d4c6cd16   2 weeks ago   68.6MB
   localhost:5000/job-runner                               2026.6.0   633cb2e03c61   2 weeks ago   1.01GB
   localhost:5000/cim-downloads                            2026.6.0   11147c2d8404   2 weeks ago   913MB
   repo.blackduck.com/containers/cim-web                   2026.6.0   700087b322a3   2 weeks ago   555MB
   repo.blackduck.com/containers/cim-tools                 2026.6.0   82bcf6c2311f   2 weeks ago   447MB
   repo.blackduck.com/containers/cache-service             2026.6.0   69e2df321765   7 weeks ago   270MB
   repo.blackduck.com/containers/storage-service-migration 2026.6.0   246635a4f3d0   7 weeks ago   223MB
   repo.blackduck.com/containers/storage-service           2026.6.0   d55ebbdaa389   7 weeks ago   28.7MB
   repo.blackduck.com/containers/common-infra              2026.6.0   d98a723afac7   7 weeks ago   37.7MB
   ...
   %
   ```
4. Repeat for all pulled images that need to be pushed to your private registry.
5. Delete any duplicate or unused images from the host node using the `docker
   rmi` command.
