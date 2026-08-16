---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "kHEInwYz8ZETaLfzVqFu4w"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:15.986373+00:00"
---

# API enhancements

- (HUB-22685)Added the
  capability to generate Postman collections in the API documentation through
  `/api-doc/postman-collection-public.json`. Users can
  import the `postman-collection-public.json` file as a Postman
  collection into Postman.
- (HUB-25767)Added the
  capability to generate OpenAPI Specification (OAS) for customer-facing
  endpoints through `/api-doc/openapi3-public.json`.
- (HUB-17862)Added the
  capability to filter projects by project owner by using
  `/api/projects?filter=owner`, which takes the URL of the
  user to search for the user-owned projects, for example,
  `/api/projects?filter=owner:https://<bd_server>/api/users/`.
- HUB-19331Added license
  ownership information as a new ownership field to the
  `/projects/{projectId}/versions/{projectVersionId}/components`
  endpoint.
- HUB-13863Added APIs for
  reading and altering the following application settings:

  - Reading analysis settings

    ```
    GET /api/settings/analysis
    ```
  - Updating analysis settings

    ```
    PUT /api/settings/analysis
    ```
  - Reading branding settings

    ```
    GET /api/settings/branding
    ```
  - Updating branding settings

    ```
    PUT /api/settings/branding
    ```
  - Reading license review settings

    ```
    GET /api/settings/license-review
    ```
  - Updating license review settings

    ```
    PUT /api/settings/license-review
    ```
  - Reading role settings

    ```
    GET /api/settings/role
    ```
  - Updating role settings

    ```
    PUT /api/settings/role
    ```
- HUB-24905Added
  `/api/component-migrations` and
  `/api/component-migrations/{componentOrVersionId}`
  endpoints to get component migration data based on specific dates or
  specific components from the KnowledgeBase.
- HUB-26144Made the
  `/license-dashboard` API public, which allows a user to
  see the in-use licenses.
- HUB-27956Resolved an issue
  with the `api/vulnerabilities/{vulnerabilityId}` endpoint
  returning a header overflow error when the vulnerability had over 100
  references. The endpoint now provides a warning and includes meta links in
  the response body when 25 or more link headers are returned in the response
  headers.
- (HUB-28262)Removed the
  "Trigger type" filter from the Activity/Journal endpoints as it is only used
  for the "user" type.
