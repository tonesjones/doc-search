---
title: "Detect requirements and release information"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-requirements-and-release-information.html"
content_id: "HwDOsOlW4MhPmunlgRU7gA"
version: "11.5.1"
section: "Detect requirements and release information"
scraped_at: "2026-08-08T23:44:00.307453+00:00"
---

# Detect requirements and release information

## General requirements

- Minimum 8GB RAM.
- Java: OpenJDK 64-bit version 8, 11, 13, 14, 15, 16, 17, or 21. If using Java 11: 11.0.5 or higher is required.
- Minimum curl version 7.34.0, recommended 8.4.0 or later.
- Bash.
- If using detect11.ps1: PowerShell versions 4.0 or higher.
- The tools required to build your project source code.

## Network requirements and information

Note: Unless you are running Detect in Air Gap mode, access to the internet is required to download and run Detect and related components from GitHub and other locations.

- Detect script downloads should only be accessed via detect.blackduck.com.
- Detect 10.0.0 and later will only work when using repo.blackduck.com.

Tip: Configure repo.blackduck.com on network allow lists to ensure connectivity for any scripts, services, or pipelines requiring access.

- Black Duck® SCA [SCA Scan Service (SCASS)](https://community.blackduck.com/s/question/0D5Uh00000O2ZSYKA3/black-duck-sca-new-ip-address-requirements-for-2025) requires customers add or update IP addresses configured in their network firewalls or allow lists. This action is required to successfully route scan data for processing.

  - scass.blackduck.com - 35.244.200.22
  - na.scass.blackduck.com - 35.244.200.22
  - na.store.scass.blackduck.com - 34.54.95.139
  - eu.store.scass.blackduck.com - 34.54.213.11
  - eu.scass.blackduck.com - 34.54.38.252
- To collect phone home metrics, the following IP address must be allowlisted:

  - static-content.app.blackduck.com - 34.117.80.109

## Running Detect in a container

Black Duck® publishes Detect Docker images which can be used to run Detect from within a Docker container. Refer to Running Detect from within a Docker container for details.

## Running Detect in an Air Gap environment

- To run Detect without internet access, refer to Air Gap Mode.

## Black Duck SCA integration requirements

- Licensed installation of the current version of Black Duck SCA with access credentials.
  Visit the [Black Duck release page](https://github.com/blackducksoftware/hub/releases) to determine the current version of Black Duck SCA.
- For information regarding compatible versions of Black Duck SCA, consult the Black Duck SCA [Release Compatibility page](https://docs.blackduck.com/r/blackduck/black-duck-compatibility-reference/black-duck-sca-release-compatibility.html)
- The Black Duck SCA notifications module must be enabled.
- A Black Duck SCA user with the required roles.
- On Alpine Linux you will also need to override the Java installation used by the Black Duck Signature Scanner as
  described here.

## Project type-specific requirements

In general, the detectors require:

- All dependencies must be resolvable. This generally means that each dependency has been installed using the package manager's cache, virtual environment, and others.
- The package manager / build tool must be installed and in the path.

Refer to the applicable package manager sections for information on specific detectors.

Important: Review requirements for Docker Inspector and NuGet Inspector.

## Risk report requirements

The risk report requires that the following fonts are installed:

- Helvetica
- Helvetica bold

## Supported Detect versions and Service duration

For information about support and service durations for Detect versions, consult the [Support and Service Schedule](https://docs.blackduck.com/r/blackduck/black-duck-compatibility-reference/product-maintenance-support-and-service-schedule.html).
