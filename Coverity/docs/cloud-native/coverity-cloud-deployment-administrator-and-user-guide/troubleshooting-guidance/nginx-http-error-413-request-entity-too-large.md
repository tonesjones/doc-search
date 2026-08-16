---
title: "NGINX HTTP error 413: Request Entity Too Large"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/nginx-http-error-413-request-entity-too-large.html"
content_id: "gga4BFyxeXR0f3gDOGwQKw"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:45:46.730727+00:00"
---

# NGINX HTTP error 413: Request Entity Too Large

If you are using NGINX for ingress and an error 413 "Request Entity Too Large" is
returned, this indicates an issue where a file being uploaded exceeds the set filesize
limit. For information on an Error 504, see also:

- [413 Payload Too Large](https://http.dev/413)

To solve this issue, increase the maximum file upload size as described in the section,
Set NGINX proxy-body-size for Coverity toolkit tar file upload to Connect.
