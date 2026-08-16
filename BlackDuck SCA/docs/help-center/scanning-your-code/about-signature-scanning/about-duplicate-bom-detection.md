---
title: "About duplicate BOM detection"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/about-duplicate-bom-detection.html"
content_id: "68RL1P_UvFFr3hKh6NZOEw"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T14:53:43.200440+00:00"
---

# About duplicate BOM detection

Duplicate BOM detection determines if a new package manager scan duplicates the existing
BOM, and if so, stops processing the scan and denotes it as complete. For high-frequency
scans that generate redundant (identical) data, Black Duck's duplicate BOM detection can
provide significant performance improvements.

The only indication in the Black Duck UI as to whether a scan is a duplicate is on the
*Scan Name* page: for duplicate scans, the scan status is "Complete" and the
number of matches is "Unchanged":

  
 [image: Scans page]   

Note the following:

- Duplicate BOM Detection is currently for *package manager scans* only and
  works with any version of Black Duck Detect. No additional Black Duck Detect properties are required.
- This feature is automatically enabled, however, you can disable this feature.
  Refer to the *Installing Black Duck using Docker Swarm* guide for more
  information.
- Black Duck only compares a scan to recent BOMs: Black Duck will not compare a
  package manager scan to a BOM that is older than 7 days.
- If results were requested when configuring the scan, those results are still
  returned from the existing data.
- If Black Duck does not detect a duplicate BOM, scan processing proceeds as
  usual.
- Duplicate BOM information, such as the number of unique and total BOMs, is shown
  in the **usage: scan completion** section of the System Information page.

HUB-28244. In Black Duck 2021.4.0, this feature
only impacts package manager (dependency) scans when the set of dependencies discovered
by Detect is identical to the set from the previous scan. This capability will be
extended in future releases.
