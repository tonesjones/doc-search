---
title: "Fixed Issues in 2022.2.1"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/fixed-issues-in-2022.2.1.html"
content_id: "LU01iIvq_FNUOatDOXcZnQ"
version: "2026.7"
section: "Release Notes"
scraped_at: "2026-08-08T15:37:44.649461+00:00"
---

# Fixed Issues in 2022.2.1

The following customer-reported issues were fixed in this release:

- (HUB-32540). Fixed a rare issue with the KbUpdateJob where a duplicate value
  insert could slow down or fail the job.
- (HUB-32544). Fixed a race condition issue where the KbUpdateJob tries to
  insert a `version_bom_component` already inserted by a
  scan.
- (HUB-33045). Fixed an issue where creating a policy rule specifically for
  Rapid Scans could cause all project versions to enter a re-computation state
  where the BOM's Status would change to "Processing".
- (HUB-32363 and HUB-33027). Fixed a possible race condition while unmapping code
  location for the following scenarios (without using
  --detect.project.codelocation.unmap=true):
  - Code location is rescanned and mapped to other project
    version.
  - Code location is manually unmapped from UI.
  - Code location is manually deleted from UI.
  - Code location is deleted by ScanPurgeJob.
- (HUB-33155). Fixed an issue where refreshes of HUB registration could stall,
  causing the jobrunner to hold a lock much longer than it should potentially
  resulting in blocked queries.
- (HUB-33132). Fixed an issue where the dependency-paths API was consuming
  large amount of service memory and paging to disk.
- (HUB-31212). Fixed an issue where members of one sub-project group could
  access all project groups and their tree.
- (HUB-33162). Fixed an issue where vulnerability results in Rapid Scans could
  display incorrect information when the highest priority Security Risk
  Ranking set does not match the vulnerability type (BDSA vs NVD) and the CVSS
  preference.
- (HUB-31756). Fixed an issue where the Project Viewer and Project Group Viewer
  roles were not assignable to users added to Projects and Project Groups.
- (HUB-33047). Fixed an issue where Null Pointer Exception errors occurring
  during the KbUpdateJob process could cause the job to progress very slowly
  or appear to be stuck.
