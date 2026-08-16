---
title: "Fixed Issues in 2021.8.1"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2021.8.1.html"
content_id: "swD~e~jSC7bOyssdQaFSHw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:05.128759+00:00"
---

# Fixed Issues in 2021.8.1

The following customer-reported issues were fixed in this release:

- (HUB-31029). Fixed an issue where the Project Manager Role settings was
  overriding the individual/group's Super User role.
- (HUB-30808). Fixed an issue where custom fields created under the BOM
  Component tab in Custom Fields Management were not returning when reviewing
  a component's "Additional fields" within any project's BOM.
- (HUB-30655). Fixed an issue where users without the Super User role could see
  "Project Group Management" option in the Management menu.
- (HUB-31077). Fixed an issue where upgrading Black Duck HUB from 2021.6.0 to
  2021.8.x would fail for Kubernetes deployments due to a change made to a
  property in the helm chart. Other prior versions are unaffected.
