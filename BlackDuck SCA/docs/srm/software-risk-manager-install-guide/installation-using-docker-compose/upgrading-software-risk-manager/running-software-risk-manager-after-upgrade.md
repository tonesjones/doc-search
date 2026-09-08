---
title: "Running Software Risk Manager After Upgrade"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/running-software-risk-manager-after-upgrade.html"
content_id: "uUoj6fF4QkEhTVHRkELieQ"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:12.947259+00:00"
content_hash: "99a99c8e6e6bf41f8cd93a02895029ce23b20e192acd657c2f0fcab5e2cc0806"
---

# Running Software Risk Manager After Upgrade

After successfully upgrading, you can run the following command to see the effects of the
upgrade:

```
docker-compose -f /path/to/your-docker-compose-file up
```

Pulling the latest files via Git ensures that you update your original files with the latest
versions. Running your Docker Compose commands with the upgraded files from the same directory
avoids unexpected behavior due to how docker-compose sets project names.
