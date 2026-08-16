---
title: "Retrieve configuration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-configuration.html"
content_id: "Rz~HZGg77ILa1O0qANvbmw"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:44.617256+00:00"
---

# Retrieve configuration

Example GET request to retrieve the configuration of the Coverity Connect server.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/serverInfo/config" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "dbDialect": "org.hibernate.dialect.PostgreSQLDialect",
  "dbDriver": "org.postgresql.Driver",
  "mainDBName": "cim",
  "mainDBUrl": "jdbc:postgresql://localhost:5432/cim",
  "mainDBUser": "coverity",
  "code": null,
  "message": null
}
```
