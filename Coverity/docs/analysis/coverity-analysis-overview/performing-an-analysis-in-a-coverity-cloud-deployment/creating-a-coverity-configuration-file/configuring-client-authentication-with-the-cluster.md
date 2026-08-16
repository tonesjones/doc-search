---
title: "Configuring client authentication with the cluster"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-client-authentication-with-the-cluster.html"
content_id: "j9I6jFWMYZ8B2rkR5hv8sg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:32:33.050011+00:00"
---

# Configuring client authentication with the cluster

To authenticate requests between the Coverity client and Coverity Connect, the Coverity
CLI uses an authentication key that is specified in either the configuration file
`coverity.yaml` or in your home directory. Requests sent to Coverity
Connect to interact with the Storage Service and Scan Service are authenticated using
HTTPS authentication. Refer to <https://datatracker.ietf.org/doc/html/rfc7617>.

Specify the username and password in the authentication key file. For example,
`"username":"admin"` and `"key":"60...e2"` (the
password), in this Coverity Connect authentication key file:

```
{
  "key":"60...e2",
  "id":10052,
  "type":"Coverity authentication key",
  "username":"admin"
  "comments": {
    "port":"8080",
    "host":"connect-dev",
    "description":"My Connect Auth Key",
    "creationDate":"2023-04-11T19:23:35.608Z",
    "ssl":"false",
    "expirationDate":"2053-04-11T19:23:35.592Z"
  },
  "domain":"local",
  "version":2
}
```
