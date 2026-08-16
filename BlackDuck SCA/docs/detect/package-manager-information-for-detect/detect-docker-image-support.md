---
title: "Detect Docker image support"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-docker-image-support.html"
content_id: "FFVX6MZXprQxxyTXmGNnog"
version: "11.5.1"
section: "Package Manager information for Detect"
scraped_at: "2026-08-08T23:44:54.031027+00:00"
---

# Detect Docker image support

## Related properties

Detector properties

## Overview

On Linux, Mac, and Windows 10 Enterprise, Detect can invoke Detect Docker Inspector to inspect Linux Docker images to discover packages installed by the Linux package manager.
For simple use cases, add `--detect.docker.image={repo}:{tag}`, `--detect.docker.tar={path to an image archive}`, or
`--detect.docker.image.id={image id}`,
to the Detect command line.

When passed a value for *detect.docker.image*, *detect.docker.image.id*, or *detect.docker.tar*,
Detect runs Detect Docker Inspector on the given image (the "target image"),
creating one BDIO file for one code location.

Detect Docker Inspector will:

1. Discover packages (components) installed in a given Linux image by analyzing the contents of the Linux package manager database.
2. Provide to Detect, for any image, potentially useful targets (file archives) for signature and binary scanning.

Detect Docker Inspector does not run the target image, so it is safe to run it on untrusted images.

While earlier versions of Detect Docker Inspector could be run standalone,
the only way to use Detect Docker Inspector now and in the future is
to run Detect on a Docker image.

## Package (component) discovery

For package discovery on a Linux image, Detect Docker Inspector extracts the Linux package manager
database from the image, and utilizes the appropriate Linux package manager to provide a list of
the installed packages, which
it returns to Detect in BDIO (Black Duck SCA Input Output) format.
Because it relies on the Linux package manager as its source of this data,
the discovered packages are limited to those installed and managed using the Linux package manager.

Detect Docker Inspector can discover package manager-installed components in
Linux Docker images that use the DPKG, RPM, or APK package manager database formats.

## Signature and binary scan targets

Signature and binary scan targets contain the container file system.
The container file system
is the file system that a container created from the target image. The
container file system is (by default) returned to Detect in two forms:
as an archive file that contains the container file system (the preferred format for binary
scanning), and as a saved squashed (single layer) image
that contains the container file system (the preferred format for signature scanning).

## Non-linux images

When run on a non-Linux image (for example, a Windows image,
or an image that contains no operating system), Detect Docker Inspector
will return to Detect a BDIO file with zero components
along with the signature and binary scan targets.
Components may be discovered for these images
during the signature and/or binary scanning performed by
Detect.

## Modes of operation

Detect Docker Inspector has two modes:

- Host mode, for running on a server or virtual machine (VM) where Detect Docker Inspector can perform Docker operations using a Docker Engine.
- Container mode, for running inside a container started by Docker, Kubernetes, OpenShift, and others.

In either mode, Detect Docker Inspector runs as a Detect inspector to extend the capaibilities of Detect.
Detect Docker Inspector is more complex than most Detect inspectors because it relies on container-based services
(the image inspector services)
to perform its job. When running on a host machine that has access to a Docker Engine ("host mode"),
Detect Docker Inspector can start and manage the image inspector services (containers) automatically.
When Detect and Detect Docker Inspector are running within a Docker container
("container mode"), the image inspector services must be started and managed by the user or
the container orchestration system.

### Host mode

Host mode (the default) is for servers/VMs where Detect Docker Inspector can perform Docker operations (such as pulling an image)
using a Docker Engine.

