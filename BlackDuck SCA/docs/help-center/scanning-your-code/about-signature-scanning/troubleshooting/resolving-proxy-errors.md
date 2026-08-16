---
title: "Resolving proxy errors"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/resolving-proxy-errors.html"
content_id: "0FDgnGMo6IXZc2cjUCz2yA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:45.663387+00:00"
---

# Resolving proxy errors

HUB-14364Black Duck
version 4.5.0 introduced a larger HTTP header size. The larger header size may cause
problems with the load balancer. If this occurs, the larger header size may cause
authentication errors in Black Duck environments running a proxy
server. To prevent possible authentication errors and to support HTTP responses from Black Duck, Black Duck Software recommends increasing the
allowed maximum HTTP header size in Black Duck versions 4.5.0 and
higher to 8192.
