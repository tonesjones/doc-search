---
title: "Volume Naming"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/volume-naming.html"
content_id: "tEiU4ekR6juC6JrOYK4u0g"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:06.868052+00:00"
content_hash: "ad3d7f5e9b1110d74d50c18d1c0c880e3103288142ccd61060c5b4c1554084c1"
---

# Volume Naming

When creating named volumes, Docker Compose will prepend the project name, which is the
current directory name by default, to the volume name. In other words, if you have a Docker
Compose install under the folder `srm-docker` and another under
`srm-docker-2`, their volume names will be distinct and contain different
data. Without specifying the `-p` option, the following two named volumes would
exist:

- `srm-docker_codedx-appdata-volume`
- `srm-docker-2_codedx-appdata-volume`

Named volumes are created when doing `docker-compose up`, so if you want to
override the default naming, you need to specify a project name the first time you execute the
following command:

```
docker-compose -p srm -f ./docker-compose.yml up
```
