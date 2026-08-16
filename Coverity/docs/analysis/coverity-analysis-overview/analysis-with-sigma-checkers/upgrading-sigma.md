---
title: "Upgrading Sigma"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/upgrading-sigma.html"
content_id: "32j1jjU2pEaQ03MgWkL_OA"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:34:42.694263+00:00"
---

# Upgrading Sigma

Warning:

Support for updating the Sigma binary used by `cov-analyze` through
the `--update-sigma-binary` and `--use-sigma-binary`
options has been deprecated and will be removed in a future release.

The Sigma scan engine and Coverity release using different schedules: Sigma
releases every 3 weeks; Coverity, every 3 months. As a result, there are
several releases of Sigma that follow the Sigma version integrated into any given
Coverity release. If you want Coverity to use a more
recent version of Sigma, you can use one of the following `cov-analyze`
options:

- The `--update-sigma-binary` option permanently updates the Sigma
  binary used by Coverity so that any succeeding calls to
  `cov-analyze` will use the newer Sigma binary.
- The `--use-sigma-binary` option performs a single analysis run
  using the Sigma binary at the specified path. Any succeeding calls to
  `cov-analyze` without this option will continue to use the
  Sigma binary bundled with Coverity. This option allows you to evaluate the
  results of a newer Sigma binary before permanently upgrading to it.

For additional information, see the description of these options in "Options: Sigma" in the Coverity 2026.6.0 Command Reference.

Be aware that using a later version of Sigma might have the following consequences:

- Defects found by newly added Sigma checkers that are committed to Coverity Connect might have
  missing Standard Attributes data.
- Coverity might not capture files in all languages newly supported by Sigma; any
  checkers for languages that are not captured by Coverity will not report any defects.
- For any new Sigma checkers that are intended to replace existing Coverity
  checkers, defect triage information in Coverity Connect might not be migrated
  correctly. Analysis scans might report duplicate defects for these checkers.
- Messages and properties for newly added Sigma checkers will not have translations
  available in languages other than English.

Upgrading the next full Coverity installation will provide better support for new Sigma
features, and resolve many of these issues.
