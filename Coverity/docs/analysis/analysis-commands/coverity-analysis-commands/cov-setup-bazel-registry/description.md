---
title: "Description"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/description.html"
content_id: "j0bRus9ulwmo4680Q~Qf~g"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:42:39.190871+00:00"
---

# Description

The `cov-setup-bazel-regsitry` command sets up a Bazel registry that contains a reference to the
`rules_coverity` Bazel module from the current Coverity Analysis installation.
With Bazel 7 or a newer version, this module can be referenced from the MODULE.bazel file on the local filesystem,
so that users can specify a registry from which to pull the `rules_coverity` Bazel module without needing to set up or modify
a more extensive network-accessible registry.
