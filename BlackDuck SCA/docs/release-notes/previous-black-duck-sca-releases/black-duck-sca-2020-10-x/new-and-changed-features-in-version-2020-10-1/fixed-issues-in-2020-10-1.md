---
title: "Fixed Issues in 2020.10.1"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2020.10.1.html"
content_id: "_rNTKABux7cpfvbOQ_iJww"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:25.120435+00:00"
---

# Fixed Issues in 2020.10.1

The following customer-reported issues were fixed in this release:

- (Hub-25489). Fixed an issue where the filters selected in the
  **Source** tab were reset when a different folder was
  selected.
- (Hub-25515). Fixed an issue when the host instance was running TLS 1.3
  where the Signature Scanner failed when uploading and displayed the
  following error message: "ERROR: Unable to secure the connection to the
  host".
- (Hub-25791). Fixed an issue where significant increases in scan time
  occurred after upgrading from version 2020.4.2 to version
  2020.6.1/2020.6.2.
- (Hub-26027). Fixed an issue where Black Duck displayed the following
  error message: "ERROR: The application has encountered an unknown error.
  (Bad Request) error.{core.rest.common_error" when attempting to upload a
  Black Duck Detect scan.
- (Hub-26085). Fixed an issue where binary scans added a second empty
  scan.
- (Hub-26090). Fixed an issue where a scan of coreutils-8.22-24 failed when
  copyright search was enabled. DUPLICATE OF 26027.
