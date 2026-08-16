---
title: "Using the Coverity CLI to override configuration defaults"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/using-the-coverity-cli-to-override-configuration-defaults.html"
content_id: "1fybBUdwmSQEzD47hfi7HA"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:25.732877+00:00"
---

# Using the Coverity CLI to override configuration defaults

This section describes the command-line options you can use to configure Coverity CLI
subcommands or to override settings in the configuration file that would affect these
subcommands. It includes options that allow you to:

- Access and edit any configuration setting in
  the configuration file from the command line.
- Specify a custom compiler configuration.
- Specify that Coverity CLI should not do build-command inference during capture.
- Specify whether
  the source code for a specific language should be captured.
- Specify
  include/exclude regular expressions to use when capturing files outside of a build.
- Specify
  include/exclude glob patterns to use when capturing files outside of a build.
- Specify a library file or directory
  to use as a dependency during capture.

The following sections describe each of these options.
