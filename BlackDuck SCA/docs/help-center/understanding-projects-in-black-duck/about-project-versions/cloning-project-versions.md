---
title: "Cloning project versions"
source_url: "https://docs.blackduck.com/r/blackduck/2026.7/black-duck-documentation/cloning-project-versions.html"
content_id: "Xxl~On4bAkRkOYq_CqjJPA"
version: "2026.7"
section: "Black Duck SCA Help Center"
scraped_at: "2026-08-08T15:14:15.262370+00:00"
---

# Cloning project versions

When creating a new project version, Black Duck SCA lets you select an
existing project version and clone its component edits, remediation details, and/or
license term fulfillment status to the new project version. Use cloning to help reduce
your workload by using the analysis and resolutions you defined in an existing project
version as a baseline for a new version.

Unlike persistent edits which synchronizes edits made in one version to all other
versions of that project, edits made to the baseline version do not propagate to the
cloned version. This gives you the ability to experiment with the cloned version while
keeping the original version intact. Note that if you have enabled persistent edits,
then edits made to the baseline version *will be* propagated to the cloned
version.

To successfully use cloning:

1. Enable cloning, as described below.
2. Run a scan to the new version.

Cloned information appears in the cloned project version for components that are the
*same* as in the original project version: if a component is not included in
the newly scanned files, then that component *will not* be included in the new
cloned project version. Cloned information *will* appear in the cloned project
version for components that were manually added in the original project version.

By default, all options are cloned:

- Additional Fields: Custom field information.
- Component Edits:

  - Component and/or version information
  - Review flag
  - License
  - Usage
  - Ignored components
  - Comments
  - Manually added components
  - Confirmed snippet adjustments
  - Policy violation overrides and comments
- Deep License Data
- Remediation Details:

  - Remediation status
  - Target date
  - Actual date
  - Remediation comments
- License Fulfillment Status. For license terms requiring fulfillment:

  - Fulfillment status (fulfilled or unfulfilled)
  - For fulfilled license terms, the user who fulfilled the term and the date
    it was fulfilled
- Version Settings:

  - License
  - Notes
  - Nickname
  - Release Date
  - Phase
  - Distribution

Note: Cloning a project version in the **Archived** phase will not retain the **Archived**
status. The cloned version will default to the **In Development** phase.

You can modify these settings by using the **Cloning** section in the **Project
Details** section of the **Settings** tab of a project, as described here.

Note: You cannot clone individual component or remediation values.

## Enabling cloning

You enable cloning:

- Select **Clone** for the version you wish to clone from the *Project
  Name* page. The version of the Clone Version dialog box that appears
  depends on whether **Version Settings** was selected as a cloning attribute
  for the project:
  - If **Version Settings** was selected, specify the version name in
    the Clone Version dialog box and click **Clone**.
  - If **Version Settings** was not selected, specify the version name
    in the Clone Version dialog box, enter any of the other project
    version settings, and click **Clone**.
- Use the **--cloneFrom** parameter when using the
  command line to scan and create a project version.
