---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "XbSeZeTfxrjJ6B7k5q_Mvw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:56.021072+00:00"
---

# Fixed issues

The following customer-reported issues have been fixed in this release:

- (HUB-33532). Fixed an issue in the Version Details report where an improperly
  escaped backslash character could cause an invalid JSON format error when
  viewing the report content.
- (HUB-36358). Fixed an issue where the Signature Scanner could fail when scanning
  files compressed using the Pack200 format. This issue occurred due to an
  incompatibility introduced by a new version of the Apache Commons Compress
  library. The problem has been resolved with a local update to this library.
- (HUB-41944). Fixed an issue when modifying a custom field for a specific
  component version, the "Updated" field in the component details tab did not
  reflect the change but the changes to the component version details and license
  are reflected correctly.
- (HUB-42604). Fixed an issue where the match count shown on the Components page of
  the BOM was displaying a different count from the Source page.
- (HUB-43043). Fixed an issue where the BOM page would automatically refresh after
  reviewing/unreviewing a component, changing a component's version/license,
  ignoring/unignoring a component, manually adding a component, adding a comment,
  confirming/editing/ignoring a snippet match. The table now still refreshes, but
  in the background no longer disappears.
- (HUB-43170). Fixed an issue where a Signature Scan could produce a
  `java.nio.file.InvalidPathException` warning message in cli
  output when invalid archive file encountered.
- (HUB-43220). Optimized a query used in license API endpoints
  (`/api/internal/composite/licenses/{licenseId}/usages` and
  `/api/licenses/{licenseId}/bom-counts`) which was causing
  longer than expected load times.
- (HUB-43307). Updated the OpenJDK version to Zulu Java 17.0.12 in Black Duck to address vulnerability issues.
- (HUB-43315). Fixed a performance issue related to the query to extract the
  copyrights in report generation post upgrade Black Duck
  2024.7.0.
- (HUB-43342). Fixed an issue where notes added to a license were not displaying in
  the BOM License Details. We will show them under a Notes section from of
  collapsible element with a show more/show less button in case notes are long. If
  the license does not have any notes added, the Notes section will not
  appear.
- (HUB-43382). Fixed an issue where source file adjustments for binary scans could
  affect mutliple files where matches are shown for both a binary and within a JAR
  file. Source file adjustments for binary scans are now disabled.
- (HUB-43389). Fixed an issue where risk warning data was not being retained after
  unmapping the scan and then remapping.
- (HUB-43502). Created a new index on the
  `version_bom_applied_adjustment` table to improve performance
  when updating license texts.
