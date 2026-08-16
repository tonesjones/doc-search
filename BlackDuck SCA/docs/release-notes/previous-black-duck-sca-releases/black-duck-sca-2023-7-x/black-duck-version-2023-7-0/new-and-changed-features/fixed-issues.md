---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "mVhjoFNLObk~95ILLbElAw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:36:50.215284+00:00"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-21449). Fixed an issue with an incorrect policy violation display for
  vulnerability count in nested components when the violation was mitigated.
- (HUB-33362). Fixed an issue when trying to set up SAML with an XML file, the file
  would not save unless SAML is disabled.
- (HUB-34720). Fixed an issue when a license is modified, e.g. to reflect the
  original instead of the generic license text whilst not changing the license ID,
  the change was not exported to the SPDX file.
- (HUB-35512). Fixed an issue when adding a component version manually in the BOM
  page with a same component+version+origin, an "Unable to add manual BOM
  component because it already exists." error message will be consistantly
  displayed even if the origin setting is removed.
- (HUB-37067). Removed the Remediation Status filter from the Find →
  Vulnerabilities page.
- (HUB-37626). Fixed an issue where generating a SBOM report either on the UI or
  via API in JSON format for either v1.3 or v1.4 and attempting to retrieve it via
  `/api/projects/{projectId}/versions/{projectVersionId}/reports/{reportId}/contents`
  would display in a non-JSON format, including "/n" characters.
- (HUB-37763). Fixed an issue where the component counts API in license management
  did not match the linked "where used" counts results.
- (HUB-37796). Fixed an issue where MaaS could experience a scan failure with the
  error "Failed to create or update code location".
- (HUB-37922). Fixed an issue when attempting to use the bulk action feature on a
  BOM with more than 100 components specified.
- (HUB-38146). Fixed an issue where project version names containing the forward
  slash character ( / ) was causing the creation of subfolders in report
  generation. The forward slash character will now be substituted with the
  underscore character ( _ ).
- (HUB-38347). Fixed an issue where the signature scan tool issue was not
  calculating the source code size properly when performing docker image inspector
  scans which could cause the scan to fail.
- (HUB-38480). Fixed an issue where the API request `/api/projects`
  always sorting by name, regardless of the sorting option used.
- (HUB-38535). Fixed an issue where the `/api/components/<component
  ID>/versions/<version ID>/licenses/<license ID>` API request
  does not return the correct license approval status after being changed.
- (HUB-38554). Fixed an issue when using the HUB UI to navigate KB component
  versions where it was forcing the pagination to be 25 regardless of entry
  specified by the user.
- (HUB-38587). Fixed an issue where the `kbMatchTimeoutProperty` was
  set inadvertantly to hardcoded value (100000ms) while the it should always read
  it from the blackduck-config.env file.
- (HUB-38590). Fixed an issue where the All origins dropdown of the Add Component
  dialog box was only displaying 10 rows which could cause some origins to not
  display.
- (HUB-38598). Fixed an issue where the Component Manager role could get a 403
  Forbidden error when trying to access custom component versions after
  creation.
- (HUB-38646). Fixed an issue where private repositories where not visible via SCM
  integration. Note that you may have to delete the existing token from Black Duck
  for the changes to take effect.
- (HUB-38679). Renamed the Fulfillment Required column to Component Version Status
  in the Components report as it contains the component version's "Approval
  Status" to improve usability.
- (HUB-38685). Fixed an issue where project auto-delete was not using the new
  settings after being updated.
- (HUB-38720). Fixed an issue where the License text area was too small.
- (HUB-38774). Fixed an issue when attempting to unset the Release Date field
  within a project version would not persist, leaving the previously set date in
  place.
