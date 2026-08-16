---
title: "Fixed Issues in 2022.7.1"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2022.7.1.html"
content_id: "Jd6CLDQq6YJmXUW4cOfdEA"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:31.385164+00:00"
---

# Fixed Issues in 2022.7.1

The following customer-reported issues were fixed in this release:

- (HUB-33693). Fixed an issue where the scanned file view of a file with snippets would not load unless the panel was clicked.
- (HUB-34246). Fixed browser display issues when printing the Project Version Comparison view.
- (HUB-34472, HUB-34781, HUB-34682). Fixed an issue where removing licenses on the Component Version page not reflect in the BOM report.
- (HUB-34511). Fixed an issue where project and version names were pulled from HTTP headers instead of the BDIO header which could cause unreadable characters when using non-latin characters.
- (HUB-34618). Improved the performance when generating the Version Detail report on KB On-prem environments.
- (HUB-35110). Fixed the documentation inside `blackduck-config.env` for the default retention period of unmapped code locations.
- (HUB-35196). Fixed an issue where using the Component/Component Version filter did not show Component name results.
- (HUB-35222). Fixed an issue where the "Affected projects" tab was not able to load pages when navigating through them for a specific vulnerability (CVE-2016-1000027).
- (HUB-35304). Fixed an issue where the super user role assigned to a user group was not migrated to the new roles introduced in 2022.7.0 when upgrading to 2022.7.0.
- (HUB-35349). Fixed an issue where Rapid Scans scans could fail after upgrading to Black Duck 2022.7.0 due to messages being sent after the matching process was finished. It was more likely to occur when the environment had multiple match containers running.
- (HUB-35407). Fixed an issue where custom fields with null values could cause the KbUpdateWorkflowJob-Component Version Update job to fail.
