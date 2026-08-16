---
title: "Announcements"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/announcements.html"
content_id: "rdPJka~gb7whkftdeIJ2cA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:09.070706+00:00"
---

# Announcements

## Introduction of Match Review Process

With the Black Duck SCA 2026.1.x release, we are excited to introduce the Match
Review process. This new feature will add a Review tab to the Bill of Materials,
where certain items identified during scanning will be placed for further
evaluation.

After the upgrade, existing Project Versions' Bills of Materials will initially
appear unchanged. However, you will gain access to additional information about
unmatched items in the new Review tab. Upon rescanning a Project Version with the
updated software, you may notice some matches moving from the Bill of Materials to
the Review tab.

New Project Versions will immediately incorporate this feature, displaying relevant
scan contents in the Review tab right away. For more details, please refer to the
User Guide.

## Deprecation of Archived Project Phase

**Effective immediately, the Archived project phase has been deprecated in favor of
Long Term Support (LTS) project versions.**

With the introduction and ongoing enhancements to LTS project versions, we are
transitioning away from the Archived phase to provide a more robust solution for
managing released software artifacts that require ongoing vulnerability tracking and
support:

- **No New Archived Versions**: New archived project versions can no longer be
  created.
- **Existing Archived Versions**: Current archived project versions will not be
  deleted or removed during upgrade. However, they will now be subject to data
  retention policies that will either transition them to LTS (by default) or
  delete them after the data retention period has been met (default 90 days).
- **Automated Transition**: An automated workflow will either delete existing
  archived project versions or transition them to LTS state, configurable through
  the System Administrator data retention settings page.
- **Mandatory Configuration**: This automated workflow cannot be disabled and
  must be configured by system administrators.
- **Future Removal**: The Archived project phase will be completely removed
  from Black Duck SCA in a future release.

**Action Required:** System administrators should review and configure the
automated transition settings in the data retention settings page to ensure proper
handling of existing archived project versions.
