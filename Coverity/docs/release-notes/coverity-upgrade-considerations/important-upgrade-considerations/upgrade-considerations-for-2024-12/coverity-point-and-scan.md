---
title: "Coverity Point and Scan"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-point-and-scan.html"
content_id: "30fUtzSShtgfek97mQdlcQ"
version: "2026.6"
section: "Coverity release notes and upgrade considerations"
scraped_at: "2026-08-12T19:56:52.818740+00:00"
---

# Coverity Point and Scan

Starting with Coverity 2024.12, the contents of the
$HOME/.synopsys/point-and-scan directory will be moved
automatically to $HOME/.coverity/point-and-scan.

Note: If there is a need to downgrade the version of
Coverity Point and Scan to one older than 2024.12.0, the contents will need to be
moved manually back from $HOME/.coverity/point-and-scan to
$HOME/.synopsys/point-and-scan in order for users to
continue to see their previous scans, logged in accounts and other data in Coverity
Point and Scan.
