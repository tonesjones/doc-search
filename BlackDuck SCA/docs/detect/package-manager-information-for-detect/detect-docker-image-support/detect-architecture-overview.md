---
title: "Detect architecture overview"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-architecture-overview.html"
content_id: "FN0L6V0Tc2WjqNwKGvWYnQ"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:44:59.798035+00:00"
---

# Detect architecture overview

Detect Docker Inspector uses up to three container-based image inspector services;
one for each of the supported Linux package manager database formats.

The three image inspector services provide coverage of the three package manager database formats: DPKG, RPM, and APK.
By default, Detect Docker Inspector submits its request to inspect the target image to the DPKG (Ubuntu) image inspector service. All services
redirect to the appropriate image inspector service if it cannot handle the request. For example,
if the target is an Alpine image, the Ubuntu inspector service, which cannot inspect an Alpine image,
redirects to the Alpine inspector
service. If most of your images have APK databases, you can improve performance by configuring Detect Docker Inspector to route requests to the Alpine (APK) image inspector service using
the Detect Docker Inspector property *imageinspector.service.distro.default*.

In host mode (the default), Detect Docker Inspector automatically uses the Docker engine to pull as
needed from Docker Hub
the following three images: blackducksoftware/blackduck-imageinspector-alpine,
blackducksoftware/blackduck-imageinspector-centos (deprecated), and blackducksoftware/blackduck-imageinspector-ubuntu.
Detect Docker Inspector starts those services as needed,
and stops and removes the containers when Detect Docker Inspector exits. It uses a shared volume to share files, such as the target Docker image,
between the Detect Docker Inspector utility and the three service containers.

In container mode, start the container running Detect Docker Inspector and the three image inspector container-based services such that
all four containers share a mounted volume and can communicate with each other using HTTP GET operations using base URLs that you provide.
For more information, refer to Deploying.

## Execution modes

### Host mode

In host mode, Detect Docker Inspector performs the following steps on the host:

1. Pulls and saves the target image to a .tar file if you passed the image by *repo:tag*.
2. Checks to see if the default image inspector service is running. If not, it pulls the inspector image and
   starts a container, mounting a shared volume.
3. Requests the Black Duck input/output (BDIO) file and container file system by sending an HTTP GET request to the image inspector service.

The following steps are performed inside the image inspector container:

1. Builds the container file system that a container would have if you ran the target image. It does not run the target image.
2. Determines the target image package manager database format, and redirects to a different image inspector service if necessary.
3. Runs the image inspector's Linux package manager on the target image package manager database to get details of
   installed packages.
4. Produces and returns a BDIO1 (.jsonld) file consisting of a graph of target image packages and, optionally, the container filesystem.

The following steps are performed back on the host when the request to the image inspector service returns:

1. Returns the output files (BDIO and signature and binary scan targets) to Detect by copying them to the output directory.
2. Stops/removes the image inspector container. Note that this can be disabled.

### Container mode

In container mode, you start four containers in such a way that they share a mounted volume and can reach each other through HTTP GET operations using
base URLs that you provide:

- One container for Detect / Detect Docker Inspector.
- One container for each of the three image inspector services: Alpine, CentOS (deprecated), and Ubuntu.

In container mode you must provide the target image in a .tar file with one of the supported formats; you cannot specify that target image by repo:tag.

Detect invokes Detect Docker Inspector, which
requests the dependency graph (in BDIO format) and signature/binary scan targets using HTTP from the default image inspector service using a
base URL that you have provided.

The following steps are performed inside the image inspector container:

1. Builds the container file system that a container would have if you ran the target image. It does not run the target image.
2. Determines the target image package manager database format, and redirects to a different image inspector service if necessary.
3. Runs the image inspector's Linux package manager on the target image package manager database to get details of the installed packages.
4. Produces and returns a BDIO1 (.jsonld) file consisting of a graph of target image packages and, optionally, the container filesystem.

The following steps are performed by Detect Docker Inspector/Detect back in the Detect container when the request to the image inspector service returns:

1. Detect Docker Inspector returns the output files (BDIO and signature and binary scan targets) to Detect by copying them to the output directory.
2. Detect converts the BDIO to BDIO2, adjusts the project, project version, and codelocation names, and uploads it to Black Duck SCA.
3. Detect performs Black Duck signature scan and Black Duck Binary Analysis on the scan targets.

#### Deploying in container mode

Deploying in container mode is challenging and requires expertise in the container platform on which you will deploy.
We recommend engaging Professional Services for a solution tailored to your environment.

You can find several container mode deployment examples on the deployment page.
