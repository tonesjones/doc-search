---
title: "Container Scan"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/container-scan.html"
content_id: "HjuODacBz8fcKYoXsN_AYQ"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:41.305251+00:00"
---

# Container Scan

Container Scan is a way of running Black Duck® Detect against any type of container image (including any non-Linux, non-Docker image) and providing component risk details for each layer of the image.

Detect will accept either a user provided local .tar file path, or remote HTTP/HTTPS URL to fetch a container image .tar file for scanning.

Container scan supports both persistent (Intelligent) and Stateless scan modes in Black Duck SCA, but must be run independently of other scan types.

Execute Container Scan by adding the following to a run of Black Duck SCA:

```
--detect.tools=CONTAINER_SCAN
--detect.container.scan.file.path=<Path to local .tar file or HTTP/HTTPS URL for remote .tar file>
```

## Requirements and Limitations

### General Requirements

- Your Black Duck SCA server must have Black Duck SCA Secure Container (BDSC) licensed and enabled.
- Must have Match as a Service (MaaS) licensed, and enabled within the Black Duck SCA instance.
- A unique project version must be provided, or the scan service will respond with an error.
- Must be running Black Duck SCA 2023.10.0 or greater.
- URL provided for a remote container image must use the HTTP(S) protocol.
- Container scanning functions both with and without SCA Scan Service (SCASS). If SCASS is not enabled, the binary scanner container/pod needs to be deployed to the Black Duck SCA instance.

### Limitations

- Container scanning is limited to images of 100GB or less for hosted or local, on-prem services.

  Note: Additional hardware allocation might be required for the BDBA container when locally scanning large images.

## Invocation

- To invoke a container scan, which executes in "Intelligent" mode by default, the following must be provided at a minimum:

```
--detect.tools=CONTAINER_SCAN
--detect.container.scan.file.path=<Path to local .tar file or HTTP/HTTPS URL for remote .tar file>
```

- To invoke a stateless container scan the following must be provided at a minimum:

```
--detect.tools=CONTAINER_SCAN
--detect.container.scan.file.path=<Path to local .tar file or HTTP/HTTPS URL for remote .tar file>
--detect.blackduck.scan.mode=STATELESS
```

## Results

Container scan findings will appear in the Black Duck SCA user interface unless the scan is executed in Stateless mode, please consult the documentation provided by Black Duck SCA.

Figure 1. Container Scan results in Black Duck SCA displaying image layer findings.
[image: Container Scan Results]

## Stateless mode results

In Stateless mode, Container Scan results are saved to a json file named `name_version_BlackDuck_DeveloperMode_Result.json` in the Scan Output directory, where `name` and `version` are the project's name and version.
