---
title: "Using the Black Duck API with OpenAPI"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/using-the-black-duck-api-with-openapi.html"
content_id: "ds_MuEnU9JqssOumd6zm1Q"
version: "2026.7"
section: "Getting Started with the Black Duck API"
scraped_at: "2026-08-08T15:32:40.347665+00:00"
---

# Using the Black Duck API with OpenAPI

For users using OpenAPI Specification (OAS), you can generate customer-facing endpoints
through `/api-doc/openapi3-public.json`.

1. Log into Black Duck.
2. Open a browser tab and paste the following URL using you Black Duck server
   address.

   `https://<your_black_duck_server>/api-doc/openapi3-public.json`
3. On the page that's generated, right-click and save as
   `openapi3-public.json`
4. Import the saved `openapi3-public.json` into your
   application.
