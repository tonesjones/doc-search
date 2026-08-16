---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "usLzlUc5lDd75XdSAG_zwg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:35:52.520277+00:00"
---

# Fixed issues

The following customer-reported issues have been fixed in this release:

- (HUB-43265). Fixed an issue where cloning projects with users and groups selected
  and there are no user groups assigned to the project could generate a HTTP 400 -
  Parameter set is empty stack trace error.
- (HUB-43391). Fixed an issue where ignored components/subprojects could still be
  included in SBOM reports.
- (HUB-43413). Fixed an issue where components with no comments could sometimes
  appear when "components with comments" filter is set.
- (HUB-43588). Fixed an issue where the License Risk count at the top of the
  Component page did not update promptly after a component's license was changed,
  sometimes taking several days to reflect the change.
- (HUB-43760). Fixed an issue where the string "(c) Copyright" could cause the
  copyright normalization job to fail.
- (HUB-43860). Fixed an issue where database dumps of `bds_hub`
  could fail to restore due to a mismatch in view definitions.
