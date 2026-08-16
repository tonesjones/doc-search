---
title: "Introduction to Coverity Platform REST Web Services API"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/introduction-to-coverity-platform-rest-web-services-api.html"
content_id: "8EumcFd_Oet6uR7cpJ3fCQ"
version: "2026.6"
section: "Coverity Connect APIs"
scraped_at: "2026-08-12T19:53:30.982027+00:00"
---

# Introduction to Coverity Platform REST Web Services API

The Coverity Platform REST Web Services API allows you to write Web applications or
scripts that communicate with Coverity Connect. The API uses REST (Representational
State Transfer) architectural style to send requests to the server using standard
HTTP/HTTPS and retrieve responses in JSON format.

You can use the API to perform the following types of operations:

- Configure Coverity Connect
- Retrieve issues from the Coverity Connect database
- Retrieve and manage existing Coverity Connect views

You can find usage examples for all API operations in this guide, grouped by resource,
with each type of resource having its own chapter.

You can access detailed reference documentation for these operations at the following URL:

```
<scheme>://<my_connect_host>:<port>/swagger/cim/index.html
```

where `<scheme>` is either `http` or `https`,
depending how you configured your Coverity Connect server, and
`<my_connect_host>:<port>` are the host and port of your
Coverity Connect server.

The reference documentation is written to the OpenAPI Specification (OAS) format, version
3, and describes the URI formats, input parameters, request schemas, and response
schemas of the operations.

You can access the OAS YAML file (from which the `index.html` file is generated)
at the following URL:

```
<scheme>://<my_connect_host>:<port>/swagger/cim/openapi.yaml
```

You can access a JSON transformation of this YAML file at the following URL:

```
<scheme>://<my_connect_host>:<port>/swagger/cim/openapi.json
```
