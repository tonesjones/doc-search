---
title: "Disabling project dashboards in the Coverity Connect interface"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/disabling-project-dashboards-in-the-coverity-connect-interface.html"
content_id: "jWZz86c~gy1d69N3xUbyWQ"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:06.695209+00:00"
---

# Disabling project dashboards in the Coverity Connect interface

By default, Coverity Connect displays graphs and charts that provide an overview of the
state of the issues in the currently selected project. Coverity Connect provides the
following Dashboard views:

- The Quality charts graph data on issues found with quality-related
  checkers.
- The Security charts graph data that is related to security-related
  checkers.

Coverity Connect allows you to remove the display of the dashboards from the Coverity
Connect interface. To remove the dashboards, add the following variables and definitions
to the <install_dir>/config/cim.properties file:

**For Quality:**

```
display.quality=false
```

**For Security:**

```
display.security=false
```

After you edit the properties file, restart Coverity Connect.
