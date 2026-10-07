---
title: "Third-party software and platform support matrix"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/third-party-software-and-platform-support-matrix.html"
content_id: "d2KtbWMSoulZuflM9WmzGw"
version: "2026.9"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-10-04T23:39:40.910980+00:00"
---

# Third-party software and platform support matrix

The following table identifies the software and cloud platform versions
supported by a Coverity
2026.9.0 cloud deployment.

Table 1. Coverity
2026.9.0 cloud deployment software and platform support matrix

| Software/Platform | Supported versions | Notes |
| --- | --- | --- |
| Kubernetes | 1.34 - 1.36 |  |
| Helm | 4.0.0 or later |  |
| NGINX | 1.30.4 |  |
| PostgreSQL | 15.x to 18.x | PostgreSQL versions supported with Coverity 2025.3.0 or newer all support PostgreSQL database read replicas and Bitnami Pgpool II. Note: There are some performance issues found with PostgreSQL 17.x. |
| Redis | 6.0 or greater |  |
| Red Hat OpenShift | 4.19 | Coverity cloud deployments have been tested on these cloud platform versions. |
| Amazon AWS | 1.34.9 |
| Google GCP | 1.35.5 |
| Microsoft Azure | 1.34.8 |
| KIND | 1.36.1 |
