---
title: "Downloading Sigma"
source_url: "https://docs.blackduck.com/r/sigma/2026.8.0/sigma-documentation/downloading-sigma.html"
content_id: "RdM25X09Uuag4~rTRldwCg"
version: "2026.8.0"
section: "Sigma User Guide"
scraped_at: "2026-08-13T00:25:03.014759+00:00"
---

# Downloading Sigma

This section explains how you get the binaries or the Docker images for Sigma. You can
use either format in the CI/CD templates used to include Sigma in your builds.

Sigma binaries or Docker images are available from the Black Duck Community.

Note: To download Sigma, you must have a current Coverity license: that is, a license that
has been granted or renewed as of June, 2021. Once you have the license, login on the
Black Duck Community (<https://community.blackduck.com/s/>),
navigate to LICENSES&DOWNLOADS > Downloads, and you can select the most current version of Sigma from the
Premium Downloads tab. (You do not need to install
Coverity.)

**The basic workflow for running Sigma from the command line**:

1. Download Sigma as a binary or Docker image.
2. Execute Sigma commands.

**The basic workflow for running Sigma in a CI/CD pipeline:**

1. Download Sigma as a binary or Docker image.
2. Upload Sigma to a location the CI/CD platform can access.
3. Create your CI/CD job templates to use the URL to download the binary, or pull
   the docker image for Sigma and run it.

   For more information, see  and .
