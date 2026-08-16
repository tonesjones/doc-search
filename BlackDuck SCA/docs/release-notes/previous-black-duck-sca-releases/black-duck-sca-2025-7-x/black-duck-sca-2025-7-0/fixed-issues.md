---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "2NgPKkpWPZASjgNCWeQ5lA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:30.145677+00:00"
---

# Fixed issues

The following customer-reported issues have been fixed in this release:

- (HUB-34976, HUB-39582). Fixed an issue where certain TAR archives could not be
  unpacked by the scan client. Previously, some TAR files were treated as single
  files rather than unpacked and scanned properly. The scan client now correctly
  detects and processes these archives.
- (HUB-38990). Fixed an issue where the Project filter may not return results in
  the Scan Mapping dialog.
- (HUB-43218). Fixed an issue where the tag:value format was not passing the SPDX
  ntia-conformance-checker in SBOM reports generated using SPDX 2.3.
- (HUB-43300). Fixed an issue where the `/api/notifications/{notifications
  id}` did not enforce proper user-based authorization.
- (HUB-43916). Fixed an issue where SCASS scans were not honoring proxy
  settings.
- (HUB-43992). Fixed a NullPointerException error during Black Duck signature scans
  caused by a null 'MatchAmbiguityDetail.'
- (HUB-44199). Fixed an issue where users could get an intermittent Unable to
  manage snippet adjustment error message when using the `PUT
  /api/projects/{projectId}/versions/{projectVersionId}/bulk-snippet-bom-entries`
  endpoint.
- (HUB-44217). Fixed an issue where BDMU files larger than 10 MB in size may not be
  processed by Black Duck.
- (HUB-44246). Updated the Black Duck SCA documentation
  related to "Hosting location for Black Duck Detect" for Code Sight
  customers.
- (HUB-44352). Fixed an issue the `st.iscomponentignored` function
  was not ignoring the `IGNORED_SNIPPET`
  `ignore_status`.
- (HUB-44469). Removed the dbschema section from the System Information debug
  page.
- (HUB-44497). Fixed an issue where navigation from an LTS project version returned
  users ti tge Active Versions tab even when no active versions existed.
- (HUB-44533). Fixed an issue where exact file matching was not enabled when
  scanning Docker images on Docker version 26 (with '--detect.docker.image') or
  images created on Docker 26 (with 'detect.docker.tar').
- (HUB-44574). Fixed an issue where match confidence was not returning in package
  manager scans executed through SCASS.
- (HUB-44586). Fixed an issue where hidden directories (/css/, /js/, /images/,
  /fonts/) were returning 403 errors instead of 404 errors during DAST scans.
- (HUB-44625). Resolved an issue where project versions remained stuck during
  conversion to LTS, causing UI spinning and failed rescans due to database
  conflicts.
- (HUB-44675). Fixed an issue causing intermittent 500 Internal Server Errors
  during parallel scans on the same code location, due to duplicate key constraint
  violations in the database.
- (HUB-44684). Improved the performance of project version license term report
  generation.
- (HUB-44738). Fixed an issue causing duplicate source trees to appear for a single
  binary scan in Black Duck. The issue, linked to switching from jsonld to
  protobuf format, has been fixed with code changes and a background job to clean
  up old scan data.
- (HUB-44807). Fixed an issue in the webapp's risk profile calculation caused by
  missing cyclic dependency checks in Source View code. The fix prevents
  adjustments that create direct cyclic references between project versions,
  ensuring proper error handling and avoiding infinite loops.
- (HUB-44811). Fixed an issue where mapping folders or files to components showed a
  success message but failed to update the component name in the components tab.
  The fix disables the Edit button when editing is not allowed and ensures the UI
  uses the correct PUT API for adjustments.
- (HUB-44844). Fixed an issue where users with the "Project Administrator" or
  "Project Manager" roles were able to read all users' access tokens via the
  `GET /api/tokens` endpoint.
- (HUB-44845). Fixed an issue where users with the project-level "Project
  Administrator" or "Project Manager" roles are able to do BOM comparisons with
  projects they do not have direct/indirect access to.
- (HUB-44888). Resolved an issue where the component's page did not indicate
  whether a component was used in Long-Term Support (LTS) projects. This prevented
  users from identifying which LTS projects were potentially affected by
  vulnerabilities associated with the component.
- (HUB-44890). Resolved an issue where the 'matched-files' REST API incorrectly
  counted matches for the same component across multiple scans as one, resulting
  in mismatched `totalCount` and `items` in the API
  response.
- (HUB-44923). Fixed an issue where the "Server Unavailable" message could persist
  on the Black Duck login screen for an extended period after a Docker Swarm
  deployment had been completed.
- (HUB-44924). Fixed an issue where any authenticated user was able to view the scan
  summary of a code location via the `GET
  /api/codelocations/<code-location-id>/scan-summaries`
  endpoint.
- (HUB-44925). Fixed an issue where CSV exports from certain API endpoint, such as
  `/api/users`, `/api/risk-profile-dashboard`,
  and `/api/codelocations`, included user-provided input that could
  allow formula injection. User input is now properly santized to prevent this
  behavior. This fix has been applied across all areas of Black Duck where CSVs
  are generated with user input.
