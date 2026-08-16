---
title: "Scenario: Notification upon completed commit"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/scenario-notification-upon-completed-commit.html"
content_id: "MYAzvA5OzUxCBMHcfsPPaA"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:47:35.959096+00:00"
---

# Scenario: Notification upon completed commit

**Goal:** To trigger an email when a commit is complete, highlighting any new defects
introduced to the project (Project Y) in the latest snapshot.

**Basic configuration:** In this scenario, a developer creates a view that filters on:

- Only in projects = Project
  Y
- Streams & Snapshots = Newly
  detected

Then, to trigger the notification after completing the commit step, the developer
runs the `cov-manage-im` command in `notification`
mode:

```
cov-manage-im --mode notification --execute --view view name			
```

To accomplish this in one step, the developer can create a script which includes each
step in the build process and ends with `cov-manage-im`. For example:

```
cov-build build options /
cov-analyze[-java] analyze options /
cov-commit-defects commit options /
cov-manage-im --mode notification --execute --view view name
```

For more information on using `cov-manage-im`,
see the Coverity 2026.6.0 Command Reference.

Note: Alternatively, in the Schedule tab of the
Notification dialog, selecting Send email when a
new snapshot is created will trigger the notification after the commit
occurs.
