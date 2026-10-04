---
title: "Directives configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/directives-configuration.html"
content_id: "STLChNr~_W_nOoORctQcdA"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:04.359008+00:00"
---

# Directives configuration

Use these values to define the security directives configuration to use during
analysis.

| Key | Type | Description |
| --- | --- | --- |
| `file` | string | Name of a file that contains security directives to use during the analysis. This key is mutually exclusive with the `config` key. |
| `config` | Resolved security directive configuration | A security directives configuration to use during the analysis. This key is mutually exclusive with the `file` key and is specified when the user wants to save the security directives configuration inline in the file. |
