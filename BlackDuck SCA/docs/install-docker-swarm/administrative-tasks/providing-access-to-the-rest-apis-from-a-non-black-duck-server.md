---
title: "Providing access to the REST APIs from a non-Black Duck server"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/providing-access-to-the-rest-apis-from-a-non-black-duck-server.html"
content_id: "4oNeRmMxohjM9mtjbL58Yg"
version: "2026.7"
section: "Installing Black Duck using Docker Swarm"
scraped_at: "2026-08-08T15:33:41.991026+00:00"
---

# Providing access to the REST APIs from a non-Black Duck server

You may wish to access Black Duck REST APIs from a web page that was
served from a non-Black Duck server. To enable access to the REST APIs
from a non-Black Duck server, Cross Origin Resource Sharing (CORS) must
be enabled.

The properties used to enable and configure CORS for Black Duck
installations are:

| Property | Description |
| --- | --- |
| BLACKDUCK_HUB_CORS_ENABLED | Required. Defines whether CORS is enabled; "true" indicates CORS is enabled. |
| BLACKDUCK_CORS_ALLOWED_​ORIGINS_​PROP_NAME | Required. Allowed origins for CORS.  The browser sends an origin header when it makes a cross-origin request. This is the origin that must be listed in the blackduck.hub.cors.allowedOrigins/BLACKDUCK_CORS_ALLOWED_​ORIGINS_PROP_NAME property.  For example, if you are running a server that serves a page from http://123.34.5.67:8080, then the browser should set this as the origin, and this value should be added to the property.  Note that the protocol, host, and port must match. Use a comma-separated list to specify more than one base origin URL. |
| BLACKDUCK_CORS_ALLOWED_​HEADERS_PROP_NAME | Optional. Headers that can be used to make the requests. |
| BLACKDUCK_CORS_EXPOSED_​HEADERS_PROP_NAME | Optional. Headers that can be accessed by the browser requesting CORS. |
| BLACKDUCK_CORS_ALLOWED_​ORIGIN_PATTERNS_PROP_NAME | Alternative to BLACKDUCK_CORS_ALLOWED_ORIGINS_​PROP_NAME*,* that supports origins declared via wildcard patterns. BLACKDUCK_CORS_ALLOWED_ORIGIN_PATTERNS_​PROP_NAME overrides BLACKDUCK_CORS_ALLOWED_ORIGINS_PROP_NAME. |
| BLACKDUCK_CORS_ALLOW_​CREDENTIALS_PROP_NAME | Specifies whether the browser should send credentials, such as cookies along with cross domain requests, to the annotated endpoint. The configured value is set on the Access-Control-Allow-Credentials response header of preflight requests. It is invalid to configure ALLOW_CREDENTIALS=true and ALLOWED_ORIGIN=*. If the 'ALL' configuration value is required for allowed origins, it should configured using the ALLOWED_ORIGIN_PATTERNS configuration property instead going forward. |

To configure these properties, edit the `blackduck-config.env` file,
located in the `docker-swarm` directory.
