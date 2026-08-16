---
title: "Fixed Issues in 2021.6.1"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2021.6.1.html"
content_id: "BjKXmGS8KnBXtvq8VZbzLw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:10.213279+00:00"
---

# Fixed Issues in 2021.6.1

The following customer-reported issues were fixed in this release:

- (HUB-29202). Fixed an issue where the binary scan container(bdba-worker) of
  2021.4.0 did not work on docker SWARM by increasing timeout and retry
  values.
- (HUB-29405). Fixed an issue where matches were being dropped, due to the
  identification of a core_i7 architecture.
- (HUB-30134). Fixed an issue where the BOM engine silently fails to start due
  to RabbitMQ connectivity issue.
- (HUB-30170). Fixed an issue where Redis fails to start due to incorrect
  configuration in the docker-entrypoint when utilizing dual stack
  Kubernetes.
- (HUB-30202). Fixed an issue where the vulnerability details page does not
  correctly change the display of the score metrics when the user clicks from
  BDSA scoring to NVD scoring and vice versa.
