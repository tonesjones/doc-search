---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "nKkDzMYUM4fwy_5z0Oh79Q"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:29.614771+00:00"
content_hash: "cd154031083e34819f2184899b6278ea78064b54de93c10421a8a4bfcb03fd3d"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide available in Black Duck.

## Removed support for `access_token` request parameter

Support for passing the authorization token (JWT) as a request parameter via the access_token request have been removed to address a security vulnerability. Users should ensure authorization tokens are passed using the Authorization HTTP header as documented in the REST API developer's guide.
