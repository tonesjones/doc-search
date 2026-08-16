---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "Mg3HFFHkkjfsL_mqr9D~dw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:47.512334+00:00"
---

# API enhancements

For more information on API requests, please refer to the REST API Developers Guide
available in Black Duck.

## Removed support for `access_token` request parameter

Support for passing the authorization token (JWT) as a request parameter via the
access_token request have been removed to address a security vulnerability. Users
should ensure authorization tokens are passed using the Authorization HTTP header as
documented in the REST API developer's guide.
