---
title: "Upgrading Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-coverity-connect.html"
content_id: "YbbVJVCZ6A3tM~ZCIEnnSQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:52:27.217976+00:00"
---

# Upgrading Coverity Connect

This section describes how to upgrade a Coverity Connect deployment. (Note that a Coverity
Connect deployment contains downloadable packages for other components, including
Coverity Reports and the Coverity Desktop plugins.)

Important: Depending on the size of the Coverity Connect database and the number of
versions in the Coverity Connect upgrade, the upgrade process might take several hours
to complete. Also, before performing an upgrade on a Coverity Connect instance, consult
Important upgrade considerations for a list of important product
changes that may affect your Coverity Connect workflow.

Important: If you are upgrading a Coverity cloud deployment, refer to
"Upgrading a Coverity cloud deployment"
in the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide. This document provides
important information for administrators who are deploying or upgrading Coverity in a
Kubernetes container environment.

This section is applicable to both Coverity Connect standalone deployments (one Coverity
Connect instance) and Coverity Connect clustered deployments (more than one Coverity
Connect instance working together). For more information about deployments, see Coverity Connect deployment options.

Upgrading a Coverity Connect clustered deployment requires upgrading one Coverity Connect
instance at a time. The procedures for deciding which instance to upgrade first and how
to upgrade each instance vary depending on whether the instance uses an embedded
database or an external database. (An embedded database is installed by default with
Coverity Connect, while an external database is created and maintained separately.)

To upgrade each Coverity Connect instance in your deployment, consult the appropriate
section:

- Upgrading instances that use an embedded database
- Upgrading instances that use an external database
