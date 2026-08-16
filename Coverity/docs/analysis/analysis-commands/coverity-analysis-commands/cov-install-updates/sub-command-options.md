---
title: "Sub-command options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sub-command-options.html"
content_id: "Q2vgK91drCNTLMuJD1GLag"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:31.246860+00:00"
---

# Sub-command options

--continue <answer>
:   By default, the `install` sub-command waits for confirmation
    if there are any warnings that impact your current installation. You can use
    the `--continue` option to automate this confirmation. You
    must use the `--continue` option with great care, otherwise
    you could inadvertently impact your installation and workflow.

    For use in scripts, the `--continue=yes` option can be used to
    provide confirmation, allowing the installation to proceed.

--end-version <version>
:   Specifies the last version, in the update path, to install. If there are
    newer available updates they will not be installed. The
    `--end-version` value is a string that represents a
    specific release version, for example, 2018.03-1. (You cannot specify a
    version older than the currently installed version.)

    If you do not specify a specific `--end-version`, then the
    default value is the newest update that has the same base version (major
    release version) as the current installation.

    Important: To install an upgrade (that is to upgrade to a newer
    *major* release) you must specify the
    `--end-version` for the newer release.

--force
:   When used with the `install` sub-command, the installer
    applies the updates only to those files that are in their original install
    state (were not altered). It skips updates for any altered files. When used
    with the `rollback` sub-command, `--force` is
    a required option, which means the roll back cannot be undone.

--installation-dir <path>
:   Provides a path to an alternate installation to be updated. If omitted, the
    installation containing this `cov-install-updates` command
    is used.

--installer-dir <path>
:   Chooses a directory where the update list and downloaded installers are
    stored temporarily. If omitted, a temporary directory is used. The temporary
    directory is removed after successful completion of the
    `cov-install-updates` command.

--show upgrades | raw
:   When `upgrades` is specified, the `list`
    subcommand will list installer packages in an update path that includes one
    or more upgrades (to a newer major release version).

    When `raw` is specified, all available update packages will
    be listed — not just those that lie along a valid update path.

    Both options can be specified using multiple `--show`
    options.

    Note: An upgrade (as opposed to an update) installs the next major release,
    which usually requires a re-emit and may include changes that cause
    churn.
