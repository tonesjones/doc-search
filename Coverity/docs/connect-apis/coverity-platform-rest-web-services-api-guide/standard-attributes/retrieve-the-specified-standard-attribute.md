---
title: "Retrieve the specified standard attribute"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-the-specified-standard-attribute.html"
content_id: "~SjGu8aKi1nXVuBRcRWX2Q"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:55.012936+00:00"
---

# Retrieve the specified standard attribute

Example GET request to retrieve the specified standard attribute. You can use this
operation to retrieve both *built-in* and *custom* standard attributes.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/standardAttributes/PCI%20DSS%202018" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "name": "PCI DSS 2018",
  "builtIn": true,
  "visible": true,
  "attributeValues": [
    {
      "name": "6.5.1",
      "description": "Injection flaws, particularly SQL injection. Also consider ..."
    },
    {
      "name": "6.5.10",
      "description": "Broken authentication and session management."
    },
    {
      "name": "6.5.2",
      "description": "Buffer overflows"
    },
    {
      "name": "6.5.3",
      "description": "Insecure cryptographic storage"
    },
    {
      "name": "6.5.4",
      "description": "Insecure communications"
    },
    {
      "name": "6.5.5",
      "description": "Improper error handling"
    },
    {
      "name": "6.5.6",
      "description": "All \"high risk\" vulnerabilities identified in the ..."
    },
    {
      "name": "6.5.7",
      "description": "Cross-site scripting (XSS)"
    },
    {
      "name": "6.5.8",
      "description": "Improper access control (such as insecure direct object ..."
    },
    {
      "name": "6.5.9",
      "description": "Cross-site request forgery (CSRF)"
    }
  ],
  "code": null,
  "message": null
}
```
