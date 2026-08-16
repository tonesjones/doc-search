---
title: "Project mapping"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/project-mapping.html"
content_id: "n_lIe4lkiy0uauVwYy~7ow"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:16.260525+00:00"
---

# Project mapping

After connecting with the Jira server, choose which Jira projects you want to export your
Coverity Connect issues to. Project mapping allows you to associate your Jira projects
with related Coverity Connect projects, so that when you export an issue, the bug is
generated in the correct Jira project, with the appropriate information included.

You can create and edit project mappings by using the options in the Bug
Tracking System: JIRA pane. After the Jira server is successfully
configured, the project list displays existing mappings between Jira projects and
Coverity Connect projects. Each project mapping consists of a Jira project, one or more
associated Coverity Connect projects, and mappings to specify which information to
include with each exported issue.

The Bug Tracking System: JIRA pane provides the following
options:

Add...
:   Opens a pop-up dialog to create new project and field mappings. Here you can
    specify a Jira project and the associated Coverity Connect projects. After
    specifying the projects to map, you specify the appropriate Jira field along
    with an associated Coverity Connect field or constant value.

Edit...
:   Opens a pop-up dialog to edit the selected project mapping.

Delete...
:   Deletes the selected project mapping.

Test Mappings
:   Tests all of the defined project mappings to check for errors.
