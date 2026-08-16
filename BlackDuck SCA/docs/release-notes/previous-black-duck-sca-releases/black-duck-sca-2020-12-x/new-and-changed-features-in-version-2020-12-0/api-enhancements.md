---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "N3uCSI82J0GXqL2x18c50g"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:22.870862+00:00"
---

# API enhancements

- HUB-22422 Added ability to
  sort projects (api/projects) by the createdAt field.
- HUB-25138 Added the ability
  to filter to the api/projects endpoint for projects created before/after a
  date.
- HUB-26099 Added the API for
  displaying vulnerability matches as part of the Vulnerability Impact
  Analysis feature.

  GET
  /api/projects/{projectId}/versions/{projectVersionId}/vulnerabilities/{vulnerabilityId}/vulnerability-matches
- HUB-23916 The KnowledgeBase
  uses originating user-agent analytics to improve the scalability of
  KnowledgeBase services and improve quality of service for users.
- HUB-23898Added the following
  BOM endpoints:
  - Get BOM status summary:

    GET
    /api/projects/{projectId}/versions/{projectVersionId}/bom-status
  - List a BOM's events:

    GET
    /api/projects/{projectId}/versions/{projectVersionId}/bom-events
  - Delete a failed BOM event:

    DELETE
    /api/projects/{projectId}/versions/{projectVersionId}/bom-events/{bomEventId}
  - Delete all failed events from a BOM:

    DELETE
    /api/projects/{projectId}/versions/{projectVersionId}/bom-events
- HUB-26051New password settings endpoints:
  - Get password settings:

    GET
    /api/password/security/settings
  - Get system password settings:

    GET
    /api/password/management/settings
  - Update system password settings:

    PUT
    /api/password/management/settings
  - Validate password:

    POST
    /api/password/security/validate
- The /api/catalog-risk-profile-dashboard API now returns HTTP 404 (Not
  Found).
