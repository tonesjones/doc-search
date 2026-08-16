---
title: "Coverity Analysis updates"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/coverity-analysis-updates.html"
content_id: "HzENOr1t0MkPS0KNbCJBfQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:27.123955+00:00"
---

# Coverity Analysis updates

Whether you can download Coverity Analysis updates from the command line depends on how your
Coverity administrator configures the Coverity Analysis update feature.

- Starting with the Coverity 2018.03 release, Black Duck allows you to download and
  install major or minor release Coverity Analysis upgrades from the command
  line.
- Starting with the Coverity 2017.07-SP2 release, Black Duck allows you to download
  and install incremental release Coverity Analysis updates from the command
  line.

If the Coverity Analysis update feature is turned on, then after a successful commit,
`cov-commit-defects` checks for any new Coverity Analysis updates. If
there are updates, a message appears with the number of updates that you can download.
Coverity Connect determines which updates are relevant based on the commit.
Coverity Connect notifies you only about relevant updates and makes them available to download.
Any other updates are ignored.

The Coverity Analysis *update* files delivered in an incremental release are
typically smaller than the Coverity Analysis *upgrade* files you receive as part of
a major or minor release. Typically, they do not contain all of the files in a Coverity Analysis installation image,
and they might or might not overwrite configuration files.
To ensure configuration files are not inadvertently overwritten, the installer first
checks to see if the files to be overwritten have changed. If they have changed, the
installer lists the modified files and stops. (If you decide to overwrite these changed
files anyway, re-run the installer using the `--force` option.

Use the `cov-install-updates` command with its sub-commands and options to
query and list the available updates, install the updates in order, and if required,
rollback an undesired update. For more information, see the `cov-install_updates` description
in the Coverity 2026.6.0 Command Reference.
