---
title: "Upgrading Coverity Analysis using updates"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-coverity-analysis-using-updates.html"
content_id: "VOM_dWwkY2OFu1~OQksj7g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:45:25.089905+00:00"
---

# Upgrading Coverity Analysis using updates

Upgrading Coverity Analysis using incremental updates involves running the update utility
and specifying a target version (`--end-version`) that contains or
depends on an incremental installer containing an update.

As with the standard update procedure, Coverity recommends that you install the updated
distribution in its own location. When using the incremental installer utility, this
involves making a verbatim copy of the existing `cov-analysis`
distribution in a new directory and applying the updates there.

Note: It is not necessary to wait until the availability of an update is indicated at the
end of a commit. The listing and installation of updates can be performed at any
time.

The update installer will only download and install updates that are
appropriate for the client on which it is run.

To update Coverity Analysis:

1. Optionally, make a backup copy of the existing installation.

   This step is not
   required, but is strongly recommended.
2. Run `cov-install-updates list <connection-options>` to obtain
   a list of available updates.

   This command uses the version of the current
   installation to determine which update packages are appropriate.

   If
   multiple updates are available, they are listed in the order in which they will
   be installed. If no updates are available, the list will be
   empty.

   Normally, only updates with the same base version as the current
   installation will be listed. To see all available updates, including those that
   contain or require an upgrade to a newer major release version, use the
   `--show upgrades` option.
3. Run `cov-install-updates install <connection-options>` to
   install the available updates.

   By default, all available updates having the same
   base version as the current installation will be installed. The
   `--end-version` option can be used to alter this
   behavior.

   Selecting an end-version that is older than the latest available
   update will install updates up to and including the specified end-version. Newer
   updates will continue to be offered by the `list` subcommand
   and by `cov-commit-defects`.

   Selecting an end version
   with a newer base version than the current installation will cause the
   installation to be upgraded as part of the update process.

   Note: Since there are
   dependencies between Coverity Analysis, Coverity Connect and the desktop
   plugins, it is still recommended that you follow the standard upgrade
   procedure Upgrading Coverity Analysis to upgrade a Coverity
   Analysis installation. However, in some cases it may be more convenient to
   upgrade analysis clients using `cov-install-updates`.
4. Review the console output from `cov-install-updates` and ensure
   that the desired updates were installed. `cov-install-updates` is
   designed to install each update package in its entirety or not at all.

   If the
   current installation has become corrupted,
   `cov-install-updates` will determine this before the
   installation of a given package begins. In that case, it will error out before
   attempting to install that package.
5. Continue with Step 2 of Upgrading Coverity Analysis.
