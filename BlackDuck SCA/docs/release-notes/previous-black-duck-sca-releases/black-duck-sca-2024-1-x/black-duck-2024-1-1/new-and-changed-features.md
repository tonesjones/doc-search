---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "4lSam4_1nr7ufvDSlPXTHg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:20.252273+00:00"
---

# New and changed features

## New Project Version SBOM field configuration

You can now configure project version SBOM fields to define the BOM component SBOM
fields when a component is used as a sub-project for a project version so that the
appropriate level of detail is provided in the SBOM without having to define it for
every project the sub-project is used in.

## Updated search functionality

The algorithm used for searching in Black Duck has been enhanced and will broaden the
scope of the search to make it easier for you to find the information you need by
enabling the retrieval of all records containing strings or partial matches. It will
provide results similar to those obtained using a Solr search, allowing you to find
relevant records even if you do not know the complete string.

## Container versions

- blackducksoftware/blackduck-postgres:14-1.21
- blackducksoftware/blackduck-postgres-upgrader:14-1.4
- blackducksoftware/blackduck-postgres-waiter:1.0.11
- blackducksoftware/blackduck-cfssl:1.0.25
- blackducksoftware/blackduck-nginx:2.0.66
- blackducksoftware/blackduck-logstash:1.0.35
- blackducksoftware/bdba-worker:2023.12.3
- blackducksoftware/rabbitmq:1.2.36
- blackducksoftware/blackduck-webui:2024.1.1
- blackducksoftware/blackduck-authentication:2024.1.1
- blackducksoftware/blackduck-bomengine:2024.1.1
- blackducksoftware/blackduck-documentation:2024.1.1
- blackducksoftware/blackduck-integration:2024.1.1
- blackducksoftware/blackduck-jobrunner:2024.1.1
- blackducksoftware/blackduck-matchengine:2024.1.1
- blackducksoftware/blackduck-redis:2024.1.1
- blackducksoftware/blackduck-registration:2024.1.1
- blackducksoftware/blackduck-scan:2024.1.1
- blackducksoftware/blackduck-storage:2024.1.1
- blackducksoftware/blackduck-webapp:2024.1.1
