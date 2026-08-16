---
title: "Adding and configuring a reverse proxy server"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/adding-and-configuring-a-reverse-proxy-server.html"
content_id: "WDvnokD_DJsQdWwPPF~Dmg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:53.699906+00:00"
---

# Adding and configuring a reverse proxy server

Note: If Coverity Connect is deployed in the cloud, this section does not apply.

This section describes how to add and configure a reverse proxy (RP) server in front of the
Coverity Connect server. This is a prerequisite for enabling Reverse Proxy
Authentication (RPA) in Coverity Connect.

The RP server configuration described in this section can handle requests from, and
responses to, any HTTP or HTTPS client. Examples include:

- browsers
- `cov-manage-im`
- `cov-run-desktop`
- `cov-commit-defects`

As shown in the diagram below, requests from these clients are addressed to the HTTPS
port on the RP server.

  
 [image: image]
