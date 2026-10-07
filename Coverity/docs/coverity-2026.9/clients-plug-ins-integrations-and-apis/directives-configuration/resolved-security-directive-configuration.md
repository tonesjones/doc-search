---
title: "Resolved security directive configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/resolved-security-directive-configuration.html"
content_id: "zp0OMfBqO1qqcaFlB6LjnQ"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:04.399975+00:00"
---

# Resolved security directive configuration

| Key | Type | Description |
| --- | --- | --- |
| `type` | string | If specified, this must be the string "Coverity analysis configuration". |
| `format_version` | Integer | The version of the directives format. Default: `12` |
| `language` | string | **Required**: The language or language family to which the directives apply. |
| `directives` | array of entries | **Required**: Security directives that conform to the directives schema. See Security Directives Reference for more information. Note: If you are using a YAML file to define configuration, you will need to translate the JSON-based directives to YAML. |
