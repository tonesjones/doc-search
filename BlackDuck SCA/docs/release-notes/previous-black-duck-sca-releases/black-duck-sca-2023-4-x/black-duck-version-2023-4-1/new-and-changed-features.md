---
title: "New and changed features"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/new-and-changed-features.html"
content_id: "Jk4_fUxrH1MRNtSNh9x5LA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:55.901362+00:00"
---

# New and changed features

## Improved unmatched file data purging

You can now purge unmatched file data for project versions that are specifically in
the Archived project phase. This can be done globally through the Admin > System
Settings > Data Retention page, which affects all projects, or locally for a
selected project on its Settings page.

Note that the global setting only applies to projects and scans that do not
explicitly specify their own setting; similarly, changing the global setting does
not affect projects or scans that do specify their own setting.

## SBOM report validation against policies

You can now configure specific project groups to validate the generation of SBOM
reports against policies.

A new setting at the project group level (with project group access) can be enabled
to prevent the generation of SBOM reports in projects that have any policy
violations and provides the ability to apply the setting to projects in a group or
all projects in all child groups.

When setting is enabled, when attempting to generate a SBOM report, you will be
informed that the report can't be generated because the project has policy
violations.

## New SPDX v2.3 support for SBOM reports

You can now export the Software Bill of Materials report for your projects in SPDX
v2.3 format.

## New Project Alias SBOM field

A new optional Project Alias SBOM field has added to override project name and
version info field at the project level. You must first activate the field under
Manage > SBOM > Project. Once enabled, you can change the project's alias under the
project's page > Settings.
