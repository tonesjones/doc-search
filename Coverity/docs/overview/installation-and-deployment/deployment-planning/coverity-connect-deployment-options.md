---
title: "Coverity Connect deployment options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-connect-deployment-options.html"
content_id: "Hga0nNXOKbWM~cBXUgdPOg"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:41.484443+00:00"
---

# Coverity Connect deployment options

Coverity Connect receives the commit and issue data that was discovered by the Coverity
analysis tools. The discovered issues can then be assigned to your organization's
developers. The developers, in turn, can view the issues in the source code, classify
the issues, and so forth. There are many more powerful features in Coverity Connect;
that you can implement to help you locate and fix issues, as well as tracking and
charting your organization's projects. For more information about Coverity Connect
features, see the Coverity Platform 2026.6.0 User and Administrator Guide.

Note:

- If Coverity Connect is deployed in the cloud, refer to the Coverity 2026.6.0 Cloud Deployment Administrator and User Guide for information on Coverity Connect
  deployment options.
- Coverity Analysis supports SNI (Server Name Indication) for all Coverity client
  tools. This means that you can place Coverity Connect behind a reverse proxy
  that serves multiple domains.

[image: image]

The are two primary methods in which to deploy Coverity Connect:

- As a stand-alone deployment.
- As a clustered environment.

  Note that in the diagram above, the clustered
  environment is represented by the coordinator and subscriber instances. At
  least one (stand alone or otherwise) Coverity Connect instance is
  required.
