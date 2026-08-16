---
title: "Upgrade Coverity Connect"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrade-coverity-connect.html"
content_id: "OQNmOs4CsavJcvKfME8Rrw"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:56.456770+00:00"
---

# Upgrade Coverity Connect

You can follow the procedures documented in "Upgrading Coverity Connect" in the Coverity 2026.6.0 Installation and Upgrade Guide. For the most common upgrade procedure,
you can start with the Quickstart Guide for Upgrades to Coverity Connect, a guide that
contains steps on upgrading a Coverity Connect instance that uses an embedded database.

Tip: Where appropriate, we advise upgrading Coverity Connect by using the automated
in-place or backup-and-restore paths provided through the installer, since they preserve
some settings better than the manual upgrade paths.

- **Running a test upgrade** - Run a test upgrade first, using your production
  database backup in a test environment. For large upgrades, this test should
  reveal possible problems and help you estimate the time that your production
  upgrade will require.
- **Committing between versions** - You can commit analysis results from the same or earlier
  version of Coverity Analysis to the same or later version of Coverity
  Connect (for specific support limitations, see Compatibility between Coverity product components in the Coverity 2026.6.0 Installation and Upgrade Guide). Note that if you want to incorporate the functionality of
  running a single, multi-language analysis instead of running separate
  analyses divided by programming language, you must commit the analysis
  results to the same stream in a new instance of Coverity Connect.
- **Coverity Desktop plug-in versions** - The Coverity Fast Desktop plugins are supported to
  work with newer versions of the Coverity Connect server (within the
  documented support timelines)
  so that
  Coverity Connect can be upgraded without users needing to upgrade their
  plugins and analysis tools at the same time.

  Please
  note, however, that the Coverity Desktop and analysis tool versions must
  continue to match each other.
