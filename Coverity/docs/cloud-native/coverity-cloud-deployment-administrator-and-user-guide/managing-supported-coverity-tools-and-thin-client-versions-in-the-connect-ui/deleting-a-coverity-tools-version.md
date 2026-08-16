---
title: "Deleting a Coverity Tools version"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/deleting-a-coverity-tools-version.html"
content_id: "INIQ56OFW_Eb7In~sl9J5A"
version: "2026.6"
section: "Cloud Native Coverity deployment"
scraped_at: "2026-08-12T23:44:49.117320+00:00"
---

# Deleting a Coverity Tools version

Note: You must be a Connect administrator to delete a Coverity Tools
version from Available Coverity Tools.

Deleting a Coverity Tools version makes that version unavailable to either CI/CD as a
Coverity Tools artifact or end users/programmers as a Thin Client download from the
Connect UI . Scans cannot be performed using the deleted version.

To delete a Coverity Tools version:

1. In the Coverity Connect UI, select Configuration >  Configure Coverity Tools. The Available Coverity Tools pane opens,
   listing all available versions of Coverity Tools.
2. In the row for the Coverity Tools version you want to delete, click in the
   Actions field, then click
   Delete in the menu.

   The Coverity Tools version is immediately deleted from the list of available
   Coverity Tools, and the Thin Client equivalent is removed from the Thin Clients
   download window in the Coverity Connect UI.

Note: To restore a deleted version, upload the version as described in
Managing supported Coverity Tools and Thin Client versions in the Connect UI. Once uploaded, that version is
available.
