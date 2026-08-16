---
title: "Generate a Connect SA admin user token"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/generate-a-connect-sa-admin-user-token.html"
content_id: "EQEZupFHS08_G9v7rwjEew"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:04.410196+00:00"
---

# Generate a Connect SA admin user token

Use the following `curl` command to generate a service account SA
`admin` user token:

```
curl -sSf --basic -u coverity-cli:<password> -d grant_type=client_credentials -d username=admin https://<connect_url>/token
```

where the options are:

- `-sSf` consists of `-sS` which returns error messages
  if curl fails, and `-f` which returns a `fail 22`
  error code for HTTP codes of 400 or greater.
- `-u <user:password>` provides the Coverity CLI username and
  password.
- `-d <data>` instances provide
  `grant_type=client_credentials` and
  `username=admin`.
- <connect_url> provides the Connect host/server URL, along with the
  `/token` directory within the Connect server.
