---
title: "Fixed Issues in 2022.4.1"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2022.4.1.html"
content_id: "zbnzZCuTm68GY_14DRHmYw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:38.279446+00:00"
---

# Fixed Issues in 2022.4.1

The following customer-reported issues were fixed in this release:

- (HUB-32395, HUB-33033). Fixed an issue where the modified declared license to
  matched component is sometimes not displayed on SPDX reports.
- (HUB-29532). Fixed an issue where Linux distro package matching was broken
  when the rootfs pathin an distro image was not starting at the root
  directory but at a subdirectory.
- (HUB-33947). Fixed an issue where the Security Risk was not updated when
  updating the Remediation Status from 'Affected Projects' page.
- (HUB-33551). Fixed an issue when uploading a bdio file with code location
  name as null, the request would fail with the status code 400 and throwing
  exception in background.
- (HUB-34065). Fixed SPDX 2.2 report format that was causing the following error
  in the SPDX validation tools:

  ```
  The following warning(s) were raised: [object instance has properties which are not allowed by the schema: ["packageSupplier"] for {"pointer":"/packages/0"}
  ```
- (HUB-33616). Fixed an issue where the scan client would in some cases (when
  there are duplicated archive entries inside scanned archive), generate a
  BDIO with incorrect ids, which in turn could produce an error when the bdio
  file is stored to the database.
- (HUB-33915, HUB-33865). Fixed an issue where the scan upload API submitted
  the entire scan data as one message into RabbitMQ without chunking, causing
  a message size error.
- (HUB-24664). Fixed an issue where the registration container logs were
  showing attempted communication over HTTP.
- (HUB-33579). Fixed an issue where the
  `--matchConfidenceThreshold` parameter was not
  functioning when used with the traditional scan.cli.
- (HUB-33311). Fixed an issue where the signature scanner could fail with the
  error code 74. A retry function was introduced to mitigate this error.
