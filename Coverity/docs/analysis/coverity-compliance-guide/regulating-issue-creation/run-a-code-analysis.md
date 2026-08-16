---
title: "Run a code analysis"
source_url: "https://docs.blackduck.com/r/coverity/2026.6/coverity-documentation/run-a-code-analysis.html"
content_id: "fXgX95tv4Q7vcelmKEJRCQ"
version: "2026.6"
section: "Coverity Analysis"
scraped_at: "2026-08-12T19:37:42.941597+00:00"
---

# Run a code analysis

As a first step in setting up Compliance Filtering, you should run an analysis of your
codebase. Doing so populates the Coverity Analysis intermediate directory with findings
data. You must run it using the `--strip-path` option. Failure to do so
will result in an error when you attempt to generate a findings report.

1. Run `cov-analyze` using the `--strip-path` option
   on your codebase, for example:

   *On Linux:*
   `` cov-analyze --dir idir --strip-path `pwd` --coding-standard-config
   config-file.json ``

   *On Windows:*
   `cov-analyze --dir idir --strip-path %cd% --coding-standard-config
   config-file.json`

   The `` `pwd` `` or `%cd%` returns the current working
   directory (which is then stripped out). Your goal in using the
   `--strip-path` option is to strip directories out of the path
   that are build-host dependent. You want to leave the directories that come from
   the code base.

   Refer to the Coverity 2026.6.0 Command Reference for more information on using
   `cov-analyze`.
