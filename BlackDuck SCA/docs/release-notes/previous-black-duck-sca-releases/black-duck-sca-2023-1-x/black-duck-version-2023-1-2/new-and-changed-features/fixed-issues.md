---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "Vo1VObFHqQ19hKF7dwCUOg"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:04.970782+00:00"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-35747). Fixed issue that would block certain periodic jobs
  (`BomAggregatePurgeOrphansJob`,
  `KbUpdateWorkflowJob`) from finishing.
- (HUB-36781). Fixed an issue where versions of Black Duck 2022.10.x could not be
  installed with custom fsGroup on Kubernetes or OpenShift.
- (HUB-36796). Fixed an issue where having a user directly assigned to a Project Group and
  the same user assigned to a User Group that's also assigned to the Project Group
  would result in multiple project groups being returned by the API, resulting in
  a Detect failure.
- (HUB-36939). Fixed an issue where the debug page exposed the password in plain
  text if the user logged into Black Duck as the sysadmin.
- (HUB-36997). Fixed an issue where license information was missing for notice
  files generated using KnowledgeBase on-prem.
- (HUB-37143). Fixed an issue where rapid scans that evaluate the policy expression 'Newer
  Versions Count' fail with internal error if the component does not have a
  version.
- (HUB-37285). Fixed an issue where new installations of Black Duck 2023.1.0 using
  an external database could fail if the default admin user name was changed.
- (HUB-37312). Fixed an issue where a `Unable to access tool` error
  could be generated if the `/opt/blackduck/hub/uploads/tools`
  directory doesn't exist in the mounted storage volume when looking for
  objects.
