---
title: "Configuring Jira export"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/configuring-jira-export.html"
content_id: "IcWRcaVoGjPBNgb2TepI~g"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:48:15.022109+00:00"
---

# Configuring Jira export

The configuration process for Jira integration consists of two main tasks:

- Server configuration
- Project mapping

Note: Field maps carried over from earlier versions of Coverity Connect are duplicated so
that there is one field map per project. This may cause some of the field mappings to be
invalid for a given project. To check that the field mappings are valid, you should
click Test Mappings to test all of the mappings, and edit or
delete mappings found to be invalid.

After you have completed the configuration tasks, the Triage panel
will include an Export button. When clicked, a new bug will be
created in the specified Jira project with the information exported from the Coverity
Connect issue.

Note that each issue can only be exported once.
