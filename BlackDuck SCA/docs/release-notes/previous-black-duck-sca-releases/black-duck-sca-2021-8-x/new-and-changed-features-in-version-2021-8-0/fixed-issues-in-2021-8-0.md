---
title: "Fixed Issues in 2021.8.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2021.8.0.html"
content_id: "te4DVDWHIqOhTYAjepkTMg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:07.429733+00:00"
---

# Fixed Issues in 2021.8.0

- (HUB-29341). Fixed an issue when exporting BOM from Protex using the
  --include-files flag and then importing it to a Hub instance would generate
  a Java heap space error.
- (HUB-29005). Fixed an issue where if a BOM has two components with the exact
  same name but different UUIDs, the filter API
  (`/api/projects/projectId/versions/versionId/components-filters?filterKey=bomComponents`)
  should return two separate components based on ID and their versions (if
  present) rather than grouping them by name.
- (HUB-29567). Fixed an issue where the “Updated” (or “Last Settings Update” in
  2021.8.0) timestamp would be updated but not the updated by user name on the
  Project version > Details view. The “Last Settings Update” timestamp and
  updated by user name will now only be updated when project version details
  are changed.
- (HUB-30139). Fixed an issue in the Protex BOM tool where an Unmarshalling
  Error: Illegal character occurred when using the --include-files flag.
- (HUB-12280). Fixed an issue where uploading a bdio file with relationships to
  the project are not visible when they are also located lower in the 'bdio
  tree'.
- (HUB-29481). Fixed an issue where licenses with the same name but different
  capital letters were being omitted from notices reports.
- (HUB-30143). Fixed an issue where the Protex BOM tool 2021.6.0 did not work
  with latest JDK (11.0.11).
- (HUB-29274). Fixed an issue where VersionReportJob could cause jobrunner Out
  Of Memory issue when there are circular references on BOM page.
- (HUB-29381). Fixed an issue when a project version is added as a component
  (using Add > Project), the component entry would show an invalid Operational
  Risk level.
- (HUB-30087). Fixed an issue where the project version query fails to find the
  version when version name includes multi-byte alpha-numeric characters.
- (HUB-23686). Fixed an issue when running Detect against a node file the
  signature scanner would get stuck.
- (HUB-25592). Fixed an issue where component (or component version)'s
  adjustments got dropped automatically from BOM.
- (HUB-25552). Fixed an issue where component (or component version) with
  'MATCH' type adjustments were automatically added/deleted from BOM.
- (HUB-29196). Fixed an issue where the policy violation pop-up did not
  disappear when it was clicked and the mouse cursor was moved away from the
  policy violation symbol quickly.
- (HUB-29573). Fixed an issue where line breaks in a policy rule's description
  were ignored when viewing the policy violation modal.
- (HUB-30611). Fixed an issue with where numeric usernames were causing errors
  in a database migration script.
- (HUB-26611). Fixed an issue where Direct/Transitive dependencies were not
  reported correctly when using aggregation in Detect. Please note that this
  fix is resolved only when using Detect 7.4 and requires using the new
  SUBPROJECT `detect.bom.aggregate.remediation.mode` in
  Detect.
- (HUB-22379). Fixed performance issues where project tagging and having tag
  policy can take hours on some instances.
- (HUB-30141). Fixed an issue with Hub swarm docker-compose.yml containing the
  unsupported "links" options.
- (HUB-29549). Fixed a performance issue with the loading of the BOM page
  caused by permission checks.
