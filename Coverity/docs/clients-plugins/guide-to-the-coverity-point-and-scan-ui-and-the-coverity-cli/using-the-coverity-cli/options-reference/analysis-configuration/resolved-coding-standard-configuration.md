---
title: "Resolved coding standard configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/resolved-coding-standard-configuration.html"
content_id: "WGwi01fpESmzttzpf3q3XA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:10.673700+00:00"
---

# Resolved coding standard configuration

Use these values for the `config` key of the coding standard configuration.

| Key | Type | Description |
| --- | --- | --- |
| `version` | string | For C, C++, and Java: The version of this code compliance configuration. Default: `2.0` |
| `title` | string | **Required:** For C, C++, and Java: The name of this code compliance configuration. |
| `deviations` | list of Coding standard deviation entries | **Required:** For C, C++, and Java: A list of deviations for this standard. |
