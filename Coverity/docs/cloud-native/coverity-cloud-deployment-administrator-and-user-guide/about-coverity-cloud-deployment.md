---
title: "About Coverity cloud deployment"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/about-coverity-cloud-deployment.html"
content_id: "95_zbXhg4U9e6xqCTYOSiw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:40:15.077078+00:00"
---

# About Coverity cloud deployment

Coverity uses a client/server architecture.

- With Coverity cloud deployment, you deploy the Coverity Connect server on a
  Kubernetes cluster in the cloud. The Connect server uses an external PostgreSQL
  database to save scan results.
- The analysis client software which you use to perform and manage analyses can be
  either:

  - A full-featured analysis client (full Coverity Analysis client), which is
    installed on the client system (not in the cloud). This client both captures
    and analyzes code. Analysis is performed locally.
  - A Thin Client which captures code, then sends the code for analysis to the
    Scan Service. Scan Service is a full-featured instance of Coverity Analysis
    that you install in the cloud, within the same Kubernetes cluster as
    Connect. Scan Service launches ephemeral analysis job containers that
    perform the analyses. Scan Service stores analysis data in the PostgreSQL
    database.

  The Thin Client, being much smaller than the full client, fits easily into CI/CD
  pipelines. It can also help with scalability by moving compute-intensive
  analysis to a central scalable set of analysis service containers.

For supported configurations and versions, refer to .

For information on installing client software on a client system, refer to Installing client software.

You can configure the analysis to be performed either locally or in the cloud by creating
and editing a configuration file and/or using CLI command options to define where the
analysis occurs. For information on editing the configuration file, performing a scan,
and reviewing scan status, refer to "Performing an
analysis in a Coverity Cloud deployment" in the Coverity Analysis 2026.6.0 User and Administrator Guide.

To review and manage analyses, you can use either the Coverity API or the Coverity
Connect UI. For further information, refer to:

- Coverity Platform 2026.6.0 User and Administrator Guide
- "Coverity Connect commands" in the Coverity 2026.6.0 Command Reference
