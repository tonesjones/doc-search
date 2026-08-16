---
title: "Add data-coverity to the Source-Code Management (SCM) exclusion list"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/add-data-coverity-to-the-source-code-management-scm-exclusion-list.html"
content_id: "kT~TupqfjyjLyNPKNeyQpw"
version: "2026.6"
section: "Clients, plug-ins, integrations, and APIs"
scraped_at: "2026-08-12T19:46:54.238545+00:00"
---

# Add data-coverity to the Source-Code Management (SCM) exclusion list

By default, local analysis intermediate data is stored in a directory called
data-coverity/, a subdirectory of whichever directory contains
the coverity.conf file. Since these files should not be checked in
to the Source-Code Management (SCM) system, you should add the name
`"data-coverity"` to the list of directories excluded by the SCM
(often stored in an "ignore" file).

You can change where intermediate data is stored, either by editing
coverity.conf or by overriding its settings on the
`cov-run-desktop` command line. However, you should not put the
intermediate data from different branches of a single code base into the same directory,
because the analysis can become confused by the presence of different versions of the
same artifacts. Furthermore, avoid putting this data in a location that will be removed
when the build is cleaned, because this forces users to rerun a build capture each time
the build has been cleaned.
