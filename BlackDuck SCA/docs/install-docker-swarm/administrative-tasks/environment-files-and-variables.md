---
title: "Environment files and variables"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/environment-files-and-variables.html"
content_id: "bL6WyfruhTPfixA50eIq_Q"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:24.273081+00:00"
content_hash: "c35d718aa5fee41a97e94c3c294002ab89bb9734a7def92a3cf69b071b9be73b"
---

# Environment files and variables

## Using environment files

Note that some configurations use environment files; for example, configuring web server, proxy, or external PostgreSQL settings. The environment files to configure these settings are located in the `docker-swarm` directory.

To configure settings that use environment files:

- To set configuration settings *before* installing Black Duck, edit the file as described below and save your changes.
- To modify existing settings *after* installing Black Duck, modify the settings and then redeploy the services in the stack.

## Environment variables and scanning binaries

When you scan binaries with Black Duck Binary Analysis (BDBA), you must ensure that the `HUB_SCAN_ALLOW_PARTIAL= 'true'` parameter is added to the Job Runner container environment variables to surface components without versions in the BOM. The BDBA scanner, unlike Black Duck scanning, surfaces components without a version when version string information is not discernible in the binary. On the BOM, the component will have a question mark ( [image: image] ) beside the name to signal to the user that this component needs to be reviewed before security vulnerabilities are assigned to the component as Black Duck requires a version to map security vulnerabilities to a component.
