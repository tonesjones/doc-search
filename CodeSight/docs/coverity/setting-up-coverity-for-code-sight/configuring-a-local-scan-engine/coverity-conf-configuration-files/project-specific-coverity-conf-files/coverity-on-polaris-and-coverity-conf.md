---
title: "Coverity on Polaris and ‘coverity.conf’"
source_url: "https://docs.blackduck.com/r/codesight/2026.9.0/code-sight-documentation/coverity-on-polaris-and-coverity.conf-.html"
content_id: "LzWYcxJ_oAyFs9Xb8ZvHGQ"
version: "2026.9.0"
section: "Coverity with Code Sight"
scraped_at: "2026-10-06T23:39:53.237956+00:00"
---

# Coverity on Polaris and ‘coverity.conf’

Code Sight continues to support legacy coverity.conf files.
These can be used with Coverity on Polaris in specific situations.

Project-specific coverity.conf files are JSON files that are specifically for
configuring Coverity Analysis and Coverity Connect behavior. If you are using a Coverity on Polaris
server and you do not need to customize Coverity Analysis behavior, then you do not
need to create or modify project-specific coverity.conf files, and with Coverity on Polaris
there is no need for a user-specific coverity.conf file.

CAUTION:

If your client connects via a Coverity on Polaris server, *do not use*
the coverity.conf file’s `"server"` or `"stream"` fields.
The Coverity on Polaris `"server"` and `"project"` values are specified
in the polaris.yml file.

For a site that uses a Coverity on Polaris server, there are only a few reasons you might want to use a project-specific coverity.conf.
The most common of these are:

- To specify a compiler configuration that is *not the standard configuration* for the IDE you use.
- To specify custom Coverity Analysis settings.

These circumstances are described in Alternative configuration settings.

For more detailed information about the format of coverity.conf and the options it supports, please see the
*Coverity Desktop Analysis User Guide*.
