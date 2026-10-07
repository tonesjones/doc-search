---
title: "Connect Web application high availability"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/connect-web-application-high-availability.html"
content_id: "sPgHBDXi5CBUPoj74b7SBA"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:18.700170+00:00"
---

# Connect Web application high availability

The 2024.6.0 release supports Connect web application high availability (HA).

High Availability uses multiple instances, or replicas, of an application to handle
larger loads and provide higher availability. Connect web application HA shares request
loads across multiple horizontally-scaled pods. Having two or more replicas for an
application provides Kubernetes high availability. Each instance is complete and
possesses its own resources.
