---
title: "Deprecated Properties"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/deprecated-properties.html"
content_id: "bGEf0T0mivmwBXYI3fcytw"
version: "12.0.0"
section: "Detect Properties"
scraped_at: "2026-09-07T21:17:03.063680+00:00"
---

# Deprecated Properties

This page lists Black Duck® Detect deprecated properties for software versions that are still supported. This page may be blank when there are no such deprecated properties. For both active and deprecated properties, refer to all properties for usage details.

## paths

| Property | Description |
| --- | --- |
| detect.java.path | Java Executable: Path to the Java executable used by Docker Inspector.  **DEPRECATED: This property is only used by Docker Inspector. Docker Inspector support is deprecated. This property will be removed in 13.0.0.** |

## docker

| Property | Description |
| --- | --- |
| detect.docker.passthrough | Docker Passthrough: Additional properties may be passed to the docker inspector by adding the prefix detect.docker.passthrough to each Docker Inspector property name and assigning a value. The 'detect.docker.passthrough' prefix will be removed from the property name to generate the property name passed to Docker Inspector (with the given value).  **DEPRECATED: Docker Inspector support is deprecated. This property will be removed in 13.0.0.** |
| detect.docker.image | Docker Image Name: The Docker image name (repo:tag) to inspect.  **DEPRECATED: Docker Inspector support is deprecated. This property will be removed in 13.0.0.** |
| detect.docker.image.id | Docker Image ID: The ID (shown in the 'IMAGE ID' column of 'docker images' output) of the target Docker image. The target image must already be local (must appear in the output of 'docker images').  **DEPRECATED: Docker Inspector support is deprecated. This property will be removed in 13.0.0.** |
| detect.docker.inspector.path | Docker Inspector Path: Use this property to point Detect to a local Docker Inspector jar file, instead of the default Docker Inspector jar file that Detect downloads from the binary repository. You need to ensure the version is compatible (the same major version that Detect downloads by default).  **DEPRECATED: Docker Inspector support is deprecated. This property will be removed in 13.0.0.** |
| detect.docker.inspector.version | Docker Inspector Version: Version of the Docker Inspector to use. By default Detect will attempt to automatically determine the version to use.  **DEPRECATED: Docker Inspector support is deprecated. This property will be removed in 13.0.0.** |
| detect.docker.path | Docker Executable: Path to the docker executable (used to load image inspector Docker images in order to run the Docker Inspector in air gap mode).  **DEPRECATED: Docker Inspector support is deprecated. This property will be removed in 13.0.0.** |
| detect.docker.platform.top.layer.id | Platform Top Layer ID: To exclude components from platform layers from the results, assign to this property the ID of the top layer of the platform image. Get the platform top layer ID from the output of 'docker inspect platformimage:tag'. The platform top layer ID is the last item in RootFS.Layers. For more information, see 'Isolating application components' in the Docker Inspector documentation.  **DEPRECATED: Docker Inspector support is deprecated. This property will be removed in 13.0.0.** |
| detect.docker.tar | Image Archive File: An image .tar file which is either a Docker image saved to a file using the 'docker save' command, or an Open Container Initiative (OCI) image .tar file. The file must be readable by all.  **DEPRECATED: Docker Inspector support is deprecated. This property will be removed in 13.0.0.** |
