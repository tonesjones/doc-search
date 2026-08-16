---
title: "Setting the default Coverity Tools version for CI/CD pipelines"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/setting-the-default-coverity-tools-version-for-ci/cd-pipelines.html"
content_id: "G2wvDJCKMJFV9C4N_Z5UIQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:46.489626+00:00"
---

# Setting the default Coverity Tools version for CI/CD pipelines

Setting a default Coverity Tools version sets the `default` Coverity Tools
artifact version that is available for use in CI/CD commands.

Note:

You must be a Connect administrator to manage the default version of Coverity
Tools.

See also Default Coverity Tools version and CI/CD pipelines.

You can set only one default Coverity Tools version at a time.

The default version is available for both CI/CD and end users, however the actual
`default` functionality is for CI/CD commands only.

To set the default Coverity Tools version:

1. In the Connect UI, select Configuration > Configure Coverity Tools. The Available Coverity Tools pane opens,
   listing all available versions of Coverity Tools.
2. In the row for the Coverity Tools version you want to set as default, click in
   the Actions field, then click Set
   default in the menu.

   The selected version is set as the default version. In the Available
   Coverity Tools list, a check mark appears in the
   Default column, identifying the default version.
