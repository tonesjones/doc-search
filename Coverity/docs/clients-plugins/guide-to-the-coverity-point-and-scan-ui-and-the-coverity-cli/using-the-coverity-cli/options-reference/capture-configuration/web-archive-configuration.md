---
title: "Web archive configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/web-archive-configuration.html"
content_id: "sf0N~02lXhqAqsy8sSscdA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:05.914429+00:00"
---

# Web archive configuration

The following configuration applies to Java capture only.

| Key | Type | Description |
| --- | --- | --- |
| `path` | string | Specifies a path to the Web application archive file or a path to the directory that contains the expanded Web application files. |
| `validate-webapp` | Boolean | Specifies whether the Web application should be checked during capture to see if it is valid. The validation check verifies that a `/WEB-INF/web.xml` file exists, and that >20% of the classes for the Web application were captured.  Default:`false` |
