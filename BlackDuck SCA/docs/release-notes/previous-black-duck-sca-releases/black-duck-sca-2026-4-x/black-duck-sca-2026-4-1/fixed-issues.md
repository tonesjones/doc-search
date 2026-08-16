---
title: "Fixed Issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "eN~PwDLjoe70lOZ~uVN~mw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:34:57.251788+00:00"
---

# Fixed Issues

The following customer-reported issues have been fixed in this release:

- (HUB-46114). Resolved an issue where bulk editing the Usage field on
  SBOM-imported component matches appeared to succeed but did not save the updated
  value. Bulk usage changes on SBOM-imported matches are now saved correctly.
- (HUB-46529). Resolved a security issue where users with the **Project
  Creator** role could retrieve sensitive user metadata via the REST API,
  despite the UI correctly restricting this access. Access controls have been
  updated to align API behavior with the UI, preventing non-admin users from
  accessing user management data.
- (HUB-46628). Resolved an issue where subprojects added to the BOM defaulted to an
  "Unreviewed" approval status with no way to change it, resulting in unavoidable
  policy violations. A new Approval Status field has been added at the Project
  Version level in Settings, allowing users to set the review status for
  subproject versions. This field is also supported via bulk actions in the
  Components tab and is carried over when cloning a project version.
- (HUB-47787). Resolved a performance issue with the `GET
  /api/projects` API where unnecessary database operations were
  causing slower response times. This optimization reduces query complexity and
  improves overall API performance, particularly for large deployments.
- (HUB-47826). Fixed an issue where the "SBOM" match type was missing from the
  Component Match Type table in the Reporting Database documentation.
- (HUB-47843). Fixed an issue where SBOM report generation failed with a
  NullPointerException when the report included subproject components.
