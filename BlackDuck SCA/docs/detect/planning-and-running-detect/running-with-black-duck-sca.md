---
title: "Running with Black Duck® SCA"
source_url: "https://docs.blackduck.com/r/detect/11.5.1/black-duck-detect/running-with-black-duck-sca.html"
content_id: "Wt7RrdRrG2TCWCawuPvqWg"
version: "11.5.1"
section: "Planning and running Detect"
scraped_at: "2026-08-08T23:44:31.978924+00:00"
---

# Running with Black Duck® SCA

Detect can be used with multiple Black Duck SCA platforms to perform Software Composition Analysis (SCA).

## Overview

When running Detect with Black Duck SCA and connection details are provided, Detect executes all eligible detection tools by default, including the following:

- The detector tool, which runs the appropriate package manager-specific detector; the Maven detector
  for Maven projects, the Gradle detector for Gradle projects, and so forth.
- The Black Duck Signature Scanner, which performs a Black Duck signature scan on the
  project directory.
- Run Black Duck Binary Analysis on given binary files.

Detect can be configured to perform additional tasks, including the following:

- Enable any of the supported snippet matching modes in the Black Duck Signature Scanner.
- Enable the Vulnerability Impact Analysis Tool on any Java project.
- Run the Black Duck Docker Inspector on a given Docker image.
- Generate a report.
- Fail on policy violation.
- Run IaC Scan on provided targets. Note: Iac Scan capabilities require Black Duck SCA 2022.7.0 or later.

Refer to Black Duck SCA Server properties, Black Duck Signature Scanner properties, and IaC Scan for details.

Tip: Available signature scanner properties can be determined by specifying `--help` when executing the signature scanner jar file from the command line.

## Offline mode

If you do not have a Black Duck SCA instance, or if your network is down, you can still run Detect in offline mode.

Note: Offline mode is not the same as air gap mode. Air gap mode requires the airgap.jar available to execute as it contains local copies of scanning libraries to support full offline execution.

In offline mode, Detect writes output files (.bdio files and, when Vulnerability Impact Analysis runs, .bdmu files) to subdirectories
within the run directory without attempting to upload them to Black Duck SCA. You can find the value of the run directory in the Detect log.
You can run Detect in offline mode using the offline mode property.

### Running in offline mode

Download the latest Detect version:
See download locations

*Choose one of the following to download.*

**Version 10.0.0 or later**`detect-X.X.X-air-gap.zip` includes scanning for Gradle, Nuget, and Docker.
`detect-X.X.X-air-gap-no-docker.zip` includes scanning for Gradle and Nuget. No Docker scanning.

**Version 8.7 to 9.10.0**`synopsys-detect-X.X.X-air-gap.zip` includes scanning for Gradle, Nuget, and Docker.
`synopsys-detect-X.X.X-air-gap-no-docker.zip` includes scanning for Gradle and Nuget. No Docker scanning.

Download the Signature Scanner from your Black Duck SCA server:
https://{blackduckserver}/download/scan.cli.zip
https://{blackduckserver}/download/scan.cli-windows.zip
https://{blackduckserver}/download/scan.cli-macosx.zip

Specify the following Detect scan properties:

- --blackduck.offline.mode=true
- --detect.scan.output.path= output of the Signature Scanner
- --detect.output.path= output directory to store files that Detect downloads or creates
- --detect.blackduck.signature.scanner.local.path= location to the signature scanner scan.cli-202x.xx.x

Note: If using air gap zip archive files for Detect scanning, see Air Gap Mode for additional information.

Detect Scan Command example:

```
java -jar  detect-x.x.x.jar --blackduck.url= --blackduck.api.token= --detect.project.name= --detect.project.version.name= --blackduck.offline.mode=true --detect.scan.output.path= --detect.output.path= --detect.blackduck.signature.scanner.local.path=
```

Upload Scan results via the Black Duck SCA UI:

The scan files to upload to Black Duck SCA are found in the output Black Duck SCA directory. There will be a scan file for the Signature Scanner and Dependency Scanner. Look at console output to check if both scanners ran. It is possible one scanner ran, but the other did not.

The following are the locations of the scan files if the following Detect properties were used:

- scan.output.path (ends in .json): {the path provided}\BlackDuckScanOutput{date and time of scan}\data
- output.path (ends in *.bdio): {the path provided}\runs{date and time of scan}\bdio

Black Duck SCA UI upload

- Go to **Scans** in the left navigation bar
- Click **+Upload** Scans
- Add scan files

## BDIO format

Detect produces dependency information for Black Duck SCA, and other products and platforms, in Black Duck SCA Input Output (BDIO) format files.
Detect supports generating BDIO version 2 documents.
