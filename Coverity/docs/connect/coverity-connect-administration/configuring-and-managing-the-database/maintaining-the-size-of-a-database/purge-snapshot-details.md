---
title: "Purge snapshot details"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/purge-snapshot-details.html"
content_id: "y6ad7GSW~_O~9mPytuLstw"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:49:16.749227+00:00"
---

# Purge snapshot details

The Purge Snapshot Details feature allows you to schedule a clean-up process in which
Coverity Connect automatically removes snapshot information that you might no longer
need if more current snapshot information is available. This feature is recommended
because it allows you to reduce and maintain the size of a Coverity Connect database.
This feature is also recommended instead of deleting snapshots, if you have been using
snapshot deletion in previous versions to save database size. Snapshot purging is
faster, more efficient, and preserves your snapshot and triage history.

This feature is implemented as follows:

- During the installation of Coverity Platform - This installation option sets a
  preconfigured interval for this feature. For more information, see the Coverity 2026.6.0 Installation and Upgrade Guide.
- Through the Coverity Connect administration configuration menu - This allows you to customize
  your interval settings. These configuration setting override the installation
  settings if you chose to implement them. For more information, see the Coverity Platform 2026.6.0 User and Administrator Guide.
