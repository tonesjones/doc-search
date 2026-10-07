---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.9/coverity-documentation/description.html"
content_id: "Vb26HrQl6Th3VFuhrUoAeA"
version: "2026.9"
section: "Coverity Analysis"
scraped_at: "2026-10-04T23:33:55.814910+00:00"
---

# Description

The `cov-upgrade-static-analysis` command upgrades an old Coverity
Static Analysis or Coverity Analysis release to Coverity Analysis version 2026.9.0. Run this command from the
<install_dir>/bin directory of the new release of
Coverity Analysis. Also, the exact upgrade process differs slightly based on file
permission and web server process owner issues.

There are two modes in which you can run this command.

- In the first (and preferred) mode of operation, specified with the
  `--use-new-release` option, the configuration and the
  database in the old release is moved into the new release.
- In the second mode, specified with the
  `--use-existing-release` option, the old release is
  upgraded in place. When the upgrade is completed, the new release is
  installed in the location that was formerly occupied by the old release.
