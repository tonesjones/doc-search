---
title: "Fixed issues"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues.html"
content_id: "t75F9HhmjvnOox6CpAzWkQ"
version: "2026.7"
section: "Black Duck SCA Release Notes"
scraped_at: "2026-10-04T23:32:32.718534+00:00"
content_hash: "3e339d042a2c7e5ce120cf01ce27870b17f49545efe3336ea26015f665fb4b49"
---

# Fixed issues

The following customer-reported issues were fixed in this release:

- (HUB-35747). Fixed issue that would block certain periodic jobs (`BomAggregatePurgeOrphansJob`, `KbUpdateWorkflowJob`) from finishing.
- (HUB-36781). Fixed an issue where versions of Black Duck 2022.10.x could not be installed with custom fsGroup on Kubernetes or OpenShift.
- (HUB-36796). Fixed an issue where having a user directly assigned to a Project Group and the same user assigned to a User Group that's also assigned to the Project Group would result in multiple project groups being returned by the API, resulting in a Detect failure.
- (HUB-36939). Fixed an issue where the debug page exposed the password in plain text if the user logged into Black Duck as the sysadmin.
- (HUB-36997). Fixed an issue where license information was missing for notice files generated using KnowledgeBase on-prem.
- (HUB-37143). Fixed an issue where rapid scans that evaluate the policy expression 'Newer Versions Count' fail with internal error if the component does not have a version.
- (HUB-37285). Fixed an issue where new installations of Black Duck 2023.1.0 using an external database could fail if the default admin user name was changed.
- (HUB-37312). Fixed an issue where a `Unable to access tool` error could be generated if the `/opt/blackduck/hub/uploads/tools` directory doesn't exist in the mounted storage volume when looking for objects.
