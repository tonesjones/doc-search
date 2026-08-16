---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "2MPEBWUmCSX6JWJ30bKOfA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:29.941521+00:00"
---

# Description

The `cov-install-updates` command manages the installation of
incremental, minor, or major Coverity Analysis updates. Use it with its sub-commands to
query and list the available updates, install the updates in order, and if required,
roll back an undesired update. The `cov-install-updates` command requires
one of the five sub-commands listed below. See each sub-command section to see the
options that apply to that sub-command.

Note: To list major version updates (upgrades), specify the `--show=upgrades`
option.

To install a major version update, you must use the
`--end-version` sub-command.
