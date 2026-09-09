---
title: "Feature availability in online and offline Detect scanning"
source_url: "https://docs.blackduck.com/r/detect/12.0.0/black-duck-detect/feature-availability-in-online-and-offline-detect-scanning.html"
content_id: "OaYesGDupP_lcfdONt1RYw"
version: "12.0.0"
section: "Planning and running Detect"
scraped_at: "2026-09-07T21:15:33.175858+00:00"
---

# Feature availability in online and offline Detect scanning

The following table summarizes the availability of Detect features when running in
online mode versus offline mode.

Table 1. Online and offline Detect feature comparison

| Feature | Included in online Detect | Included in offline Detect | Notes |
| --- | --- | --- | --- |
| BDIO file generation | Yes | Yes | If no code locations are identified, a BDIO file is not generated.  You can force BDIO file generation by using:   ``` --blackduck.offline.mode.force.bdio=true ``` |
| Rapid scan | Yes | No | Requires a connection to Black Duck SCA. |
| BDBA/Binary scanning | Yes | No | Requires uploading the binary to Black Duck SCA. |
| Snippets | Yes | No | Uses Black Duck SCA APIs and is not included in JSON or BDIO output files. |
| Package managers (post-build) | Yes | Yes | Supported only when using the local air-gap Detect package for offline scanning. |
| Impact analysis | Yes | No | Requires file uploads and is not included in JSON or BDIO output files. |
| Report generation through Detect | Yes | No | Detect does not communicate with Black Duck SCA when running offline. |
| Docker scanning by image | Yes | No | Offline mode cannot access Docker Hub or other external image repositories.  You can scan a locally available image by using:   ``` --detect.docker.image.id ```   This option requires the air-gap Detect package.  If only connectivity to Black Duck SCA is unavailable, Docker scanning can still be performed using:   ``` --detect.docker.image ``` |
| Signature scan | Yes | Yes |  |
| Stateless scanning | Yes | No | Requires network connectivity. |
| Detect policy check | Yes | No | Offline mode cannot connect to Black Duck SCA to evaluate project policies. |
| Infrastructure as Code (IaC) scanning | Yes | Yes* | *Available only in air-gap mode when Sigma is provided locally by specifying:   ``` --detect.iac.scanner.local.path ```   IaC scanning does not generate a BDIO file. |
