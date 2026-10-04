---
title: "Accessing the API documentation through a proxy server"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/accessing-the-api-documentation-through-a-proxy-server.html"
content_id: "xmEJehAlKPfbEYa9~3Uiug"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-10-04T23:32:24.341673+00:00"
content_hash: "e2d4c0f359c837d20233ec0845e99c078722de2ce4728d5a97aafd97040f5592"
---

# Accessing the API documentation through a proxy server

If you are using a reverse proxy and that reverse proxy has Black Duck under a subpath, configure the BLACKDUCK_SWAGGER_PROXY_PREFIX property so that you can access the API documentation. The value of BLACKDUCK_SWAGGER_PROXY_PREFIX is the Black Duck path. For example, if you have Black Duck being accessed under 'https://customer.companyname.com/hub' then the value of BLACKDUCK_SWAGGER_PROXY_PREFIX would be 'hub'.

To configure this property, edit the `blackduck-config.env` file located in the `docker-swarm` directory.
