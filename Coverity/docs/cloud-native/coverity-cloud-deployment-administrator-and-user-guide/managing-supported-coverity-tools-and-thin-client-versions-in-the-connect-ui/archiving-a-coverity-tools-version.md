---
title: "Archiving a Coverity Tools version"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/archiving-a-coverity-tools-version.html"
content_id: "d7WwhFfM3I30zmURmL9UkQ"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:48.434836+00:00"
---

# Archiving a Coverity Tools version

Note: You must be a Connect administrator to archive a version of
Coverity Tools.

Archiving a version of Coverity Tools makes that Coverity Tools version unavailable for
download, and removes the equivalent Thin Client version from the Thin Clients window of
the Connect UI.

CI/CD cannot run scans using an archived version of Coverity Tools.

Users/programmers cannot download an archived version of Thin Client as it is removed
from the Thin Clients window of the Connect UI. However, if the archived Thin Client
version is already installed on a user's client system, and if the Thin Client version
is supported by the Coverity version deployed in Kubernetes, the user can perform scans
using that version.

To archive a version of Coverity Tools:

1. In the Coverity Connect UI, select Configuration > Configure Coverity Tools. The Available Coverity Tools pane opens,
   listing all available versions of Coverity Tools.
2. In the row for the Coverity Tools version you want to archive, click in the
   Actions field, then click
   Archive in the menu.

   Connect archives the selected Coverity Tools version. The archived version
   displays in the Available Coverity Tools window with the
   version number crossed out. The only available actions include
   Delete and if the archived version is the default,
   the Unset default action.

   Note: To unarchive a version of Coverity Tools, upload the
   version as described in Managing supported Coverity Tools and Thin Client versions in the Connect UI. Once
   uploaded, that Coverity Tools version is available.
