---
title: "Fixed Issues in 2021.2.1"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2021.2.1.html"
content_id: "ZV6W3kpJ8GwGKUL5rYIQZg"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:35.956231+00:00"
content_hash: "f744f3701df5c925f9a2f6d8f7299a8a940e61bb3813e44bbedb9e0f4ee955b6"
---

# Fixed Issues in 2021.2.1

The following customer-reported issues were fixed in this release:

- (Hub-23928). Fixed an issue where a confirmed snippet match was changed after a rescan.
- (Hub-26898). Fixed an issue whereby a scan appeared to be completed, however, Black Duck Detect timed out as it failed to get a bom_complete notification from Black Duck.
- (Hub-27179). Fixed a Java execution problem occurring on the scan and webapp containers.
- (Hub-27688). Fixed an issue whereby the API call for matched files returned no information for transitive and direct dependency matches.
- (Hub-28410). Fixed an issue where the RabbitMQ container could not be started on Kubernetes which was resolved by introducing a persistent volume.
- (Hub-28208, 28386). Fixed an issue whereby the incorrect code base size was displayed on the Product Registration page.
- (Hub-28278). Fixed an issue where a missing persistent volume for RabbitMQ container caused excessive logging in the BOM Engine and scan failures.
- (Hub-28292). Fixed an issue with scaling the BOM Engine container.
