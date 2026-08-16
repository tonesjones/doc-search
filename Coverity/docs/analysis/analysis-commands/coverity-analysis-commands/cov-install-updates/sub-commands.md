---
title: "Sub-commands"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/sub-commands.html"
content_id: "W8f_Kx16AHeWldvxJYiHyg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:41:30.613943+00:00"
---

# Sub-commands

check
:   Communicates with the Coverity Connect server and checks if there are any
    Coverity Analysis updates available newer than the installed Coverity
    Analysis version, as it appears in the `VERSION.xml` file.

    If there are updates available, it displays on the console the number of
    updates available to download and install.

    If there are updates available, the exit code is 0.

    If there are no updates available, the exit code is 1.

    This sub-command requires connection options sufficient to access update
    information from a connected Coverity Connect server. For details, see the Connection options
    section.

    This sub-command also accepts the following options as described in the Sub-command options section.

    - `--installer-dir`
    - `--installation-dir`

install
:   Determines the upgrade path, downloads the available Coverity Analysis update
    files, creates a backup of the current Coverity Analysis installation, lists
    the updates and any warnings, and then installs each Coverity Analysis
    update in order. Some updates can impact your normal workflow: therefore,
    they contain a warning message that prints to the console. If any warnings
    are present, the install sub-command will wait for confirmation before
    proceeding with the installation. If not confirmed, the installation will
    abort. See the `--continue` sub-command option for more
    information about installation confirmation.

    The `install` command selects from available updates to create
    an update path from the currently-installed version to the selected
    end-version. See the `--end-version` option for more
    details.

    This sub-command requires connection options sufficient to access update
    information from a connected Coverity Connect server. For details, see the Connection options
    section.

    This sub-command also accepts the following options as described in the Sub-command options section.

    - `--continue`
    - `--end-version`
    - `--force`
    - `--installer-dir`
    - `--installation-dir`

    The `install` sub-command returns with an exit code of 0 if
    updates were successfully installed. The exit code is 1 if the command
    completed successfully but no updates were installed.

list
:   Displays a list of the available Coverity Analysis updates with a brief
    description for each update.

    This sub-command requires connection options sufficient to access update
    information from a connected Coverity Connect server. For details, see the Connection options
    section.

    This sub-command also accepts the following options as described in the Sub-command options section.

    - `--installer-dir`
    - `--installation-dir`
    - `--show`

rollback
:   Rolls back the Coverity Analysis installation to the state it was in before
    you last ran the `cov-install-updates install` command.
    Since it is possible for the `install` sub-command to
    install several updates within the same session, the effect of the
    `rollback` sub-command is to roll back all the
    updates.

    Note: Occasionally, an update package may contain a post-installation script.
    When this occurs, the installer will discontinue installing packages in the
    selected sequence and transfer control to the script. The script performs
    special actions and then normally continues the installation by re-invoking
    `cov-install-updates`. When this occurs, rolling back
    an installation can only return to the installation state that existed
    following execution of the script.

    This sub-command accepts the following options as described in the Sub-command options section.

    - `--force`
    - `--installer-dir`
    - `--installation-dir`

version
:   Displays the version number for the installed Coverity Analysis, as it
    appears in the `VERSION.xml` file.

    This sub-command accepts the following options as described in the Sub-command options section.

    - `--installation-dir`
