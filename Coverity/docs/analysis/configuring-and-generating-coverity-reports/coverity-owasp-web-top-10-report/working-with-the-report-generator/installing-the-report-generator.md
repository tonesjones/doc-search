---
title: "Installing the report generator"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/installing-the-report-generator.html"
content_id: "L5KNnY9g9etgQ7DuWxwk0w"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:38:56.802804+00:00"
---

# Installing the report generator

The report generators are installed separately from Coverity Connect and can be installed on
either Windows or Linux machines. You can obtain the Coverity Reports installer from the
Downloads page in Coverity Connect. The Coverity Reports
installer installs all of the report generators.

Alternatively, obtain the installer for Coverity Reports from the Coverity Connect installation
directory (for example,
<install_dir>/server/base/webapps/downloads/cov-reports-linux64-2026.6.0.sh or
<install_dir>/server/base/webapps/downloads/cov-reports-win64-2026.6.0.exe).

**To download the reports installer from Connect:**

1. Log in to Coverity Connect.
2. In Help > Downloads, select the Coverity Reports installer that is appropriate for
   your system.
3. Save the installer application to an appropriate folder in your system.

**To install the reports generators:**

1. Make sure that the system you want to run the installer on can connect to the Coverity
   Connect server.
2. You have the option to use the install wizard or to install from the command
   line. To use the wizard, launch the installer, and follow the instructions in
   the wizard.

   To use the command line, proceed to the next step.
3. To run the installer from the command line, execute one of the following commands, depending
   on your operating system and your preference for quiet mode
   (`-q`) or console mode (`-c`). In quiet mode,
   there is no user interaction: installation is performed automatically using
   default values.

   | Operating System | Command |
   | --- | --- |
   | Windows | `start /wait "" cov-reports-win64-<version_number>.exe -c` |
   | Windows - quiet mode | `cov-reports-win64-<version_number>.exe -q -dir C:/target-dir` |
   | Linux | `./cov-reports-linux64-<version_number>.sh -c` |
   | Linux - quiet mode | `./cov-reports-linux64-<version_number>.sh -q -dir ~/target-dir` |

   If you do not specify a target-dir for the installation, a
   default installation directory is used. The directory name is shown at
   runtime.

   You can use the following parameters in the command line:

   | Parameter | Action |
   | --- | --- |
   | `-c` | Run in console mode. User interaction is performed in the terminal window where the installer (or uninstaller) is invoked. |
   | `-console` | On Windows, use with `-q` to open a console window to display output in quiet mode. |
   | `-dir [directory]` | Set the installation directory in quiet mode. |
   | `-Dname=value` | Set system properties. |
   | `-h` | Display help. |
   | `-manual` | On Windows, in GUI mode only, manually select a Java Runtime Environment. |
   | `-overwrite` | Overwrite all files in quiet mode. |
   | `-q` | Run in unattended (quiet) mode. There is no user interaction, and installation is performed automatically using default values. |
   | `-splash [title]` | Display a progress bar in quiet mode. |
   | `-varfile` | Use a response file. |

The directory where the Coverity Reports were installed contains the following files that
you would be using:

- The bin/ folder contains all the report generators. Some of
  the reports can be generated using a GUI. All of the reports can be generated
  using a command-line tool.
- The config/ folder contais a sample configuration file
  (config.yaml), a sample JSON file for the CVSS report,
  and an example plugin configuration file (plugin.yaml)
- The docs/ folder contains the documentation for each report
  type.
