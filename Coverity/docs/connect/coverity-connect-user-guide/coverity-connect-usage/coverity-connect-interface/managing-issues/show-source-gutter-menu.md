---
title: "Show Source Gutter Menu"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/show-source-gutter-menu.html"
content_id: "OkjqpLKLg6sqj2HlFcItMg"
version: "2026.6"
section: "Coverity Connect"
scraped_at: "2026-08-12T18:46:57.481805+00:00"
---

# Show Source Gutter Menu

The Show Source Gutter Menu is activated by clicking on the Show
gutter control icon - [image: image] icon. The
Show Source Gutter Menu allows you to control the display of
the following information:

- SCM Author - The username of the user who checked the code in.
- SCM Modification Date - The date that the changed code was checked into an
  SCM system.
- SCM Revision - The revision number corresponding to the check-in of the
  changed code. Revision values depend on the SCM system.
- Line Numbers - The line numbers for each line of code.
- Issue Events - The events that lead to the issue.
- Coverage - The lines of code that are covered by analyzed developer tests.
  This information was available only with Test Advisor which is end-of-life
  and unavailable as of the 2021.9.0 release.
- Coverage Exclusions - Allows you show, hide, or change on the fly, coverage
  rules. This information was available only with Test Advisor which is
  end-of-life and unavailable as of the 2021.9.0 release.

In order to see SCM data in Coverity Connect, it is necessary to run the
`cov-import-scm` command prior to running
`cov-analyze`. For more information, see
`cov-import-scm`
in the Coverity 2026.6.0 Command Reference.
