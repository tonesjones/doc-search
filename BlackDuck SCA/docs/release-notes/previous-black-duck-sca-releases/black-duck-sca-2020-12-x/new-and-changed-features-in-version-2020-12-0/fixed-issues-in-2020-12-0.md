---
title: "Fixed Issues in 2020.12.0"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2020.12.0.html"
content_id: "O5G0zflcVCPREuyed4f2wg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:38:23.446853+00:00"
---

# Fixed Issues in 2020.12.0

The following customer-reported issues were fixed in this release:

- Hub-22422, 25138- API ENHANCEMENT?
- HUB-24339, 24618- NO HUB FIX
- Hub-25612 - Fixed in an earlier release
- (Hub-24731). No Hub fix
- (Hub-24780). No Hub fix
- (Hub-24827, 25315, 25455, 25849, 26346). Duplicate
- Hub-26189 - Info added to install guide
- (Hub-26428 - Logstash new version1.0.8
- (Hub-24839). Fixed an issue where some component origin IDs could not be
  selected from the Add/Edit Component dialog box.
- (Hub-24911). Fixed an issue where a failed KBUpdateJob skipped component
  updates.
- (Hub-25230). Fixed an issue where the license text window did not appear when
  the user attempted to open or edit license text.
- (Hub-25360). Fixed an issue where copyright search failed to find copyright holders when the
  copyright statement spanned multiple lines. OPEN-Triage
- (Hub-25436). Fixed an issue where after upgrading to version 2020.6.2, some of the
  vulnerabilities in Chromium (Google Chrome), version 50.0.2661.94 did not appear
  in the BOM due to an error in the KbUpdateJob. OPEN
- (Hub-25452). Fixed an issue so that the **Discovery Type** filter is
  automatically added when a license type is selected when viewing license
  search results page in the **Source** tab.
- (Hub-25489). Fixed an issue where the filter in the **Source** tab was
  reset when the subfolder was changed.
- (Hub-25603). Fixed an issue so that the path shown in the **Matched File
  Path** field in the Snippet View dialog box on the **Source** tab
  refreshed when an alternative path was selected.
- (Hub-25681). Fixed an issue where the Protex BOM Tool failed to import
  licenses for generic/unspecified component versions.
- (Hub-25715). Fixed an issue where the Active status in the Custom Fields
  Management page could not be modified unless the mouse was used.
- (Hub-25739). Fixed an issue where all comments for a BOM component could not
  be viewed.
- (Hub-25874). Fixed an issue where the
  `bom_component_custom_fields_date_time.csv`
  report listed different data than the
  `components_date_time.csv` report even though the
  data was in the same column name.
- (Hub-26302). Fixed an issue where cloning project via API dropped component
  edits. API DOC FIX
- (Hub-26442). Fixed an issue whereby a scan could not be deleted inside a
  project version by a project owner.
- (Hub-26493). Fixed a confusing error message so that it was clear that a user could not
  remove themselves as a member of a project. IN 2021.2 RELEASE
- (Hub-26496). Fixed an issue where a policy violation for license risk was
  still triggered although the license risk had changed when the component's
  usage was changed.
