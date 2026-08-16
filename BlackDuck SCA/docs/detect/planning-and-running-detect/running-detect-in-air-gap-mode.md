---
title: "Running Detect in air gap mode"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/running-detect-in-air-gap-mode.html"
content_id: "fiejezghcCGSNUvG6~Qs7Q"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:39.024236+00:00"
---

# Running Detect in air gap mode

Running Detect in air gap mode requires adding scanners, inspectors, and associated libraries to a jar file such that they can be executed without network access.

Note: Air gap mode is not the same as running in Offline mode. Air gap mode allows for scanning when operating in an air gapped environment and relies on a jar file that contains the required scanning libraries. Offline mode is used when you do not wish to download scanners or upload results files directly to Black Duck SCA, but still supports the use of a local signature scanner instance.

## Adding the Black Duck Signature Scanner to your air gap archive

To create an air gap archive that includes the Black Duck Signature Scanner, follow these steps:

1. Unzip the Detect air gap archive to create the Detect air gap directory.
2. Download the appropriate Black Duck Signature Scanner zip file from your Black Duck SCA instance (System > Tools > Legacy Downloads > Signature Scanner), and unzip it. This will create a directory with a name like scan.cli-x.y.z.
3. Move that scan.cli-x.y.z directory to the top level of the Detect air gap directory.
4. Zip the enhanced Detect air gap directory to create your enhanced air gap archive.

When you later run Detect from the directory created by unzipping your enhanced air gap archive, set property detect.blackduck.signature.scanner.local.path to the path to the scan.cli-x.y.z directory in your enhanced air gap archive directory.

## Preparing and running in air gap mode

To prepare to run Detect in air gap mode, unzip the air gap archive to create the air gap directory.
Do not make changes to files in the air gap directory.
Invoke the Detect .jar file from its original unzipped location at the top level of the air gap directory.
For more information on invoking the .jar file, refer to Running the Detect .jar.
