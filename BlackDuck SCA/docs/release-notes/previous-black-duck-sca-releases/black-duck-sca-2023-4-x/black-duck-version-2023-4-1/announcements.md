---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "_gfHlcfF~uCFke_6JaWudA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:55.340105+00:00"
---

# Announcements

## Node constraints for storage and registration

With Black Duck 2023.4.1, users with multi-node swarm deployments are reminded to
check the node constraints for storage and registration. This change will help
alleviate the container shifting nodes and spreading data across multiple
systems.

```
    #deploy:
    #  placement:
    #    constraints:
    #    - node.labels.type == db
```
