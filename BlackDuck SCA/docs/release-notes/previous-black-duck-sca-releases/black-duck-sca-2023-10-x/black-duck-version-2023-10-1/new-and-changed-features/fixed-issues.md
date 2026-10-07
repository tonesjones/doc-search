---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "9DUoIY62WeeT8CyVR6iCPQ"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:31.378762+00:00"
content_hash: "5f32c348ded60bd8619546ab540a26eb685be394880bcb57ccd6f96b05202cb1"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-37681). Added the missing public API: `api/projects/{projectId}/versions/{versionId}/bom-status/{scanId}`to the REST API Developers Guide.
- (HUB-39616). Updated the API response for `matched-files` queries to include a `uri` field. See the API enhancements section for more information.
- (HUB-39693). Moved log messages related to symlink to the Trace level when using scan cli.
- (HUB-40316). Fixed an issue where the scan client could fail to write data to the BDIO file when the file name was blank. Validation has been added to verify that the file name is present and not a null string.
- (HUB-40354). Clarified the Notices File report documentation regarding sub-project name and license handling.
- (HUB-40524). Clarified the documentation regarding Detect Hosting Location for Internally Hosted options.
- (HUB-40631). Fixed an issue where a null pointer exception could occur when generating a Version Details report if a project version is added to another project as a subproject and the subproject doesn’t have a nickname.
