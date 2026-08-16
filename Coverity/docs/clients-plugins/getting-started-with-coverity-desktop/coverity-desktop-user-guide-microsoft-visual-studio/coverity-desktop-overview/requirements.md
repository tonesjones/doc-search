---
title: "Requirements"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/requirements.html"
content_id: "Mvmfs_~3xymvRpXfHqa~Ig"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:49:03.401342+00:00"
---

# Requirements

Coverity Desktop for Microsoft Visual Studio has the following
requirements:

- Coverity Connect
  2026.6.0
- Coverity Analysis
  2026.6.0 (required for local analysis. Typically installed at
  the same time as the plug-in)
- Visual Studio (refer to the "Coverity Desktop" chapter of the
  Coverity 2026.6.0 Installation and Upgrade Guide for supported version numbers)
- Memory requirements: the minimum is 3 GB of RAM and more if you use parallel analysis. Refer
  to "Minimum
  requirements" in the Coverity 2026.6.0 Installation and Upgrade Guide for more
  information.

Before getting started with Coverity Desktop, make sure that you also
have the following Coverity Connect access information:

- Host name
- Port number and type (HTTP or HTTPS)
- Authentication key file, or your user name and password for creating a new
  authentication key.
- Stream name

Note: This information is dependent on your Coverity Connect
administrator configuring the server and running an initial analysis and commit. See
the Coverity Platform 2026.6.0 User and Administrator Guide for information on configuring Coverity Connect for use with Desktop Analysis.
