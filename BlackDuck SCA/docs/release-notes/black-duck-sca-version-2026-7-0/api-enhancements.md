---
title: "API Enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "Hi94QJuNj4aAkjWqDjtfUw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:34:48.296119+00:00"
---

# API Enhancements

For more information on API requests, please refer to the REST API Developers Guide
available in Black Duck SCA.

## Removal of User Token API

As previously announced in the 2026.1.0 release, the following API related to user
tokens has been removed in this update. Any requests to this API will now result in
an HTTP 410 Gone response, indicating that the resource is no longer available:

- `PUT /api/current-user/tokens/<token-id>`

## Sunset of Component Vulnerability APIs

As part of our ongoing efforts to streamline our API offerings, the component
vulnerability APIs
(`/api/components/<component-id>/vulnerabilities`) have
undergone several changes in recent releases. These APIs were first deprecated, then
reduced in functionality, and subsequently adjusted to return an HTTP 410 Gone
response.

With this release, we are completing the sunset process by removing the component
vulnerability APIs entirely. Users are encouraged to transition to alternative
solutions as needed.
