---
title: "Retrieve all standard attributes"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/retrieve-all-standard-attributes.html"
content_id: "4ygTzWJ1CWq5xDGCm3kexQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:54:55.661649+00:00"
---

# Retrieve all standard attributes

Example GET request to retrieve all standard attributes, both *built-in* and *custom*.

**cURL request**

```
curl --location \
--request GET "http://my_connect_host:8080/api/v2/standardAttributes" \
--header 'Accept: application/json' \
--user my_username:my_password \
```

**Response body**

```
{
  "attributes": [
    {
      "name": "OWASP Web Top Ten 2021",
      "builtIn": true,
      "visible": true,
      "attributeValues": [
        {
          "name": "A1",
          "description": "Restrictions on what authenticated users are allowed to ..."
        },
        {
          "name": "A10",
          "description": "Server-side request forgery occurs when a server is ..."
        },
        {
          "name": "A2",
          "description": "Many web applications and APIs do not properly protect ..."
        },
        {
          "name": "A3",
          "description": "Injection flaws, such as SQL, NoSQL, OS, and LDAP ..."
        },
        {
          "name": "A4",
          "description": "Insecure design encompasses a wide range of ..."
        },
        {
          "name": "A5",
          "description": "Security misconfiguration is commonly a result of ..."
        },
        {
          "name": "A6",
          "description": "Components, such as libraries, frameworks, and other ..."
        },
        {
          "name": "A7",
          "description": "Application functions related to authentication and ..."
        },
        {
          "name": "A8",
          "description": "Software and data integrity failures result from ..."
        },
        {
          "name": "A9",
          "description": "Insufficient logging and monitoring, coupled with missing ..."
        }
      ]
    },
    {
      "name": "OWASP Web Top Ten 2017",
      "builtIn": true,
      "visible": true,
      "attributeValues": [
        {
          "name": "A1",
          "description": "Injection flaws, such as SQL, NoSQL, OS, and LDAP ..."
        },
        {
          "name": "A10",
          "description": "Insufficient logging and monitoring, coupled with ..."
        },
        {
          "name": "A2",
          "description": "Application functions related to authentication and ..."
        },
        {
          "name": "A3",
          "description": "Many web applications and APIs do not properly protect ..."
        },
        {
          "name": "A4",
          "description": "Many older or poorly configured XML processors evaluate ..."
        },
        {
          "name": "A5",
          "description": "Restrictions on what authenticated users are allowed to do ..."
        },
        {
          "name": "A6",
          "description": "Security misconfiguration is the most commonly seen issue ..."
        },
        {
          "name": "A7",
          "description": "XSS flaws occur whenever an application includes untrusted ..."
        },
        {
          "name": "A8",
          "description": "Insecure deserialization often leads to remote code execution..."
        },
        {
          "name": "A9",
          "description": "Components, such as libraries, frameworks, and other software ..."
        }
      ]
    },
============================ MANY OMITTED LINES =================================
  ],
  "code": null,
  "message": null
}
```
