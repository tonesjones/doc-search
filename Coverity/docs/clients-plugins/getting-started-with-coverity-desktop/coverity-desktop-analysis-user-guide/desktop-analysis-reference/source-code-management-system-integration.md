---
title: "Source code management system integration"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/source-code-management-system-integration.html"
content_id: "4keoP0AKhKGH0SK3UJSlZw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:57.722630+00:00"
---

# Source code management system integration

Desktop Analysis can be integrated with your source code management (SCM) system to help
determine which files have been recently modified, and thus require local analysis.
Using the `cov-run-desktop` option,
`--analyze-scm-modified`, will query your SCM to determine which of
your source files have been modified locally, and then proceed with Desktop Analysis on
those files.

You can also use your SCM to decide which reference snapshot to use with Desktop Analysis. By
passing the `--reference-snapshot scm` option to
`cov-run-desktop`, or setting
"`settings.cov_run_desktop.reference_snapshot`" to
"`scm`" in coverity.conf, Desktop Analysis will
determine the creation date and time of your current code version, and use that as the
date and time for which to determine the appropriate reference snapshot.

Note: When
using `--analyze-scm-modified` or `--reference-snapshot
scm`, you must also pass the `--scm` option, or set
"`settings.scm.scm`" in coverity.conf, in
order to specify which SCM you are using. For more information on these and other
SCM-related options, see `cov-run-desktop` in the Coverity 2026.6.0 Command Reference.
