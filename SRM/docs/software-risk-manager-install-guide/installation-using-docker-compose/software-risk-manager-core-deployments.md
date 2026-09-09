---
title: "Software Risk Manager Core Deployments"
source_url: "https://docs.blackduck.com/r/srm/latest/software-risk-manager-documentation/software-risk-manager-core-deployments.html"
content_id: "ceJXwaYbN5DK9YTYuMFWow"
version: "latest"
section: "Software Risk Manager Install Guide"
scraped_at: "2026-09-08T20:05:01.004367+00:00"
content_hash: "63bf099805fbc2f5c4e3f51171a1fa858bc961807f28b95c5cc4e107246cb99b"
---

# Software Risk Manager Core Deployments

The footprint of your Software Risk Manager Docker-Compose deployment depends on whether or
not you plan to use an external database.

The Software Risk Manager web application requires a MariaDB (version 10.6.x) or a MySQL
(version 8.0.x) database instance. You can provide a database instance or use what's included
in the default Compose file. An external database can be a standalone instance or one managed
for you by a cloud provider such as AWS or Azure.

A deployment using an external database consists of one Software Risk Manager Docker
container for the web application that depends on a Docker volume.

Figure 1. Core Deployment with an External Database
[image: image]

A deployment without an external database includes an additional Docker container for the
Software Risk Manager Web database instance. The MariaDB database instance stores data using a
Docker volume.

Figure 2. Core Deployment without an External Database
[image: image]
