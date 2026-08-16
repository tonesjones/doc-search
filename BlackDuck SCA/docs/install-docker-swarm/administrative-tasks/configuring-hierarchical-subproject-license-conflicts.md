---
title: "Configuring hierarchical subproject license conflicts"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-hierarchical-subproject-license-conflicts.html"
content_id: "PVb6Hc1TjIG9iqZ4ho7bcA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:34:12.177598+00:00"
---

# Configuring hierarchical subproject license conflicts

By default, hierarchical subproject license conflicts are enabled in your environment.
You can disable hierarchical subproject license conflicts by setting the following
parameter:

```
USE_HIERARCHICAL_LICENSE_CONFLICTS=FALSE
```

Subproject depth is set to 5 levels by default, but can be configured with the following
parameter:

```
HIERARCHICAL_LICENSE_CONFLICT_DEPTH_LIMIT=<value desired>
```
