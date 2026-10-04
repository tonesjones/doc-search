---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "qP59hOW4copJyj_yl7yXfg"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:32.323442+00:00"
content_hash: "e1c81eff207eba8132ca3ebf243964d88a90a715aed28b8a4ed16d92e66666c9"
---

# Announcements

## Node constraints for storage and registration

With Black Duck 2023.4.1, users with multi-node swarm deployments are reminded to check the node constraints for storage and registration. This change will help alleviate the container shifting nodes and spreading data across multiple systems.

```
#deploy: # placement: # constraints: # - node.labels.type == db
```
