---
title: "Unsetting the default Coverity Tools version for CI/CD pipelines"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/unsetting-the-default-coverity-tools-version-for-ci/cd-pipelines.html"
content_id: "~OUA0Shl7BgWHfKN5DX1LA"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:47.135815+00:00"
---

# Unsetting the default Coverity Tools version for CI/CD pipelines

Unsetting a default Coverity Tools version clears the default Coverity Tools artifact
version that is available for use in CI/CD commands.

Important: If you unset default Coverity Tools version,
CI/CD commands that use `default` will fail unless you specify another
default version.

Note:

You must be a Connect administrator to unset the default version of Coverity
Tools.

See also Default Coverity Tools version and CI/CD pipelines.

The default version is available for both CI/CD and end users, however the actual
`default` functionality is for CI/CD commands only.

To clear (unset) the Coverity Tools default version:

1. In the Connect UI, select Configuration > Configure Coverity Tools. The Available Coverity Tools pane opens,
   listing all available versions of Coverity Tools.
2. In the row for the Coverity Tools version you want to unset as default, click in
   the Actions field, then click Unset
   default in the menu.

   This clears the default version. There will be no default version unless you set
   one.
