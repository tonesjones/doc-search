---
title: "Configuring hierarchical subproject license conflicts"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/configuring-hierarchical-subproject-license-conflicts.html"
content_id: "DD6IvD4gg6UQyXUPrxWYNA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.628610+00:00"
content_hash: "4955ee2e85b740490bfaf59369a56ed9dfec78e966d88cd2cae97c84eaf119f0"
---

# Configuring hierarchical subproject license conflicts

By default, hierarchical subproject license conflicts are enabled in your environment. You can disable hierarchical subproject license conflicts by setting the following parameter:

```
USE_HIERARCHICAL_LICENSE_CONFLICTS=FALSE
```

Subproject depth is set to 5 levels by default, but can be configured with the following parameter:

```
HIERARCHICAL_LICENSE_CONFLICT_DEPTH_LIMIT=<value desired>
```
