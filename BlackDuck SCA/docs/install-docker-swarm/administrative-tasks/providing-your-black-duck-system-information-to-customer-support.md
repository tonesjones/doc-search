---
title: "Providing your Black Duck system information to Customer Support"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/providing-your-black-duck-system-information-to-customer-support.html"
content_id: "wM_ZgqQXdFnKdqU27tjc2w"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:25.075902+00:00"
content_hash: "b5a120b9f1ce7f4a7ba36c73effd0ae5f5c44d2bf7588a847e24a929480b8eda"
---

# Providing your Black Duck system information to Customer Support

Hub-10824Customer Support may ask you to provide them with information regarding your Black Duck installation, such as system statistics and environmental or network information. To make it easier for you to quickly obtain this information, Black Duck provides a script, `system_check.sh`, which you can use to collect this information. The script outputs this information to a file, `system_check.txt`, located in your working directory, which you can then send to Customer Support.

The `system_check.sh` script is located in the `docker-swarm/bin` directory:

```
./bin/system_check.sh
```

Note that to run this script, you may need to be a user in the docker group, a root user, or have `sudo` access.
