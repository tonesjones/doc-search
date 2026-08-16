---
title: "Environment files and variables"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/environment-files-and-variables.html"
content_id: "wVapguRovmlkZV8ECn9VXA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:39.725665+00:00"
---

# Environment files and variables

## Using environment files

Note that some configurations use environment files; for example, configuring web
server, proxy, or external PostgreSQL settings. The environment files to configure
these settings are located in the `docker-swarm` directory.

To configure settings that use environment files:

- To set configuration settings *before* installing Black Duck, edit the file as described below and save your
  changes.
- To modify existing settings *after* installing Black Duck, modify the settings and then redeploy the
  services in the stack.

## Environment variables and scanning binaries

When you scan binaries with Black Duck Binary Analysis (BDBA), you must
ensure that the `HUB_SCAN_ALLOW_PARTIAL= 'true'` parameter is
added to the Job Runner container environment variables to surface components
without versions in the BOM. The BDBA scanner, unlike Black Duck scanning, surfaces components without a version when version string
information is not discernible in the binary. On the BOM, the component will
have a question mark ( [image: image] ) beside
the name to signal to the user that this component needs to be reviewed before
security vulnerabilities are assigned to the component as Black Duck requires a version to map security vulnerabilities
to a component.
