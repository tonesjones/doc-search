---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "~ppZyDduM2~AcBvCqO0FTw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:19.978095+00:00"
---

# API enhancements

- HUB-21225 API documentation
  is now only available at https://<Black Duck server
  URL>/api-doc/public.html.
- HUB-26561 Added the
  capability to filter code locations (/api/codelocations) by creation
  date.
- HUB-27622 Fixed the API
  used to download the SAML Identity Provider Metadata XML file
  (api/sso/idp-metadata endpoint) that was working incorrectly in previous
  versions.
- HUB-26959 The
  remediation-guidance endpoint (GET
  /api/components/{componentId}/versions/{componentVersionId}/remediating) no
  longer returns a “410 GONE” response. You must switch to the
  upgrade-guidance endpoint, (GET
  /api/components/{componentId}/versions/{componentVersionId}/upgrade-guidance)
  which is incompatible with the remediation-guidance endpoint that was
  removed.
- HUB-26598Added a report
  dependency-paths endpoint to show dependency paths for a component:

  /api/project/{projectId}/version/{projectVersionId}/origin/{originId}/dependency-paths
- Added the Black Duck Detect URI endpoint which is only used to set or update
  reading the Black Duck Detect URI on the System Settings page:

  /external-config/detect-uri
