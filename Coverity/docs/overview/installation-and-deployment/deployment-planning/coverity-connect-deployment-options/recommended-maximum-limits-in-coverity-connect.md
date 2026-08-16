---
title: "Recommended maximum limits in Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/recommended-maximum-limits-in-coverity-connect.html"
content_id: "Y19q1FJ6yhyjlvm1jKw9VA"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:43.725691+00:00"
---

# Recommended maximum limits in Coverity Connect

Coverity recommends the following boundary limits to ensure that Coverity Connect runs
properly and does not experience performance degradation. It is important to estimate
for these limits, the results may affect the way you deploy Coverity Connect and the
hardware you choose for the deployment. To estimate the limits in your organization, see
the Deployment checklist.

See the Coverity glossary for basic definitions of the items described below.

You should not exceed any of the following:

Table 1. Coverity Connect maximum settings

| System item | Maximum number |
| --- | --- |
| Streams | 1000 |
| Projects | 1000 |
| Triage stores | 1000 - This number should be much smaller than the number of streams (1 is ideal). |
| Users | 20,000 |
| User Groups | 100 |
| Component maps | 100 |
| Components per component map | 100 |
| Defects per source file | 100 |
| Number of lines per source file | 10,000 |
| Database size | 600 GB |
| Custom RBAC roles | 20 |

When working with the desktop
deployment model, the following deployment memory requirements should support
only up to the listed number of users:

- 8GB (medium installer settings) - 100 users
- 16GB - 500 users
- 32GB - 1000 users

This guidance assumes that each Desktop Analysis client performs 20 operations per
day and that there are periodic commits against the Coverity Connect server which
consist of a full analysis of the code base. The same stream is compared (using the
latest snapshot) against each individual `cov-run-desktop` operation.
