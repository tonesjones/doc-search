---
title: "Web app security configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/web-app-security-configuration.html"
content_id: "GOG~e~AfZNLMrUjo5R~5mQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:16.514533+00:00"
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
