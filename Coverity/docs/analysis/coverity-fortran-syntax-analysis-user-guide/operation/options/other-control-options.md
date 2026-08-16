---
title: "Other control options"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/other-control-options.html"
content_id: "MvcCdmYOytSdljIVU2QxKg"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:36:13.547508+00:00"
---

# Other control options

Additional control options control defect generation. The `impact` option
selects the defects to be reported from among the flaws detected by the analysis. The
flaws are categorized as having `Low`, `Medium` or
`High` impact, based on how the nature of the flaw. These correspond
to informational [I], warning [W] and error [E] message in the text output files.

The `--append` option allows the outputs from subsequent invocations of
`cov-run-fortran` to be combined. By default, the results from one
invocation of `cov-run-fortran` overwrite any results already present in
the intermediate directory. The `--strip-path` option can be used to
remove a common prefix from filenames store in the intermediate directory. This reduces
storage requirements and improves the speed of `cov-commit-defects`.
