---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "WKuiJOGb1Eqk6L3zLy2mFw"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:12.316755+00:00"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-32387). Fixed an issue where redis could not access /data on default
  Openshift environments.
- (HUB-33820). Fixed an issue where a warning could appear after a component was
  updated in the BOM (e.g. its status in the KnowledgeBase is set to "reviewed")
  but would not disappear until the user reloaded the page manually.
- (HUB-34056). Fixed an issue where individual component edit displayed different
  results from bulk component edit when "Adjust Snippets and Confirm" was checked
  at the Edit dialog.
- (HUB-34374). Fixed an issue where the value in Discovery Types column on the
  source tab of the project version page could display inconsistently with
  filters.
- (HUB-34502). Fixed an issue where confirmed/unconfirmed snippet results were not
  included in the source report when including ignored components in reports.
- (HUB-34596). Fixed an issue where a duplicate constraint error would occur when
  attempting to create a SAML user sharing the same username as the internal
  user.
- (HUB-34725). Fixed an issue with duplicated
  `FILE_DEPENDENCY_DIRECT` and
  `FILE_DEPENDENCY_TRANSITIVE` entries in version reports.
- (HUB-34756). Fixed an issue where the scope showing as 'Server' when user group
  roles assigned through project groups using the API.
- (HUB-34947). Fixed an issue where ignored snippets could be displayed in SPDX
  reports.
- (HUB-35472). Fixed an issue where changing the value of
  `MAX_TOTAL_SOURCE_SIZE_MB` did not apply correctly in
  synopsysctl.
- (HUB-35557). Fixed an issue where improperly formed /api/projects/ requests would
  return a HTTP 5xx error code instead of a HTTP 4xx error code.
- (HUB-35585). Fixed an issue where the "Updated By" data was not updated and
  always reflecting "System Administrator" as the username of the user who made
  the change and has the old date/time.
- (HUB-35764). Fixed some GUI bugs in the top menu and in the snippet window.
- (HUB-35912). Fixed an issue where confirmed and then ignored snippet matches
  would disappear when the license risk filter with all the options selected was
  applied.
- (HUB-35914). Fixed an incorrect flag in the the system_check.sh script (using -z
  instead of -n).
- (HUB-35927). Fixed an issue where the remediation status and comment was not
  reverted by the Auto-Remediation feature if there are change in CVE BDSA mapping
  for components.
- (HUB-35945). Fixed an issue where the Scan Size value on the Project Version's
  Scans page did not include the size value of code locations as displayed on the
  main Scans page.
- (HUB-36321). Fixed an issue where the Edit option in the Source view for snippets
  was available to the Project Viewer role.
- (HUB-36382). Fixed a rare race condition generating an error when receiving more
  than one scan in rapid succession.
- (HUB-36498). Fixed an issue where the GET /api/vulnerabilities/<CVE
  RECORD>/affected-projects could return a HTTP 400 error code if the CVE had too
  many records.
- (HUB-36629). Fixed an issue where Rapid Scans could report extra vulnerabilities
  violating a policy rule.
- (HUB-36703). Fixed an issue where the Match type in the Black Duck UI and
  `/api/projects/{projectId}/versions/{projectVersionId}/matched-files`
  API request were different. See the API enhancements section above for
  details.
- (HUB-36707). Fixed an issue where Rapid Scan could timeout instead of end in
  error quickly if the project or version name was misspelled.
