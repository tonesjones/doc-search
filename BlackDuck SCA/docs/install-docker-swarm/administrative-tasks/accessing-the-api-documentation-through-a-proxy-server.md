---
title: "Accessing the API documentation through a proxy server"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/accessing-the-api-documentation-through-a-proxy-server.html"
content_id: "uUaFgiZ~hYGnYToqCN~L6A"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:41.417558+00:00"
---

# Accessing the API documentation through a proxy server

If you are using a reverse proxy and that reverse proxy has Black Duck
under a subpath, configure the BLACKDUCK_SWAGGER_PROXY_PREFIX property so that you can
access the API documentation. The value of BLACKDUCK_SWAGGER_PROXY_PREFIX is the Black Duck path. For example, if you have Black Duck
being accessed under 'https://customer.companyname.com/hub' then the value of
BLACKDUCK_SWAGGER_PROXY_PREFIX would be 'hub'.

To configure this property, edit the `blackduck-config.env` file located
in the `docker-swarm` directory.
