---
title: "Providing your Black Duck system information to Customer Support"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/providing-your-black-duck-system-information-to-customer-support.html"
content_id: "8ShW8Otl_sLYJ3ExTTIMJA"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:58.625812+00:00"
---

# Providing your Black Duck system information to Customer Support

Hub-10824Customer Support may ask you to
provide them with information regarding your Black Duck installation,
such as system statistics and environmental or network information. To make it easier
for you to quickly obtain this information, Black Duck provides a
script, `system_check.sh`, which you can use to collect this information.
The script outputs this information to a file, `system_check.txt`,
located in your working directory, which you can then send to Customer Support.

The `system_check.sh` script is located in the
`docker-swarm/bin` directory:

```
./bin/system_check.sh
```

Note that to run this script, you may need to be a user in the docker group, a root user,
or have `sudo` access.
