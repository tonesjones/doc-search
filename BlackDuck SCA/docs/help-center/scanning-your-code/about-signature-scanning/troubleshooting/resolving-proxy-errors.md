---
title: "Resolving proxy errors"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/resolving-proxy-errors.html"
content_id: "DS2T5OMG94UeAuniRV2ERg"
version: "2026.7"
section: "Welcome to Black Duck SCA"
scraped_at: "2026-10-04T23:32:11.026598+00:00"
content_hash: "19c3975a37c19d5a71fafc64ade468caf197960ae7ed8a44b94817df7c0d3167"
---

# Resolving proxy errors

HUB-14364Black Duck version 4.5.0 introduced a larger HTTP header size. The larger header size may cause problems with the load balancer. If this occurs, the larger header size may cause authentication errors in Black Duck environments running a proxy server. To prevent possible authentication errors and to support HTTP responses from Black Duck, Black Duck Software recommends increasing the allowed maximum HTTP header size in Black Duck versions 4.5.0 and higher to 8192.
