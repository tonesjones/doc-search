---
title: "New and Changed Features in Version 2021.6.1"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features-in-version-2021.6.1.html"
content_id: "zCkAx2XP1anjw52K~J_Z2A"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:09.646688+00:00"
---

# New and Changed Features in Version 2021.6.1

## Black Duck Security Advisory (BDSA) Remote Code Execution Exposure

Black Duck highlights vulnerabilities that may allow Remote Code Execution (RCE) in
the 2021.6.1 release. In the Black Duck UI, if the BDSA vulnerability has a RCE tag
it will appear in the full BDSA record, the table of vulnerabilities, and in the
Security tab of a particular component.

The vulnerability APIs report the vulnerability using an array with the name
bdsaTags. If the bdsaTag array includes “RCE” then that vulnerability may allow
Remote Code Execution.

- /api/components/{componentId}/vulnerabilities
- /api/components/{componentId}/versions/{componentVersionId}/vulnerabilities
- /api/components/{componentId}/versions/{componentVersionId}/origin/{componentVersionOriginId}/vulnerabilities
- /api/projects/{projectId}/versions/{versionId}/components/{componentId}/versions/{componentVersionId}/origins/{componentVersionOriginId}/vulnerabilities

## Container versions

- blackducksoftware/blackduck-postgres:9.6-1.1
- blackducksoftware/blackduck-datadog:1.0.1
- blackducksoftware/blackduck-solr:1.0.0
- blackducksoftware/blackduck-authentication:2021.6.1
- blackducksoftware/blackduck-webapp:2021.6.1
- blackducksoftware/blackduck-scan:2021.6.1
- blackducksoftware/blackduck-jobrunner:2021.6.1
- blackducksoftware/blackduck-cfssl:1.0.2
- blackducksoftware/blackduck-logstash:1.0.10
- blackducksoftware/blackduck-registration:2021.6.1
- blackducksoftware/blackduck-nginx:2.0.3
- blackducksoftware/blackduck-documentation:2021.6.1
- blackducksoftware/blackduck-upload-cache:1.0.17
- blackducksoftware/blackduck-redis:2021.6.1
- blackducksoftware/blackduck-bomengine:2021.6.1
- blackducksoftware/blackduck-matchengine:2021.6.1
- blackducksoftware/blackduck-webui:2021.6.1
- blackducksoftware/bdba-worker:2021.06
- blackducksoftware/rabbitmq:1.2.2
