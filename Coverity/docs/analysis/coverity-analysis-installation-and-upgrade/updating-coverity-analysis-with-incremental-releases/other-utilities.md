---
title: "Other utilities"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/other-utilities.html"
content_id: "Iwmo62io3IzttSItcxEzwQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:24.458930+00:00"
---

# Other utilities

You can use the `cov-install-updates check` command to check if there are any
updates available for a given client. This command requires connection options, so it
can query a connected Coverity Connect instance for available update information. The
`check` subcommand only looks for updates that have the same base
version as the current installation. To see if there are upgrade installers available,
use `cov-install-updates list --show=upgrades`.

For use in scripts, `cov-install-updates check` returns 0 if updates are
available, and 1 if not. An error code of 2 indicates that the inputs were invalid.

You can use the `cov-install-updates version` command to determine which version
(including updates) is currently installed. Version numbers use the format
*YYYY*.*MM*.*V*, where *YYYY* is the year, *MM* is the
month, and *V* is the minor (or update) version, for example, 2023.9.0.
