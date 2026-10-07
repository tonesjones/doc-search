---
title: "Configure Coverity Analysis to use Coverity on Polaris"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/configure-coverity-analysis-to-use-coverity-on-polaris.html"
content_id: "TAeoWatPXJXJXz2qIUDFrQ"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:52.513175+00:00"
---

# Configure Coverity Analysis to use Coverity on Polaris

Configuring a Code Sight client to access Black Duck scan engines via a Coverity on Polaris
server, you can use a polaris.yml file.

## The polaris.yml file

The polaris.yml file is a YAML file that is standard for Coverity on Polaris installations.

To configure a Code Sight client, you need to specify the `serverUrl`
and the `project` sections of polaris.yml

For more information about the configuration file, please see the section
[*Coverity on Polaris Help* →
“Command Line” → “Configuration File Overview”](https://documentation.blackduck.com/bundle/coverity-on-polaris/page/topics/c_conf-overview.html).

Please keep in mind the following:

- For Code Sight configuration, you do not need to edit other sections of polaris.yml.
- The polaris.yml is a standard component of Coverity on Polaris
  configurations, so this file might already be present in your code base.

  If your code base has not used Coverity on Polaris before, you might need to create a new
  polaris.yml file. You can use the Coverity on Polaris
  command-line interface to do so. For a description of the steps to follow,
  please see the section
  [*Coverity on Polaris Help* → “Command Line” → “Command Line Overview” → “CLI Scanning QuickStart Guide” → “Initialize a Project”](https://documentation.blackduck.com/bundle/coverity-on-polaris/page/topics/t_init-project.html).
- Code Sight retrieves only URL, project, branch, and revision information from polaris.yml.
  Any local custom compiler configuration or custom analysis settings must be done via a local configuration file.

## Coverity Analysis customization

If you are adding support for Coverity, you can create a new scan configuration
and choose the Coverity (.yaml, .json) option.
These files, which support Coverity CLI option specifications, are the preferred method.

Note:
Code Sight does continue to support the legacy coverity.conf file format.
See Coverity on Polaris and ‘coverity.conf’.
