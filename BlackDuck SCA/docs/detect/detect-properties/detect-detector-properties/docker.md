---
title: "docker"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/docker.html"
content_id: "Y2HPtopKAGoG81QIe4rHtA"
version: "11.5.1"
section: "Detect Properties"
scraped_at: "2026-08-08T23:45:35.415996+00:00"
---

# docker

## Docker Executable

```
--detect.docker.path
```

Path to the docker executable (used to load image inspector Docker images in order to run the Docker Inspector in air gap mode).

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `/usr/local/bin/docker` |

## Docker Image ID

```
--detect.docker.image.id
```

The ID (shown in the 'IMAGE ID' column of 'docker images' output) of the target Docker image. The target image must already be local (must appear in the output of 'docker images').

detect.docker.image, detect.docker.tar, and detect.docker.image.id are three alternative ways to specify an image (you should only set one of these properties).

| Details |  |
| --- | --- |
| Added | 6.1.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `fe1cc5b91830` |

## Docker Image Name

```
--detect.docker.image
```

The Docker image name (repo:tag) to inspect.

For Detect to run Docker Inspector, either this property, detect.docker.tar, or detect.docker.image.id must be set. Docker Inspector finds packages installed by the Linux package manager in Linux-based images. detect.docker.image, detect.docker.tar, and detect.docker.image.id are three alternative ways to specify an image (you should only set one of these properties). When a value of this property is provided, Docker Inspector will use the Docker engine to pull the image.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `ubuntu:22.04` |

## Image Archive File

```
--detect.docker.tar
```

An image .tar file which is either a Docker image saved to a file using the 'docker save' command, or an Open Container Initiative (OCI) image .tar file. The file must be readable by all.

detect.docker.image, detect.docker.tar, and detect.docker.image.id are three alternative ways to specify an image (you should only set one of these properties). The .tar file must conform to either of the following image format specifications: 1. Docker Image Specification v1.2.0 (https://github.com/moby/docker-image-spec/blob/main/v1.2.md), which is the format produced by the "docker save" command, or 2. Open Container Initiative Image Format Specification (https://github.com/opencontainers/image-spec/blob/main/spec.md).

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `./ubuntu21_04.tar` |

## Docker Inspector Path (Advanced)

```
--detect.docker.inspector.path
```

Use this property to point Detect to a local Docker Inspector jar file, instead of the default Docker Inspector jar file that Detect downloads from the binary repository. You need to ensure the version is compatible (the same major version that Detect downloads by default).

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional Path |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |

## Docker Inspector Version (Advanced)

```
--detect.docker.inspector.version
```

Version of the Docker Inspector to use. By default Detect will attempt to automatically determine the version to use.

| Details |  |
| --- | --- |
| Added | 3.0.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `9.1.1` |

## Docker Passthrough (Advanced)

```
--detect.docker.passthrough
```

Additional properties may be passed to the docker inspector by adding the prefix detect.docker.passthrough to each Docker Inspector property name and assigning a value. The 'detect.docker.passthrough' prefix will be removed from the property name to generate the property name passed to Docker Inspector (with the given value).

| Details |  |
| --- | --- |
| Added | 6.0.0 |
| Type | None |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `(This example is unusual in that it shows a complete propertyname=value) detect.docker.passthrough.imageinspector.service.log.length=1000` |

## Platform Top Layer ID (Advanced)

```
--detect.docker.platform.top.layer.id
```

To exclude components from platform layers from the results, assign to this property the ID of the top layer of the platform image. Get the platform top layer ID from the output of 'docker inspect platformimage:tag'. The platform top layer ID is the last item in RootFS.Layers. For more information, see 'Isolating application components' in the Docker Inspector documentation.

If you are interested in components from the application layers of your image, but not interested in components from the underlying platform layers, you can exclude components from platform layers from the results by using this property to specify the boundary between platform layers and application layers.

| Details |  |
| --- | --- |
| Added | 6.1.0 |
| Type | Optional String |
| Default Value |  |
| Comma Separated | No |
| Case Sensitive | No |
| Acceptable Values | Any |
| Strict | No |
| Example | `sha256:f6253634dc78da2f2e3bee9c8063593f880dc35d701307f30f65553e0f50c18c` |
