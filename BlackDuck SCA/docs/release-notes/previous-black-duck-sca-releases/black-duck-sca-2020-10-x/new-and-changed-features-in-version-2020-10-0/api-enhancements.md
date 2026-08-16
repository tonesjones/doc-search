---
title: "API enhancements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/api-enhancements.html"
content_id: "v3tpl1bOB4Jc7IISSHnKTQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:26.874448+00:00"
---

# API enhancements

- (Hub-25643)Added an
  endpoint to determine the Single Sign-On (SSO) status of Black Duck.

  GET /api/sso/status
- (Hub-25637)Added endpoints
  for retrieving SAML/LDAP configurations (Admin use only).

  - Read SSO configuration:

    GET /api/sso/configuration
  - Download an IDP metadata file:

    GET /api/sso/idp-metadata
  - These SSO endpoints were also added:
    - Update SSO configuration:

      POST
      /api/sso/configuration
    - Upload an IDP metadata file:

      POST
      /api/sso/idp-metadata
- (Hub-24402)Added the
  following BOM hierarchical component endpoints:

  - List hierarchical root components:

    GET
    /api/projects/{projectId}/versions/{projectVersionId}/hierarchical-components
  - List hierarchical children components:

    GET
    /api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/hierarchical-components/{hierarchicalId}/children
  - List hierarchical children component versions:

    GET/api/projects/{projectId}/versions/{projectVersionId}/components/{componentId}/versions/{componentVersionId}/hierarchical-components/{hierarchicalId}/children
- (Hub-25641)New fields were
  added to the notifications API for vulnerabilities to enable further
  classification of notifications. These notifications involve vulnerability
  information that has changed in a BOM and includes the following fields:

  - vulnerabilityNotificationCause

    Information about the kind of vulnerability event that occurred and
    triggered a notification such as a vulnerability was added or
    removed, changed comment, changed remediation details, changed
    severity of vulnerability, or the status changed.
  - eventSource

    Information about the source that generated the notification, such as
    a scan, Black Duck KB update, or user actions such as
    remediation, reprioritization, or adjustment.
- The /api/catalog-risk-profile-dashboard API now returns HTTP 410 (GONE).
