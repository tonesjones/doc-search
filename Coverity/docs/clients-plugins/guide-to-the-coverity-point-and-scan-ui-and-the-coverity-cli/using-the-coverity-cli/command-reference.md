---
title: "Command reference"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/command-reference.html"
content_id: "0cQ_EqNneN9sIQGtnnEzHQ"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:45:58.755477+00:00"
---

# Command reference

The following table lists the Coverity CLI commands. For detailed information on each command,
see "Coverity CLI commands" in the Coverity 2026.6.0 Command Reference.

Note:
If you enter `coverity` without specifying a subcommand,
the Coverity CLI prompts you to enter the name of the subcommand to run.

| Command | Action |
| --- | --- |
| `coverity analyze` | Analyzes the code that was captured. Default for the project directory is the current working directory. |
| `coverity capture` | Captures source from the project directory. Options allow you to specify a different project directory and the intermediate directory to use for captured input.  Default for the project directory is the current working directory. |
| `coverity commit` | Uploads analysis results to Coverity Connect, to a local directory, or to both locations. Default for the project directory is the current working directory. |
| `coverity help` | Displays help for the specified command. |
| `coverity list` | Lists the files that have been captured with the `coverity capture` command or the `coverity scan` command. Options allow you to specify a different project directory and the intermediate directory to use for captured input. |
| `coverity scan` | Performs the capture, analyze, and commit steps. |
| `coverity setup` | Generates a configuration file that defines your project. Options allow you to specify the directory of the source files and the name and location of the config file to generate. Default for the project directory is the current working directory.  Default for the config file is `<project-dir>/coverity.yaml`. Either YAML or JSON format is accepted.  For more information about configuration, see Configuring the Coverity CLI. |

For more detailed information,
see "Coverity CLI commands" in the Coverity 2026.6.0 Command Reference.

Note:
As of release 2024.12.0, buildless capture (`cov-capture`) and filesystem capture have been discontinued.
Use the CLI `coverity capture` command to capture code, or `coverity scan` to perform the capture, analyze, and commit steps.

Important:
When using the Coverity CLI, file inclusions and exclusions apply *only* to files captured by scanning the file system.
Files that are captured by observing a build process are *always* captured.
For example, if the Coverity CLI is invoked by a command line such as `coverity scan -- make`, any files that are observed to be compiled by the
`make` command will be captured regardless of which directory they are in or of the presence of any specified file inclusions or exclusions.

For more information, please see Using the Coverity CLI to override configuration defaults.

Attention: The Coverity CLI has a known issue when
reading the Coverity Connect password in the Cygwin shell using the `coverity
setup` or `coverity scan` commands. To work around this
issue, run `coverity setup` using the Windows command shell
`cmd.exe`. You can then switch back to the Cygwin shell.