Host mode requires that Detect Docker Inspector can access a Docker Engine. https://github.com/docker-java/docker-java utilizes the
[docker-java library](https://github.com/docker-java/docker-java) to act as a client of that Docker Engine.
This enables Detect Docker Inspector to pull the target image from a Docker registry such
as Docker Hub. Alternatively, you can save an image to a .tar file by using the *docker save* command. Then, run Detect Docker Inspector (via Detect)
on the .tar file. See Supported image formats for details on supported .tar file formats.

In Host mode, Detect Docker Inspector can also pull, run, stop, and remove the image inspector service images as needed,
greatly simplifying usage, and greatly increasing run time.

### Container mode

Container mode is for container orchestration environments (Kubernetes, OpenShift, etc.)
where Detect and Detect Docker Inspector run
inside a container where Detect Docker Inspector cannot perform Docker operations.
For information on running Detect Docker Inspector in container mode,
refer to Deploying.

It is possible to utilize container mode when running Detect and Detect Docker Inspector on a host
that supports host mode. Container mode is more difficult to manage than host mode,
but you might choose container mode in order to increase throughput (to scan more images per hour).
Most of the time spent by Detect Docker Inspector running in host mode is spent starting and stopping the image inspector services.
When these services are already running (in the usual sense of the word "service")
as they do in container mode,
Detect Docker Inspector executes much more quickly than it would in host mode.

## Requirements

Requirements for including Detect Docker Inspector in a Detect run
include of all of Detect's requirements plus:

- Three available ports for the image inspector services. By default, these ports are 9000, 9001, and 9002.
- The environment must be configured so that files created by Detect Docker Inspector are readable by all. On Linux, this means an appropriate umask value (for example, 002 or 022 would work). On Windows, this means the
  Detect "output" directory (controlled by the Detect property *detect.output.path*)
  must be readable by all.
- In host mode: access to a Docker Engine versions 17.09 or higher running as root.
- In container mode: you must start the Detect Docker Inspector container that meets the preceding requirements, and three container-based
  "image inspector" services. All four of these containers must share a mounted volume and be able to reach each other through HTTP GET operations using base URLs
  that you provide. For more information, refer to Deploying.

## Running Detect Docker Inspector

To invoke Detect Docker Inspector, pass a docker image to
Detect via one of the following properties:

- detect.docker.image
- detect.docker.image.id
- detect.docker.tar

## Advanced usage (using passthrough properties)

The most common cases of Detect Docker Inspector can be configured using
Detect properties.
However, there are scenarios (including container mode)
that require access to Detect Docker Inspector advanced properties for which there is no corresponding
Detect property.
For the list of Detect Docker Inspector advanced properties, see Advanced properties.

When you need to set one of the Detect Docker Inspector advanced properties,
construct the Detect property name by prefixing the Docker Inspector property name with `detect.docker.passthrough.`.

Suppose you need to set Docker Inspector's `service.timeout` value (the length of time Docker Inspector waits for a response from the Image Inspector services that it uses) to 480000 milliseconds. You add the prefix to the Docker Inspector property name to derive the Detect property name `detect.docker.passthrough.service.timeout`. Therefore, add `--detect.docker.passthrough.service.timeout=480000` to the Detect command line.

For example:

```
./detect11.sh --detect.docker.image=ubuntu:latest --detect.docker.passthrough.service.timeout=480000
```

You can set any Detect Docker Inspector property using this method.
However, you should not use this method to change the value of the Detect Docker Inspector property `output.path`.
Detect sets this property and changing its value via the passthrough mechanism will make it impossible
for Detect to find Detect Docker Inspector's output files.

## Transitioning from Black Duck SCA Docker Inspector to Detect

If you have been running the Black Duck SCA Docker Inspector directly, and need to transition to
invoking Detect Docker Inspector from Detect, here are some recommendations likely to
help you make the transition:

1. If you run Black Duck SCA Docker Inspector with `blackduck-docker-inspector.sh`, replace `blackduck-docker-inspector.sh` in your command line with `detect11.sh` (adjust the Detect major version as necessary or run `detect.sh` to always pick up the latest Detect release).
   See the Detect documentation for information on where to get the Detect script.
2. If you run Black Duck SCA Docker Inspector with `java -jar blackduck-docker-inspector-{version}.jar`, replace `blackduck-docker-inspector-{version}.jar` in your command line with `blackduck-detect-{version}.jar`.
   See the Detect documentation for information on where to get the Detect .jar.
3. For each of the following properties used in your command line, add `detect.` to the beginning of the property name: docker.image, docker.image.id, docker.tar, docker.platform.top.layer.id. For example, change `--docker.image=repo:tag` with `--detect.docker.image=repo:tag`.
4. For all other Docker Inspector properties used in your command line, add `detect.docker.passthrough.` to the beginning of the property name. For example, change `--bdio.organize.components.by.layer=true` to `--detect.docker.passthrough.bdio.organize.components.by.layer=true`.