- (HUB-44958). Fixed an issue where attempting to change a component's 'Usage'
  type (e.g., from "Prerequisite" to "Dynamically Linked") displayed a success
  message but did not save the changes. The issue was limited to certain 'Usage'
  types, while others, like "Source Code," worked as expected.
- (HUB-44971). Resolved an issue where users encountered 403 errors during
  signature scans despite having the project code scanner role assigned. The
  problem was linked to specific dataset inconsistencies after upgrading from
  2024.4.1 to 2025.1.1 and was not reproducible on a clean HUB instance.
- (HUB-45073). Fixed an issue where custom components with Black Duck
  reference IDs in SBOMs were not auto-created during import, resulting in
  incomplete BOMs.
- (HUB-45082). Resolved an issue where moving a project group resulted in the
  removal of its description, displaying "No description." The fix ensures that
  group descriptions are preserved when groups are moved within the Manage →
  Project Groups interface.
- (HUB-45087). Fixed an issue where `scan_start_at` was incorrectly
  mapped in `scan_view` and `scan_stats_view`, using
  the CL creation time instead of the actual scan start time. This caused all
  scans on the same CL to share the same start date. The mapping has been
  corrected to reflect the accurate scan start time.
- (HUB-45100). Fixed an issue where cloning a project version with
  `update=true` did not preserve the "unknown license" value
  from the original request.
- (HUB-45112). Fixed an issue where Black Duck failed to process valid CycloneDX
  1.4 SBOMs if the "tools" field was missing, despite it not being mandatory per
  the CycloneDX 1.4 specification. The fix ensures SBOMs without the "tools" field
  are processed successfully, aligning with the schema requirements.
- (HUB-45139). Fixed a bug where components from BDBA protobuf BDIO scans failed to
  appear correctly in the HUB UI, unlike JSON BDIO scans. The issue was linked to
  differences in matching methods and API inconsistencies. The KBAPI 6.2.0 update
  addressed these matching issues, improving protobuf BDIO component visibility,
  with ongoing HUB-side fixes required for complete resolution.
- (HUB-45140). Fixed an issue where custom fields added to project conditions in
  policy rules displayed duplicated values instead of the correct individual
  entries.
- (HUB-45142). Fixed an issue where certain components from Rocky Linux did not
  display the correct origin ID or namespace in Black Duck scans.
- (HUB-45167). Fixed an issue in version 2025.1.1 causing SPDX report generation
  failures when reference locators contained spaces.
- (HUB-45186). Fixed an issue where license fulfillment terms were not correctly
  reflected in the policy violations view for unfulfilled licenses. Changes made
  in the legal terms tab did not update the version view, causing inconsistencies
  between the top-level view and the BOM view. The fix ensures accurate
  synchronization across views when license terms are marked as fulfilled.
- (HUB-45187). Resolved an issue where cryptography data failed to display unless
  the component version's approval status was set to 'Unreviewed'. The issue
  involved incorrect handling of approval statuses other than 'Unreviewed',
  preventing cryptography data from populating correctly.
- (HUB-45213). Fixed an issue where the match content was missing in the version
  report for components with Match Type Exact and Binary and File Modified.
- (HUB-45353). Corrected the documentation error regarding the IFM property for
  creating custom signatures. The documentation incorrectly listed the property as
  `--blackduck.signature.scanner.individual.file.matching`,
  which should be
  `--detect.blackduck.signature.scanner.individual.file.matching`.
- (HUB-45354). Updated the Artifactory plugin installation documentation to replace
  the outdated sig-repo URL with the correct URL.
- (HUB-45389). Updated the description for Custom Scan Signature to be more inline
  with its actual functionality.
- (HUB-45396). Resolved an issue where SBOM imports resulted in unmatched
  components due to incorrect character encoding of '+' in PURLs. The encoding
  error converted '+' to '%20' instead of '%2B', causing lookup failures. The fix
  ensures proper encoding, allowing successful PURL lookups and matching of
  components.
- (HUB-45488). Fixed an issue where roles where duplicated on the User Groups
  page.
- (HUB-45515). Fixed a signature scan failure (ERR05_1076) experienced by ASML,
  caused by a NullPointerException in the Hub system. The issue stemmed from a
  null ScanMatchNode channel version after a MaaS-side fix. The fix involves
  updating Hub handling of null ScanMatchNode.
- (HUB-45530). Re-enabled source file adjustments for all binary matches and
  restored functionality as it existed in Black Duck
  2024.10.0.
- (HUB-45620). Resolved a bug where comments on components in one child project
  were incorrectly attributed to all child projects in the parent project’s
  component report. The fix ensures comments are now correctly limited to the
  child project where they were added.
- (HUB-45659). Fixed a UI issue where a "Failed to load custom fields" banner
  error appeared on the custom fields page for projects, project versions,
  components, etc. Despite the error, functionality to view and edit custom fields
  remained unaffected.
