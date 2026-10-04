---
title: "Web app security configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/web-app-security-configuration.html"
content_id: "GOG~e~AfZNLMrUjo5R~5mQ"
version: "2026.9"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-10-04T23:35:04.609288+00:00"
---

# Web app security configuration

**Location in the configuration file (YAML format):**

```
analyze:
    checkers:
        webapp-security:
```

| Key |  |  |
| --- | --- | --- |
| `aggressiveness-level` | string | Sets the web application checker's aggressiveness level to one of `low`, `medium`, or `high`. Default: `low` |
| `enabled` | Boolean | Enables the checkers used for Web application security analysis. Default: `false` |
