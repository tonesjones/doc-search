---
title: "Getting the Docker Image"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/getting-the-docker-image.html"
content_id: "VWG4WRpwJiLzkSqo3Qq1YA"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:04.322552+00:00"
---

# Getting the Docker Image

Please see Downloading Sigma for prerequisites.

You download the Sigma Docker image as a tarball. If you're using the image in a
CI/CD pipeline, you can then use Docker to upload that image to the Docker registry
you have configured.

**Follow these steps to download the Docker image and upload it to your Docker
registry.**

1. Download the Sigma Docker image

   Download the gzipped tar ball (.tar.gz) from Black Duck Community.
2. For CI/CD: Use the `docker` command to login to the registry and
   be able to push the image:

   ```
   docker login <YOUR_DOCKER_REGISTRY_SERVER>
   ```
3. For CI/CD: Load the Sigma image into the local registry with a name and a
   tag.

   ```
   docker load < <PATH_TO_TARBALL>
   ```

   Replace `<PATH_TO_TARBALL>` with the path where the docker
   image tarball is located.
4. For CI/CD: Check that the image was loaded into your registry. You can use
   this information to retag the image if needed.

   ```
   docker images
   ```
5. For CI/CD: Once you have the current repository name and tag after loading the
   image, you can then tag it with a name of your choosing.

   ```
   docker tag <LOADED_REPO_NAME>:<LOADED_TAG_NAME> <REPO_NAME>:<TAG_NAME>
   ```

   For CI/CD integrations, the `REPO_NAME` and
   `TAG_NAME` will be used in the job/workflow template to
   identify the image to pull from the registry in order to run Sigma.
6. For CI/CD: Push the Sigma image to the registry.

   ```
   docker push <REPO_NAME>:<TAG_NAME>
   ```

   Pushing the image allows any CI/CD job runner to access the image from the
   Docker registry if the CI/CD runner has access to the registry.

   Note: If you use `docker push` with the same image name and tag
   name as an image already present in the registry, the image you are pushing
   will replace the image in the registry.
7. For CI/CD: Log out of your Docker registry after you are done using the
   `docker push` command.
8. For CI/CD: Create your CI/CD job templates to use Sigma with a Docker
   image.
