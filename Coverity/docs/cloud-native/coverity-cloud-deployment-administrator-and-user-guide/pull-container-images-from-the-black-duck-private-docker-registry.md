---
title: "Pull container images from the Black Duck private Docker registry"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/pull-container-images-from-the-black-duck-private-docker-registry.html"
content_id: "So_ZG_HgCjdBCeNWmGjeKw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:45.166873+00:00"
---

# Pull container images from the Black Duck private Docker registry

This section describes how to pull Coverity cloud container images from the Black Duck
private Docker registry.

Refer to Docker documentation for Docker CLI command syntax: <https://docs.docker.com/engine/reference/commandline/docker/>

The Black Duck registry is `repo.blackduck.com`. In `docker` commands, do not
include `https://`.

To pull container images from the Black Duck private Docker registry:

1. Log into the Black Duck private Docker registry at
   `repo.blackduck.com` using the Docker login command:

   ```
   % docker login repo.blackduck.com
   ```

   Provide the credentials returned by **View/Request Docker Registry
   Credential** in the Black Duck Community Licenses page. See
   Access the Black Duck private Docker registry credentials
2. Pull the container images as needed from the Black Duck private Docker registry. For a list of container images provided with this
   release, refer to Coverity container images.

   ```
   docker pull repo.blackduck.com/containers/{image_name}:{version}
   ```

   For
   example, to pull the `cim-downoads` image for 2026.6.0:

   ```
   % docker pull repo.blackduck.com/containers/cim-downloads:2026.6.0
   ```

   Or,
   to pull the job runner
   image:

   ```
   % docker pull repo.blackduck.com/containers/job-runner:2026.6.0
   ```
3. When finished pulling images, logout of the Black Duck private Docker
   registry:

   ```
   % docker logout
   ```
