---
title: "Central build deployment model"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/central-build-deployment-model.html"
content_id: "ikQt~0_wNRABclrUvYVQ1A"
version: "2026.6"
section: "Coverity overview"
scraped_at: "2026-08-12T03:18:39.804900+00:00"
---

# Central build deployment model

Build engineers typically write scripts that automatically run Coverity Analysis on the
source repository at some scheduled interval (typically nightly). They can also allow
developers to subscribe to automatically receive email notifications of new issues in
their source files. Developers triage and annotate the defects within Coverity Connect
or Coverity Desktop. The central build model introduces the least amount of change to
the development process and provides a strict separation between developer and build
engineer tasks. A developer interacts with Coverity Analysis by adding or modifying
source files in the code repository and viewing issue results in Coverity Connect. A
build engineer writes scripts to check out the source from the repository, build it,
initiate an analysis, and store the results in a Coverity Connect database. Optionally,
the build engineer can automatically notify developers of new issues in their source
code. The build engineer can integrate Coverity Analysis with the build process to
automatically provide Coverity Analysis consumers with fresh snapshots each morning or
at another desired interval.

[image: image]
