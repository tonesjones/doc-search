---
title: "Detect Air Gap mode"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/detect-air-gap-mode.html"
content_id: "~senNQqZziBX21Ydk5Hh_A"
version: "11.5.1"
section: "Downloading and Installing Detect"
scraped_at: "2026-08-08T23:44:03.996835+00:00"
---

# Detect Air Gap mode

To run Black Duck® Detect on an air-gapped computer or network, you must first download and install Detect and dependencies that Detect normally downloads as it runs. These include inspectors for Docker, NuGet and other files. These files are packaged together in an air gap archive that will be extracted on the target system.

## Downloading or creating an air gap archive

Air gap archives are available for download from the location specified in download locations.
These air gap archives contain the versions of the dependencies that were current at the time of the Detect release.

As an alternative, you can create an air gap archive yourself.
An air gap archive that you create will contain the versions of the dependencies that are current at the time you create the air gap archive
(the same versions Detect would download if run at that time).

To create an air gap archive, run Detect with the
-z or --zip command line option.
Optionally you can follow --zip with a space and an argument (for example: --zip FULL) to customize the air gap zip.

Possible values:

- FULL (produce a full air gap zip; the default)
- NO_DOCKER (do not include the Docker Inspector)

## Running in air gap mode

For information refer to Running in air gap mode.
