---
title: "‘coverity.conf’ configuration files"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/coverity.conf-configuration-files.html"
content_id: "DD5YnWinIYvZ01gUuXAhPw"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:52.676910+00:00"
---

# ‘coverity.conf’ configuration files

Coverity (.conf) is the legacy *scan configuration* for Coverity.
If this is the active scan configuration, then Code Sight uses one or more coverity.conf files for configuration.

Attention:
The preferred method is to use the scan configuration Coverity (.yaml, .json) option, which is compatible with Coverity CLI settings.
See Coverity scan configurations and custom scan settings.

The coverity.conf file can be used in a couple of different ways.

- When Coverity Analysis uses Coverity Connect as a server, a *user-specific* coverity.conf, can reside on the user’s system.
  The purpose of a user-specific coverity.conf file is to specify the local file path (`known_installations`) of the Coverity Analysis tool.

  In some situations, a user-specific coverity.conf file is created when Coverity Analysis is installed.
- A *project-specific* coverity.conf file might be used to customize the Coverity configuration.

  As the name implies, there can be one such coverity.conf file for each code base to analyze.
  All users analyzing a particular code base should use the same project-specific coverity.conf file.
