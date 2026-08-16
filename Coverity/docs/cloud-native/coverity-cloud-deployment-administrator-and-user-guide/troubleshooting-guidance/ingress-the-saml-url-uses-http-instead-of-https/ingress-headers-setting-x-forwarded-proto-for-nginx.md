---
title: "Ingress headers: setting X-Forwarded-proto for NGINX"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/ingress-headers-setting-x-forwarded-proto-for-nginx.html"
content_id: "0qDKxrUwYmylklbwIGpGiA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:45.423072+00:00"
---

# Ingress headers: setting X-Forwarded-proto for NGINX

This section describes how to resolve an issue where the SAML Assertion Consumer Service
(ACS) URL uses http instead of https within a Coverity cloud cluster. This issue affects
communication between the IdP and the SP. All communications must use https, not
http.

For an NGINX ingress controller, configure the following header:

```
proxy_set_header X-Forwarded-Proto $scheme
```

where `$scheme` is the request scheme, which is either "http" or
"https".

For example:

```
proxy_set_header X-Forwarded-Proto https
```

If the above method does not help, add `scheme="https"` to the
`server.xml` file:

```
<cc installed>/server/base/conf/server.xml
```

For example:

```
<Connector port="8080" protocol="HTTP/1.1" URIEncoding="UTF-8" /
  connectionTimeout="20000"  /
  compression="10240"  /
  compressableMimeType="text/html,text/xml,text/plain,application/json"  /
  redirectPort="8443" scheme="https" server=$serverName />
```
