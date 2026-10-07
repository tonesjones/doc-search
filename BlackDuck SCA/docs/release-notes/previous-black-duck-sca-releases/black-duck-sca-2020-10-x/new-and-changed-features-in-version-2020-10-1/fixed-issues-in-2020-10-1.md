---
title: "Fixed Issues in 2020.10.1"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2020.10.1.html"
content_id: "tAvhaF5mRO_pYG7xMaW2Mw"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:36.275554+00:00"
content_hash: "2920d42aa799261450fcd55b57cd1573c65cb390569546381e1933ced41aa149"
---

# Fixed Issues in 2020.10.1

The following customer-reported issues were fixed in this release:

- (Hub-25489). Fixed an issue where the filters selected in the **Source** tab were reset when a different folder was selected.
- (Hub-25515). Fixed an issue when the host instance was running TLS 1.3 where the Signature Scanner failed when uploading and displayed the following error message: "ERROR: Unable to secure the connection to the host".
- (Hub-25791). Fixed an issue where significant increases in scan time occurred after upgrading from version 2020.4.2 to version 2020.6.1/2020.6.2.
- (Hub-26027). Fixed an issue where Black Duck displayed the following error message: "ERROR: The application has encountered an unknown error. (Bad Request) error.{core.rest.common_error" when attempting to upload a Black Duck Detect scan.
- (Hub-26085). Fixed an issue where binary scans added a second empty scan.
- (Hub-26090). Fixed an issue where a scan of coreutils-8.22-24 failed when copyright search was enabled. DUPLICATE OF 26027.
