---
title: "Connection schema elements"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/connection-schema-elements.html"
content_id: "joumlyjiTqSXotcueF~BjQ"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:39.958447+00:00"
---

# Connection schema elements

The connection schema should include the following keys:

| Key | Class Type | Description | Default | Required? |
| --- | --- | --- | --- | --- |
| `ssl-ca-certs` | String | Lists the pathname to a file containing additional CA certificates that are used in establishing a secure HTTPS connection through an SSL handshake. Pathnames must be entered in PEM format. | N/A | No |
| `url` | String | Lists the URL of the Coverity Connect instance. This URL must not include user name and password. | N/A | Yes |
| `username` | String | Lists the user name that is used to connect to Coverity. | N/A | Yes |
