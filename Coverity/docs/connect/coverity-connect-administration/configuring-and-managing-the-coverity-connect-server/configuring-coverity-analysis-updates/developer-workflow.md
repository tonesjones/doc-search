---
title: "Developer workflow"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/developer-workflow.html"
content_id: "zRlTp~EmYQsZe6qT_L2vAg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:11.900934+00:00"
---

# Developer workflow

When a Coverity Analysis user commits defects to Coverity Connect, using the
`cov-commit-defects` command, Coverity Connect sends a notification
if there are new updates. Coverity Connect determines which updates are relevant based
on the commit. Coverity Connect notifies Coverity Analysis only about relevant updates
and makes them available to download. Any other updates are ignored. In addition, if the
request determines that an update is required, but it is not stored locally on Coverity
Connect, then Coverity Connect requests the update from Black Duck. (This occurs whether
or not there is enough storage available to store it locally; if there is not enough
storage then Coverity Connect does not store it locally.) In this way, the Coverity
Analysis user always gets the latest updates regardless of the amount of storage that
Coverity Connect allows for storing the update files.

The Coverity Analysis user can use the `cov-install-updates` command
with its sub-commands to query and list the available updates, install the updates in
order, and if required, rollback an undesired update. For more information, see the Coverity 2026.6.0 Command Reference.
