---
title: "Running Detect within a Docker container"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/running-detect-within-a-docker-container.html"
content_id: "l9KpH52rqj9Vz~c659xKQA"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:38.411817+00:00"
---

# Running Detect within a Docker container

Detect publishes Docker images which can be used to run Detect from within a Docker container.

Detect Docker images are published to `hub.docker.com` and `repo.blackduck.com`.

## To obtain and use Detect images

To run a container built from a Detect image, use the Docker CLI's `docker run` command.

- Use the -it options to view logs during the container run.
- Use the -v option to create a bind mount that will link a provided path to project source on your host to the /source directory within the container. Do this in place of providing the --detect.source.path property, as you would when running Detect via the script or jar.
- You may also use the -v option to create a bind mount that will link a provided path to an output directory on your host to the /output directory within the container. Do this in place of providing the --detect.output.path property, as you would when running Detect via the script or jar.
- Use the --rm option to clean up the container once it exits.
- Provide Detect property values as you would when running via the Detect script or the Detect jar, at the end of the `docker run` command.

Find available images via [Docker public image registry](https://hub.docker.com/r/blackducksoftware/detect) or [Black Duck private image registry](https://repo.blackduck.com/containers/blackducksoftware/detect).

Example pull commmands:

```
#hub.docker.com
docker pull blackducksoftware/detect:10.4.0
#repo.blackduck.com
docker pull repo.blackduck.com/containers/blackducksoftware/detect:10.4.0
```

Find the source, Dockerfiles [here](https://github.com/blackducksoftware/detect-docker).

The format of image names is: `blackducksoftware/detect:[detect_version]-[package_manager]-[package_manager_version]`

- If you want an image with the latest supported release for a major version of Detect, and the latest supported version of a package manager, such images are named in the following format: `blackducksoftware/detect:[detect_major_version]-[package_manager]`

### Detect Basic Images

If you wish to build your own custom Detect image, to run Detect in buildless mode, or to run non-detector tools such as the Signature Scanner or Binary Scanner, there also exist "simple" Detect images. These images contain no package manager files or executables.

The format of "simple" image names is: `blackducksoftware/detect:[detect_version]`

- If you want an image with the latest supported release for a major version of Detect, such images are named in the following format: `blackducksoftware/detect:[detect_major_version]`

#### Detect Buildless Images

There also exist "buildless" Detect images. These images automatically pass the argument --detect.accuracy.required=NONE when running to make Detect as resilient as possible (it will evaluate all applicable detectors, regardless of their accuracy, in order to get results).

The format of "buildless" image names is: `blackducksoftware/detect:[detect_version]-buildless`

- If you want a buildless image with the latest supported release for a major version of Detect, such images are named in the following format: `blackducksoftware/detect:[detect_major_version]-buildless`

#### Detect IaC Images

If you wish to perform an IaC Scan via Detect in a Docker container, there exist "iac" Detect images. The scanner that Detect uses to perform IaC scans is not supported in other Detect images.

The format of "iac" image names is: `blackducksoftware/detect:[detect_version]-iac`

- If you want an iac image with the latest supported release for a major version of Detect, such images are named in the following format: `blackducksoftware/detect:[detect_major_version]-iac`

### Examples

`docker run -it --rm -v [/path/to/source]:/source -v [/path/to/outputDir]:/output blackducksoftware/detect:[detect_image_tag] [detect_arguments]`

`docker run -it --rm -v /home/my/gradle/project:/source -v /home/for/detect/output/files:/output blackducksoftware/detect:10.0.0 --blackduck.url=https://my.blackduck.url --blackduck.api.token=MyT0kEn`

`docker run -it --rm -v /home/my/maven/project:/source -v /home/for/detect/output/files:/output blackducksoftware/detect:9 --blackduck.url=https://my.blackduck.url --blackduck.api.token=MyT0kEn`

`docker run -it --rm -v /home/my/project:/source -v /home/for/detect/output/files:/output blackducksoftware/detect:9.7.0 --blackduck.url=https://my.blackduck.url --blackduck.api.token=MyT0kEn --detect.accuracy.required=NONE`

`docker run -it --rm -v /home/my/project:/source -v /home/for/detect/output/files:/output blackducksoftware/detect:9.6.0 --blackduck.url=https://my.blackduck.url --blackduck.api.token=MyT0kEn --detect.tools=SIGNATURE_SCAN,BINARY_SCAN`
