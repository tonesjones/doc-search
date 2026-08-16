---
title: "Fixed Issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "oh0T9lmvKBRTWbhirWZw2g"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:04.614783+00:00"
---

# Fixed Issues

The following issues have been fixed in this release:

- (HUB-47787). Fixed an issue where the project search API (`GET
  /api/projects`) caused excessive database resource consumption due
  to an inefficient authorization query. The query unnecessarily joined
  `central_project_version` and `version_bom`
  tables when resolving project access, resulting in degraded database performance
  under load. The authorization query has been optimized to remove these
  unnecessary joins, significantly reducing database utilization.
- (HUB-47791). Fixed a performance issue where high-volume read queries on the
  component_adjustment table executed full sequential scans, resulting in
  significantly degraded performance on deployments with large BOM datasets.
  Database indexes have been added on the `project_id` and
  `version_id` columns to ensure efficient query execution.
